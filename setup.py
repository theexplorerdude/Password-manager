import os
import getpass
os.system("figlet SPM")
os.system("touch config.spm")
os.system("touch simplepasswordmanager.db")
print("Please enter your master password")
masterpass = getpass.getpass()
masterhash = hash(masterpass)
p = abs(masterhash)
f = open("config.spm", "w")
string = str(p)
f.write(string)
print(string)
input("Now run the program with [Python app.py], Prees any key to exit...")
