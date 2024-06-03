from flask import Flask, request, send_file
from flask_cors import CORS
import yt_dlp as youtube_dl
import os

app = Flask(__name__)
CORS(app)

@app.route('/download', methods=['POST'])
def download():
    data = request.get_json()
    url = data['url']
    format = data['format']
    quality = data['quality']
    
    ydl_opts = {
        'format': f'best[height<={quality[:-1]}]' if format == 'mp4' else 'bestaudio',
        'outtmpl': f'temp.{"mp4" if format == "mp4" else "mp3"}'
    }
    
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    
    return send_file(f'temp.{"mp4" if format == "mp4" else "mp3"}', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)