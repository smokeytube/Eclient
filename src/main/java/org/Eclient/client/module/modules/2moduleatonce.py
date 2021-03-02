from threading import Thread;
from phase import Phase as Phase;
from speed import Speed as Speed;

class twoModulesAtOnce:
    def Main():
        Thread(target = Phase.Main).start();
        Thread(target = Speed.Main).start();

if __name__ == '__main__':
    twoModulesAtOnce.Main();