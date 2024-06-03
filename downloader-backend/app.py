from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import yt_dlp as youtube_dl
import os

app = Flask(__name__)
CORS(app)

@app.route('/download', methods=['POST'])
def download_video():
    data = request.json
    url = data['url']
    format = data['format']
    quality = data['quality']
    
    ydl_opts = {
        'format': 'best',
        'progress_hooks': [my_hook],
    }

    if format == 'mp3':
        ydl_opts['format'] = 'bestaudio/best'
        ydl_opts['postprocessors'] = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
        filename = 'audio.mp3'
    else:
        filename = 'video.mp4'
        if quality == '360p':
            ydl_opts['format'] = 'bestvideo[height<=360]+bestaudio/best'
        elif quality == '720p':
            ydl_opts['format'] = 'bestvideo[height<=720]+bestaudio/best'
        elif quality == '1080p':
            ydl_opts['format'] = 'bestvideo[height<=1080]+bestaudio/best'

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    
    return send_file(filename, as_attachment=True)

def my_hook(d):
    if d['status'] == 'downloading':
        print(d['_percent_str'], d['_eta_str'])

if __name__ == '__main__':
    app.run(port=5000)