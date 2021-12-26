import os
import webbrowser
import time

while True:
    file = input(">>> $ ")
    if file == "exit()":
        break
    elif file == "help()":
        print("""
exit - Exit
run() - Run a script with paths specified
delete() - Delete a script with paths specified
open() - Open any website with paths specified
run -sh - Run real shell commands
back -sh - Return to EviShell (Only in OuterShell mode) Use -f for force
              """)
    elif file == "run()":
        pathr = input("Specify paths ")
        print("Opened file")
        os.startfile(pathr)
    
    elif file == "delete()":
        pathd = input("Specify paths ")
        print("Deleted file")
        os.remove(pathd)
    
    elif file == "open()":
        url = input("Specify Url ")
        print("Opened Site")
        webbrowser.open(url)
    
    elif file == "run -sh":
        print("Exiting EviShell, Turning on Security, logging in, loading command line interface |\\/|")
        time.sleep(5)
        while not file == "back -sh -f" or not file == "back -sh":
            c = input("EviShell -r sub cli $ ")
            os.system(c)
            if c == "back -sh" or c == "back -sh -f":
                print("Exiting EviShell sub cli, turning off Security, logging out, loading EviShell")
                break
        

                    
        
    else:
        print(f"{file} is not recognized as an internal or external command, operable program or batch file.")