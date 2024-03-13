import requests, yaml

CONFIG_FILE = "./config.yaml"

body = {}
body["output_mode"] = "json"

params = 

def getDashboards(host, port, user, password):
    requestDashboards = host + ":" + port + "/servicesNS/-/-/data/ui/views"
    response = requests.get(url=requestDashboards, auth=(user, password), data=body, verify=False, params=).json()
    return response


with open(CONFIG_FILE) as configFile:
    serversFile = yaml.safe_load(configFile)
    servers = serversFile['servers']

if(len(servers) < 0):
    raise Exception("There are no servers in the file: " + CONFIG_FILE)



for server in servers:
    response = getDashboards(server['host'], str(server['port']), servers[0]['user'],servers[0]['password'])

    print(response)