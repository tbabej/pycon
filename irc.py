import socket
import sys

# No need to change this
SERVER = 'cameron.freenode.net'
CHANNEL = '#pyconczcrypto'
PORT = 6667

# Please change this!
NICK = 'randomnick123'

class Client(object):
    def __init__(self, server, port, nick):
        self.server = server
        self.nick = nick
        self.port = port

        self.connection = socket.socket()
        self.connection.connect((server, port))
        self.send('NICK {0}\n'.format(nick))
        self.send('USER {0} 0 * :{1}\n'.format(nick, nick))
        self.send('JOIN #pyconczcrypto\n')

    def send(self, line):
        sys.stdout.write("Send: {0}".format(line))
        self.connection.send(line)

    def pong(self, line):
        self.send(line.replace("PING", "PONG"))

    def received_message(self, line):
        pass

    def main(self):
        while True:
            line = self.connection.recv(500)
            sys.stdout.write("Recv: {0}".format(line))

            if line.startswith("PING"):
                self.pong(line)
            elif "PRIVMSG" in line:
                self.received_message(line)

client = Client(SERVER, PORT, NICK)
client.main()
