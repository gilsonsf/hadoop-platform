#!/usr/bin/env python
import sys

prev_word          = "  "
                
line_cnt           = 0  #count input lines

output = {}

def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

for line in sys.stdin:
    line       = line.strip()       #strip out carriage return
    key_value  = line.split('\t')   #split line, into key and value, returns a list
    line_cnt   = line_cnt+1  
    curr_word  = key_value[0]         #key is first item in list, indexed by 0
    value_in   = key_value[1]         #value is 2nd item

    if RepresentsInt(value_in):
        if curr_word in output:
            output[curr_word] += int(value_in)
    else:
        if value_in == "ABC":
            print(curr_word)
            output[curr_word] = 0
for keys,values in output.items():
    print keys, values

