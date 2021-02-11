page-xml-draw
=============

A powerful CLI tool for visualization and encoding of [PAGE-XML](https://github.com/PRImA-Research-Lab/PAGE-XML) files.

Developed in order to enable the process of parsing PAGE-XML files and drawing their layout annotations on the pages images without having to write code, while still providing the maximum of the [OpenCV](https://opencv.org/) polygon drawing capabilities to the user.

Built around the [2019-07-15 Page Content PAGE-XML schema](https://www.primaresearch.org/schema/PAGE/gts/pagecontent/2019-07-15/pagecontent.xsd).

Supports colors in RGB hex string format (e.g. `ffffff`) and also color names following the [CSS3 convention](https://www.w3.org/TR/2018/REC-css-color-3-20180619/) through the [webcolors package](https://pypi.org/project/webcolors/). 

Table of contents
=================

<!--ts-->
   * [page-xml-draw](#page-xml-draw)
   * [Installation](#installation)
   * [Usage](#usage)
      * [Help Manual](#help-manual)
      * [Examples](#examples)
<!--te-->

Installation
============

```
git clone https://github.com/GBN-DBP/page-xml-draw.git
cd page-xml-draw/
pip3 install .
```

or simply

```
pip3 install git+https://github.com/GBN-DBP/page-xml-draw.git
```

Usage
=====

Help Manual
-----------

```
usage: page-xml-draw [-h] -i <path/to/file>.xml -o <path/to/file>.{png,jpg} [-b <path/to/dir>] [-p <path/to/file>.json]
                     [--page] [--border] [--print-space] [--text-region] [--image-region] [--line-drawing-region]
                     [--graphic-region] [--table-region] [--chart-region] [--map-region] [--separator-region]
                     [--maths-region] [--chem-region] [--music-region] [--advert-region] [--noise-region]
                     [--unknown-region] [--custom-region] [--text-line] [--word] [--glyph] [--graphemes] [--grapheme]
                     [--fill-color (<hex> | <name>)] [--edge-color (<hex> | <name>)] [--edge-thickness [0 .. +inf]]
                     [--opacity [0.0 - 1.0]]

optional arguments:
  -h, --help                             show this help message and exit
  -i, --input <path/to/file>.xml         path to input PAGE-XML file
  -o, --output <path/to/file>.{png,jpg}  path to output image file
  -b, --base-dir <path/to/dir>           path to base directory relative to PAGE-XML file content
  -p, --profile <path/to/file>.json      path to pre-defined json profile describing what has to be done
  --page                                 visit the 'Page' PAGE-XML annotations
  --border                               visit the 'Border' PAGE-XML annotations
  --print-space                          visit the 'PrintSpace' PAGE-XML annotations
  --text-region                          visit the 'TextRegion' PAGE-XML annotations
  --image-region                         visit the 'ImageRegion' PAGE-XML annotations
  --line-drawing-region                  visit the 'LineDrawingRegion' PAGE-XML annotations
  --graphic-region                       visit the 'GraphicRegion' PAGE-XML annotations
  --table-region                         visit the 'TableRegion' PAGE-XML annotations
  --chart-region                         visit the 'ChartRegion' PAGE-XML annotations
  --map-region                           visit the 'MapRegion' PAGE-XML annotations
  --separator-region                     visit the 'SeparatorRegion' PAGE-XML annotations
  --maths-region                         visit the 'MathsRegion' PAGE-XML annotations
  --chem-region                          visit the 'ChemRegion' PAGE-XML annotations
  --music-region                         visit the 'MusicRegion' PAGE-XML annotations
  --advert-region                        visit the 'AdvertRegion' PAGE-XML annotations
  --noise-region                         visit the 'NoiseRegion' PAGE-XML annotations
  --unknown-region                       visit the 'UnknownRegion' PAGE-XML annotations
  --custom-region                        visit the 'CustomRegion' PAGE-XML annotations
  --text-line                            visit the 'TextLine' PAGE-XML annotations
  --word                                 visit the 'Word' PAGE-XML annotations
  --glyph                                visit the 'Glyph' PAGE-XML annotations
  --graphemes                            visit the 'Graphemes' PAGE-XML annotations
  --grapheme                             visit the 'Grapheme' PAGE-XML annotations
  --fill-color (<hex> | <name>)          fill annotation polygons with specified color
  --edge-color (<hex> | <name>)          draw annotation polygon edges with specified color
  --edge-thickness [0 .. +inf]           draw annotation polygon edges with specified thickness
  --opacity [0.0 - 1.0]                  draw annotation polygons with specified opacity
```

Examples
--------

- [Semi-transparent contrasting example](examples/contrast/README.md)
- [Opaque binary (black-and-white) example](examples/binary/README.md)