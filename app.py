import os
from flask import Flask, render_template, request, send_file
from pytube import YouTube

app = Flask(__name__)

# Use /tmp/downloads as the download folder (writable in Vercel's environment)
DOWNLOAD_FOLDER = os.path.join("/tmp", "downloads")
if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/download", methods=["POST"])
def download():
    url = request.form.get("url")
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        filename = f"{yt.title}.mp4"
        file_path = os.path.join(DOWNLOAD_FOLDER, filename)
        stream.download(DOWNLOAD_FOLDER, filename=filename)
        return send_file(file_path, as_attachment=True)
    except Exception as e:
        return f"Error: {str(e)}", 500

if _name_ == "_main_":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)