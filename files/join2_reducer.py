#!/usr/bin/env python
import sys

last_key      = None             
running_total = 0

list_tvshow=[]
list_tvshow_views=[]


for input_line in sys.stdin:
    input_line = input_line.strip()
    
    key_value  = input_line.split("\t")
    this_key     = key_value[0].strip()   
    value   = key_value[1].strip()   
 
    if(value[0:3]=='ABC'):
        list_tvshow.append(this_key)
    
    
for tvs in list_tvshow:
    
    total_viewers=0;

    for input_line in sys.stdin:
        input_line = input_line.strip()
    
        this_key, value = input_line.split("\t", 1)
        
        if(value.isdigit()):
            value = int(value)
            
            if this_key == tvs:
                total_viewers+=value
            
    list_tvshow_views.append( "{0}\t{1}".format(tvs, total_viewers) )  
        
for view in list_tvshow_views:
    print( view )
    	
    