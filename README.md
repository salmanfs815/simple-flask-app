# simple-flask-app

A simple Flask application for a RESTful web service

## Setup Environment

```bash
virtualenv env
source env/Scripts/activate
pip install -r requirements.txt
```

## Run Locally (testing)

```bash
export FLASK_ENV=development
export FLASK_APP=application
flask run
```

## Deploy to AWS
```bash
zappa init
zappa deploy <stage>
```
