class Instance():
    '''
    Utilities for parsing a JSON instance
    '''
    def __init__(self, data, traverser):
        self.data = data
        self.traverser = traverser

    def __bool__(self):
        '''
        Operator override for boolean evaluation
        '''
        return bool(self.data)

    def __getitem__(self, key):
        '''
        Operator override for dict-like access (read)
        '''
        item = self.data[key]

        if isinstance(item, dict):
            return Instance(item, self.traverser)
        else:
            return item

    def __setitem__(self, key, item):
        '''
        Operator override for dict-like access (write)
        '''
        self.data[key] = item

    def __contains__(self, key):
        '''
        Operator override for checking if a key is contained
        '''
        return key in self.data

    def items(self):
        '''
        Retrieve keys and their respective items
        '''
        keys = []
        items = []

        for key, item in self.data.items():
            keys.append(key)

            if isinstance(item, dict):
                items.append(Instance(item, self.traverser))
            else:
                items.append(item)

        return zip(keys, items)

    def get_properties_by_prefix(self, prefix):
        '''
        Retrieve properties with specified prefix
        '''
        items = Instance({}, self.traverser)

        for key, item in self.items():
            if key.startswith(prefix):
                suffix = key.split('/').pop()

                items[suffix] = item

        return items

    def draw(self):
        '''
        Invoke traverser with retrieved drawing properties
        '''
        if 'FillColor' not in self:
            self['FillColor'] = None

        if 'EdgeColor' not in self:
            self['EdgeColor'] = None
            self['EdgeThickness'] = None

        if 'EdgeColor' in self and 'EdgeThickness' not in self:
            # Fallback edge thickness:
            self['EdgeThickness'] = 1

        if 'Opacity' not in self:
            # Fallback opacity:
            self['Opacity'] = 0.3

        self.traverser.draw_focused(
            self['FillColor'],
            self['EdgeColor'],
            self['EdgeThickness'],
            self['Opacity']
        )

    def map(self):
        '''
        Invoke traverser with retrieved drawing properties
        '''
        if 'FillColor' not in self:
            self['FillColor'] = None

        if 'EdgeColor' not in self:
            self['EdgeColor'] = None
            self['EdgeThickness'] = None

        if 'EdgeColor' in self and 'EdgeThickness' not in self:
            # Fallback edge thickness:
            self['EdgeThickness'] = 1

        if 'Opacity' not in self:
            # Fallback opacity:
            self['Opacity'] = 0.3

        self.traverser.map_focused(
            self['FillColor'],
            self['EdgeColor'],
            self['EdgeThickness'],
            self['Opacity']
        )

    def traverse_and_draw(self):
        '''
        Traverse PAGE-XML tree as specified in JSON instance and draw layout
        annotations accordingly
        '''
        page_props = self.get_properties_by_prefix('PAGE-XML')
        drawing_props = self.get_properties_by_prefix('Drawing')

        # Only draw if drawing properties are specified:
        if drawing_props:
            drawing_props.draw()

        for key, item in page_props.items():
            self.traverser.focus_on_children(key)
            item.traverse_and_draw()
            self.traverser.focus_on_parents()

    def traverse_and_map(self):
        '''
        Traverse PAGE-XML tree as specified in JSON instance and map layout
        annotations accordingly
        '''
        page_props = self.get_properties_by_prefix('PAGE-XML')
        drawing_props = self.get_properties_by_prefix('Drawing')

        # Only draw if drawing properties are specified:
        if drawing_props:
            drawing_props.map()

        for key, item in page_props.items():
            self.traverser.focus_on_children(key)
            item.traverse_and_map()
            self.traverser.focus_on_parents()
