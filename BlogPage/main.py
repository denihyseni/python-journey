from flask import Flask, render_template
import requests

posts = requests.get("https://api.npoint.io/4d377aa1a0a22de667aa").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html",all_posts=posts)



@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog in posts:
        if blog['id'] == index:
            requested_post = blog
    return render_template("post.html", post=requested_post)




if __name__ == "__main__":
    app.run(debug=True)
