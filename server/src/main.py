from flask import Flask, send_from_directory, request, redirect, send_file
import pdf_writer
import fitz


def save(path):
    pdffile = path
    doc = fitz.open(pdffile)
    page = doc.load_page(0)
    pix = page.get_pixmap()
    output = "../../public/1.png"
    pix.save(output)

app = Flask(__name__, static_url_path='/../../public')


@app.route("/")
def base():
    return send_from_directory('../../public', 'index.html')


@app.route('/generate', methods=['POST'])
def generate():
    name = request.form.get('name')
    type = request.form.get('type')
    if type == 'certproject':
        type = 'project'
    if type == 'project':
        pdf_writer.write_project(name, request.form.get('project'))
        save(f"output/project_{name}.pdf")
    elif type == 'teacher':
        pdf_writer.write_teacher(name)
        save(f"output/teacher_{name}.pdf")
    elif type == 'jury':
        pdf_writer.write_jury(name)
        save(f"output/jury_{name}.pdf")
    return send_file(f'output/{type}_{name}.pdf', as_attachment=True)


@app.route("/<path:path>")
def home(path):
    return send_from_directory('../../public', path)


if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=8080)
