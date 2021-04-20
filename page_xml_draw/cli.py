import os
import argparse

from pathlib import Path
from json import loads

from page_xml_draw.struct.json import JsonSchema, JsonInstance


def kebab2camel(string):
    '''
    Converts kebab-case to CamelCase
    Based on https://stackoverflow.com/a/1176023
    '''
    return ''.join(word.title() for word in string.split('-'))


class HelpFormatter(argparse.HelpFormatter):
    '''
    Help Formatter for custom help spacing and usage instructions formatting
    Based on https://stackoverflow.com/a/31124505
    '''
    def __init__(self, prog):
        super().__init__(prog, max_help_position=60, width=120)

    def _format_action_invocation(self, action):
        if not action.option_strings or action.nargs == 0:
            return super()._format_action_invocation(action)

        default = self._get_default_metavar_for_optional(action)
        args_string = self._format_args(action, default)
        return ', '.join(action.option_strings) + ' ' + args_string


class Namespace(argparse.Namespace):
    def __init__(self, schema):
        super().__init__()

        # Save json schema:
        self.schema = schema

        # Initialize instance of json struct to be built:
        self.instance = {}

        # Initialize stack with current annotation name, schema and instance:
        self.stack = [(None, self.schema, self.instance)]


class PageXmlAction(argparse.Action):
    # Flag (no args):
    def __init__(self, nargs=0, **kw):
        super().__init__(nargs=nargs, **kw)

    def __call__(self, parser, namespace, values, option_string=None):
        # Get annotation name from kebab-case CLI option name and convert it to
        # CamelCase to match PAGE-XML format:
        annot = kebab2camel(option_string)

        # Get previously declared annotation:
        _, schema, instance = namespace.stack[-1]

        # If current annotation is not a child of the last one, go back
        # until a valid parent is found:
        while len(namespace.stack) > 1 and not schema.has_property(annot):
            namespace.stack.pop()
            _, schema, instance = namespace.stack[-1]

        if len(namespace.stack) <= 1 and not schema.has_property(annot):
            raise argparse.ArgumentError(
                "Unable to find parent annotation of '%s' in specified tree "
                "structure" % annot
            )

        # Get subschema for current annotation:
        schema = schema.get_property(annot)

        # Initialize json instance for current annotation::
        instance[annot] = {}
        instance = instance[annot]

        # Push annotation info:
        namespace.stack.append((annot, schema, instance))


class DrawingAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        # Get attribute name from kebab-case CLI option name and convert it to
        # CamelCase:
        attr = kebab2camel(option_string)

        # Get previously declared annotation:
        annot, schema, instance = namespace.stack[-1]

        # Check is annotation supports this drawing attribute:
        if schema.get_property("Style").has_property(attr):
            # Save attribute:
            if "Style" not in instance:
                instance["Style"] = {}

            instance["Style"][attr] = values
        else:
            raise argparse.ArgumentError(
                "Annotation '%s' has no attribute '%s'" % (annot, attr)
            )


