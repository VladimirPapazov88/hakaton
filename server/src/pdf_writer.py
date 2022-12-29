from pypdf import PdfWriter, PdfReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

cords = {
    "project": {"name": (240, 365),
                "project": (245, 210)
                },
    "teacher": {
        "name": (240, 390),
    },
    "jury": {
        "name": (240, 370),
    }
}

fonts = {
    "name": {"font": 'main', "size": 30},
    "project": {"font": "main2", "size": 20}
}


def write(cordinates, data, filename, output_prefix):
    pdfmetrics.registerFont(TTFont('main', 'font.ttf'))
    pdfmetrics.registerFont(TTFont('main2', 'font2.ttf'))

    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)

    for b in cordinates:
        cord = cordinates[b]
        can.setFont(fonts[b]['font'], fonts[b]['size'])
        wrap_text = data[b].split(' ')
        for ii in range(len(wrap_text)):
            can.drawString(cord[0], cord[1] - 28 * ii, wrap_text[ii])

    packet.seek(0)
    can.save()
    new_pdf = PdfReader(packet)
    existing_pdf = PdfReader(open(f"{filename}.pdf", "rb"))
    output = PdfWriter()
    page = existing_pdf.pages[0]
    page.merge_page(new_pdf.pages[0])
    output.add_page(page)
    output_stream = open(f"output/{filename}_{output_prefix}.pdf", "wb")
    output.write(output_stream)
    output_stream.close()


def write_project(name, project_name):
    data = {
        "name": name,
        "project": project_name
    }
    write(cords['project'], data, filename="project", output_prefix=project_name)


def write_jury(name):
    data = {
        "name": name
    }
    write(cords['jury'], data, filename="jury", output_prefix=name)


def write_teacher(name):
    data = {
        "name": name
    }
    write(cords['teacher'], data, filename="teacher", output_prefix=name)


if __name__ == '__main__':
    write_project('test test test', 'proejct111')
    write_jury('awfawf awaowfhis wadiawd')
    write_teacher('oihiyegf awuawfoeifp segfhosiegp')
