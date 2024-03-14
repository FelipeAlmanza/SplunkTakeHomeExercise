import requests, yaml

CONFIG_FILE = "./config.yaml"

body = {}
body["output_mode"] = "json"

params = {"count": "0"}

def getDashboards(hostname, host, port, user, password, objectList):
    requestDashboards = host + ":" + port + "/servicesNS/-/-/data/ui/views"
    response = requests.get(url=requestDashboards, auth=(user, password), data=body, verify=False, params=params).json()

    dashboards = response["entry"]

    for dashboard in dashboards:
        dbEntry = {"splunk_host" : hostname,
                   "type": "Dashboard",
                   "object_info" : dashboard,
                   "custom_meta_labels" : [],
                   "custom_classification" : ""
                   }
        
        objectList.append(dbEntry)
        
def getSavedSearches(hostname, host, port, user, password, objectList):
    requestSearches = host + ":" + port + "/servicesNS/-/-/saved/searches"
    response = requests.get(url=requestSearches, auth=(user, password), data=body, verify=False, params=params).json()

    savedSearches = response["entry"]

    for savedSearch in savedSearches:
        dbEntry = {"splunk_host" : hostname,
                   "type": "Dashboard",
                   "object_info" : savedSearch,
                   "custom_meta_labels" : [],
                   "custom_classification" : ""
                   }
        
        objectList.append(dbEntry)

def getApps(hostname, host, port, user, password, objectList):
    requestApps = host + ":" + port + "/services/apps/local&f=table&f=label&f=title&f=version&f=description"

    appsParams = {"count": "0",
                    "search": "disabled=0"}
    response = requests.get(url=requestApps, auth=(user, password), data=body, verify=False, params=appsParams).json()

    apps = response["entry"]
    
    for app in apps:
        dbEntry = {"splunk_host" : hostname,
                   "type": "Dashboard",
                   "object_info" : app,
                   "custom_meta_labels" : [],
                   "custom_classification" : ""
                   }
        
        objectList.append(dbEntry)


with open(CONFIG_FILE) as configFile:
    serversFile = yaml.safe_load(configFile)
    servers = serversFile['servers']

if(len(servers) < 0):
    raise Exception("There are no servers in the file: " + CONFIG_FILE)

objectList = []

for server in servers:
    getDashboards(server["hostname"],
                                server['host'],
                                str(server['port']),
                                servers[0]['user'],
                                servers[0]['password'],
                                objectList)
    


    print(objectList)