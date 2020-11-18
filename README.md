# PAGE XML Draw

A CLI application that enables quick visualization of [PAGE-XML](https://github.com/PRImA-Research-Lab/PAGE-XML) files using python.

* adicionar imagem exemplo

## Usage

* guia de instalação

`python3 page-xml-draw -i [path/to/page.xml] -o [path/to/output.png] --base-dir [path/to/base/directory]`

* `--border` draws the document border, often omitted in PAGE.xml files that skip the cropping stage.

* `--text-regions` draws the text regions described in the file.

* `--text-lines` draws the text lines within the text regions.

* `--fill-color [COLOR]` determines the interior color of each overlay

* `--outline-color [COLOR]` determines the outline's color of each overlay.

* `--thickness [THICKNESS]` determines how thick the lines of each overlay are.

Colors are provided by [webcolors](https://webcolors.readthedocs.io/en/1.11.1/index.html).
