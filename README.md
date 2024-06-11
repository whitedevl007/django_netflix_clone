# Django Netflix Clone
This is a clone of the popular video streaming site Netflix. Built using Django and uses the requests library to handle data from TMDB API.

!(Screenshot.PNG)

## Requirements
The user can perform the following functions:

- A user can view the different movies and Tv shows that are available.
- A user can view a description Of the movie.
- A user can create profiles based on age limit.

## Installation / Setup instruction
The application requires the following installations to operate:
- pip
- gunicorn
- django
- sqlite3
- requests

## Technologies Used
- python 3.10.12

## Project Setup Instructions
1) git clone the repository 
```
https://github.com/steve-njuguna-kDjango-Netflix-Clone.git
```
2. cd into Django-Netflix-Clone
```
cd Django-Netflix-Clone
```
3. create a virtual env
```
py -m venv env
```
4. activate env
```
env\scripts\activate
```
5. Open CMD & Install Dependancies
```
pip install -r requirements.txt
```
6. Make Migrations
```
py manage.py makemigrations
```
7. Migrate DB
```
py manage.py migrate
```
8. Run Application
```
py manage.py runserver
```

## Known Bugs
- There are no known bugs currently but pull requests are allowed incase you spot a bug
