import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
    const [url, setUrl] = useState('');
    const [format, setFormat] = useState('mp4');
    const [quality, setQuality] = useState('360p');
    const [progress, setProgress] = useState(0);
    const [isDownloading, setIsDownloading] = useState(false);

    const handleDownload = async () => {
        setIsDownloading(true);
        setProgress(0);

        try {
            const response = await axios.post('http://localhost:5000/download', {
                url,
                format,
                quality
            }, {
                responseType: 'blob',
                onDownloadProgress: (progressEvent) => {
                    const total = progressEvent.total;
                    const current = progressEvent.loaded;
                    const percentCompleted = Math.floor((current / total) * 100);
                    setProgress(percentCompleted);
                }
            });

            const downloadUrl = window.URL.createObjectURL(new Blob([response.data]));
            const link = document.createElement('a');
            link.href = downloadUrl;
            link.setAttribute('download', `video.${format}`);
            document.body.appendChild(link);
            link.click();

            setIsDownloading(false);
        } catch (error) {
            console.error('Error downloading the file:', error);
            setIsDownloading(false);
        }
    };

    return (
        <div className="App">
            <h1>YouTube Downloader</h1>
            <input 
                type="text" 
                placeholder="Enter YouTube URL" 
                value={url} 
                onChange={(e) => setUrl(e.target.value)} 
            />
            <select value={format} onChange={(e) => setFormat(e.target.value)}>
                <option value="mp4">MP4</option>
                <option value="mp3">MP3</option>
            </select>
            <select value={quality} onChange={(e) => setQuality(e.target.value)}>
                <option value="360p">360p</option>
                <option value="720p">720p</option>
                <option value="1080p">1080p</option>
            </select>
            <button onClick={handleDownload} disabled={isDownloading}>
                {isDownloading ? `Downloading ${progress}%` : 'Download'}
            </button>
            {isDownloading && <progress value={progress} max="100">{progress}%</progress>}
        </div>
    );
}

export default App;