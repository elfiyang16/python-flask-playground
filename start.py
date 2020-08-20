from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/<name>")
def user(name):
    return f"Hello {name}!"


@app.route("/admin/")
def admin():
    # redirect to user and pass in name arg as Admin!
    return redirect(url_for("user", name="Admin!"))


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
      # comes in as a dictionary
        user = request.form["name"]
        return redirect(url_for("user", usr=user))
    else:
        return render_template("/login.html")


@app.route("/<usr>")
def iser(usr):
    return f"<h1>{usr}</h1>"


if __name__ == "__main__":
    app.run(debug=True)
