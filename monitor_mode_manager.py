# Monitor Mode Tool
# Copyright (c) 2026 Arhaan Patolia


# The Libraries Used For The Program
import subprocess
import time
import sys

def run(cmd):
    # Run a command and return True on success, False on failure.
    # Prints a message instead of crashing if the program is missing.
    try:
        r = subprocess.run(cmd, capture_output=True, text=True)
    except FileNotFoundError:
        print(f"Not Installed: {cmd[0] if cmd[0] != 'sudo' else cmd[1]}")
        return False
    if r.returncode != 0:
        print(f"Failed To Run The Command!\n")
        print("----------------------------------------------------------------------\n")
        print("\nEnter Another Task To Do!\n")
        return False
    return True

def check():
    # Using 'iw dev' and 'iwconfig' To Get The Necessary Information About The Interface
    subprocess.run(["clear"])
    print("Interface Status:")
    time.sleep(0.2)

    #This Is To Prevent The Program From Crashing
    try:
        iw_dev_out = subprocess.run(['iw', 'dev'], capture_output=True, text=True)  # Capture the output instead of printing it
    except FileNotFoundError:
        print("Not Installed: iw")
        return
    time.sleep(1)

    #Declaring The Variable To Store The Information
    interface = "N/A"
    mac = "N/A"
    essid = "N/A"
    itype = "N/A"
    ap = "N/A"

    #Parsing The Output From 'iw dev' And Then Storing Them In The Variables Above
    for line in iw_dev_out.stdout.splitlines():
        line = line.strip()
        if line.startswith('Interface'):
            interface = line.split()[1].strip()
        elif line.startswith('addr'):
            mac = line.split()[1].strip()
        elif line.startswith('ssid'):
            essid = line.split(None, 1)[1].strip()
        elif line.startswith("type"):
            itype = line.split()[1]

    #Verifying Whether There Is An Interface Available Before Running 'iwconfig', To Get Other Information
    if interface != "N/A":
        try:
            iwconfig_out = subprocess.run(['iwconfig', interface],
                                          capture_output=True, text=True).stdout
            for line in iwconfig_out.splitlines():
                if 'Access Point:' in line:              # The Access Point The Interface Is Connected To
                    ap = line.split('Access Point:', 1)[1].strip()
        except FileNotFoundError:
            pass

    # Output The Information After Parsing
    print(f"""
    Interface     : {interface}
    MAC Address   : {mac}
    Type          : {itype}
    ESSID         : {essid}
    Access Point  : {ap}
    """)
    # The Footer
    print("----------------------------------------------------------------------\n")
    print("\nEnter Another Task To Do!\n")

def enable_monitor_mode():
    # Enable Monitor Mode On The Chosen Interface Using Airmon-ng
    subprocess.run(["clear"])
    interface = input("Enter Interface (e.g. wlan0): ").strip()    # Entering The Interface

    # Ask for the interface name and repeat until it isn't empty
    while True:
        if interface == "":
            print("Please Enter A Valid Interface!")
            interface = input("Enter Interface (e.g. wlan0): ").strip()
        else:
            break
    print("\nKilling Processes...")
    if not run(["sudo", "airmon-ng", "check", "kill"]):   # NetworkManager And wpa_supplicant Would Switch The Interface
        return                                            #  Back To Managed Mode, So Stop Them First
    time.sleep(0.8)
    print("\nEnabling Monitor Mode...\n")
    if not run(["sudo", "airmon-ng", "start", interface]):  # Enabling Monitor Mode
        return
    time.sleep(0.6)

    # Airmon-ng May Rename The Interface (e.g. wlan0 --> wlan0mon), So Read The Real Name From 'iw dev'
    iw_out = subprocess.run(['iw', 'dev'], capture_output=True, text=True)
    current_interface = "N/A"
    monitor_interface = None
    for line in iw_out.stdout.splitlines():   # Parsing From The Output Of The 'iw dev' Command
        line = line.strip()
        if line.startswith('Interface'):                                # Getting The Interface And Storing It
            current_interface = line.split()[1]
        elif line.startswith('type') and line.split()[1] == 'monitor':  # Checking Whether Monitor Mode Is Enabled
            monitor_interface = current_interface

    # Output Of The Verification And New Interface Name
    if monitor_interface:
        print(f"\nMonitor Mode Is Now Enabled!\nInterface: {monitor_interface}\n")
    else:
        print("\nCould Not Confirm Monitor Mode. Check Option 1 For Details.\n")
    # Footer
    print("----------------------------------------------------------------------\n")
    print("\nEnter Another Task To Do!\n")

