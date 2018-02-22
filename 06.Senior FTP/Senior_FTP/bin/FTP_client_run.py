import os
import sys

path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(path)

from foo.main_class import Main


if __name__ == "__main__":
    m = Main()
    m.main()