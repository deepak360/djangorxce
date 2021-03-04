# Matrimony Website

# Create a virtual environment.
    python3 -m venv venv

# Activate the virtual environment.
    source venv/bin/activate

# Install python pip
    sudo apt-get install python3-pip

# Install django using pip package manager.
    pip3 install django

# Create django project
    django-admin startproject <PROJECT-NAME>

# Create a new app inside django project.
    python3 manage.py startapp <APP-NAME>

# Set your git remote upstream
    git remote add upstream https://github.com/deepak360/djangorxce.git

# Pull latest code
    git pull upstream master

# Push your branch code
    sudo git push origin WRITE-BRANCH-NAME-HERE

# How to check your current branch
    git branch

# Create new branch
    git checkout -b YOUR-BRANCH-NAME

# Activate virtual env
    source env/bin/activate

# Locate your project folder
    cd djangorxce

# Install dependencies
    pip3 install -r requirements.txt

# Run your django application
    python3 manage.py runserver

# Create dependencies file (DO NOT RUN BELOW COMMAND)
    pip3 freeze > requirements.txt