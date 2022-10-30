# Annotation Tool V 0.0.1

This is very simple annotation tool, with minimum 3rd party libraries, based on CANVAS HTML/CSS/JS & Python (Flask).


To generate image list place your images to `static/img` it's much better to keep unix type file names (snake_case without special symbols).

Right now `.PNG`, `JPG`, `JPEG` formats are supported.

Make sure that `data.json` exists in the project root.

You can view detailed video presentation (here)[https://youtu.be/XdZvH-sYCs0] .

More documentation is presented in (Wiki)[https://github.com/labadze/annotation_tool/wiki] .

If you have found some issue please write down (Here)[https://github.com/labadze/annotation_tool/issues]

NOTE __I'm checking non critical issues every 24 hours every working day (Monday-Friday)__



## First and One time setup

To run application you need one time setup per machine. 

Make sure you've installed python 3.8 or higher.

Just open terminal for linux or cmd for windows and type `python --version` and you will see python version as output.


Create virtual environment using script:
 - For Linux Mac BSD systems `setup.sh`
 - For Windows `setup.cmd`



## Run application

All you need is run `main.sh` for Linux / Mac or click `main.cmd` for Windows .

Note for display any changes you need to rerun application (Close `main.cmd` or `main.sh` window and run it again.


## Usage specifications

There is no image upload mechanism for this application. So to build annotation make sure that you have 2 components:

 - In `/static/img` placed images
 - `data.json` in project root

IMPORTANT please choose file names without spaces or special characters, the best way is shown in an example bellow:

`file_name.extenstion`

For example: `image.png`, `pucture.jpg`, `some_name_of_file.jpeg` .


### Supported file types

All images supported by browsers can be used, now it's tested with file types: `.PNG`, `JPG`, `JPEG`


## How to report issue:

Issue must have following format:

 - OS (Windows, Linux, Mac) please



## Folder stricture

    .
    ├── ...
    ├── static                           # Static folder files and folders located here are accessable for browsers
    │   ├── img                          # !!!IMPORTTANT!!! Your content (IMAGES) must be here...
    │   ├── favicon.con                  # Favicon file
    │   ├── snackbar.css                 # Snackbar styles file
    │   └── w3.css                       # Stylesheet CSS for goo visual
    ├── templates                        # Here are files which python renders in browser
    │   └── index.html                   # Main file which is shown for user at start, most operations are called from here
    ├── .gitignore                       # Requered to prevent load venv to git repository
    ├── app.py                           # Programmatically everything nice happens here
    ├── data.json                        # Here is stored annotations data, coordinates, other values including image names from img folder
    ├── LICENSE                          # Standard license from upwork copied here
    ├── main.cmd                         # Start application script for MS Windows users
    ├── main.sh                          # Start application script for Linux users
    ├── README.md                        # you're here
    ├── requirements.txt                 # Installed packeges via pip are stored here.
    ├── setup.sh                         # Setup script for Linux users
    └── setup.cmd                        # Setup script for MS Windows users



