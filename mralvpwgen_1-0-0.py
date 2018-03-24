# -*- coding: utf-8 -*-
# MrALvar0 Password Generator
# using social-engineering
print """
• ▌ ▄ ·. ▄▄▄       ▄▄▄· ▄▄▌  ▌ ▐· ▄▄▄· ▄▄▄             ▄▄▄·▄▄▌ ▐ ▄▌·▄▄▄▄       ▄▄ • ▄▄▄ . ▐ ▄ ▄▄▄ .▄▄▄   ▄▄▄·▄▄▄▄▄      ▄▄▄  
·██ ▐███▪▀▄ █·    ▐█ ▀█ ██• ▪█·█▌▐█ ▀█ ▀▄ █·▪         ▐█ ▄███· █▌▐███▪ ██     ▐█ ▀ ▪▀▄.▀·•█▌▐█▀▄.▀·▀▄ █·▐█ ▀█•██  ▪     ▀▄ █·
▐█ ▌▐▌▐█·▐▀▀▄     ▄█▀▀█ ██▪ ▐█▐█•▄█▀▀█ ▐▀▀▄  ▄█▀▄      ██▀·██▪▐█▐▐▌▐█· ▐█▌    ▄█ ▀█▄▐▀▀▪▄▐█▐▐▌▐▀▀▪▄▐▀▀▄ ▄█▀▀█ ▐█.▪ ▄█▀▄ ▐▀▀▄ 
██ ██▌▐█▌▐█•█▌    ▐█ ▪▐▌▐█▌▐▌███ ▐█ ▪▐▌▐█•█▌▐█▌.▐▌    ▐█▪·•▐█▌██▐█▌██. ██     ▐█▄▪▐█▐█▄▄▌██▐█▌▐█▄▄▌▐█•█▌▐█ ▪▐▌▐█▌·▐█▌.▐▌▐█•█▌
▀▀  █▪▀▀▀.▀  ▀     ▀  ▀ .▀▀▀. ▀   ▀  ▀ .▀  ▀ ▀█▄▀▪    .▀    ▀▀▀▀ ▀▪▀▀▀▀▀•     ·▀▀▀▀  ▀▀▀ ▀▀ █▪ ▀▀▀ .▀  ▀ ▀  ▀ ▀▀▀  ▀█▄▀▪.▀  ▀

COPYRIGHT Álvaro González - All rights reserved
VERSION 1.0.0

"""
start = raw_input("Welcome, I need you to give me some information about your victim, please use ALWAYS lower-case. Are you ready?: ")
name = raw_input("Name (JUST name): ")
#sname = raw_input("Surnames WITHOUT SPACES, leave blank if none: ")
nick = raw_input("Nickname: ")
dob = raw_input("Date of birth FORMAT: DD-MM-YYYY (WITHOUT -'s , add 0's if neccesary: ")
poc = raw_input("Place of childhood (Without spaces): ")
#fcolor = raw_input("Favourite color: ")
#ffood = raw_input("Favourite food: ")

