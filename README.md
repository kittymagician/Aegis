<img src="https://github.com/kittymagician/Aegis/blob/master/img/logo.svg" width="200" height="100">
Aegis - Flask web interface for scanning files with YARA

This application was designed with end users in mind. Upload any file and Aegis will provide a YARA scan report and delete the uploaded file.

## Installation Guide

step 0 - git clone this repo.


step 1 - place the yara rules in /rules


step 2 - compile YARA and install packages for python.


step 3 - Start the web app with python3 aegis.py


step 4 - visit the web app by default the port is set to 3000 (in aegis.py) however this can be modified to use port 80 by using [gunicorn/nginx](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04).

## Screenshots
<img src="https://github.com/kittymagician/Aegis/blob/master/img/Upload.png" width="275" height="180">
Upload Page
<img src="https://github.com/kittymagician/Aegis/blob/master/img/Results.png" width="311" height="111">
Results Page

## Requirements
Python3 - https://python.org


YARA - https://virustotal.github.io/yara/


yara-python - https://pypi.org/project/yara-python/


## Does Aegis test rules before execution?
No. Please test your YARA rules before including them in the Rules folder.

## Get more rules
[Yara-Rules](https://github.com/Yara-Rules/rules)


[Neo23x0 Signature-Base](https://github.com/Neo23x0/signature-base/tree/master/yara)


[InQuest Awesome-Yara](https://github.com/InQuest/awesome-yara)

## Licence
Aegis is licenced under the MIT licence.

