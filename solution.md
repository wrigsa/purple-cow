# The Purple Cow Project
This repository contains code for the Purple Cow Project. 

The Purple Cow Project includes:
* A restful API served on port 3000.
* endpoints on the "/items" resource that allow clients to retrieve the current items, set the list of items, and delete all of the items. Mosre on this below.
* Item objects with two attributes, "id" and "name."
* Items persisted in memory while the application is running. More on this below.

To build the web app, run docker-compose up -d --build in the base directory

To run the web app, run docker-compose exec web python manage.py create_db

To tear down the web app, run docker-compose down -v
