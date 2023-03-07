from flask import Flask, render_template,send_from_directory
import json

with open('config.json') as config_file:
    config = json.load(config_file)

print("ok")
app = Flask(__name__)

app.config['SECRET_KEY'] = config.get('SECRET_KEY')


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/info')
def info():
    return 'Qui troverai informazioni sulla nostra azienda.'

@app.route('/privacy/manifestosardo')
def manifestosardo():
    return render_template("manifestosardo.html")


@app.route('/img/<path:filename>')
def serve_image(filename):
    return send_from_directory('img', filename)

if __name__ == '__main__':
    app.run()
