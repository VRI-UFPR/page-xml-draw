import copy
import json
import jsonschema


class Schema():
    def __init__(self, data, resolver=None):
        self.data = data

        if resolver is None:
            self.resolver = jsonschema.RefResolver.from_schema(self.data)
        else:
            self.resolver = resolver

    @staticmethod
    def from_string(string):
        return Schema(json.loads(string))

    @staticmethod
    def from_stream(stream):
        return Schema.from_string(stream.read())

    def __getitem__(self, key):
        item = self.data[key]

        if isinstance(item, dict):
            return Schema(item, resolver=self.resolver)
        else:
            return item

    def has_property(self, prop):
        return prop in self.data['properties']

    def get_property(self, prop):
        prop_data = copy.deepcopy(self.data['properties'][prop])

        while '$ref' in prop_data:
            ref = self.resolver.resolve(prop_data.pop('$ref'))[1]

            for key, item in ref.items():
                if key not in prop_data:
                    prop_data[key] = item

        return Schema(prop_data, resolver=self.resolver)

    def validate(self, instance):
        jsonschema.validate(instance, self.data)
