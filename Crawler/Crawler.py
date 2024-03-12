import requests, yaml

CONFIG_FILE = "./config.yaml"

with open(CONFIG_FILE) as configFile:
    serversFile = yaml.safe_load(configFile)
    servers = serversFile['servers']

if(len(servers) < 0):
    raise Exception("There are no servers in the file: " + CONFIG_FILE)

body = {}
body["output_mode"] = "json"

for server in servers:
    requestDashboards = server['host'] + ":" + str(server['port']) + "/servicesNS/-/-/data/ui/views"
    response = requests.get(url=requestDashboards, auth=(servers[0]['user'], servers[0]['password']), data=body, verify=False).json()

    print(response['entry'][0])