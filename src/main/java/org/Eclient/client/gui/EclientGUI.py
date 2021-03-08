import eel
import json
import os

eel.init((os.getcwd()+'\\src\\main\\java\\org\\Eclient\\client\\gui\\web\\'))

@eel.expose
def togglemodule(modulenm):
    with open(os.getenv('AppData')+'\\.minecraft\\mcpipy\\src\\main\\java\\org\\Eclient\\client\\Eclientconfig.json', 'r') as configpath:
        json_data = json.load(configpath)
        isenabled = json_data['modules'][modulenm]['Enabled']
        json_data['modules'][modulenm]['Enabled'] = not json_data['modules'][modulenm]['Enabled']

    with open(os.getenv('AppData')+'\\.minecraft\\mcpipy\\src\\main\\java\\org\\Eclient\\client\\Eclientconfig.json', 'w') as configs:
        json.dump(json_data, configs, indent=2)
        return str(isenabled)

@eel.expose
def loadmodules():
    with open(os.getenv('AppData')+'\\.minecraft\\mcpipy\\src\\main\\java\\org\\Eclient\\client\\Eclientconfig.json', 'r') as configpath:
        json_data = json.load(configpath)

        modulearr = {}
        for module in json_data['modules']:
            modulearr[str(module)] = str(json_data['modules'][module]['Enabled'])
        return modulearr

eel.start('EclientGUI.html')