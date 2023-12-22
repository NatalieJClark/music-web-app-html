# Music Web App HTML

## Introduction

- This is my Music Web App HTML project for Makers Module 4 - Web Applications
- It is the second project for phase 3 of the module
- It is a simple music web app that stores album and artist data in a database and shows the user requested data as HTML pages.
- The user can view an HTML page listing the albums or artists.
- The user can view an HTML page for an individual album or artist from the main list.
- The user can fill in a form to add new albums and artists, which then show up in the main list.

## Objectives

I used this project to:
- [x] Consolidate HTML structure knowledge
- [x] Consolidate knowledge of testing for HTML content
- [x] Learn how to use templates to return dynamic HTML
- [x] Learn how to use links to send GET requests
- [x] Learn how to test links
- [x] Learn how to use forms to send POST requests
- [x] Learn how to test drive a form

## Problems

- Currently all new Albums created have `artist_id=1`

## Setup

```shell
# Clone the repository to your local machine
; git clone https://github.com/NatalieJClark/music_web_app_html.git YOUR_PROJECT_NAME

# Enter the directory
; cd YOUR_PROJECT_NAME

# Install dependencies and set up the virtual environment
; pipenv install

# Activate the virtual environment
; pipenv shell

# Install the virtual browser we will use for testing
; playwright install
# If you have problems with the above, contact your coach

# Create a test and development database
; createdb YOUR_PROJECT_NAME
; createdb YOUR_PROJECT_NAME_test

# Open lib/database_connection.py and change the database names
; open lib/database_connection.py

# Seed the development database (ensure you have run `pipenv shell` first)
; python seed_dev_database.py

# Run the tests (with extra logging)
; pytest -sv

# Run the app
; python app.py
# Now visit http://localhost:5001/albums or http://localhost:5001/artists in your browser

```
