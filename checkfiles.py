import os.path 
from os import path

requirement_one = path.exists("node_modules")
requirement_two = path.exists("lky_root")

correct = True
incorrect = False

def main():
    if requirement_one == correct:
        print("--> Node Modules Directory Found! [Correct]")
    else:
        print("--> Node Modules Directory NOT Found! [INCORRECT]")
    if requirement_two == correct:
        print("--> Lowkey Directores Found! [Correct]")
    else:
        print("--> Lowkey Directories NOT Found! [INCORRECT]")


if __name__ == "__main__":
    main()
