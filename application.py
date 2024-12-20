from flask import Flask,render_template,request,session
from flask_session import Session

app=Flask(__name__,template_folder=r"D:\project prac\started-with-program")

app.config["SESSION_PERMANENT"]=False
app.config['SESSION_TYPE']='filesystem'
Session(app)

names=[]

@app.route("/",methods=["GET","POST"])
def index():
    if request.method=="POST":
        name=request.form.get("uname")
        names.append(name)
    return render_template("index.html",users=names)
if __name__=="__main__":
    app.run()