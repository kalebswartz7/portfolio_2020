from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/static/<path:filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)