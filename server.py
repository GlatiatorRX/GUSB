from time import sleep
from PodSixNet.Server import Server
from channel import ClientChannel


class MyServer(Server):

    channelClass = ClientChannel

    def Connected(self, channel, addr):
        print('new connection:', channel)


myserver = MyServer()
while True:
    myserver.Pump()
    sleep(0.0001)
