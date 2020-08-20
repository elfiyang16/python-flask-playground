from flask import Flask, redirect, url_for, render_template, request, session

app = Flask(__name__)
app.secret_key = "elfi"


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
      # comes in as a dictionary
        user = request.form["name"]
        session["user"] = user
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for("user"))
        return render_template("login.html")


@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return f"<h1>{user}</h1>"
    else:
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
