from flask import Flask, render_template,send_from_directory
import glob 
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/info')
def info():
    return 'Qui troverai informazioni sulla nostra azienda.'

@app.route('/privacy/<string:appname>')
def privacy(appname):
    if appname in  [i.split("/")[-1][:-5] for i in  glob.glob("templates/*.html") if not "index" in i ]:
        return render_template(appname+".html")
    return "App not found.."



@app.route('/img/<path:filename>')
def serve_image(filename):
    return send_from_directory('img', filename)

if __name__ == '__main__':
    app.run(debug=True)