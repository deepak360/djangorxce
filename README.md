# Matrimony Website

# activate virtual env
    source env/bin/activate

# locate your project folder
    cd djangorxce

# run your django application
    python3 manage.py runserver

# create dependencies file (DO NOT RUN BELOW COMMAND)
    pip3 freeze > requirements.txt

# install dependencies
    pip3 install -r requirements.txt

# set your git remote upstream
    git remote add upstream https://github.com/deepak360/djangorxce.git

# pull latest code
    git pull upstream master

# push your branch code
    sudo git push origin WRITE-BRANCH-NAME-HERE

# how to check your current branch
    git branch

# create new branch
    git checkout -b YOUR-BRANCH-NAME