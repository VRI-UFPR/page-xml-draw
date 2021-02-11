import re
import inspect
import textwrap


# You must include the following class definition at the top of
#   your method specification file.
#
class MethodSpec(object):
    def __init__(self,
                 name='',
                 source='',
                 class_names='',
                 class_names_compiled=None):
        """MethodSpec -- A specification of a method.
        Member variables:
            name -- The method name
            source -- The source code for the method.  Must be
                indented to fit in a class definition.
            class_names -- A regular expression that must match the
                class names in which the method is to be inserted.
            class_names_compiled -- The compiled class names.
                generateDS.py will do this compile for you.
        """
        self.name = name
        self.source = source
        if class_names is None:
            self.class_names = ('.*', )
        else:
            self.class_names = class_names
        if class_names_compiled is None:
            self.class_names_compiled = re.compile(self.class_names)
        else:
            self.class_names_compiled = class_names_compiled

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_source(self):
        return self.source

    def set_source(self, source):
        self.source = source

    def get_class_names(self):
        return self.class_names

    def set_class_names(self, class_names):
        self.class_names = class_names
        self.class_names_compiled = re.compile(class_names)

    def get_class_names_compiled(self):
        return self.class_names_compiled

    def set_class_names_compiled(self, class_names_compiled):
        self.class_names_compiled = class_names_compiled

    def match_name(self, class_name):
        """Match against the name of the class currently being generated.
        If this method returns True, the method will be inserted in
          the generated class.
        """
        if self.class_names_compiled.search(class_name):
            return True
        else:
            return False

    def get_interpolated_source(self, values_dict):
        """Get the method source code, interpolating values from values_dict
        into it.  The source returned by this method is inserted into
        the generated class.
        """
        source = self.source % values_dict
        return source

    def show(self):
        print('specification:')
        print('    name: %s' % (self.name, ))
        print(self.source)
        print('    class_names: %s' % (self.class_names, ))
        print('    names pat  : %s' % (self.class_names_compiled.pattern, ))


def get_Coords_polygon(self):
    '''
    Get polygon from element which is parent of a Coords element
    '''
    points = [point for point in self.Coords.points.split(' ')]
    return [[int(coord) for coord in point.split(',')] for point in points]


def get_Page_polygon(self):
    '''
    Get polygon from Page element (whole image)
    '''
    x0y0 = [0, 0]
    x1y0 = [self.imageWidth - 1, 0]
    x1y1 = [self.imageWidth - 1, self.imageHeight - 1]
    x0y1 = [0, self.imageHeight - 1]

    return [x0y0, x1y0, x1y1, x0y1, x0y0]


def get_imageFilename(self):
    '''
    Get image filename from root
    '''
    return self.Page.imageFilename


def make_class_names(names):
    '''
    Concatenate class types in string for method spec
    '''
    return '^(' + '|'.join(names) + ')'


get_Coords_polygon_name = "get_polygon"
get_Page_polygon_name = "get_polygon"
get_imageFilename_name = "get_imageFilename"

get_Coords_polygon_class_names = make_class_names(
    [
        "BorderType",
        "PrintSpaceType",
        "RegionType",
        "TextLineType",
        "WordType",
        "GlyphType",
        "GraphemeType"
    ]
)
get_Page_polygon_class_names = make_class_names(
    [
        "PageType"
    ]
)
get_imageFilename_class_names = make_class_names(
    [
        "PcGtsType"
    ]
)

get_Coords_polygon_source = textwrap.indent(
    inspect.getsource(get_Coords_polygon).replace(
        "get_Coords_polygon",
        "get_polygon"
    ),
    ' ' * 4
)
get_Page_polygon_source = textwrap.indent(
    inspect.getsource(get_Page_polygon).replace(
        "get_Page_polygon",
        "get_polygon"
    ),
    ' ' * 4
)
get_imageFilename_source = textwrap.indent(
    inspect.getsource(get_imageFilename),
    ' ' * 4
)

METHOD_SPECS = (
    MethodSpec(
        name=get_Coords_polygon_name,
        class_names=get_Coords_polygon_class_names,
        source=get_Coords_polygon_source
    ),
    MethodSpec(
        name=get_Page_polygon_name,
        class_names=get_Page_polygon_class_names,
        source=get_Page_polygon_source
    ),
    MethodSpec(
        name=get_imageFilename_name,
        class_names=get_imageFilename_class_names,
        source=get_imageFilename_source
    )
)
