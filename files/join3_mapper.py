#!/usr/bin/env python
import sys

# --------------------------------------------------------------------------

# --------------------------------------------------------------------------



for line in sys.stdin:
    line       = line.strip()   #strip out carriage return
    key_value  = line.split(",")   
    key_in     = key_value[0].split(" ")   #key is first item in list
    value_in   = key_value[1]   #value is 2nd item 

    
    print( '%s\t%s' % (key_in[0], value_in) ) 
