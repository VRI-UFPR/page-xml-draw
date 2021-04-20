from __future__ import annotations
from typing import Any

from copy import deepcopy
from json import loads
from jsonschema import RefResolver, validate
from pkg_resources import resource_string


class JsonSchema:
    data: dict
    resolver: RefResolver

    def __init__(self, data: dict, resolver: RefResolver = None) -> JsonSchema:
        self.data = data

        if resolver is None:
            self.resolver = RefResolver.from_schema(self.data)
        else:
            self.resolver = resolver

    @staticmethod
    def from_string(string: str) -> JsonSchema:
        return JsonSchema(loads(string))

    @staticmethod
    def default() -> JsonSchema:
        string = str(resource_string(__name__, "schema.json"), "utf-8")
        return JsonSchema.from_string(string)

    def __getitem__(self, key: str) -> Any:
        item = self.data[key]

        if isinstance(item, dict):
            return JsonSchema(item, resolver=self.resolver)
        else:
            return item

    def has_property(self, prop: str) -> bool:
        return prop in self.data['properties']

    def get_property(self, prop: str) -> JsonSchema:
        prop_data = deepcopy(self.data['properties'][prop])

        while '$ref' in prop_data:
            ref = self.resolver.resolve(prop_data.pop('$ref'))[1]

            for key, item in ref.items():
                if key not in prop_data:
                    prop_data[key] = item

        return JsonSchema(prop_data, resolver=self.resolver)

    def validate(self, instance: JsonInstance) -> None:
        validate(instance.data, self.data)


class JsonInstance:
    data: dict

    def __init__(self, data: dict) -> JsonInstance:
        self.data = data

    def __bool__(self) -> bool:
        return bool(self.data)

    def __getitem__(self, key: str) -> Any:
        item = self.data[key]

        if isinstance(item, dict):
            return JsonInstance(item)
        else:
            return item

    def __setitem__(self, key: str, item: Any) -> None:
        self.data[key] = item

    def __and__(self, keyset: set) -> set:
        return set(self.data) & keyset

    def __or__(self, keyset: set) -> set:
        return set(self.data) | keyset

    def __xor__(self, keyset: set) -> set:
        return set(self.data) ^ keyset

    def __contains__(self, key: str) -> bool:
        return key in self.data

    def items(self) -> list[tuple[Any, Any]]:
        result = []

        for key, item in self.data.items():
            if isinstance(item, dict):
                item = JsonInstance(item)

            result.append((key, item))

        return result
