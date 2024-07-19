from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def index():
    req = requests.get("https://api.npoint.io/674f5423f73deab1e9a7")
    context = {
        "blog_data": req.json(),
        "nof_blogs": len(req.json())
    }
    return render_template("index.html", **context)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/post<int:id>')
def post(id):
    req = requests.get("https://api.npoint.io/674f5423f73deab1e9a7")
    context = {
        "id": id,
        "blog_data": req.json()
    }
    return render_template("post.html", **context)


if __name__ == "__main__":
    app.run(debug=True)