print "Success! Copy your Passwords"
#DOB AND POC
print str(dob) + str(poc).title()
print str(dob) + str(poc).upper()
print str(dob) + str(poc)
print str(dob).upper() + str(poc)
print str(poc).title() + str(dob)
print str(poc).upper() + str(dob)
print str(poc) + str(dob)
print str(dob)[0] + str(dob)[1] + str(dob)[2] + str(dob)[3] + str (poc)
print str(dob)[0] + str(dob)[1] + str(dob)[2] + str(dob)[3] + str (poc).upper()
print str(dob)[0] + str(dob)[1] + str(dob)[2] + str(dob)[3] + str (poc).title()
print str(poc) + str(dob)[0] + str(dob)[1] + str(dob)[2] + str(dob)[3]
print str(poc).upper() + str(dob)[0] + str(dob)[1] + str(dob)[2] + str(dob)[3]
print str(poc).title() + str(dob)[0] + str(dob)[1] + str(dob)[2] + str(dob)[3]
print str(dob)[0] + str(dob)[1] + str(dob)[2] + str(dob)[3] + str (poc) + str(dob)[4] + str(dob)[5] + str(dob)[6] + str(dob)[7]
print str(dob)[0] + str(dob)[1] + str(dob)[2] + str(dob)[3] + str (poc).upper() + str(dob)[4] + str(dob)[5] + str(dob)[6] + str(dob)[7]
print str(dob)[0] + str(dob)[1] + str(dob)[2] + str(dob)[3] + str (poc).title() + str(dob)[4] + str(dob)[5] + str(dob)[6] + str(dob)[7]
#DOB AND NAME
print str(dob) + str(name)
print str(dob) + str(name).upper()
print str(dob) + str(name).title()
print str(name) + str(dob)
print str(name).upper() + str(dob)
print str(name).title() + str(dob)
print str(name) + str(dob)[0] + str(dob)[1] + str(dob)[2] + str(dob)[3]
print str(name).upper() + str(dob)[0] + str(dob)[1] + str(dob)[2] + str(dob)[3]
print str(name).title() + str(dob)[0] + str(dob)[1] + str(dob)[2] + str(dob)[3]
print str(dob)[0] + str(dob)[1] + str(dob)[2] + str(dob)[3] + str (name) + str(dob)[4] + str(dob)[5] + str(dob)[6] + str(dob)[7]
print str(dob)[0] + str(dob)[1] + str(dob)[2] + str(dob)[3] + str (name).upper() + str(dob)[4] + str(dob)[5] + str(dob)[6] + str(dob)[7]
print str(dob)[0] + str(dob)[1] + str(dob)[2] + str(dob)[3] + str (name).title() + str(dob)[4] + str(dob)[5] + str(dob)[6] + str(dob)[7]
print str(poc) + str(name)
print str(poc).upper() + str(name).upper()
print str(poc).upper() + str(name)
print str(poc) + str(name).upper()
print str(poc) + str(name).title()
print str(name) + str(poc)
print str(name).upper() + str(poc)
print str(name) + str(poc).upper()
print str(name).upper() + str(poc).upper()
print str(name).title() + str(poc)
#DOB AND NICK
print str(dob) + str(nick)
print str(dob).upper() + str(nick)
print str(dob) + str(nick).upper()
print str(dob).upper() + str(nick).upper()
print str(nick) + str(dob)
print str(nick).upper() + str(dob)
print str(nick) + str(dob).upper()
print str(nick).upper() + str(dob).upper()
print str(nick) + str(dob)[0] + str(dob)[1] + str(dob)[2] + str(dob)[3]
print str(nick).title() + str(dob)[0] + str(dob)[1] + str(dob)[2] + str(dob)[3]
print str(nick).upper() + str(dob)[0] + str(dob)[1] + str(dob)[2] + str(dob)[3]
print str(dob)[0] + str(dob)[1] + str(dob)[2] + str(dob)[3] + str (nick) + str(dob)[4] + str(dob)[5] + str(dob)[6] + str(dob)[7]
print str(dob)[0] + str(dob)[1] + str(dob)[2] + str(dob)[3] + str (nick).title() + str(dob)[4] + str(dob)[5] + str(dob)[6] + str(dob)[7]
print str(dob)[0] + str(dob)[1] + str(dob)[2] + str(dob)[3] + str (nick).upper() + str(dob)[4] + str(dob)[5] + str(dob)[6] + str(dob)[7]
print str(poc) + str(nick)
print str(poc).upper() + str(nick)
print str(poc) + str(nick).upper()
print str(poc).upper() + str(nick).upper()
print str(nick) + str(poc)
print str(nick).upper() + str(poc)
print str(nick) + str(poc).upper()
print str(nick).upper() + str(poc).upper()
#MIX OF DOB, POC, NAME AND NICK
#WITHOUT NAME
print str(dob) + str(nick) + str(poc)
print str(dob) + str(nick).upper() + str(poc)
print str(dob) + str(nick) + str(poc).upper()
print str(dob) + str(nick).upper() + str(poc).upper()
print str(dob) + str(poc) + str(nick)
print str(dob) + str(poc).upper() + str(nick)
print str(dob) + str(poc) + str(nick).upper()
print str(dob) + str(poc).upper() + str(nick).upper()
print str(poc) + str(nick) + str(dob)
print str(poc) + str(nick).upper() + str(dob)
print str(poc).upper() + str(nick) + str(dob)
print str(poc).upper() + str(nick).upper() + str(dob)
print str(nick) + str(poc) + str(dob)
print str(nick).upper() + str(poc) + str(dob)
print str(nick) + str(poc).upper() + str(dob)
print str(nick).upper() + str(poc).upper() + str(dob)
print str(nick) + str(dob) + str(poc)
print str(nick).upper() + str(dob) + str(poc)
print str(nick) + str(dob) + str(poc).upper()
print str(nick).upper() + str(dob) + str(poc).upper()
print str(poc) + str(dob) + str(nick)
print str(poc).upper() + str(dob) + str(nick)
print str(poc) + str(dob) + str(nick).upper()
print str(poc).upper() + str(dob) + str(nick).upper()
#WITH NAME
print str(dob) + str(name) + str(poc)
print str(dob) + str(name).upper() + str(poc)
print str(dob) + str(name) + str(poc).upper()
print str(dob) + str(name).upper() + str(poc).upper()
print str(dob) + str(poc) + str(name)
print str(dob) + str(poc).upper() + str(name)
print str(dob) + str(poc) + str(name).upper()
print str(dob) + str(poc).upper() + str(name).upper()
print str(poc) + str(name) + str(dob)
print str(poc) + str(name).upper() + str(dob)
print str(poc).upper() + str(name) + str(dob)
print str(poc).upper() + str(name).upper() + str(dob)
print str(name) + str(poc) + str(dob)
print str(name).upper() + str(poc) + str(dob)
print str(name) + str(poc).upper() + str(dob)
print str(name).upper() + str(poc).upper() + str(dob)
print str(name) + str(dob) + str(poc)
print str(name).upper() + str(dob) + str(poc)
print str(name) + str(dob) + str(poc).upper()
print str(name).upper() + str(dob) + str(poc).upper()
print str(poc) + str(dob) + str(name)
print str(poc).upper() + str(dob) + str(name)
print str(poc) + str(dob) + str(name).upper()
print str(poc).upper() + str(dob) + str(name).upper()