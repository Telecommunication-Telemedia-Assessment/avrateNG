---
classoption: aspectratio=169

title:  AvrateNG
subtitle: demo and short overview
author:
    - Steve Göring
    - Alexander Raake
date: 04.03.2019

header-includes:
    - \usepackage{caption}
    - \captionsetup{labelformat=empty,labelsep=none}
    - \definecolor{gray}{RGB}{155,155,155}
    - \setbeamertemplate{footline}{\raisebox{5pt}{\makebox[\paperwidth]{\hfill\makebox[20pt]{\color{gray} \normalsize\insertframenumber}}}\hspace*{5pt}}
    - \definecolor{links}{HTML}{2A1B81}
    - \hypersetup{colorlinks,linkcolor=,urlcolor=links}
    - \usepackage{color}
    - \definecolor{lightblue}{rgb}{0.3,0.6,1.0}
    - \definecolor{lightgray}{rgb}{0.5,0.6,0.6}
    - \definecolor{lightred}{rgb}{1.0,0.4,0.4}
    - \definecolor{lightgreen}{rgb}{0.4,1.0,0.4}
    - \definecolor{blue}{rgb}{0,0.3,0.6}
    - \definecolor{darkblue}{rgb}{0,0.1,0.4}
    - \definecolor{green}{rgb}{0,0.7,0.2}
    - \definecolor{darkerblue}{rgb}{0.2,0.5,1.0}
    - \definecolor{textColor}{rgb}{0,0,0}
    - \definecolor{TUILOrange}{RGB}{255, 121, 0}
    - \definecolor{TUILBlack}{RGB}{0, 0, 0}
    - \definecolor{TUILGreen}{RGB}{0, 116, 122}
    - \definecolor{TUILBlue}{RGB}{0, 51, 89}
    - \definecolor{TUILGray}{RGB}{149,149,149}
    - \setbeamercolor{title}{fg=TUILOrange}
    - \setbeamercolor{author}{fg=TUILBlue}
    - \setbeamercolor{frametitle}{fg=TUILOrange}
    - \setbeamercolor{background canvas}{bg=white}
    - \setbeamertemplate{itemize item}{\color{TUILGreen}$\blacktriangleright$}
    - \setbeamertemplate{itemize subitem}{\color{TUILGreen}$\circ$}
    - \setbeamercolor{section in toc}{fg=TUILGray}
    - \setbeamercolor{subsection in toc}{fg=TUILGray}
    - \setbeamercolor{normal text}{fg=TUILBlue}
    - \usebibitemtemplate{\insertbiblabel}
    - \newcommand{\xG}[1]{\textcolor{TUILOrange}{#1}}
    - \newcommand{\xR}[1]{\textcolor{red}{#1}}
    - \newcommand{\xB}[1]{\textcolor{blue}{#1}}
    - \renewcommand{\emph}[1]{{\em\xG{#1}}}
    - \renewcommand{\textbf}[1]{{\em\xR{#1}}}
    - \let\olditem\item
    - \renewcommand{\item}{\vfill\olditem}
    - \usepackage{pgf}
    - \logo{\pgfputat{\pgfxy(-0.2,7.3)}{\pgfbox[right,base]{\includegraphics[height=0.7cm]{imgs/logo.pdf}}}}
---

# AvrateNG

* software to collect ratings for subjective tests
    * \xG{e.g. ACR ratings}
    * \xG{open source:} [https://bit.ly/2QlCGft](https://bit.ly/2QlCGft)
* written in python, client server architecture
    * \xG{ensures flexibility}
    * \xG{rating variants implemented using HTML templates}
* suitable for image, video and general multimedia tests
    * \xG{external player can be configured; command line player}
    * e.g. ffplay, mpv, vlc, ...
* possible to use it for general surveys

# Architecture
![AvrateNG overview](imgs/avrate.pdf){width=85%}

* configuration via: `config.json`, `playlist.list`, `training.list`

# Configuration -- config.json

```json
{
    "player": "... \"{filename}\"",
    "player_linux": "mpv --fs '{filename}'",
    "http_user_name": "max",
    "http_user_password": "123",
    "http_port" : "12347",
    "rating_template" : "radio1.tpl",
    "playlist" : "playlist.list",
    "template_folder" : "templates",
    "training" : true,
    "trainingsplaylist" : "training.list",
    "shuffle": true,
    "gray_video": "videos/gray.mkv",
    "no_video_playback": false,
    "question": "What is your opinion of the video quality?", ...
}
```

# Configuration -- playlists
```
./videos/02.mkv
./videos/01.mkv | ./videos/01.mkv
```
* simple list of video filenames
* separated handling of training and rating part
* trainingsplaylist: always same stimuli ordering
* play one video as stimuli or multiple videos as "one" stimuli

# Demo

* start avrateNG.py  (or via win_start_avrateng.bat)
* open browser http://localhost:12347/
* enter name + password
* start rating


# Questions

![Thank you for your attention](imgs/questions2.jpg){width=40%}
