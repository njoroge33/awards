# Awards

 An application like Awwards that will allow a user to post a project he/she has created and get it reviewed by his/her peers.

## As users you can :
* Sign in to the application to start using.
* Upload your projects images to the application.
* You can view other users projects on the home page.
* Rate a project according to its usability.

### Usage example

1. signup then login.
2. Open the website and browse the projects.
3. If you see a project that interests you you can click on it to view it.***


## Development setup

- To access the Code behind this site, you will need to:

1. Clone this repo:
  ```bash
  git clone https://github.com/njoroge33/awards
  ```
2. Move to the folder and install requirements
  ```bash
  cd awards
  pip install -r requirements.txt
  ```
3. Create database on psql shell
  ```SQL
  psql
  CREATE DATABASE awards;
  ```
4. Migrate the database and run the application
  ```bash
  python manage.py migrate
  python manage.py runserver
  ```

## Technologies Used
- Python3.6
- Django

## License
MIT &copy;2020 [John Gichuhi](https://github.com/njoroge33/awards/blob/master/LICENSE)
Awards

