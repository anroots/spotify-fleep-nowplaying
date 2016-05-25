#!/usr/bin/env python
"""
Sets currently playing Spotify track as Fleep.io display name.
"""
import dbus
import requests
import json
import time
import click
import signal
from dbus.exceptions import DBusException
import sys

# Set up CLI usage
@click.command()
@click.option('--email', prompt='Email', help='Your Fleep account email')
@click.option(
    '--sleep-duration', default=60,
    help='How many seconds to wait between status updates')
@click.option('--password', prompt='Password', help='Your Fleep account password')

def hello(email, password, sleep_duration):
    """Shows currently playing Spotify track as your Fleep.io display name"""

    bus = dbus.SessionBus()

    # Try to get an 'instance' of Spotify on DBus.
    # Will fail if Spotify is not running
    try:
        spotify = bus.get_object('org.mpris.MediaPlayer2.spotify', '/org/mpris/MediaPlayer2')
    except DBusException:
        click.echo('Unable to connect to Spotify via Dbus', err=True)
        return

    # Login to Fleep
    credentials = login(email, password)
    if not credentials:
        click.echo('Invalid credentials, unable to login.', err=True)
        sys.exit(1)

    # Store original display name so we can revert it later
    original_name = credentials['display_name']

    def shutdown(*unused):
        """Change display name back to its original state"""
        click.echo('Shutting down, restoring original display name...')
        update_name(credentials, original_name)
        sys.exit(0)
    signal.signal(signal.SIGINT, shutdown)

    click.echo('Starting polling. Hit CTRL+C to stop.')

    while True:
        new_name = "%s (Spotify: %s)" % (original_name, get_track(spotify))

        # Update display name on Fleep
        if update_name(credentials, new_name):
            click.echo("[ok]: %s" % new_name)
        else:
            click.echo('Fleep API responded with an error', err=True)

        time.sleep(sleep_duration)

def login(email, password):
    """Login to Fleep, return session information"""
    response = requests.post(
        "https://fleep.io/api/account/login",
        headers={"Content-Type": "application/json"},
        data=json.dumps({"email": email, "password": password})
        )
    if response.status_code is not 200:
        return False
    data = response.json()
    return {
        'ticket': data["ticket"],
        'token_id':response.cookies["token_id"],
        'display_name': data['display_name']
    }


def get_track(spotify):
    """Return the name(+extra details) of the currently playing track from Spotify"""
    trackinfo = spotify.Get("org.mpris.MediaPlayer2.Player", "Metadata")

    # Get track information from DBus dictionary
    album = trackinfo.get("xesam:album")
    title = trackinfo.get("xesam:title")
    url = trackinfo.get("xesam:url")

    # The artist list is provided as an array. Combine all artists to a single string.
    artist = str(", ".join(trackinfo.get("xesam:artist"))).strip()

    return "%s - %s [%s] (%s)" % (title, artist, album, url)

def update_name(credentials, name):
    """Change display name in Fleep"""
    response = requests.post(
        "https://fleep.io/api/account/configure",
        headers={"Content-Type": "application/json"},
        cookies={"token_id": credentials['token_id']},
        data=json.dumps({"display_name": name, "ticket": credentials['ticket']})
        )
    return response.status_code == 200


if __name__ == '__main__':
    hello()
