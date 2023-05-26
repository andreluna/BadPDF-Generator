import sys
import io
import bz2
import base64
import argparse

parser = argparse.ArgumentParser(description='python3 badpdf.py --file my_report.pdf --host https://my.phishingpage.com')
parser.add_argument('--file', required=True, help='filename to output.')
parser.add_argument('--host', required=True, help='url or ip address.')
args = parser.parse_args()

filename = args.file
host = args.host

with open(filename, "w") as file:
    file.write('%PDF-1.7\n\n')
    file.write('1 0 obj\n')
    file.write('  << /Type /Catalog\n')
    file.write('     /Pages 2 0 R\n')
    file.write('  >>\n')
    file.write('endobj\n\n')
    file.write('2 0 obj\n')
    file.write('  << /Type /Pages\n')
    file.write('     /Kids [3 0 R]\n')
    file.write('     /Count 1\n')
    file.write('     /MediaBox [0 0 595 842]\n')
    file.write('  >>\n')
    file.write('endobj\n\n')
    file.write('3 0 obj\n')
    file.write('  << /Type /Page\n')
    file.write('     /Parent 2 0 R\n')
    file.write('     /Resources\n')
    file.write('      << /Font\n')
    file.write('          << /F1\n')
    file.write('              << /Type /Font\n')
    file.write('                 /Subtype /Type1\n')
    file.write('                 /BaseFont /Courier\n')
    file.write('              >>\n')
    file.write('          >>\n')
    file.write('      >>\n')
    file.write('     /Annots [<< /Type /Annot\n')
    file.write('                 /Subtype /Link\n')
    file.write('                 /Open true\n')
    file.write('                 /A 5 0 R\n')
    file.write('                 /H /N\n')
    file.write('                 /Rect [0 0 595 842]\n')
    file.write('              >>]\n')
    file.write('     /Contents [4 0 R]\n')
    file.write('  >>\n')
    file.write('endobj\n\n')
    file.write('4 0 obj\n')
    file.write('  << /Length 67 >>\n')
    file.write('stream\n')
    file.write('  BT\n')
    file.write('    /F1 22 Tf\n')
    file.write('    30 800 Td\n')
    file.write('    (PDF Blocked: \'Click Here\'     ) Tj\n')
    file.write('  ET\n')
    file.write('endstream\n')
    file.write('endobj\n\n')
    file.write('5 0 obj\n')
    file.write('  << /Type /Action\n')
    file.write('     /S /URI\n')
    file.write('     /URI (' + str(host) + '/)\n')
    file.write('  >>\n')
    file.write('endobj\n\n')
    file.write('xref\n')
    file.write('0 6\n')
    file.write('0000000000 65535 f\n')
    file.write('0000000010 00000 n\n')
    file.write('0000000069 00000 n\n')
    file.write('0000000170 00000 n\n')
    file.write('0000000629 00000 n\n')
    file.write('0000000749 00000 n\n')
    file.write('trailer\n')
    file.write('  << /Root 1 0 R\n')
    file.write('     /Size 6\n')
    file.write('  >>\n')
    file.write('startxref\n')
    file.write('854\n')
    file.write('%%EOF\n')

