def clean_timestamp(time_stamp, current: bool = False):
    if current:
        return time_stamp.strftime("%Y-%m-%d %H:%M:%S")
    clean_str = time_stamp.replace('Z', '+00:00')
    return datetime.fromisoformat(clean_str).strftime("%Y-%m-%d %H:%M:%S")

def get_top_artists(limit=5):
    names = []
    top = sp.current_user_top_artists(limit)
    for item in top['items']:
        names.append(item['name'])
    return names

def get_recently_played(limit):
    results = sp.current_user_recently_played(limit)
    tracks = []
    for item in results['items']:
        items = {}
        timestamp = clean_timestamp(item['played_at'])
        track = item['track']
        track_name = track['name']
        artist_name = track['album']['artists'][0]['name']
        album = None if track['album']['album_type'] == 'single' else track['album']['album_type']
        if album:
            album_name = track['album']['name']
        items['track_name']=track_name
        items['artist_name']=artist_name
        # items['album_name']=album_name
        items['timestamp']=timestamp
        tracks.append(items)
        # items.clear()
    return tracks

def get_currently_playing():
    try:
        song = sp.current_playback()
        track_name = song['item']['name']
        artist_name = song['item']['album']['artists'][0]['name']
        time_stamp = clean_timestamp(datetime.now(), True)
        release_date = song['item']['album']['release_date']
        return [track_name, artist_name, time_stamp, release_date]
    except TypeError as e:
        print(e)
        return None
