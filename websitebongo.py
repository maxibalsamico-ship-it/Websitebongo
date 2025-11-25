from urllib import request
import pickle
print("")
website = ()
command = ()
x = ()
def help():
    print ("this is websitebongo")
    print ("the following commands are used as listed")
    print ("dtf (this command stand for downloading files of the giging websites to an generated file)")
    print ("help (the standart command for seeing what commands are possible to use)")
    exit
def dtf ():#downloadtofile
    exit
  
while True :               #main loop wich is just asking fo an comman and can be exitted vie ctrl c
    command = input()
    if command == "--help" :
        help()
    elif command == "dtf":
        website = input()
        x = request.urlopen(website)
        print(type(x))
        print(dir(x))
        data = x.read()  
        with open("dumpfile.txt", "wb") as dumpfile:
            pickle.dump(data, dumpfile)
    else:
        help()
