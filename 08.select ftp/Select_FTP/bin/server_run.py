import os
import sys


path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(path)

from foo.server_class import Server

if __name__ == "__main__":
    s = Server()
    s.server_connect()