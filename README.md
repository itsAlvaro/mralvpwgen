# mralvpwgen
For Python 2.7
1. BASIC EXPLANATION:

  This is a Python script I made in just one day (i will be updating it) which generates you a list of passwords using the data
  you have provided to it.
  
  The way it works is by making permutations between strings.
  
  It uses the str(), lower() and title() function, as well as the str()[-] to take the firsts characters of a string

Knowing that:

    dob = date of birth
    
    name = personal name
    
    poc = place of birth
    

  A example of a permutation made by the script is:
  
    str(dob) + str(name)  
    
  This just joins both strings
    
  A more complex example is:
  
    print str(dob)[0] + str(dob)[1] + str(dob)[2] + str(dob)[3] + str (poc).upper() + str(dob)[4] + str(dob)[5] + str(dob)[6] + str(dob)[7]

  This one takes the first four digits of the string 'date of birth', adds the 'Place of child' string (in uppercase) and then adds
  the last four digits of the string 'date of birth'

2. VERSION HISTORY:

VERSION 1.0.0 

    Public Release: 24-3-2018

    Nº of permutations: 108

    Nº of strings: 5 
    start
    name
    nick
    dob
    poc

