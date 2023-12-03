from distutils.log import debug 
from fileinput import filename 
from flask import *  
app = Flask(__name__)   
UPLOAD_FOLDER = 'C:/Users/Vikas/Desktop/ReactApp'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
@app.route('/')   
def main():   
    return render_template("index.html")   
import os
@app.route('/success', methods = ['POST'])   
def success():   
    if request.method == 'POST':   
        f = request.files['file'] 
        f.save(os.path.join(app.config['UPLOAD_FOLDER'],f.filename))
        return render_template("Acknowledgement.html", name = f.filename)   
  
if __name__ == '__main__':   
    app.run(debug=True)