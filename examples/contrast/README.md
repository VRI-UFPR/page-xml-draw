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
      --fill-opacity 0.3 \
      --stroke-color darkblue \
      --stroke-opacity 0.3 \
      --stroke-width 5 \
      --text-line \
        --fill-color crimson \
        --fill-opacity 0.3
        --stroke-color darkred \
        --stroke-opacity 0.3 \
        --stroke-width 3
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
    "Page": {
        "TextRegion": {
            "FillColor": "cyan",
            "FillOpacity": 0.3,
            "StrokeColor": "darkblue",
            "StrokeOpacity": 0.3,
            "StrokeWidth": 5,
            "TextLine": {
                "FillColor": "crimson",
                "FillOpacity": 0.3,
                "StrokeColor": "darkred",
                "StrokeOpacity": 0.3,
                "StrokeWidth": 3
            }
        }
    }
}
```

Output
------

| [![Original](../../assets/images/OCR-D-IMG_DerGemeindebote-p08.png)](Original) | [![Contrast](output.png)](Binary) |
|:---:|:---:|