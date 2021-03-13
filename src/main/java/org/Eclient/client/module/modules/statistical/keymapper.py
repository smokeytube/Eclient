#// /py src/main/java/org/Eclient/client/module/modules/statistical/keymapper.py

from mine import *;
import json;
import os;


class KeyMapper:
    @staticmethod
    def loadconfig() -> dict:
        with open(os.getenv('AppData')+'\\.minecraft\\mcpipy\\src\\main\\java\\org\\Eclient\\client\\Eclientconfig.json') as configpath:
            return json.load(configpath);

    def Main() -> None:
        modulenm: str = str(__class__.__name__);
        configs: dict = KeyMapper.loadconfig()['modules'][modulenm];
        sleeptime: int = configs['sleep'];
        outputtxt: str = configs['outputfile'];

        keymapperpath: str = (os.getenv('AppData')+'\\.minecraft\\mcpipy\\src\\main\\java\\org\\Eclient\\client\\module\\modules\\statistical\\data\\keymapper\\');
        os.system(keymapperpath+'keymapper.exe '+str(sleeptime)+' '+keymapperpath+outputtxt);


if __name__ == '__main__':
    KeyMapper.Main();