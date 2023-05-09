# CAR SHOWROOM "KARAT-AVTO" 

This is my first django project in production. This project is a web resource for the car dealership "Karat Auto"

Technologies: Python-3.10, Django-4, Postgres, HTML/CSS/JS, Google Maps API, Google SMTP.  

## QUICK LOCAL START

All commands only for Linux (Debian) systems! If you want start this project local you need do this steps:

### STEP 1

Install packages

    sudo apt-get update
    sudo apt-get install -y git python3-dev python3-venv python3-pip supervisor vim libpq-dev postgresql postgresql-contrib gettext

### STEP 2

Clone this git project

    git clone https://github.com/tsyhanenkod/karat-avto.git
    
And open project dir

    cd karat-avto

### STEP 3

Create new database and user (Save the login, password and other important data for future connection in the .env file)

    sudo -u postgres psql
    
    CREATE DATABASE <dbname>;
    CREATE USER <username> WITH PASSWORD '<user_password>';
    ALTER ROLE <username> SET client_encoding TO 'utf8';
    ALTER ROLE <username> SET default_transaction_isolation TO 'read committed';
    ALTER ROLE <username> SET timezone TO 'UTC';
    GRANT ALL PRIVILEGES ON DATABASE <dbname> TO <username>;
    
    \q

### STEP 4

Create venv

    sudo python3 -m venv venv
    
And activate it
    
    source venv/bin/activate  

### STEP 5

Install all pip pakages from requirements.txt file:

    sudo pip3 install -r requirements.txt
    
Also you can install environ for venv vars

    sudo apt-get install environ

### STEP 6

Create .env file or copy .env_template:

    less .env_template > .env
    
Or 
    
    vim .env
    
After change all vars on your values

### STEP 7 

Make migrations in django project:

    python manage.py makemigrations
    python manage.py migrate
    
Also you can create super user for login in admin panel (127.0.0.1:8000/admin)

    python manage.py createsuperuser
    
And input your data

### STEP 8 

Run project local:

    python3 manage.py runserver 127.0.0.1:8000
    
In requirements.txt we have Gunicorn, becouse you can run it

    gunicorn karat_avto.wsgi -b 127.0.0.1:8000
    
