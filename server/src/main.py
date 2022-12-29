from flask import Flask, send_from_directory, request, redirect
import pdf_writer

app = Flask(__name__, static_url_path='/../../public')


@app.route("/")
def base():
    return send_from_directory('../../public', 'index.html')


@app.route("/<path:path>")
def home(path):
    return send_from_directory('../../public', path)


if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=8080)
