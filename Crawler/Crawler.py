import requests, yaml, pymongo

CONFIG_FILE = "./config.yaml"

DB_CONFIG = "../Database/dbconfig.yaml"

body = {}
body["output_mode"] = "json"

params = {"count": "0"}

def getDashboards(hostname, host, port, user, password, objectList):
    url = host + ":" + port
    requestDashboards = url + "/servicesNS/-/-/data/ui/views"
    response = requests.get(url=requestDashboards, auth=(user, password), data=body, verify=False, params=params).json()

    dashboards = response["entry"]

    for dashboard in dashboards:
        dbEntry = {"splunk_host" : hostname + "@" + url,
                   "type": "Dashboard",
                   "object_info" : dashboard,
                   "custom_meta_labels" : [],
                   "custom_classification" : ""
                   }
        
        objectList.append(dbEntry)
        
def getSavedSearches(hostname, host, port, user, password, objectList):
    url = host + ":" + port
    requestSearches = url + "/servicesNS/-/-/saved/searches"
    response = requests.get(url=requestSearches, auth=(user, password), data=body, verify=False, params=params).json()

    savedSearches = response["entry"]

    for savedSearch in savedSearches:
        dbEntry = {"splunk_host" : hostname + "@" + url,
                   "type": "Report",
                   "object_info" : savedSearch,
                   "custom_meta_labels" : [],
                   "custom_classification" : ""
                   }
        
        objectList.append(dbEntry)

def getApps(hostname, host, port, user, password, objectList):
    url = host + ":" + port
    requestApps = url + "/services/apps/local?f=table&f=label&f=title&f=version&f=description"

    appsParams = {"count": "0",
                    "search": "disabled=0"}
    response = requests.get(url=requestApps, auth=(user, password), data=body, verify=False, params=appsParams).json()

    apps = response["entry"]
    
    for app in apps:
        dbEntry = {"splunk_host" : hostname + "@" + url,
                   "type": "App",
                   "object_info" : app,
                   "custom_meta_labels" : [],
                   "custom_classification" : ""
                   }
        
        objectList.append(dbEntry)


# TODO : Might need to create custom endpoint. Need to do more research
def getFields():
    return 0

#---------------MAIN------------------

def main():
    with open(CONFIG_FILE) as configFile:
        serversFile = yaml.safe_load(configFile)
        servers = serversFile['servers']

        if(len(servers) < 0):
            raise Exception("There are no servers in the file: " + CONFIG_FILE)

    with open(DB_CONFIG) as dbConfigFile:
        dbConfig = yaml.safe_load(dbConfigFile)
    
    client = pymongo.MongoClient(dbConfig["client"])
    
    db = client[dbConfig["database"]]
    dbCollection = db[dbConfig["collection"]]

    objectList = []

    for server in servers:
        getDashboards(server["hostname"],
                                server['host'],
                                str(server['port']),
                                servers[0]['user'],
                                servers[0]['password'],
                                objectList)
        getSavedSearches(server["hostname"],
                                server['host'],
                                str(server['port']),
                                servers[0]['user'],
                                servers[0]['password'],
                                objectList)
        getApps(server["hostname"],
                                server['host'],
                                str(server['port']),
                                servers[0]['user'],
                                servers[0]['password'],
                                objectList)
        
    if (len(objectList) > 0):
        result = dbCollection.insert_many(objectList)
        # print(result.inserted_ids)

    client.close()
        
if __name__ == "__main__":
    main()