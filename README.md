# YouTube Downloader

This is a full-stack YouTube downloader application developed using Flask for the backend and React for the frontend. 
The application allows users to download YouTube videos by providing the URL and selecting the desired format and quality.

## Table of Contents

- [Installation](#installation)
- [Backend](#backend)
  - [Setting Up the Backend](#setting-up-the-backend)
- [Frontend](#frontend)
  - [Setting Up the Frontend](#setting-up-the-frontend)
- [Running the Application](#running-the-application)

## Installation

To get started with this project, clone the repository:

<u>Back-end</u> 

_Navigate to the downloader-backend directory_ 

1. Create a virtual enviroment and activate it :

   `python -m venv venv`
   `source venv/bin/activate` #on
   Windows, use `venv\Scripts\activate`

2. Install the required packages :

   `pip install -r requirements.txt`

3. Create a Procfile in the downloader-backend directory with the following content : #not required 

   `web : python app.py`

<u>Front-end</u>

_Navigate to the downloader-frontend directory_ 

1. Install the required packages :

   `npm install`

## Run the Application 

1. Activate your python virtual enviroment
2. then `flask run`
3. Start the React frontend `npm start`
       
