#!/usr/bin/env python
import sys

for line in sys.stdin:
    line       = line.strip()
    key_value  = line.split(",")
    tv_show     = key_value[0].strip()   
    count_channel   = key_value[1].strip()   

    if count_channel.isdigit() or count_channel[0:3]=='ABC':
        print( '%s\t%s' % (tv_show, count_channel) ) 
         