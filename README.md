# SplunkTakeHomeExercise

Take home exercise for Splunk position.

For database config we could use a .env instead.

## Crawler.py

Crawler process to extract certain objects from several Splunk servers, such as:

- Apps
- Dashboards
- Fields
- Saved Searches or Reports

Dependencies:

- requests
- yaml
- pymongo

## Storage

Data is stored in a MongoDB database.

## Server

Deployed in Flask.

Dependencies:

- flask
- flask_pymongo
- flask_cors
- yaml
- bson

### Endpoints

- /
  - Method: GET
  - Index page
- /overview

  - Method: GET
  - Returns an JSON array with all the object types and the number of that type (count)

- /list?type=

  - Method: GET
  - List of type or get all by using type all

- /add

  - Method: POST
  - type: meta-tag or classification
  - Body:

    {
    "id" : "\_id",
    "value" : ["a", "b", ...] if meta tag or "classification_type"
    }

- / Method: GET -> index

## Client

### Had to downgrade Webpack

https://www.npmjs.com/package/webpack?activeTab=versions
https://stackoverflow.com/questions/43589964/how-to-downgrade-version-of-webpack

### Issue with querystring

https://stackoverflow.com/questions/70640271/getting-the-error-module-not-found-error-cant-resolve-querystring-how-do

Link SPLUNK_HOME environment to app.
