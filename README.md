# SplunkTakeHomeExercise

Take home exercise for Splunk position.

For database config we could use a .env instead.

## Crawler.py

Crawler process to extract certain objects from several Splunk servers, such as:

- Apps
- Dashboards
- Fields
- Saved Searches or Reports

## Storage

Data is stored in a MongoDB database.

## Client

### Had to downgrade Webpack

https://www.npmjs.com/package/webpack?activeTab=versions
https://stackoverflow.com/questions/43589964/how-to-downgrade-version-of-webpack

### Issue with querystring

https://stackoverflow.com/questions/70640271/getting-the-error-module-not-found-error-cant-resolve-querystring-how-do

Link SPLUNK_HOME environment to app.
