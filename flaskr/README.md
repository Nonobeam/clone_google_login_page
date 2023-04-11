# FPTAlumni

This reposity only be used for FPT Alumni under monitoring.

PLEASE DO NOT COPY UNDER ANY CIRCUMSTANCE

SETUP REQUIRE IF YOU WANT TO USE FLASK

**FOLLOW THE FILE STRUCTURE RECOMMNED FROM FLASK**

```
/home/user/Projects/flask-tutorial
├── flaskr/
│   ├── __init__.py
│   ├── db.py
│   ├── schema.sql
│   ├── auth.py
│   ├── blog.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── auth/
│   │   │   ├── login.html
│   │   │   └── register.html
│   │   └── blog/
│   │       ├── create.html
│   │       ├── index.html
│   │       └── update.html
│   └── static/
│       └── style.css
├── tests/
│   ├── conftest.py
│   ├── data.sql
│   ├── test_factory.py
│   ├── test_db.py
│   ├── test_auth.py
│   └── test_blog.py
├── venv/
├── setup.py
└── MANIFEST.in
```

**SETUP VIRTUAL ENVIRONMENT**
*First, install python from the main python website*

*Install pip form python using this line*

``` py get-pip.py ```

*In this case I will do this in Window and python v3*

```py -3 -m pip install virtualenv```

*Create the env folder using cmd*

```mkdir <your project name here>```

*Move inside the new project*

```cd <your project name here>```

*Create env*

```py -3 -m venv venv```

*Activate the environment*

```venv\Scripts\activate```

**INSTALL FLASK**

```pip install flask```

**RUNNING APPLICATION**

*Activate the env first using the above cmd line*
*Start your python file*

```flask --app <your python file name> run```