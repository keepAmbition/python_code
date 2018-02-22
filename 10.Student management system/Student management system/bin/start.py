import sys
import os

path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(path)

from module.main import Main


if __name__ == "__main__":
    m = Main()
    m.main()