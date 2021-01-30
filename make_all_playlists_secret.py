"""
    make_all_playlists_secret.py

        Changes a users spotify playlists to secret.
        Can be modified to change to public.
"""
import os
import spotipy


ACCESS_TOKEN = os.getenv("SPOTIFY_ACCESS_TOKEN")
OWNER_ID = os.getenv("SPOTIFY_OWNER_ID")

sp = spotipy.Spotify(ACCESS_TOKEN)

offset = 0
n = 0
results_length = 1

while results_length > 0:
    results = sp.current_user_playlists(limit=50, offset=offset)
    results_length = len(results["items"])

    for i, item in enumerate(results['items']):
        n += 1

        playlist = sp.playlist(item["id"])
        if playlist["owner"]["id"] == OWNER_ID and playlist["followers"]["total"] > 0:
            pass
        else:
            print("%d %s - making secret" % (n, item['name']))
            sp.playlist_change_details(item["id"], public=False)

    offset += 50
