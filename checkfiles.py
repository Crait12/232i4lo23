import os.path 
from os import path

requirement_one = path.exists("node_modules")
requirement_two = path.exists("lky_root")
f1 = os.path.isfile('proxies.txt')
f2 = os.path.isfile('lky_root/ua.txt')
f3 = os.path.isfile('proxies.txt')
f4 = os.path.isfile('lky_root/rf.txt')
f5 = path.exists('lky_root/proxies')
f6 = os.path.isfile('lky_root/proxies/proxies.txt')
f7 = os.path.isfile('main.py')
f8 = os.path.isfile('destroy.py')
f9 = os.path.isfile('installer.py')
f10 = os.path.isfile('package.json')
f11 = os.path.isfile('z3ntl3_v1.js')
f12 = os.path.isfile('z3ntl3_v2.js')
f13 = os.path.isfile('lky_root/proxies/rf.txt')
f14 = os.path.isfile('lky_root/proxies/ua.txt')
correct = True
incorrect = False


def main():
    value = 0
    if requirement_one == correct:
        print("--> Node Modules Directory Found! \033[32m[Correct]\033[0m")
    else:
        print("--> Node Modules Directory NOT Found! \033[31m[INCORRECT]\033[0m")
    if requirement_two == correct:
        print("--> Lowkey Directores Found! \033[32m[Correct]\033[0m")
    else:
        
        print("--> Lowkey Directories NOT Found! \033[31m[INCORRECT]\033[0m")
    if f1 == correct:
        value = value + 1
        print(f"--> Lowkey Files Check {value} \033[32m[Correct]\033[0m")
    else:
        value = value + 1
        print(f"--> Lowkey Files Check {value} NOT Found! \033[31m[INCORRECT]\033[0m")
    if f2 == correct:
        value = value + 1
        print(f"--> Lowkey Files Check {value} \033[32m[Correct]\033[0m")
    else:
        value = value + 1
        print(f"--> Lowkey Files Check {value} NOT Found! \033[31m[INCORRECT]\033[0m")
    if f3 == correct:
        value = value + 1
        print(f"--> Lowkey Files Check {value} \033[32m[Correct]\033[0m")
    else:
        value = value + 1
        print(f"--> Lowkey Files Check {value} NOT Found! \033[31m[INCORRECT]\033[0m")
    if f4 == correct:
        value = value + 1
        print(f"--> Lowkey Files Check {value} \033[32m[Correct]\033[0m")
    else:
        value = value + 1
        print(f"--> Lowkey Files Check {value} NOT Found! \033[31m[INCORRECT]\033[0m")
    if f5 == correct:
        value = value + 1
        print(f"--> Lowkey Files Check {value} \033[32m[Correct]\033[0m")
    else:
        value = value + 1
        print(f"--> Lowkey Files Check {value} NOT Found! \033[31m[INCORRECT]\033[0m")
    if f6 == correct:
        value = value + 1
        print(f"--> Lowkey Files Check {value} \033[32m[Correct]\033[0m")
    else:
        value = value + 1
        print(f"--> Lowkey Files Check {value} NOT Found! \033[31m[INCORRECT]\033[0m")
    if f7 == correct:
        value = value + 1
        print(f"--> Lowkey Files Check {value} \033[32m[Correct]\033[0m")
    else:
        value = value + 1
        print(f"--> Lowkey Files Check {value} NOT Found! \033[31m[INCORRECT]\033[0m")
    if f8 == correct:
        value = value + 1
        print(f"--> Lowkey Files Check {value} \033[32m[Correct]\033[0m")
    else:
        value = value + 1
        print(f"--> Lowkey Files Check {value} NOT Found! \033[31m[INCORRECT]\033[0m")
    if f9 == correct:
        value = value + 1
        print(f"--> Lowkey Files Check {value} \033[32m[Correct]\033[0m")
    else:
        value = value + 1
        print(f"--> Lowkey Files Check {value} NOT Found! \033[31m[INCORRECT]\033[0m")
    if f10 == correct:
        value = value + 1
        print(f"--> Lowkey Files Check {value} \033[32m[Correct]\033[0m")
    else:
        value = value + 1
        print(f"--> Lowkey Files Check {value} NOT Found! \033[31m[INCORRECT]\033[0m")
    if f11 == correct:
        value = value + 1
        print(f"--> Lowkey Files Check {value} \033[32m[Correct]\033[0m")
    else:
        value = value + 1
        print(f"--> Lowkey Files Check {value} NOT Found! \033[31m[INCORRECT]\033[0m")
    if f12 == correct:
        value = value + 1
        print(f"--> Lowkey Files Check {value} \033[32m[Correct]\033[0m")
    else:
        value = value + 1
        print(f"--> Lowkey Files Check {value} NOT Found! \033[31m[INCORRECT]\033[0m")
    if f13 == correct:
        value = value + 1
        print(f"--> Lowkey Files Check {value} \033[32m[Correct]\033[0m")
    else:
        value = value + 1
        print(f"--> Lowkey Files Check {value} NOT Found! \033[31m[INCORRECT]\033[0m")
    if f14 == correct:
        value = value + 1
        print(f"--> Lowkey Files Check {value} \033[32m[Correct]\033[0m")
    else:
        value = value + 1
        print(f"--> Lowkey Files Check {value} NOT Found! \033[31m[INCORRECT]\033[0m")

if __name__ == "__main__":
    main()