def get_opts():
    # Load schema from package files:
    schema = JsonSchema.default()

    parser = argparse.ArgumentParser(
        formatter_class=lambda prog: HelpFormatter(prog)
    )

    parser.add_argument(
        "-i", "--input",
        type=Path,
        dest="input",
        required=True,
        metavar=("<path/to/file>.xml"),
        help="path to input PAGE-XML file"
    )

    parser.add_argument(
        "-o", "--output",
        type=Path,
        dest="output",
        required=True,
        metavar=("<path/to/file>.png"),
        help="path to output image file"
        # TODO: Support other extensions like TIFF
    )

    parser.add_argument(
        "-b", "--base-dir",
        type=Path,
        dest="base_dir",
        default=Path.cwd(),
        metavar=("<path/to/dir>"),
        help="path to base directory relative to PAGE-XML file content"
    )

    parser.add_argument(
        "-p", "--profile",
        type=Path,
        dest="profile",
        metavar=("<path/to/file>.json"),
        help="path to pre-defined json profile describing what has to be done"
    )

    parser.add_argument(
        "--html",
        action="store_true",
        help="output HTML image map instead of image"
    )

    parser.add_argument(
        "--page",
        action=PageXmlAction,
        help="visit the 'Page' PAGE-XML annotations"
    )

    parser.add_argument(
        "--border",
        action=PageXmlAction,
        help="visit the 'Border' PAGE-XML annotations"
    )

    parser.add_argument(
        "--print-space",
        action=PageXmlAction,
        help="visit the 'PrintSpace' PAGE-XML annotations"
    )

    parser.add_argument(
        "--text-region",
        action=PageXmlAction,
        help="visit the 'TextRegion' PAGE-XML annotations"
    )

    parser.add_argument(
        "--image-region",
        action=PageXmlAction,
        help="visit the 'ImageRegion' PAGE-XML annotations"
    )

    parser.add_argument(
        "--line-drawing-region",
        action=PageXmlAction,
        help="visit the 'LineDrawingRegion' PAGE-XML annotations"
    )

    parser.add_argument(
        "--graphic-region",
        action=PageXmlAction,
        help="visit the 'GraphicRegion' PAGE-XML annotations"
    )

    parser.add_argument(
        "--table-region",
        action=PageXmlAction,
        help="visit the 'TableRegion' PAGE-XML annotations"
    )

    parser.add_argument(
        "--chart-region",
        action=PageXmlAction,
        help="visit the 'ChartRegion' PAGE-XML annotations"
    )

    parser.add_argument(
        "--map-region",
        action=PageXmlAction,
        help="visit the 'MapRegion' PAGE-XML annotations"
    )

    parser.add_argument(
        "--separator-region",
        action=PageXmlAction,
        help="visit the 'SeparatorRegion' PAGE-XML annotations"
    )

    parser.add_argument(
        "--maths-region",
        action=PageXmlAction,
        help="visit the 'MathsRegion' PAGE-XML annotations"
    )

    parser.add_argument(
        "--chem-region",
        action=PageXmlAction,
        help="visit the 'ChemRegion' PAGE-XML annotations"
    )

    parser.add_argument(
        "--music-region",
        action=PageXmlAction,
        help="visit the 'MusicRegion' PAGE-XML annotations"
    )

    parser.add_argument(
        "--advert-region",
        action=PageXmlAction,
        help="visit the 'AdvertRegion' PAGE-XML annotations"
    )

    parser.add_argument(
        "--noise-region",
        action=PageXmlAction,
        help="visit the 'NoiseRegion' PAGE-XML annotations"
    )

    parser.add_argument(
        "--unknown-region",
        action=PageXmlAction,
        help="visit the 'UnknownRegion' PAGE-XML annotations"
    )

    parser.add_argument(
        "--custom-region",
        action=PageXmlAction,
        help="visit the 'CustomRegion' PAGE-XML annotations"
    )

    parser.add_argument(
        "--text-line",
        action=PageXmlAction,
        help="visit the 'TextLine' PAGE-XML annotations"
    )

    parser.add_argument(
        "--word",
        action=PageXmlAction,
        help="visit the 'Word' PAGE-XML annotations"
    )

    parser.add_argument(
        "--glyph",
        action=PageXmlAction,
        help="visit the 'Glyph' PAGE-XML annotations"
    )

    parser.add_argument(
        "--graphemes",
        action=PageXmlAction,
        help="visit the 'Graphemes' PAGE-XML annotations"
    )

    parser.add_argument(
        "--grapheme",
        action=PageXmlAction,
        help="visit the 'Grapheme' PAGE-XML annotations"
    )

    parser.add_argument(
        "--fill-color",
        type=str,
        action=DrawingAction,
        metavar=("(<hex> | <name>)"),
        help="fill annotation polygons with specified color"
    )

    parser.add_argument(
        "--fill-opacity",
        type=float,
        action=DrawingAction,
        metavar=("[0.0 - 1.0]"),
        help="fill annotation polygons with specified opacity"
    )

    parser.add_argument(
        "--stroke-color",
        type=str,
        action=DrawingAction,
        metavar=("(<hex> | <name>)"),
        help="draw annotation polygon strokes with specified color"
    )

    parser.add_argument(
        "--stroke-opacity",
        type=float,
        action=DrawingAction,
        metavar=("[0.0 - 1.0]"),
        help="draw annotation polygon strokes with specified opacity"
    )

    parser.add_argument(
        "--stroke-width",
        type=int,
        action=DrawingAction,
        metavar=("[0 .. +inf]"),
        help="draw annotation polygon strokes with specified width/thickness"
    )

    options = parser.parse_args(namespace=Namespace(schema))

    input_abs = options.input.absolute()

    if not input_abs.exists():
        raise argparse.ArgumentError(
            "Cannot read input: '%s' does not exist" % input_abs
        )

    if not input_abs.is_file():
        raise argparse.ArgumentError(
            "Cannot read input: '%s' is not a file" % input_abs
        )

    if not os.access(input_abs, os.R_OK):
        raise argparse.ArgumentError(
            "Cannot read input: '%s' is not readable" % input_abs
        )

    output_abs = options.output.absolute()

    # Check directory where output will be written:
    output_dir = output_abs.parents[0]

    if not output_dir.exists():
        raise argparse.ArgumentError(
            "Cannot write output: '%s' does not exist" % output_dir
        )

    if not output_dir.is_dir():
        raise argparse.ArgumentError(
            "Cannot write output: '%s' is not a directory" % output_dir
        )

    if not os.access(output_dir, os.W_OK):
        raise argparse.ArgumentError(
            "Cannot write output: '%s' is not writable" % output_dir
        )

    base_dir_abs = options.base_dir.absolute()

    if not base_dir_abs.exists():
        raise argparse.ArgumentError(
            "Base directory '%s' does not exist" % base_dir_abs
        )

    if not base_dir_abs.is_dir():
        raise argparse.ArgumentError(
            "Base directory '%s' is not a directory" % base_dir_abs
        )

    if not os.access(base_dir_abs, os.R_OK):
        raise argparse.ArgumentError(
            "Base directory '%s' is not readable" % base_dir_abs
        )

    if options.html:
        output_format = "text/html"
    else:
        output_format = "image/png"

    if options.profile:
        with open(str(options.profile), 'r') as fp:
            instance = loads(fp.read())
    else:
        instance = options.instance

    instance = JsonInstance(instance)

    # Validate json instance against schema:
    schema.validate(instance)

    return input_abs, output_abs, base_dir_abs, output_format, instance
