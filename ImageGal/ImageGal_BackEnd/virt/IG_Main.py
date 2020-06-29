from flask import Flask, render_template
from IG_render_Index import render_Index


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('template_index.html', rs_dados_iniciais=render_Index())

@app.route('/about')
def about():
    return render_template('template_about.html')
    
@app.route('/admin')
def admin():
    return render_template('template_admin.html')
    
if (__name__ == "__main__"):

    print("Server ImageGallery Iniciado !")



    app.run(debug=True)
