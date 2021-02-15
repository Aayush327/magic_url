# Magic Url

Backend is live at 	`http://magic-url-api.herokuapp.com/`

# Get/Post/List urls
Urls: `	http://magic-url-api.herokuapp.com/endpoints/url`

# Get details of url
Urls: `http://magic-url-api.herokuapp.com/endpoints/test/<url>`

Run following commands:
    install python3.6
    install pip3:

`pip install virtualenvwrapper`
`mkvirtualenv <env-name>`
Activate the virtual environment:
    workon <env-name>

Clone the project from the github:
    git clone https://github.com/Aayush327/magic_url.git


Install requirement by `pip install -r requirements.txt`
Install RabbitMQ by `sudo apt-get install rabbitmq-server`

Check if RabbitMQ server running by `sudo service rabbitmq-server status`, if its not run server by running `sudo service rabbitmq-server start`

Run celery worker along with beat scheduler by running `celery -A magic_url worker --beat --loglevel=debug`

Run the migrations
    `python manage.py migrate`

Create a superuser:
    `python manage.py createsuperuser`

Run server:
    `python manage.py runserver`

Deactivate the virtual environment:
    `deactivate`

# Urls:
1 - `/endpoints/url`
2 - `endpoints/test/<url>`
