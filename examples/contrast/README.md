Contrast Example
================

Source of [image](../../assets/images/OCR-D-IMG_DerGemeindebote-p08.png): [GBN Dataset](https://web.inf.ufpr.br/vri/databases/gbn/)

[PAGE-XML file](../input.xml) generated through: [ocrd-gbn](https://github.com/GBN-DBP/ocrd-gbn) + [ocrd-export-larex](https://github.com/bertsky/workflow-configuration/blob/master/ocrd-export-larex) 

Pure CLI
--------

```bash
$ page-xml-draw \
  -i ../input.xml \
  -o output.png \
  --base-dir ../../assets/images
  --page
    --text-region \
      --fill-color cyan \
      --edge-color darkblue \
      --edge-thickness 5 \
      --opacity 0.3 \
      --text-line \
        --fill-color crimson \
        --edge-color darkred \
        --edge-thickness 3 \
        --opacity 0.3
```

CLI + JSON
----------

```bash
$ page-xml-draw \
  -i ../input.xml \
  -o output.png \
  --base-dir ../../assets/images
  --profile profile.json
```

where the content of [profile.json](profile.json) is

```json
{
    "PAGE-XML/Page": {
        "PAGE-XML/TextRegion": {
            "Drawing/FillColor": "cyan",
            "Drawing/EdgeColor": "darkblue",
            "Drawing/EdgeThickness": 5,
            "Drawing/Opacity": 0.3,
            "PAGE-XML/TextLine": {
                "Drawing/FillColor": "crimson",
                "Drawing/EdgeColor": "darkred",
                "Drawing/EdgeThickness": 3,
                "Drawing/Opacity": 0.3
            }
        }
    }
}
```

Output
------

<img src="../../assets/images/OCR-D-IMG_DerGemeindebote-p08.png" width="45%"/>
<img src="output.png" width="45%"/> 