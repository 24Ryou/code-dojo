import sys
sys.path.append("src")
from utils import *

def main():
    print("What to do?")
    print("0 - Load")
    print("1 - Save")
    print("2 - Setup")

    _ = input(("Enter number: "))

    if _ == "0" :
        load()
    elif _ == "1":
        save()
    else:
        setup()


if __name__ == "__main__":
    main()