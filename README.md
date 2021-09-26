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
# e.g. You have log202108.adi and log202109.adif
# cp log202108.adi log202109.adif ./input
#
docker-compose build
docker-compose up
#
# You'd get PDF files  under ./output
# (e.g. log202108.adi.pdf and log202109.adif.pdf)
#
#
```
