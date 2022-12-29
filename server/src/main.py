from flask import Flask, send_from_directory, request, redirect, send_file
import pdf_writer
from pdf2image import convert_from_path

app = Flask(__name__, static_url_path='/../../public')


@app.route("/")
def base():
    return send_from_directory('../../public', 'index.html')


@app.route('/generate', methods=['POST'])
def generate():
    name = request.form.get('name')
    type = request.form.get('type')
    if type == 'certproject':
        pdf_writer.write_project(name, request.form.get('project'))
        img = convert_from_path(pdf_path=f'output/project_{name}.pdf',
                          poppler_path=r'C:\pf\poppler-22.12.0\Library\bin')
        img[0].save('../../public/1.jpg', "JPEG")
    elif type == 'teacher':
        pdf_writer.write_teacher(name)
        img = convert_from_path(pdf_path=f'output/teacher_{name}.pdf',
                          poppler_path=r'C:\pf\poppler-22.12.0\Library\bin')
        img[0].save('../../public/1.jpg', "JPEG")
    elif type == 'jury':
        pdf_writer.write_jury(name)
        img = convert_from_path(pdf_path=f'output/jury_{name}.pdf',
                          poppler_path=r'C:\pf\poppler-22.12.0\Library\bin')
        img[0].save('../../public/1.jpg', "JPEG")
    return send_file(f'output/{type}_{name}.pdf', as_attachment=True)


@app.route("/<path:path>")
def home(path):
    return send_from_directory('../../public', path)


if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=8080)
