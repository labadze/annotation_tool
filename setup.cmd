ECHO OFF
ECHO Creating virtual environment

python -m pip install --upgrade pip

python -m pip --version

python -m pip install --user virtualenv

python -m venv venv

ECHO Activating virtual environment

`.\venv\Scripts\activate`

where python

pip install -r requirements.txt

ECHO After successful installation you can close this window...