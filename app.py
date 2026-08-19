from flask import Flask, Response, redirect, render_template, request
import os

app = Flask(__name__)

CANONICAL_HOST = "junkbegonenm.com"
REDIRECT_HOSTS = {
    "junkbegoneclovis.com",
    "www.junkbegoneclovis.com",
    "www.junkbegonenm.com",
}


@app.before_request
def redirect_to_canonical_domain():
    host = request.host.split(":", 1)[0].lower()
    if host not in REDIRECT_HOSTS:
        return None

    target = f"https://{CANONICAL_HOST}{request.path}"
    if request.query_string:
        target += f"?{request.query_string.decode()}"

    return redirect(target, code=301)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/free-stuff")
def free_stuff():
    return render_template("free_stuff.html")


@app.route("/sitemap.xml")
def sitemap():
    xml = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>https://junkbegonenm.com/</loc></url>
  <url><loc>https://junkbegonenm.com/free-stuff</loc></url>
</urlset>
"""
    return Response(xml, mimetype="application/xml")


@app.route("/robots.txt")
def robots():
    text = "User-agent: *\nAllow: /\nSitemap: https://junkbegonenm.com/sitemap.xml\n"
    return Response(text, mimetype="text/plain")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
