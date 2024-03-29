# /py src/module/misc/privateserverfinder

import threading
from queue import Queue
from mine import *
import winsound
import os
from src.module.misc.mcstatus.server import MinecraftServer

def Main():
    ipblocks = open((os.getcwd()+"\\src\\module\\misc\\"+"minecraftipblocks.txt"))
    for halfip in ipblocks:
        halfip = halfip.strip('\n')
        iptxtfle = (os.getcwd()+"\\src\\module\\misc\\ips\\"+"{0}0-{1}255.txt".format(halfip, halfip))
        for exxx in range(0, 256):
            ip = "{0}{1}".format(halfip, exxx)

            def scan_ip_and_port(ekis):
                try:
                    server = MinecraftServer.lookup("{0}:{1}".format(ip, ekis))
                    status = server.status()
                    latency = server.ping()
                    with open(iptxtfle, "a+") as ips:
                        ips.write("{0}:{1}\n".format(ip, ekis))
                    ips.close()
                    if status.players.online > 0:
                        with open("ONLINE.txt", "a+") as onlind:
                            onlind.write("{0}:{1}\n".format(ip, ekis))
                    print([status.players.online, status.latency, latency])
                    return [status.players.online, status.latency, latency]
                except:
                    return []

            queue = Queue()
            open_ports = []

            def fill_queue(port_list):
                for port in port_list:
                    queue.put(port)

            def worker():
                while not queue.empty():
                    port = queue.get()
                    if scan_ip_and_port(port):
                        open_ports.append(port)

            port_list = range(25500, 25600)
            fill_queue(port_list)

            thread_list = []

            for t in range(100):
                thread = threading.Thread(target=worker)
                thread_list.append(thread)

            for thread in thread_list:
                thread.start()

            for thread in thread_list:
                thread.join()

        winsound.Beep(440, 250)
        winsound.Beep(550, 250)
        winsound.Beep(660, 250)
        winsound.Beep(880, 500)


if __name__ == '__main__':
    Main()