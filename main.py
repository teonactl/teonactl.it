from flask import Flask, render_template,send_from_directory

app = Flask(__name__)
app.config["SERVER_NAME"] = "localhost:5000"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/info')
def info():
    return 'Qui troverai informazioni sulla nostra azienda.'

@app.route('/privacy')
def privacy():
    return 'Qui troverai la nostra politica sulla privacy.'

@app.route('/', subdomain='git')
def git():
    return 'Benvenuto sulla nostra pagina Git!'

@app.route('/img/<path:filename>')
def serve_image(filename):
    return send_from_directory('img', filename)

if __name__ == '__main__':
    app.run(debug=True)