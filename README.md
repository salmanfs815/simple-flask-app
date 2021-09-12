# simple-flask-app

A simple Flask application for a RESTful web service

[Tutorial](https://salmanfs.ca/posts/developing-a-flask-app-deploying-on-aws/) on how to create this application and deploy to AWS.

## Setup Environment

```bash
virtualenv env
source env/Scripts/activate
pip install -r requirements.txt
```

## Run Locally

```bash
export FLASK_ENV=development
export FLASK_APP=application
flask run
```

## Deploy to AWS Elastic Beanstalk

```bash
eb init -i
eb create <env_name>
```

## Deploy to AWS Lambda

```bash
zappa init
zappa deploy <stage>
```
