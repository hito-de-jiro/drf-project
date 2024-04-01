## Online Learning Platform (API)
This demo project is an API for an online platform built on Django Rest Framework.<br>
It provides the ability to interact with educational materials such as lessons and courses through a convenient and secure interface.<br>
Users can access their accounts, explore available products and lessons, and track their learning progress.<br>
This project demonstrates the key features of an API for creating and managing an online educational platform using Django Rest Framework.
### How to clone the repository?
To clone the repository, run the following command.
```shell
git clone https://github.com/hito-de-jiro/drf-project
```
### Preparation
Install Python venv.
```shell
pip install virtualenv
virtualenv venv
```
Activate venv (windows).
```shell
venv\Scripts\activate
```
### Build
1. Install dependencies of project.
   ```shell
   pip install -r requirements.txt
   ```
2. Make and apply project migrations.
   ```shell
   python manage.py makemigrations
   python manage.py migrate
   ```
3. Create superuser.
   ```shell
    python manage.py createsuperuser
   ```
4. Run server.
   ```shell
   python manage.py runserver
   ```
### Using the app
Product and lesson data are manually added to the database.<br>
Changing the viewing time is possible using the appropriate API at the [link](http://127.0.0.1:8000/api/v1/update-lesson/) <br>