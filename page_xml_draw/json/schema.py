import copy
import json
import jsonschema


class Schema():
    '''
    Utilities for parsing the JSON schema
    '''
    def __init__(self, data, resolver=None):
        self.data = data

        if resolver is None:
            self.resolver = jsonschema.RefResolver.from_schema(self.data)
        else:
            self.resolver = resolver

    @staticmethod
    def from_string(string):
        '''
        Get dictionary structure from JSON string
        '''
        return Schema(json.loads(string))

    @staticmethod
    def from_stream(stream):
        '''
        Get dictionary structure from JSON file stream
        '''
        return Schema.from_string(stream.read())

    def __getitem__(self, key):
        '''
        Operator override for dict-like access (read)
        '''
        item = self.data[key]

        if isinstance(item, dict):
            return Schema(item, resolver=self.resolver)
        else:
            return item

    def has_property(self, prop):
        '''
        Check if schema object contains the specified property
        '''
        return prop in self.data['properties']

    def get_property(self, prop):
        '''
        Retrieve schema under specified property
        '''
        # Copy subschema so the main schema is not modified:
        prop_data = copy.deepcopy(self.data['properties'][prop])

        # Recursively resolve any reference in first level of subschema:
        while '$ref' in prop_data:
            ref = self.resolver.resolve(prop_data.pop('$ref'))[1]

            for key, item in ref.items():
                if key not in prop_data:
                    prop_data[key] = item

        # Keep parent schema resolver so all the definitions are reachable:
        return Schema(prop_data, resolver=self.resolver)

    def validate(self, instance):
        '''
        Validate JSON instance against schema
        '''
        jsonschema.validate(instance, self.data)
