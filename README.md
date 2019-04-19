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
#### 1. Step 1 Name
Step 1 description.

#### 2. Step 2 Name
Description with code example
```
$ example terminal things here
```
Terminal output expectation here.

#### Troubleshooting
Based on experience, a few things may cause problems when attempting to install or run the application. These issues are enumerated below.
##### 1. Issue 1 title

## Running the Server
After the installation instructions have been followed, the server can be run locally at any time by following these instructions.

Description with code example
```
$ example terminal things here
```
Terminal output expectation here.