# **Monitor Mode Tool**



A small Python script that automates checking a wireless interface and switching it between managed and monitor mode on Linux, in the terminal





### ***Features***



1. ###### Check interface status (name, MAC address, type, ESSID, access point)
2. ###### Enable monitor mode with airmon-ng
3. ###### Disable monitor mode with one of three methods (aircrack-ng, iwconfig, or iw)
4. ###### Confirms the result after enabling or disabling, and shows the real interface name
5. ###### Reports errors instead of silently failing



### ***Requirements***



* ###### Linux
* ###### Python 3 (standard library only, no pip install needed)
* ###### iw
* ###### aircrack-ng (provides airmon-ng)
* ###### NetworkManager (systemctl)
* ###### Optional: net-tools (ifconfig) and wireless-tools (iwconfig), only needed for option 2 when disabling monitor mode and for the access point line in the status check





### ***To install the tools on Debian/Ubuntu/Kali:***



###### &#x20; sudo apt install iw aircrack-ng net-tools wireless-tools





### ***Usage***



###### &#x20; git clone https://github.com/ArhaanPatolia/monitor-mode-manager.git

###### &#x20; cd monitor-mode-manager

###### &#x20; python3 monitor\_mode\_tool.py







### ***Important Notes***





* ###### Enabling monitor mode will disconnect you from Wi-Fi. It runs airmon-ng check kill, which stops NetworkManager and wpa\_supplicant. Disabling monitor mode restarts NetworkManager to restore your connection.



* ###### Some versions of airmon-ng rename the interface (for example wlan0 becomes wlan0mon), so use the name shown in the confirmation message when disabling.





### ***Known Limitations***



1. ###### Tested on: Kali Linux, using a coconut wifi adapter (WA02).
2. ###### The status check shows information for a single interface; with several adapters the details may be mixed and unreliable.
3. ###### iwconfig and ifconfig are deprecated and missing on many modern distributions, so option number 2 may fail when disabling monitor mode (option 3 is the reliable one).





### ***Menu***



|**1**|**Check Interface Status**|
|-|-|
|**2**|**Enable Monitor Mode**|
|**3**|**Disable Monitor Mode**|
|**4**|**Exit The Program**|







### ***Responsible Use***



###### Only use this tool on devices and networks you own or have explicit permission to test. You are responsible for following the laws and rules that apply where you are.





### ***License***



###### Distributed under the MIT License. See LICENSE for details.



### ***Author***



###### Arhaan Patolia

