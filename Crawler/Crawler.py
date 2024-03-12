import requests, yaml

CONFIG_FILE = "./config.yaml"

with open(CONFIG_FILE) as configFile:
    serversFile = yaml.safe_load(configFile)
    servers = serversFile['servers']

if(len(servers) < 0):
    raise Exception("There are no servers in the file: " + CONFIG_FILE)

requestUrl = servers[0]['host'] + ":" + str(servers[0]['port']) + "/servicesNS/-/-/saved/searches"

body = {}
body["output_mode"] = "json"

print(requestUrl)

response = requests.get(url=requestUrl, auth=(servers[0]['user'], servers[0]['password']), data=body, verify=False)


print(response.json())