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
usage: page-xml-draw [-h] -i /path/to/input.xml -o /path/to/output.{png,jpg} [--base-dir /path/to/base/dir/] [--background] [--border]
                     [--print-space] [--text-regions] [--image-regions] [--line-drawing-regions] [--graphic-regions] [--table-regions]
                     [--chart-regions] [--separator-regions] [--maths-regions] [--chem-regions] [--music-regions] [--advert-regions]
                     [--noise-regions] [--unknown-regions] [--custom-regions] [--text-lines] [--words] [--glyphs] [--graphemes]
                     [--fill-color [COLOR]] [--edge-color [COLOR]] [--edge-thickness [1 .. inf]] [--opacity [0.0 .. 1.0]]

optional arguments:
  -h, --help                     show this help message and exit
  -i /path/to/input.xml          path to the input PAGE-XML file
  -o /path/to/output.{png,jpg}   path to the output image (PNG/JPEG) file
  --base-dir /path/to/base/dir/  path to the base directory for the image paths in the PAGE-XML file
  --background                   if this option is provided, the background of the page is drawn
  --border                       if this option is provided, the Border anottation of the page is drawn
  --print-space                  if this option is provided, the PrintSpace anottation of the page is drawn
  --text-regions                 if this option is provided, the TextRegion anottations of the page are drawn
  --image-regions                if this option is provided, the ImageRegion anottations of the page are drawn
  --line-drawing-regions         if this option is provided, the LineDrawingRegion anottations of the page are drawn
  --graphic-regions              if this option is provided, the GraphicRegion anottations of the page are drawn
  --table-regions                if this option is provided, the TableRegion anottations of the page are drawn
  --chart-regions                if this option is provided, the ChartRegion anottations of the page are drawn
  --separator-regions            if this option is provided, the SeparatorRegion anottations of the page are drawn
  --maths-regions                if this option is provided, the MathsRegion anottations of the page are drawn
  --chem-regions                 if this option is provided, the ChemRegion anottations of the page are drawn
  --music-regions                if this option is provided, the MusicRegion anottations of the page are drawn
  --advert-regions               if this option is provided, the AdvertRegion anottations of the page are drawn
  --noise-regions                if this option is provided, the NoiseRegion anottations of the page are drawn
  --unknown-regions              if this option is provided, the UnknownRegion anottations of the page are drawn
  --custom-regions               if this option is provided, the CustomRegion anottations of the page are drawn
  --text-lines                   if this option is provided, the TextLine anottations of the page are drawn
  --words                        if this option is provided, the Word anottations of the page are drawn
  --glyphs                       if this option is provided, the Glyph anottations of the page are drawn
  --graphemes                    if this option is provided, the Grapheme anottations of the page are drawn
  --fill-color [COLOR]           CSS3 name or RGB hex string of the color to fill the polygons with
  --edge-color [COLOR]           CSS3 name or RGB hex string of the color to draw the polygon edges with
  --edge-thickness [1 .. inf]    thickness of the edges of the polygons to be drawn
  --opacity [0.0 .. 1.0]         opacity of the polygons to be drawn
```

Examples
--------

Source of image: [GBN Dataset](https://web.inf.ufpr.br/vri/databases/gbn/)

PAGE-XML file generated through: [ocrd-gbn](https://github.com/GBN-DBP/ocrd-gbn) + [ocrd-export-larex](https://github.com/bertsky/workflow-configuration/blob/master/ocrd-export-larex) 

```
$ page-xml-draw \
  -i OCR-D-IMG_DerGemeindebote-p08.xml \
  -o OCR-D-IMG_DerGemeindebote-p08-contrast.png \
  --text-regions \
    --fill-color cyan \
    --edge-color darkblue \
    --edge-thickness 5 \
    --opacity 0.3 \
  --text-lines \
    --fill-color crimson \
    --edge-color darkred \
    --edge-thickness 3 \
    --opacity 0.3
```

![Contrast](assets/examples/OCR-D-IMG_DerGemeindebote-p08-contrast.png)

```
$ page-xml-draw \
  -i OCR-D-IMG_DerGemeindebote-p08.xml \
  -o OCR-D-IMG_DerGemeindebote-p08-binary.png \
  --background \
    --fill-color black \
    --opacity 1.0 \
  --text-lines \
    --fill-color white \
    --opacity 1.0
```

![Binary](assets/examples/OCR-D-IMG_DerGemeindebote-p08-binary.png)