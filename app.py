"""main routine of qsl-pdf-generator"""
import glob
import os
import sys
from typing import NamedTuple
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML, CSS
from adif_log_parse import adif_log_parse

INPUT_DIRECTORY = '/work/input/'
OUTPUT_DIRECTORY = '/work/output/'
CSS_FILE = '/work/styles/style.css'


def main():
    """ main routine """

    log_files = get_log_file_list(INPUT_DIRECTORY)

    for log_file in log_files:
        print(f'starting to process {log_file.basename} ...', file=sys.stderr)
        html_file_path = OUTPUT_DIRECTORY + log_file.basename + '.html'
        pdf_file_path = OUTPUT_DIRECTORY + log_file.basename + '.pdf'
        qso_log = parse_qso_log(log_file_path=log_file.path)
        write_out_html(qso_log=qso_log, html_file_path=html_file_path)
        write_out_pdf(html_file_path=html_file_path,
                      css_file_path=CSS_FILE,
                      pdf_file_path=pdf_file_path)


class LogFile(NamedTuple):
    """ named tuple which has basename and path """
    basename: str
    path: str


def get_log_file_list(search_directory: str) -> tuple:
    """ get log File list """
    log_file_list = []
    file_patterns = ('*.adi', '*.adif')

    for file_pattern in file_patterns:
        filepaths = glob.glob(os.path.join(search_directory, file_pattern))
        for filepath in filepaths:
            log_file_list.append(LogFile(
                basename=os.path.basename(filepath),
                path=filepath
            ))

    return tuple(log_file_list)


def parse_qso_log(log_file_path: str):
    """ parse qso log from log file """
    print('  Parsing log ...', file=sys.stderr)
    return adif_log_parse(filename=log_file_path)


def write_out_html(qso_log: list, html_file_path: str):
    """ write out html file based on QSO log """
    print('  Generating HTML ...', file=sys.stderr)
    env = Environment(loader=FileSystemLoader('./templates'))
    template = env.get_template('index.html')
    html = template.render({'qsos': qso_log})

    with open(html_file_path, 'w', encoding='utf-8') as html_file:
        html_file.write(html)


def write_out_pdf(html_file_path: str, css_file_path: str, pdf_file_path: str):
    """ write out PDF file by printing HTML and CSS files """
    print('  Generating PDF ...', file=sys.stderr)
    HTML(
        filename=html_file_path
    ).write_pdf(
        target=pdf_file_path,
        stylesheets=[CSS(css_file_path)]
    )


main()
