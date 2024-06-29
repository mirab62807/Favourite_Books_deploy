#!/bin/bash
# exit on error

set -o errexit

# Activate the virtual environment
source python/myDjangoEnv/Scripts/activate.bat

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate