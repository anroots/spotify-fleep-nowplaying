
import dbus
import requests
import json
import time


email = ''
password = ''

bus = dbus.SessionBus()
spotify = bus.get_object('org.mpris.MediaPlayer2.spotify',
    '/org/mpris/MediaPlayer2')


def login():
    r = requests.post("https://fleep.io/api/account/login",
     headers = {"Content-Type": "application/json"},
     data = json.dumps({"email": email, "password": password}))
    return {'ticket':r.json()["ticket"],'token_id':r.cookies["token_id"]}

def get_track():

    trackinfo = spotify.Get("org.mpris.MediaPlayer2.Player","Metadata")

    # Get track information from DBus dictionary
    album       = trackinfo.get("xesam:album")
    title       = trackinfo.get("xesam:title")
    trackNumber = str(trackinfo.get("xesam:trackNumber"))
    discNumber  = str(trackinfo.get("xesam:discNumber"))
    trackid     = str(trackinfo.get("xesam:trackid"))
    length      = trackinfo.get("xesam:length")
    artUrl      = trackinfo.get("xesam:artUrl")
    url         = trackinfo.get("xesam:url")

    # The artist list is provided as an array. Combine all artists to a single string.
    artist = str(", ".join(trackinfo.get("xesam:artist"))).strip()

    return "Ando \"David\" Roots (Spotify: %s - %s [%s] (%s))" % (title, artist, album, url)

def update_name(credentials, name):
    r = requests.post("https://fleep.io/api/account/configure",
         headers = {"Content-Type": "application/json"},
         cookies = {"token_id": credentials['token_id']},
         data = json.dumps({"display_name": name, "ticket": credentials['ticket']}))
    return r.status_code == 200

def main():
    print 'Starting polling script'
    print "*** Hit CTRL+C to stop ***"
    credentials = login()
    while True:
        now_playing = get_track()
        if update_name(credentials, now_playing):
            print "[ok]: %s" % (now_playing)
        else:
            print "Fleep API responded with an error"
        print "Sleeping..."
        time.sleep(60)
main()