# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 20:58:16 2022

@author: adenn
"""

def add_time(starttime, duration, day_input = None):
    
    #split everything into its parts
    starttime_parts = starttime.split(' ')
    starttime_num = starttime_parts[0]
    starttime_xm = starttime_parts[1]
    
    starttime_num_parts = starttime_num.split(':')
    starttime_hour = starttime_num_parts[0]
    starttime_min = starttime_num_parts[1]
    
    duration_parts = duration.split(':')
    duration_hour = duration_parts[0]
    duration_min = duration_parts[1]
    
    #convert input time into 24 hour format
    #   but don't add anything to 12pm!
    #   and convert 12am to 0!
    if ((starttime_xm == 'PM') and (int(starttime_hour) != 12)):
        starttime_hour = int(starttime_hour) + 12
    elif (starttime_xm == 'AM') and (int(starttime_hour) == 12):
        starttime_hour = 0
    
    #perform basic number addition
    res_hour_raw = int(starttime_hour) + int(duration_hour)
    res_min_raw = int(starttime_min) + int(duration_min)
    
    #check for minute wrap beyond 60
    if res_min_raw >= 60:
        res_hour_raw += 1
        res_min = res_min_raw - 60
    else:
        res_min = res_min_raw
    
    if res_min < 10:
        res_min = '0' + str(res_min)
        

    #check for 24 hour wrap, reduce hour number to within 24
    day_wrap = int(res_hour_raw)//24
    
    res_hour24 = res_hour_raw - (24*day_wrap)
    
    
    if res_hour24 > 12:
        res_hour = res_hour24 - 12
        res_xm = 'PM'
    elif res_hour24 == 0:
        res_hour = 12
        res_xm = 'AM'
    elif res_hour24 == 12:
        res_hour = res_hour24
        res_xm = 'PM'
    else:
        res_hour = res_hour24
        res_xm = 'AM'
    
    #Generate days later statement
    if day_wrap == 1:
        days_later_statement = ' (next day)'
    elif day_wrap > 1:
        days_later_statement = ' (' + str(day_wrap) + ' days later)'
    else:
        days_later_statement = ''
          
    
    weekday=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    if day_input is not None:
        day = day_input.capitalize()
        
        day_index = weekday.index(day)
        res_day_raw = day_index + day_wrap
        
        week_wrap = res_day_raw//7
        res_day_index = res_day_raw - (7*week_wrap)
        
        res_day = ', ' + weekday[res_day_index]
    else:
        res_day = ''
        
    res_time = str(res_hour) + ':' + str(res_min) + ' ' + res_xm
    
    time_result = res_time + res_day + days_later_statement
    
    return time_result

