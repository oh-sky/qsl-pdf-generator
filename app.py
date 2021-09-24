import sys
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML, CSS


OUTPUT_HTML_FILE = '/work/output/qsl-cards.html'
OUTPUT_PDF_FILE = '/work/output/qsl-cards.pdf'
CSS_FILE = '/work/styles/style.css'


def main():
    qsoLog = parseQsoLog()
    writeOutHtml(qsoLog=qsoLog)
    writeOutPDF()


def parseQsoLog():
    print('Parsing log ...', file=sys.stderr)
    return {
        'qsos': [
            {
                'callsign': 'JJ1AYZ/1',
                'transferCallsign': 'JJ1AYZ',
                'date': '12th/Aug/2021',
                'time': '11:05',
                'rst': '51',
                'band': '430MHz',
                'mode': 'FM',
                'rig': 'FT-818ND',
                'power': '5W',
                'antenna': '3 ele Yagi',
                'groundHeight': '1mh',
                'qth': '東京都北区 飛鳥山公園 #100117',
                'remarks': 'FBな1st QSO、ありがとうございました。',
            },
            {
                'callsign': '123456',
                'transferCallsign': '123456',
                'date': '13th/Sep/2021',
                'time': '14:59',
                'rst': '599',
                'band': '7MHz',
                'mode': 'A1A',
                'rig': 'FT-450D',
                'power': '50W',
                'antenna': 'DP',
                'groundHeight': '10mh',
                'qth': '常置場所',
                'remarks': 'いつもありがとうございます。',
            }
        ]
    }


def writeOutHtml(qsoLog):
    print('Generating HTML ...', file=sys.stderr)
    env = Environment(loader=FileSystemLoader('./templates'))
    template = env.get_template('index.html')
    html = template.render(qsoLog)

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
