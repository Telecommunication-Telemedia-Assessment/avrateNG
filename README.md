# avrateNG
avrateNG is a video/image/.. rating system, heavily based on [AVrate](https://github.com/Telecommunication-Telemedia-Assessment/AVRate).
avrateNG is developed as part of research in the [AVT Group](https://www.tu-ilmenau.de/en/audio-visual-technology/).


# Requirements
The only software you need to install is python3 for windows or linux,
for linux you can install it via
```
sudo apt-get install python3
```

For windows you can use the provided python3 distribution and setup files in `thirdparty` folder.

Furthermore you also need a player, e.g. for linux (ubuntu) you can use `mpv` (install it via `sudo apt-get install mpv`), for windows you can use the version that is stored in `thirdparty`

## Plotscript
For the `generate_plots.py` script you need pandas and seaborn `sudo pip3 install pandas seaborn`. `generate_plots.py` is **experimental**.

## First Steps
Before you should start with your specific processed video files, you should try to run avrateNG.
If you correctly checkout the repository, everything should work.
So just start `avrateNG.py` and open http://127.0.0.1:12347/ in your favorite webbrowser.
(default user/password is `max`, and `123`, change it in the `config.json`).

All ratings are stored in a sqlite3 database, for a simple conversion you can use `convert_ratings_to_csv.py` this script will create a `csv` file of all stored ratings.



## Configuration

### General settings
All general settings can be changed in `config.json`, e.g.
```
{
    "player": "thirdparty\\mpv-x86_64-20161225\\mpv.exe --fs \"{filename}\"", // default windows player path, \"{filename}\" is a template for the video filename
    "player_linux": "mpv --fs '{filename}'", // linux player
    "http_user_name": "max",  // user login name
    "http_user_password": "123", // user password
    "http_port" : "12347", // http port where the service is running
    "rating_template" : "radio1.tpl", // template that will be used , e.g. change it to "radio1.tpl"
    "playlist"  : "playlist.list",  //  Playlist file that will be used (Define your playlist here)
    "template_folder" : "templates",    //  Folder with your custom templates (Take a look in "/templates/")
    "training"  :  true,    //  Training stage up front? (true/false)
    "trainingsplaylist" :   "training.list",    //  if training is true, this trainingsplaylist will be presented
    "voiceRecognition"  :   false,  // rating using voice recognition? (a little buggy...)
    "voiceRecognition_template" : "radio_voice-recognition.tpl" // template that will be used for voice recognition
    "shuffle": true // Randomized playback of videos in playlist? (true: Randomization, false: linear playback according to playlist)
}

```

### Player setup

You just need to change the `player` or `player_linux` value in the `config.json`
to your favorite video player corresponding to your operating system, e.g. it also works with media player classic, vlc or ffplay.
Please try use command line flags and no manually configured gui settings, so that your experiment can be run without spending hours in configuration of the player.

#### Player experiences

* mpv: some problems with 4k content and 60 fps, and vp9
    * command line arguments: -cache 8388608 -fs --cursor-autohide=0 --osc=no --no-input-default-bindings --hwdec=auto
* media player classic: problems with 4k, 60fps and vp9
* ffplay: slower than mpv for 4k
* vlc: slowest player ever (not yet tested with version 3.0)
* following is the command for optiplay in the avrateNG config file:
```bash
thirdparty\OptiPlay-0.7beta1.exe -an -f v210 -video_size 3840x2160 -framerate 60 -i {filename}
```

### Playlist creation

The playlist `playlist.list` consist just of lines with corresponding video files, e.g.
```
./videos/01.mkv
./videos/02.mkv
```
you can also define a training playlist `training.list`.
The playlists to render are defined in the `config.json` file. Also set trainig to true or false in there.

#### multiple videos per line
You can specify multiple videos in one playlist entry if you separate them by ` | ` (spaces are important).
```
./videos/01.mkv | ./videos/01.mkv
./videos/02.mkv
```

The configured player will now get as `{filename} = "./videos/01.mkv" "./videos/01.mkv"`

#### gray video
A 2 second gray video will be played before and after a video, for disabling
just remove `"gray_video": "..."` in your config file.


### Advanced command line flags
just run `avrateNG.py -h` and you will get the following screen:
```
usage: avrateNG.py [-h] [-configfilename CONFIGFILENAME] [--standalone]

avrate++

optional arguments:
  -h, --help            show this help message and exit
  -configfilename CONFIGFILENAME
  --standalone          run as standalone version (default: False)

stg7 2018
```


### Templates

There are several rating templates implemented, they can be changed in the `config.json`.
Default template is a classic ACR rating scheme.


### Developers
* Steve Göring
* Maximilian Schaab
* Serge Molina
* Anton Schubert

### License
see LICENSE file in this repository
