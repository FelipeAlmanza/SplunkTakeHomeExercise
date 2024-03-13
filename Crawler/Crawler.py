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
        
def getSavedSearchesOrReports(hostname, host, port, user, password, objectList):
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