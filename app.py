from flask import Flask, render_template, request, send_file
from pytube import YouTube
import os

app = Flask(_name_)

# Directory to store downloads
DOWNLOAD_FOLDER = "downloads"
if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/download", methods=["POST"])
def download():
    try:
        url = request.form["url"]
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        file_path = os.path.join(DOWNLOAD_FOLDER, f"{yt.title}.mp4")
        
        stream.download(DOWNLOAD_FOLDER, filename=f"{yt.title}.mp4")

        return send_file(file_path, as_attachment=True)
    except Exception as e:
        return str(e)

if _name_ == "_main_":
    app.run(debug=True)