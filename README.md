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

# createsuperuser
    python3 manage.py createsuperuser
    
# postgre commands
    1.  sudo -i -u rxce
    2.  postgres@deepak:~$ psql
    3.  connect DB : postgres=# \c rxce
    4.  rxce-# psql -U postgres -d rxce
    5.  rxce-# \dt
    6.  rxce=# \dt+

# Postgres Installation & Configuration 
    sudo apt-get update
    sudo apt-get install postgresql postgresql-contrib
    ls /etc/postgresql/9.5/main/
    service postgresql
    service postgresql status
    sudo su postgres
    psql
    \l (All User)
    \du (All databases)
    ALTER USER postgres WITH PASSWORD 'password'; (change default user password postgres)
    CREATE USER rxce_user WITH PASSWORD 'password'; (create new user)
    ALTER USER rxce_user WITH SUPERUSER; (add privilages)


    1.  service postgresql
    2.  sudo su postgres (this is default user)
    3.  psql(command line tool open)
    4.  \l (DATABASE)
    5.  \du (ALL USER)

    A.  Change user 
        ALTER TABLE postgres WITH PASSWORD 'password';
    
    B.  create user
        CREATE USER user_1 WITH PASSWORD 'test123';
    
    C. provide previllege to user
        ALTER USER root WITH SUPERUSER;

    D. delete user
        DROP USER user_1;

    E. see all commands of psql
        man psql

    F. GRANT ALL PRIVILEGES ON DATABASE rxce TO root;

#   RESET MIGRATION
    1.  Delete all migrations folder
    2.  delete all tables from database except django_migrations
    3.  truncate table django_migrations
    4.  python3 manage.py reset_migrations profiledetail
    5.  python3 manage.py reset_migrations api

#   CREATE SUPERUSER