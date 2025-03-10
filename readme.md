# Tasks of the lab

## fire up the flask app

    - create a git repo
    - download the flask app(material.zip)
    - create a venv(using python 3.12)
        > python3.12 -m venv venv
        > source venv/bin/activate
    - install the requirements
        > pip install -r app/requirements.txt
    - run the flask app
        > flask run --host=0.0.0.0 --port=5005 --debug
        /* you need to specify the debug mode otherwise by default the terminal starts the server without the debug mode which leads reflecting no changes.*/

        > python app.py
        /*alternatively you can run this so that the server starts from app.py itself where you have mentioned to run the debug mode*/

## putting in git and merging branches

    > git init, add, create main branch, add remote repo
    >
