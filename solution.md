# The Purple Cow Project
This repository contains code for the Purple Cow Project. 

The Purple Cow Project includes:
* A restful API served on port 3000.
* endpoints on the "/items" resource that allow clients to retrieve the current items, set the list of items, delete all of the items, and more. More on this below.
* Item objects with two attributes, "id" and "name."
* Items persisted in memory while the application is running. The application utilizes a postgres database to store and retrieve data. 

To build the web app, run `docker-compose up --build` in the base directory

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

## Upcoming

In the future, I'd like to work to do more error handling to check the data passed to the endpoints. I'd also like to identify and test the corner cases for robustness.

Feature-wise, I'd like to add the ability to seach for items by name, trash items instead of deleting them to soft delete items, and I'd like to add the ability to create relationships between the items so that the user may easily traverse the database by accessing those relationships.

