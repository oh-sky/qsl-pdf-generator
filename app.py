import sys
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML, CSS
from adif_log_parser import AdifLogParser


OUTPUT_HTML_FILE = '/work/output/qsl-cards.html'
OUTPUT_PDF_FILE = '/work/output/qsl-cards.pdf'
CSS_FILE = '/work/styles/style.css'


def main():
    qsoLog = parseQsoLog()
    writeOutHtml(qsoLog=qsoLog)
    writeOutPDF()


def parseQsoLog():
    print('Parsing log ...', file=sys.stderr)
    return AdifLogParser.parse(filename='/work/input/qso-log.adif')


def writeOutHtml(qsoLog):
    print('Generating HTML ...', file=sys.stderr)
    env = Environment(loader=FileSystemLoader('./templates'))
    template = env.get_template('index.html')
    html = template.render({ 'qsos': qsoLog })

    fp = open(OUTPUT_HTML_FILE, 'w')
    fp.write(html)


def writeOutPDF():
    print('Generating PDF ...', file=sys.stderr)
    HTML(
        filename=OUTPUT_HTML_FILE
    ).write_pdf(
        target=OUTPUT_PDF_FILE,
        stylesheets=[CSS(CSS_FILE)]
    )


main()
