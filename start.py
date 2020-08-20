from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "elfi"
# permanent session
app.permanent_session_lifetime = timedelta(minutes=15)


@app.route("/")
def home():
    return render_template("index.html")


# @app.route("/admin/")
# def admin():
#     # redirect to user and pass in name arg as Admin!
#     return redirect(url_for("user", name="Admin!"))


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
      # comes in as a dictionary
        user = request.form["name"]
        session["user"] = user
        flash("Login Successfully")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for("user"))
        return render_template("login.html")


@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return render_template("login.html", user=user)
    else:
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    session.pop("user", None)
    flash("you have been logged out!", "info")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
