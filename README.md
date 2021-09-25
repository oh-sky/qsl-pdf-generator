# QSL PDF Generator

It generates the QSL cards as PDF file from QSO log.

# Usage

```bash
git clone git@github.com:oh-sky/qsl-pdf-generator.git
cd qsl-pdf-generator
#
# prepar log
# put ADIF files (*.adif) into ./input
#
docker-compose build
docker-compose up
#
# you'd get pdf file under ./output
#
```
