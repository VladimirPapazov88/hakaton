from pypdf import PdfWriter, PdfReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

packet = io.BytesIO()
can = canvas.Canvas(packet, pagesize=letter)
pdfmetrics.registerFont(TTFont('main', 'font.ttf'))
can.setFont('main', 30)
can.drawString(240, 385, "hello world")
can.save()

# move to the beginning of the StringIO buffer
packet.seek(0)

# create a new PDF with Reportlab
new_pdf = PdfReader(packet)
# read your existing PDF
existing_pdf = PdfReader(open("train.pdf", "rb"))
output = PdfWriter()
# add the "watermark" (which is the new pdf) on the existing page
page = existing_pdf.pages[0]
page.merge_page(new_pdf.pages[0])
output.add_page(page)
# finally, write "output" to a real file
outputStream = open("train_out.pdf", "wb")
output.write(outputStream)
outputStream.close()
