# pdf-extractor
Simple PDF extractor using opencv and tesseract 
## Docker Setup
To Start up a postgre db and django container 
Quickly run the project using 
```bash
docker-compose up -d --build
```
This should be executed for migrations
```bash
docker-compose exec web python manage.py migrate
```
## Create Virtual environment

After cloning the repo you need to create a Virtual environment using the following command and install django for working with the examples.

First install virtualenv package globally

```bash
pip install virtualenv
```
Open cli in the folder of the cloned repo and then create env
```bash
virtualenv env
```
To activate the env (For windows, For other OS you can easily google)
```bash
env\Scripts\activate
```
Then insatll requirements 
```bash
pip install -r requirements.txt
```
Start the local setup using
```bash
python manage.py runserver
```
