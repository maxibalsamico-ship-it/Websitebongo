from urllib import request
import pickle
from colorama import Fore
print(Fore.Red + r"""
              /@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\
             /@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\
            /@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\
           /@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\
	""")
website = ()
print(Fore.Red + r"""
           /@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\
          /@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\
         /@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\
        /@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\
       """)
print(Fore.Red + r"""
       |@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  @  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@|
       |@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ @@@@# @@@@@@@@@@@@@@@@@@@@@@@@@@@|
       |@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   @@@@@@@    @@@@@@@@@@@@@@@@@@@@@@@|
       """)
command = ()
print(Fore.Red + r"""
       |@@@@@@@@@@@@@@@@@@@@@@@@@@@@   #@@@@@@@@@@@@@@@@  +@@@@@@@@@@@@@@@@@@@|
       |@@@@@@@@@@@@@@@@@@@@@@@    @@@@@@@@@@@@@@@@@@@@@@@@. =@@@@@@@@@@@@@@@@|
       |@@@@@@@@@@@@@@@@@@@   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  @@@@@@+=@@@@@@|
       """)
x = ()
print(Fore.Red + r"""
       |@@@@@  @@@@+  +@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  @@%@**@@ @@|
       |@@@@@: @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#@@@@#@**@ @@|
       |@@@@@@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   =@@@@@@@@@@@+++@@@ @@|
       """)
filename = ()
print(Fore.Red + r"""
       |@@@@@@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   =@@@@@@@@@@@+++@@@ @@|
       |@@@@@@% @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   /@@@*@@@@@@@@@@@@@@@@@@@ @@|
       |@@@@@@@ @@@@@@@@*      -@@@@@@@@@@@@    /@@@@@@@@@@@@@@@@@@@@@@@@@@  @|
       """)
leer = ()
print(Fore.Red + r"""
       |@@@@@@@ .@@@@@@  @@@**@: @.  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%      .@@@|
       |@@@@@@@ :@@@@@ @@#@@@@@ @  @@@@@@@@@@@@@@@@@@@@@@%        .@@@@@@@@@@@|
       |@@@@@@ *@@@@@@@@@@++%#@@ @@@@@@@@@@@@@@@@@@@      -@@@@@@@@@@@@@@@@@@@|
       """)
def help ():
    print ("this is websitebongo")
    print ("the following commands are used as listed")
    print ("dtf (this command stand for downloading files of the giging websites to an generated file)")
    print ("help (the standart command for seeing what commands are possible to use)")
    exit
print(Fore.Red + r"""
       |@@@@@ +@@@@@@@@@@@#%@@@@ @@@@@@@@@@%       @@@@@@@@@@@@@@@@@@@@@@@@@@@|
       |@@@@  @@@@@@@@@@@@@@@@@@ @@@=      @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@|
       """)
def owndtf ():#downloadtofile
    filename = input()
    website = input()
    print (website)
    x = request.urlopen(website)
    print(type(x))
    print(dir(x))
    data = x.read()
    with open(filename, "wb") as filename:
        pickle.dump(data, filename)
    exit
print(Fore.Red + r"""
           \@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/
            \@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/
             \@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/
       """)
def dtf ():
        print ("website url")
        website = input()
        print (website)
        x = request.urlopen(website)
        print(type(x))
        print(dir(x))
        data = x.read()  
        with open("dumpfile.txt", "wb") as dumpfile:
            pickle.dump(data, dumpfile)
        exit
print(Fore.Red + r"""
               -----------------------------------------------------------""")
while True :               #main loop wich is just asking fo an comman and can be exitted vie ctrl c
    command = input()
    if command == "--help" :
        help()
    elif command == "dtf":
	    dtf() 
    elif command == "own dtf" :
        owndtf()
    else:
        print(command, "is not an accseptabele command")
        help()

