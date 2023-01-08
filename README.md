# RSA Algorithm
## Description
Student project containing a small web app written in python with flask framework that can encrypt
and decrypt text messages using RSA algorithm. Bootstrap was used for help with front-end and I used
pipenv as packaging tool.

## How to use
Usage is quite simple. First make sure you are in root of this repo and then run these commands.<br>
```
pipenv install
pipenv run python app.py
```
If you get an error saying python 3.9 was not found on your system. Simple workaround is to change
```
python_version = "3.9"
```
to
```
python_version = "*"
```
in Pipfile.
