from urllib import request
import pickle
import os
print("")
website = ()
command = ()
x = ()
filename = ()
leer = ()
def help ():
    print ("this is websitebongo")
    print ("the following commands are used as listed")
    print ("dtf (this command stand for downloading files of the giging websites to an generated file)")
    print ("help (the standart command for seeing what commands are possible to use)")
    exit
def dtf (filename):#downloadtofile
    if filename != leer
         website = input()
        print (website)
        x = request.urlopen(website)
        print(type(x))
        print(dir(x))
        data = x.read()
        os.mkdir(filename)
        with open(filename, "wb") as filename:
        pickle.dump(data, filename)
        exit
    else
        website = input()
        print (website)
        x = request.urlopen(website)
        print(type(x))
        print(dir(x))
        data = x.read()  
        with open("dumpfile.txt", "wb") as dumpfile:
        pickle.dump(data, dumpfile)
        exit
while True :               #main loop wich is just asking fo an comman and can be exitted vie ctrl c
    command = input()
    if command == "--help" :
        help()
    elif command == "dtf":
				dtf() 
    else:
      print(command, "is not an accseptabele command")
        help()
