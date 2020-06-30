import os
import json
from flask import Flask, render_template, request, redirect, url_for
from IG_Index_Data import fetch_Index_data
from werkzeug.utils import secure_filename

app = Flask(__name__)

# UPLOAD_FOLDER = '/static/assets/Upload_Images/Original/'
UPLOAD_FOLDER = "\\static\\assets\\Upload_Images\\Original"
ALLOWED_EXTENSIONS = {"png", "jpg", "peg", "gif"}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def upload_file():

    contaArq = 0
    finalFileName = ""
    fileNameIsOk = False

    if request.method == 'POST':

        for filex in request.files:

            if contaArq == 0:

                file = request.files[filex]

                dirname = os.path.dirname(__file__) + UPLOAD_FOLDER
                # return dirname

                fileNameIsOk = allowed_file(file.filename)
                finalFileName = secure_filename(file.filename)

                if file and fileNameIsOk:
                    file.save(os.path.join(dirname, finalFileName))

            contaArq = contaArq + 1

        if contaArq > 0:
            
            if fileNameIsOk == False:
                return "Arquivo não permitido: " + finalFileName, 403
            
            return "OK"

                                                
        else:
            return "Nenhum arquivo enviado", 400
            # return render_template('Index.html', rs_dados_iniciais=fetch_Index_data())




@app.route('/')
def index():
    return render_template('Index.html', rs_dados_iniciais=fetch_Index_data())

@app.route('/upload', methods = ['POST', 'GET'])
def upload():
    
    if request.method == 'POST':
        return upload_file()
        # return render_template('Upload_POST.html')
        
    else:
        return render_template('Upload.html')
    

@app.route('/about')
def about():
    return render_template('About.html')
    
@app.route('/admin')
def admin():
    return render_template('Admin.html')
    
if (__name__ == "__main__"):

    print("Server ImageGallery Iniciado !")

    app.run(debug=True)
