# Spotify Stats

A small Python project that uses the Spotify API to collect and analyze listening data.

This project is still in its very early preliminary stages, so there is plenty more to come.

## Current Features

- Get recently played tracks
- Get top tracks and artists
- Retrieve currently playing music
- Basic Spotify data filtering
- Work with Spotify's Web API using Spotipy

## Coming Soon

- Data visualizations and charts
- More detailed listening statistics
- More advanced analysis
- Dynamic playlist creation
- More ways to explore and filter listening history

## Setup

Clone the repository:

```bash
git clone https://github.com/yourusername/spotipy.git
cd spotipy
````

Install the dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file and add your Spotify API credentials:

```env
SPOTIPY_CLIENT_ID=your_client_id
SPOTIPY_CLIENT_SECRET=your_client_secret
SPOTIPY_REDIRECT_URI=http://127.0.0.1:8080/callback
```

Then run:

```bash
python main.py
```

## Built With

* Python
* Spotipy
* Spotify Web API
* python-dotenv

## Status

Early development. The current version focuses on getting the core Spotify data collection working. More advanced statistics, visualizations, and dynamic playlist features will be added in future versions.

```
