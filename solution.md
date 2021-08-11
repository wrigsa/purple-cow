# The Purple Cow Project
This repository contains code for the Purple Cow Project. 

The Purple Cow Project includes:
* A restful API served on port 3000.
* endpoints on the "/items" resource that allow clients to retrieve the current items, set the list of items, and delete all of the items. Mosre on this below.
* Item objects with two attributes, "id" and "name."
* Items persisted in memory while the application is running. More on this below.

To build the web app, run docker-compose up --build in the base directory

## cURL requests to interact with the endpoints

### Set, Get, and Delete all Items

To set all the items in the database, run (replacing the names with your desired names)

`curl --location --request POST 'http://127.0.0.1:3000/items' \
--header 'Content-Type: text/plain' \
--data-raw '[{"name": "catty mcCatFace"}, {"name": "batty mcBatFace"}]'`

To get all the items in the database, run 

`curl --location --request GET 'http://127.0.0.1:3000/items'`

To delete all the items in the database, run 

`curl --location --request DELETE 'http://127.0.0.1:3000/items'`

### Add to the List of Items

To add to the list of items in the databse. run (replacing the names with your desired names)

`curl --location --request POST 'http://127.0.0.1:3000/items/add' \
--header 'Content-Type: text/plain' \
--data-raw '[{"name": "catty mcCatFace"}, {"name": "batty mcBatFace"}]'`

### Get item, delete item, or update item by ID

To get an item by id, run (replacing \<id\> with your desired id)

`curl --location --request GET 'http://127.0.0.1:3000/items/<id>'`

To delete an item by id, run (replacing \<id\> with your desired id)

`curl --location --request DELETE 'http://127.0.0.1:3000/items/<id>'`


To update an item by id, run (replacing \<id\> with your desired id and replacing the name with your desired name)

`curl --location --request PUT 'http://127.0.0.1:3000/items/3' \
--header 'Content-Type: text/plain' \
--data-raw '{"name": "catty mcCatFace"}'`

