"""main routine of qsl-pdf-generator"""
import sys
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML, CSS
from adif_log_parser import AdifLogParser


OUTPUT_HTML_FILE = '/work/output/qsl-cards.html'
OUTPUT_PDF_FILE = '/work/output/qsl-cards.pdf'
CSS_FILE = '/work/styles/style.css'


def main():
    """ main routine """
    qso_log = parse_qso_log()
    write_out_html(qso_log=qso_log)
    write_out_pdf()


def parse_qso_log():
    """ parse qso log from log file """
    print('Parsing log ...', file=sys.stderr)
    return AdifLogParser.parse(filename='/work/input/qso-log.adif')


def write_out_html(qso_log):
    """ write out html file based on QSO log """
    print('Generating HTML ...', file=sys.stderr)
    env = Environment(loader=FileSystemLoader('./templates'))
    template = env.get_template('index.html')
    html = template.render({ 'qsos': qso_log })

    file = open(OUTPUT_HTML_FILE, 'w', encoding='utf-8')
    file.write(html)


def write_out_pdf():
    """ write out PDF file by printing HTML and CSS files """
    print('Generating PDF ...', file=sys.stderr)
    HTML(
        filename=OUTPUT_HTML_FILE
    ).write_pdf(
        target=OUTPUT_PDF_FILE,
        stylesheets=[CSS(CSS_FILE)]
    )


main()
