import sys
import time
import subprocess
from unicodedata import name


## ADD SOME TRY/CATCH MECHANISM FOR DIFFERENT ETHERNET NAMES ##
## MIGHT HAVE TO FIND A TRY/CATCH EQUIVALENT FOR POWERSHELL SCRIPTS ##


def main():

    def initiate():
        # SUBPROCESS TO REFRESH NETWORK USING SUBPROCESS MODULE
        # PARAMETERS: subprocess.Popen(["terminal application", "script file location", "stdout=sys.stdout using standard system output"])
        p = subprocess.Popen(["powershell.exe", 
            "C:\\Users\\Wes\\Desktop\\PowerShell_Script\\kill_net.ps1"], 
            stdout=sys.stdout)
        p.communicate()
        print("Ethernet disabled :(")
        # ARBITRARY WAIT TO MAKE SURE NETWORK IS DEAD
        time.sleep(3)

        # SUBPROCESS TO REFRESH NETWORK USING SUBPROCESS MODULE
        # PARAMETERS: subprocess.Popen(["terminal application", "script file location", "stdout=sys.stdout using standard system output"])
        q = subprocess.Popen(["powershell.exe", 
            "C:\\Users\\Wes\\Desktop\\PowerShell_Script\\restore_net.ps1"], 
            stdout=sys.stdout)
        q.communicate()
        print("Ethernet restored :)")
        # WAIT TO MAKE SURE NETWORK IS RESTORED

    initiate()

if __name__ == "__main__":
    main()
