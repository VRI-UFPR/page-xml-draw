# PAGE XML Draw

A CLI application that enables quick visualization of [PAGE-XML](https://github.com/PRImA-Research-Lab/PAGE-XML) files using python.

* adicionar imagem exemplo

## Installing

### Manually

1. Clone this repository
2. (Recommended) activate a virtual environment 
3. `cd [path/to/cloned/repo]`
4. `pip install .`

## Usage

`python3 page-xml-draw -i [path/to/page.xml] -o [path/to/output.png] --base-dir [path/to/base/directory]`

* `--border` draws the document border, often omitted in PAGE.xml files that skip the cropping stage.

* `--text-regions` draws the text regions described in the file.

* `--text-lines` draws the text lines within the text regions.

* `--fill-color [COLOR]` determines the interior color of each overlay

* `--outline-color [COLOR]` determines the outline's color of each overlay.

* `--thickness [THICKNESS]` determines how thick the lines of each overlay are.

It is also possible to provide arguments in json format, through the `--json-file [path/to/file.json]` option.

Colors are provided by [webcolors](https://webcolors.readthedocs.io/en/1.11.1/index.html).
