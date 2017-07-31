import os
import sys

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path)

from modules.main import main

if __name__ == "__main__":
    main()