from emptyline import *
from typing import Counter
from flask import *
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route('/upload',methods=['POST'])
def convert():
    global save_file
    if request.method=="POST":
        fl=request.files['file']
        save_file=fl.save(fl.filename)
        return redirect(url_for('download'))
    
@app.route('/download',methods=['POST','GET'])
def download():
   file=open("random.txt","r")
   result=find_empty(file.read())
   return render_template("empty.html",content=result)
   #return render_template("empty.html")

if __name__=="__main__":
    app.run(debug=True)