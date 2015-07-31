# Now Playing Plugin For Spotify + Fleep

[![Scrutinizer](https://img.shields.io/scrutinizer/g/anroots/spotify-fleep-nowplaying.svg)](https://scrutinizer-ci.com/g/anroots/spotify-fleep-nowplaying)
[![Scrutinizer Build](https://img.shields.io/scrutinizer/build/g/anroots/spotify-fleep-nowplaying.svg)](https://scrutinizer-ci.com/g/anroots/spotify-fleep-nowplaying)
[![GitHub release](https://img.shields.io/github/release/qubyte/rubidium.svg)](https://github.com/anroots/spotify-fleep-nowplaying/releases)
[![GitHub license](https://img.shields.io/github/license/anroots/spotify-fleep-nowplaying.svg)](https://github.com/anroots/spotify-fleep-nowplaying/blob/master/LICENSE)

Appends the currently playing track name from Spotify to your [Fleep.io](https://fleep.io) display name.

Original script by [Erik Nosar](https://github.com/enosar/xchat-spotify-np) for XChat. Modified to work with Fleep.

## Requirements

- Linux
- Python 2.7 (not tested on other versions)
- [Click](http://click.pocoo.org/4/) framework installed
- Spotify + DBus
- [Fleep.io](https://fleep.io) account

## Install

Verify that the dependencies are OK. Simply place the updater.py file anywhere in your machine.

## Usage

Start Spotify. Run the script from a terminal, like so:
```bash
$ python updater.py --email=<fleep-email> --password=<fleep-password>
```

The script will run forever, until you kill it with CTRL+C. By default, it updates your Fleep display name ever 60 seconds.

See `python updater.py --help` for more info.

## Testing

None

## Change log

Please see [CHANGELOG](CHANGELOG.md) for more information what has changed recently.

## Contributing

Contributions are **welcome** and will be fully **credited**.

Contributions are accepted via Pull Requests on [Github](https://github.com/anroots/spotify-fleep-nowplaying).

### Pull Requests

- **Document any change in behaviour** - Make sure the `README.md`, `CHANGELOG.md` and any other relevant documentation are kept up-to-date.

- **Consider our release cycle** - We try to follow [SemVer v2.0.0](http://semver.org/). Randomly breaking public APIs is not an option.

- **Create feature branches** - Don't ask us to pull from your master branch.

- **One pull request per feature** - If you want to do more than one thing, send multiple pull requests.

- **Send coherent history** - Make sure each individual commit in your pull request is meaningful. If you had to make multiple intermediate commits while developing, please [squash them](http://www.git-scm.com/book/en/v2/Git-Tools-Rewriting-History#Changing-Multiple-Commit-Messages) before submitting.

## Licence

MIT