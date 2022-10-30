ECHO OFF

ECHO Upgrading pip
ECHO =============

python -m pip install --upgrade pip

ECHO Getting pip version
ECHO ===================

python -m pip --version

ECHO Installing virtualenv
ECHO =====================

python -m pip install --user virtualenv


ECHO Creating virtual env
ECHO =====================

python -m venv venv

ECHO Activating virtual environment
ECHO ==============================

.\venv\Scripts\activate & pip install -r requirements.txt

ECHO Getting where python is
ECHO ========================

where python

ECHO Installing requirements pip install -r requirements.txt
ECHO ========================


ECHO Deactivationg env
ECHO ==========================

deactivate

ECHO After successful installation you can close this window...

PAUSE
