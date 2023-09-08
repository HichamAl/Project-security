# Kadaster

## Getting Started

### SSH
First [upload your SSH key to gitlab]() if you haven't done it already.

Clone the repository and switch to the `Kadaster` branch

```sh
git clone git@gitlab.fdmci.hva.nl:almakrh/project-security.git Kadaster
cd Kadaster
git checkout Kadaster
```

## Installation

### Python Virtual Environment
First make a virtual environment in Python. Make sure that you have Python on your device before creating virtual environment.
```sh
python3 or python -m venv venv
```

#### Windows
In windows you can activate the virtual environment by running the active script while you are in the `Kadaster`directory.
```sh
venv\Scripts\activate
```

### Install Packages
Install the packages with pip
```sh
pip install -r requirements.txt
```

## Quick Start
If you followed the getting started section you can now run the app.
```
cd Project_security
python manage.py runserver
```


## Support


Documentation [Django website](https://docs.djangoproject.com/en/4.1/intro/tutorial01/).
Documentation[Gitlab](https://git-scm.com/docs).




