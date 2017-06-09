avrateNG
========

Requirements
------------
The only software you need to install is python3 for windows or linux,
for linux you can install it via
```
sudo apt-get install python3
```

For windows you can use the provided python3 distribution and setup files in `thirdparty` folder.

Furthermore you also need a player, e.g. for linux (ubuntu) you can use `mpv` (install it via `sudo apt-get install mpv`), for windows you can use the version that is stored in `thirdparty`

First Steps
-----------
Before you should start with your specific processed video files, you should try to run avrateNG.
If you correctly checkout the repository, everything should work.
So just start `avrateNG.py` and open http://0.0.0.0:12347/ in your favorite webbrowser.
(default user/password is max, and 123).

All ratings are stored in a sqlite3 database, for a simple conversion you can use `convert_ratings_to_csv.py` this script will create a csv file of all stored ratings.




Configuration
-------------

### General settings
All general settings can be changed in `config.json`, e.g.
```
{
    "player": "thirdparty\\mpv-x86_64-20161225\\mpv.exe --fs \"{filename}\"", // default windows player path, \"{filename}\" is a template for the video filename
    "player_linux": "mpv --fs '{filename}'", // linux player
    "http_user_name": "max",  // user login name
    "http_user_password": "123", // user password
    "http_port" : "12347", // http port where the service is running
    "rating_template" : "slider1.tpl", // template that will be used , e.g. change it to "radio1.tpl"
    "voiceRecognition_template" : "radio_voice-recognition.tpl" // template for voice recognition
}

```

### Player setup

You just need to change the `player` or `player_linux` value in the `config.json`
to your favorite video player, e.g. it also works with media player classic, vlc or ffplay.
Please try use command line flags and no manually configured gui settings, so that your experiment can be run without spending hours in configuration of the player.

#### Player experiences

* mpv: some problems with 4k content and 60 fps, and vp9
* media player classic: problems with 4k, 60fps and vp9
* ffplay: slower than mpv for 4k
* vlc: slowes player ever

### Playlist creation

The playlist `playlist.list` consist just of lines with corresponding video files, e.g.
```
./videos/01.mkv
./videos/02.mkv
```
you can also define a training playlist `training.list` all filenames can also be configured via command line interface of avrateNG.

### Advanced command line flags
just run `avrateNG.py -h` and you will get the following screen:
```
usage: avrateNG.py [-h] [-configfilename CONFIGFILENAME] [-playlist PLAYLIST]
                    [--standalone] [-trainingsplaylist TRAININGSPLAYLIST]
                    [-shuffle] [-voiceRecognition]

avrate++

optional arguments:
  -h, --help            show this help message and exit
  -configfilename CONFIGFILENAME
                        configuration file name (default: config.json)
  -playlist PLAYLIST    video sequence play list (default: playlist.list)
  --standalone          run as standalone version (default: False)
  -trainingsplaylist TRAININGSPLAYLIST
                        playlist for training session. If none is given: No
                        training (default: )
  -shuffle              Set, when playlist should be randomized (default:
                        True)
  -voiceRecognition     Set, when selection should be made using voice
                        recognition (default: False)

stg7 2017
```


### Templates

TODO(stg7)

Development Notes
-----------------

Development of a stable and new version of avrate, based on HTTP server technology.

Requirements:

* platform independent (not only windows)
* possible to use external "rating" device (via webpage rating)
* python3
* mpv

### Ideas

* use python3, bottle and html5 (bootstrap) skeleton


### Structure
in `old` you can find some ideas and sketches of a possible avrateNG (the old avrate and minirate)


### openTasks

* collect features of avrate and summarize them