def disable_monitor_mode():
    # This Function Is To Disable Monitor Mode Using 3 Programs/Suites
    subprocess.run(["clear"])
    print("To Disable Monitor Mode\n")
    print("Here Is A List Of The Commands/Suites To Use, First Enter\nYour Interface Before Choosing.\n")
    print("""
            1. Using Aircrack-ng Suite
            2. Using iwconfig            # Most Effective
            3. Using iw dev              # Most Effective""")
    print()
    print()
    # Ask for the interface name and repeat until it isn't empty
    interface = input("Enter Interface (e.g. wlan0mon): ").strip()
    while True:
        if interface == "":
            print("Please Enter A Valid Interface!")
            interface = input("Enter Interface (e.g. wlan0mon): ").strip()
        else:
            break
    # Validating The Input For The Options
    choice = input("Enter Your Choice (1, 2 or 3): ").strip()
    while True:
        if choice == "1":
            subprocess.run(["clear"])                     # Option 1 Uses The Aircrack-ng Suite To Disable Monitor Mode
            print("\nRunning Aircrack-ng Suite...\n")
            if not run(["sudo", "airmon-ng", "stop", interface]):
                return
            time.sleep(2)
            # "check kill" Stopped NetworkManager, So Restart It To Bring Wi-Fi Back
            print("\nRestarting Network Manager... (This May Take A Few Seconds)\n")
            run(["sudo", "systemctl", "restart", "NetworkManager"])
            time.sleep(2)
            break
        elif choice == "2":                           # Option 2 Uses The 'ifconfig' and 'iwconfig' Commands To Disable Monitor Mode
            subprocess.run(["clear"])
            print("\nRunning iwconfig...\n")
            if not run(["sudo", "ifconfig", interface, "down"]):
                return
            time.sleep(0.4)
            if not run(["sudo", "iwconfig", interface, "mode", "managed"]):
                return
            time.sleep(0.4)
            if not run(["sudo", "ifconfig", interface, "up"]):
                return
            time.sleep(0.4)
            # "check kill" Stopped NetworkManager, So Restart It To Bring Wi-Fi Back
            print("\nRestarting Network Manager... (This May Take A Few Seconds)\n")
            run(["sudo", "systemctl", "restart", "NetworkManager"])
            time.sleep(2)
            break
        elif choice == "3":
            subprocess.run(["clear"])             # Option 3 Uses The 'iw dev' and 'ip link' Commands To Disable Monitor Mode
            print("\nRunning iw dev...\n")
            if not run(["sudo", "ip", "link", "set", interface, "down"]):
                return
            time.sleep(0.4)
            if not run(["sudo", "iw", "dev", interface, "set", "type", "managed"]):
                return
            time.sleep(0.4)
            if not run(["sudo", "ip", "link", "set", interface, "up"]):
                return
            time.sleep(0.4)
            # "check kill" Stopped NetworkManager, So Restart It To Bring Wi-Fi Back
            print("\nRestarting Network Manager... (This May Take A Few Seconds)\n")
            run(["sudo", "systemctl", "restart", "NetworkManager"])
            time.sleep(2)
            break
        else:
            print("Invalid Choice!")              # The Validation Process In Case Of A Wrong Input
            print("Choice Must Be 1, 2, or 3!")
            print("Try Again!")
            choice = input("Enter Your Choice (1, 2 or 3): ").strip()

    iw_out = subprocess.run(['iw', 'dev'], capture_output=True, text=True)
    current_interface = "N/A"         # Declaring Variable Which Will Store The Necessary Information
    managed_interface = None
    for line in iw_out.stdout.splitlines():      # Parsing The Output From 'iw dev' Command To Get Information
        line = line.strip()                      # After Disabling Monitor Mode
        if line.startswith('Interface'):
            current_interface = line.split()[1]       # Assigning The Collected Information Into The Variables
        elif line.startswith('type') and line.split()[1] == 'managed':
            managed_interface = current_interface

    # Output The Information After Parsing
    if managed_interface:
        print(f"\nMonitor Mode Is Now Disabled!\nInterface: {managed_interface}\n")
    else:
        print("\nCould Not Confirm Managed Mode. Check Option 1 For Details.\n")
    print("----------------------------------------------------------------------\n")
    print("\nEnter Another Task To Do!\n")

def shut_down():
    # This Function Is To Exit The Program
    print("\n----------------------------------------------------------------------\n")
    print("Exiting...")
    time.sleep(1)
    subprocess.run(["clear"])
    sys.exit()


def main():
    # This Is The Main Part
    subprocess.run(["clear"])
    print()
    print("----------------------------------------------------------------------")
    print("| This Program Will Automate Checking The Interface And", " " * 12, "|\n| Enable/Disable Monitor Mode", " " * 38, "|")
    print("----------------------------------------------------------------------")
    print("| BY: Arhaan Patolia |\n----------------------")

    while True:
        # The Tasks The User May Want To Run
        print("\n\n1. Check Interface Status")
        print("2. Enable Monitor Mode")
        print("3. Disable Monitor Mode")
        print("4. Exit The Program")
        print()

        usr_input = input("Enter Your Choice: ").strip()
        print()
        # Validating The User Input
        while True:
            if usr_input == "1":                          # Option 1 Checks For The Interface Status
                print("\nChecking Interface Status...")
                time.sleep(0.3)
                check()
                break
            elif usr_input == "2":
                print("\nEnabling Monitor Mode...\n")     # Option 2 Enables Monitor Mode Of The Interface
                time.sleep(0.1)
                print("This Will Disconnect You From Wi-Fi\n")
                time.sleep(2)
                enable_monitor_mode()
                break
            elif usr_input == "3":
                print("\nThis Will Also Reset Your Network Manager\n")     # Option 3 Disables Monitor Mode
                time.sleep(0.1)
                print("Executing Monitor Mode  -->  Managed Mode...")
                time.sleep(2)
                disable_monitor_mode()
                break
            elif usr_input == "4":      # Option 4 Exits The Program
                print()
                time.sleep(0.2)
                shut_down()
            else:
                print("Invalid Input!")      # This Is To Validate The User's Choice
                print("Choice Must Be 1, 2, 3 or 4!")
                print("Try Again!")
                usr_input = input("Enter Your Choice: ").strip()

if __name__ == "__main__":
   main()