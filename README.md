
## sys_admin

This repo contains files for a simple Flask-based web server.

## Setup

* Create a virtual environment

    `python3 -m venv .venv`

* Activate the virtual environment

    `source .venv/bin/activate`

* Install the required packages

    `pip install -r requirements.txt`



## Launch Server in Debug Mode

Flask comes with the ability to run the app using a development server.  This is useful
for testing, but should not be used in production.


* Launch the app (NOTE: The code specifies port 8000) 
    `python app.py`

* Open a web browser and load `http://localhost:8000/hello` 


## Launch the Server with Gunicorn

[Gunicorn](https://gunicorn.org/) is a production-quality web server.  When we launch


* Launch `gunicorn`  NOTE: `0.0.0.0` means "bind to all networks."  This allows outside network traffic.  Also, this command launches on port 5000

    `gunicorn --bind 0.0.0.0:5000 app:app`
* Open a web browser and load `http://localhost:5000/hello` 

## Launch at boot (on AWS)

* Copy `flask.service` to `/etc/systemd/system/`
* Run `sudo systemctl enable flask`
* Run `sudo systemctl start flask`
* Status: `sudo systemctl status flask`
* Logs: `sudo journalctl -u flask`


## Auto-Configure on AWS

When you launch an instance using the Learner Lab

* Specify a name for the machine
* Select `vockey` for the Key Pair
* Select "Allow HTTP traffic from the internet" under "Network settings"
* Expand the "Advanced details," and in "User data" add

```
#!/bin/bash
yum install -y git
git clone https://github.com/cs220s23/sys_admin.git /sys_admin
python3 -m venv /sys_admin/.venv
/sys_admin/.venv/bin/pip install -r /sys_admin/requirements.txt
cp /sys_admin/aws/flask.service /etc/systemd/system
systemctl enable flask
systemctl start flask
```
