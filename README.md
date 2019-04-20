# Jacob's Ladder Profile Assessment API
A Django Rest Framework based back-end of the new electronic student assessment system at [Jacob's Ladder Center](https://www.jacobsladdercenter.com/) in Roswell, GA.

The front-end code for the tool can be found here: [AssessmentTool](https://github.com/JacobsLadderJD/AssessmentTool).

## Release notes

## Libraries to know about
- **pip [v9.0.1]:** A Python package installer ([docs](https://pypi.org/project/pip/))
- **Django [v2.1.7]:** A Python-based web framework ([docs](https://djangoproject.com))
- **Django Rest Framework [v3.9.1]:** A Django framework used for creating REST APIs ([docs](https://www.django-rest-framework.org/))
- **django-cors-headers [v2.4.0]:** A Django App that assists in use of Cross Origin Resource Sharing headers ([docs](https://pypi.org/project/django-cors-headers/))
- **psycopg2 [v2.7.7]:** A library adapting PostgreSQL database commands to Python ([docs](http://initd.org/psycopg/))

## Project installation
These installation instructions are designed with UNIX-based systems in mind. Both Mac and Ubuntu will be covered here. Windows installation may vary, but links to external tutorials are provided where appropriate.

### Installing Python and related tools
#### 1. Install Python 3
Go to https://www.python.org/downloads/ and download the latest version of Python 3.

Follow the installer instructions. These should be relatively straightforward, and there are many resources available online.

After completing the install, verify it worked by opening a terminal window and typing:
```
$ python --version
```
This should report which version of Python you installed. If this does not work, or it says it is version 2, you may need to type `python3` instead of `python`. If this is the case, continue to use `python3` until the virtual environment is loaded (in a later step).

#### 2. Create a virtual environment
Go to the folder that holds the AssessmentAPI project (where you find `manage.py`) in a terminal window, then type the following:
```
$ python -m venv ./env
```
This should create a folder here called "env", and along with it installed Python and pip in that environment. Activate the virtual environment at any type by opening a terminal and typing:
```
$ source env/bin/activate
```
You can also exit the virtual evironment at any time by closing the terminal window, or typing:
```
$ deactivate
```
You will need to have the virtual environment activated throughout the following steps, and whenever you want to run or manage the server.

**Note:** Even if you previously had to type `python3` instead of `python`, whenever the virtual environment has been activated, you can just type `python`.

#### Troubleshooting
Based on experience, you may encounter the following problems when attempting to follow the above instructions.
##### 1. Python is not recognized after the install
Try typing `python3` instead of `python`. If this is the case, continue to use `python3` until you are in a virtual environment.
##### 2. 'No such file or directory' when trying to activate the virtual environment
The second part of the activation command is the path to the `activate` file. Find this file in a file explorer, and ensure you are giving `source` the correct path.

### Installing Django and its libraries
#### 1. Activate the virtual environment
If the virtual environment is not already activated, go to the folder that holds the AssessmentAPI project (where you find `manage.py`) in a terminal window, then type the following:
```
$ source env/bin/activate
```
If you have any issues with this, see the above "Create a virtual environment".

#### 2. Install Django
Type the following commands in order, each after the previous finishes sucessfully:
```
$ pip install django
```
```
$ pip install django-cors-headers
```
```
$ pip install djangorestframework
```
You should see each of the Django components being installed in the virtual environment.

### Setting up the database
This part differs greatly between systems running OSX and systems running Linux. The instructions have been divided to reflect this.
#### Mac (OSX) instructions
##### 1. Install Homebrew
If you do not already have Homebrew installed, go to https://brew.sh/ and follow the Install Homebrew instructions there.

##### 2. Install PostgreSQL
Open a terminal window and run the following command:
```
$ brew install postgresql
```
Follow the instructions to complete the installation.

##### 3. Run the postgresql service
Every time you work with the server or the database on an OSX system, run the following command first:
```
$ brew services start postgresql
```
You can stop it at any time by replacing `start` with `stop`, but make sure you start it again before working with the server or the database.

After it is running, run the follwing command:
```
$ psql postgres
```

#### 4. Create the database
Run the following commands in order:
```
$ CREATE USER jlcassessmentuser WITH PASSWORD 'jacobsladder';
$ ALTER ROLE jlcassessmentuser SET client_encoding TO 'utf8';
$ ALTER ROLE jlcassessmentuser SET default_transaction_isolation TO 'read committed';
$ ALTER ROLE jlcassessmentuser SET timezone TO 'UTC';
$ CREATE DATABASE jlcassessment;
$ GRANT ALL PRIVILEGES ON DATABASE jlcassessment TO jlcassessmentuser;
$ \q
```
This should have created the new database.

#### 5. Install psycopg2
Ensure the virtual environment is activated, then run the following:
```
$ pip install psycopg2
```

#### 6. Migrate the database
Finally, we have to get the new database ready to run the Assessment API. Make sure your terminal window is in the same folder as `manage.py` and a virtual environment is activated, then run the following:
```
$ python manage.py migrate
```
This should give you feedback showing that the database has been successfully migrated. You can now continue to the instructions for running the server for the first time.

##### Troubleshooting
Based on experience, you may encounter the following problems when attempting to follow the above instructions.
###### 1. psql: could not connect to server: No such file or directory
Go to your computer's settings and remove the Postgres user. Then run the following commands:
```
$ brew services stop postgresql
$ brew uninstall postgresql
```
After this, remove any remnants of the PostgreSQL installation on your system, then start the installation instructions from the beginning.

#### Linux instructions
##### 1. Install Postgres
Go to https://www.postgresql.org/download/ and select the installation instructions for your variety of Linux. Follow them exactly. If you are having issues getting it to properly install, search online for specific walkthroughs for your Linux version.

##### 2. Running the postgres utility
In a terminal window, run the following:
```
$ sudo su - postgres
```
This will ask for your password, then run the terminal as the special postgres user. Run the PostgreSQL utility by typing:
```
$ psql
```

#### 3. Create the database
Run the following commands in order:
```
$ CREATE USER jlcassessmentuser WITH PASSWORD 'jacobsladder';
$ ALTER ROLE jlcassessmentuser SET client_encoding TO 'utf8';
$ ALTER ROLE jlcassessmentuser SET default_transaction_isolation TO 'read committed';
$ ALTER ROLE jlcassessmentuser SET timezone TO 'UTC';
$ CREATE DATABASE jlcassessment;
$ GRANT ALL PRIVILEGES ON DATABASE jlcassessment TO jlcassessmentuser;
$ \q
```
This should have created the new database. You can now exit the special postgres user terminal by typing:
```
$ exit
```

#### 4. Install psycopg2
Ensure the virtual environment is activated, then run the following:
```
$ pip install psycopg2
```

#### 5. Migrate the database
Finally, we have to get the new database ready to run the Assessment API. Make sure your terminal window is in the same folder as `manage.py` and a virtual environment is activated, then run the following:
```
$ python manage.py migrate
```
This should give you feedback showing that the database has been successfully migrated. You can now continue to the instructions for running the server for the first time.

##### Troubleshooting
Based on experience, you may encounter the following problems when attempting to follow the above instructions.
###### 1. Ubuntu installation is not working by the instructions on the PostgreSQL website
Try running the following commmands:
```
$ sudo apt-get remove postgresql postgresql-contrib
$ sudo apt-get update
$ sudo apt-get install python-pip python-dev libpq-dev postgresql postgresql-contrib
```

## Running the Server
After the installation instructions have been followed, the server can be run to support the front-end AssessmentTool.


### First time setup
If the server has not been run before, after all the setup described above has been completed, there are a few things that need to be done.
#### 1. Create the admin user
The server has to have an administrator-level user. Their username needs to be a **valid email** for other parts of the server to function. Activate the virtual environment, then run the following command:
```
$ python manage.py createsuperuser
```
When asked for the username, make sure it is a valid email. The actual email field can be left blank.
#### 2. Run the server
Run the following command:
```
$ python manage.py runserver
```
This command takes over the terminal, and stays active as long as the server is running. The server can be stopped at any time by pressing `Ctrl+C` on the keyboard.
#### 3. Finish admin user setup
Open a web browser and navigate to <localhost:8000/admin>. Log in with the username and password you created in the first step.

When the admin panel comes up, select "Users" and then the user you created. Scoll to the bottom, and where you see fields for "firstName" and "lastName", fill them out, then hit Save.

### Running the Server other times
After the initial setup has been completed, the server can be run at any time by opening a terminal window, navigating to the folder with `manage.py`, activating the virtual environment, the running `python manage.py runserver`. It can then be stopped at any time by pressing `Ctrl+C` on the keyboard.

## Common Server Tasks
Occasionally, something needs to be done with the API that cannot be done from the front-end. These things are listed below.

### Creating a new user
Run the server, then open a web browser and navigate to <localhost:8000/admin>. After logging in, select Users, then in the top-right, hit "Add User". Make sure to fill out all fields, then hit "Save".

This new user is not an administrator user, and thus cannot log into the admin panel on the back-end, but can use the front-end AssessmentTool just as well as any user.

### Editing an existing user's data
Run the server, then open a web browser and navigate to <localhost:8000/admin>. After logging in, select Users, then select the user you want to edit. Make the changes, then hit "Save".

### Deleting a user
Run the server, then open a web browser and navigate to <localhost:8000/admin>. After logging in, select Users, then hit the checkbox next to the users you want to delete. Find the dropdown at the top of the list titled "Actions", select "Delete selected users", then hit "Go". If this user has had any evaluations attributed to them, these must also be deleted, so the admin panel will ask you to confirm this. If you do not want to delete those evaluations, but would rather assign them to another evaluator, you must cancel the user deletion, go to Evaluations in the admin panel, then manually remove them as an evaluator from each evaluation attributed to them (or add a different evaluator if they were the only one). Then you can delete that user.

**Note:** If you delete the administrator user this way, you will need to complete the "First time setup" instructions for the server again.

### Creating a new student
Run the server, then open a web browser and navigate to <localhost:8000/admin>. After logging in, select Students, then in the top-right, hit "Add Student". Make sure to fill out all fields, then hit "Save".

### Editing an existing student's data
Run the server, then open a web browser and navigate to <localhost:8000/admin>. After logging in, select Students, then select the student you want to edit. Make the changes, then hit "Save".

### Deleting a student
Run the server, then open a web browser and navigate to <localhost:8000/admin>. After logging in, select Students, then hit the checkbox next to the students you want to delete. Find the dropdown at the top of the list titled "Actions", select "Delete selected students", then hit "Go". If this student has had any evaluations created for them, these must also be deleted, so the admin panel will ask you to confirm this.