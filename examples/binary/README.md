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
  --page \
    --fill-color black \
    --opacity 1.0 \
    --text-region
      --text-line \
        --fill-color white \
        --opacity 1.0
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
        "Drawing/FillColor": "black",
        "Drawing/Opacity": 1.0,
        "PAGE-XML/TextRegion": {
            "PAGE-XML/TextLine": {
                "Drawing/FillColor": "white",
                "Drawing/Opacity": 1.0
            }
        }
    }
}
```

Output
------

| [![Original](../../assets/images/OCR-D-IMG_DerGemeindebote-p08.png)](Original) | [![Binary](output.png)](Binary) |
|:---:|:---:|