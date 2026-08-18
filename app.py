from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def home():
    featured_video_path = os.path.join(app.static_folder, "featured-junk-be-gone.mp4")
    return render_template(
        "index.html",
        featured_video_exists=os.path.isfile(featured_video_path),
    )

@app.route("/free-stuff")
def free_stuff():
    return render_template("free_stuff.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
