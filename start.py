from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", content=["elfi", "julia"])


@app.route("/<name>")
def user(name):
    return f"Hello {name}!"


@app.route("/admin/")
def admin():
    # redirect to user and pass in name arg as Admin!
    return redirect(url_for("user", name="Admin!"))


if __name__ == "__main__":
    app.run()
