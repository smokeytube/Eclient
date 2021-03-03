# Eclient

![Eclient](media/branding/eclientTMofficial.png)

Use threading to run 2 modules at once
```python
from threading import Thread;
from phase import Phase as Phase;
from speed import Speed as Speed;

class twoModulesAtOnce:
    def Main():
        Thread(target = Phase.Main).start();
        Thread(target = Speed.Main).start();

if __name__ == '__main__':
    twoModulesAtOnce.Main();
```

For production we will most likely need a file with a similar structure of
```python
from module1 import module1 as module1;
from module2 import module2 as module2;
from module3 import module3 as module3;
from module4 import module4 as module4;
from module5 import module5 as module5;

import json;

class Main:
    def loadconfig():
        with open(os.getenv('AppData')+'\\.minecraft\\mcpipy\\src\\main\\java\\org\\Eclient\\client\\Eclientconfig.json') as configpath:
            return json.load(configpath);

    def Main():
        configs = Phase.loadconfig()['modules'];
        Yspeed = configs['phaseamount'];
        if configs['module1']['Enabled'] == True:
            Thread(target = Module1.Main).start();

        if configs['module2']['Enabled'] == True:
            Thread(target = Module2.Main).start();

        if configs['module3']['Enabled'] == True:
            Thread(target = Module3.Main).start();

        if configs['module4']['Enabled'] == True:
            Thread(target = Module4.Main).start();

        if configs['module5']['Enabled'] == True:
            Thread(target = Module5.Main).start();
```

All modules are required to have the command to run the module by itself, for example speed.py
will have
```
#// /py src/main/java/org/Eclient/client/module/modules/movement/speed
```
At the top of the file



Note: Scripts outside of the client that just display statistics (such as graph.py) will be written
like normal python and will not have any command in the headers.