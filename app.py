from flask import Flask, render_template, redirect, request, session
# The Session instance is not used for direct access, 
# you should always use flask_session
from flask_session import Session
from datetime import timedelta
app = Flask(__name__)
app.config["SESSION_PERMANENT"] = True
app.permanent_session_lifetime = timedelta(minutes=1)
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
@app.route("/")
def index():
    if not session.get("name"):
        return redirect("/login")
    return render_template('index.html')
 
 
@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session["name"] = request.form.get("name")
        if session["name"]=="Singh":
            return redirect("/")
        else:
            return render_template("sorry.html")
    return render_template("login.html")
 
 
@app.route("/logout")
def logout():
    session["name"] = None
    return redirect("/")
 
 
if __name__ == "__main__":
    app.run(debug=True)