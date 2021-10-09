"""
main routine of qsl-pdf-generator
"""
import sys
import typing
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML, CSS
from qsl_pdf_publisher.log_file_utils.get_log_file_list import get_log_file_list
from qsl_pdf_publisher.log_file_utils.parse_qso_log import parse_qso_log
from qsl_pdf_publisher.log_file_utils.sort import sort_by_callsign
from qsl_pdf_publisher.user_config import read_user_config_file
from qsl_pdf_publisher.qso import Qso

INPUT_DIRECTORY = '/work/input/'
OUTPUT_DIRECTORY = '/work/output/'
CSS_FILE = '/work/styles/style.css'


def main() -> None:
    """
    main routine
    """

    log_files = get_log_file_list(INPUT_DIRECTORY)
    user_config = read_user_config_file()

    for log_file in log_files:
        print(f'starting to process {log_file.basename} ...', file=sys.stderr)
        html_file_path = OUTPUT_DIRECTORY + log_file.basename + '.html'
        pdf_file_path = OUTPUT_DIRECTORY + log_file.basename + '.pdf'

        qso_log = parse_qso_log(log_file_path=log_file.path)
        if user_config.output_settings.sort_by_callsign if user_config else None:
            qso_log = sort_by_callsign(qso_log)

        write_out_html(qso_log=qso_log, html_file_path=html_file_path)
        write_out_pdf(html_file_path=html_file_path,
                      css_file_path=CSS_FILE,
                      pdf_file_path=pdf_file_path)


def write_out_html(qso_log: typing.Tuple[Qso, ...], html_file_path: str) -> None:
    """ write out html file based on QSO log """
    print('  Generating HTML ...', file=sys.stderr)
    env = Environment(loader=FileSystemLoader('./templates'))
    template = env.get_template('index.html')
    html = template.render({'qsos': qso_log})

    with open(html_file_path, 'w', encoding='utf-8') as html_file:
        html_file.write(html)


def write_out_pdf(html_file_path: str, css_file_path: str, pdf_file_path: str) -> None:
    """ write out PDF file by printing HTML and CSS files """
    print('  Generating PDF ...', file=sys.stderr)
    HTML(
        filename=html_file_path
    ).write_pdf(
        target=pdf_file_path,
        stylesheets=[CSS(css_file_path)]
    )


main()
