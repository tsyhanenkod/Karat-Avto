# CAR SHOWROOM "KARAT-AVTO" 

This is my first django project for deployment. You can try to user whis web-service to link: www.karat-avto.com.ua

Technologies: Python-3.10, Django-4, Bootstrap-5, HTML/CSS/JS, Google Maps API, Google SMTP.  

## QUICK LOCAL START

All commands only for Linux systems! If you want start this project local you need do this steps:

### STEP 1

Install packages for venv and python:

    sudo apt install python3.10 pip3
    sudo pip3 insatll environment

### STEP 2

Create virtualenv by commands:

    sudo python3 -m venv venv
    source .venv/bin/activate   //activate venv 

### STEP 3

Clone this repository on your local machine:
    
    git clone 'link on this project'

### STEP 4

Install all pip pakages from requirements.txt file:

    sudo pip3 insatll -r requirements.txt

### STEP 5

Copy .ent_template data to .env file and change vars value:

    cp .env_template /.env

### STEP 6 

Export all env vars to project by bash:

    while read file; do
        export "$file"
        done < .env

### STEP 7 

Run project local:

    python3 manage.py runserver 127.0.0.1:8000