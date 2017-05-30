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
So just start `avrateNG.pyw` and open http://0.0.0.0:12347/ in your favourite webbrowser.
(default user/password is max, and 123).

All ratings are stored in a sqlite3 database, for a simple conversion you can use `convert_ratings_to_csv.py` this script will create a csv file of all stored ratings.




Configuration
-------------

### General settings

### Player setup

### Playlist creation

###




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