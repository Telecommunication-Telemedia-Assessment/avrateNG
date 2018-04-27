
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





TODOS
-----
* speech controling of rating: first steps
* maybe add some "webcamera" recoding for eye tracking ...
    * reuse pierres ruby code
* integrate different rating models/approaches, e.g. MUSHRA,  DCR, SUMWIK, ACR (done)
    * some generalize which method will be used

skipped
-------
* change styles of templates for rating so somehow optimize users perception of rating scale scheme

DONE
----
* FIX Filename/path problems
* add current slider value to slider template
* add template folder as configarable
* move some command line flags to config file, because it is easier for windows users to configure
