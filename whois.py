#1/usr/bin/python2
import os
import sys
os.system("clear")
os.system("apt install figlet -y")


print("\033[93m ")
os.system ("figlet script written BY Rohit")
print("special thanks to Awesome Tech")



url = raw_input("[+]enter website (without subdomain and http): ")
os.system("whois %s" % (url))
