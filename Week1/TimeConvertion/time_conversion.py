""" time = '07:05:45PM'
new_time = time.split(':')
print(new_time) """

def time_conversion(time: str):
    time_separate_in_list = time.split(':')
    new_time = ''
    if 'PM' in time_separate_in_list[2]:
        if time_separate_in_list[0] == '12': 
            time_separate_in_list[2] = time_separate_in_list[2].replace('PM', '')
        else:
            hour = int(time_separate_in_list[0]) + 12
            if hour == 24:
                hour = 0
            time_separate_in_list[0] = str(hour)
            time_separate_in_list[2] = time_separate_in_list[2].replace('PM', '')
    elif '12' in time_separate_in_list[0]:
            time_separate_in_list[0] = '00'
            time_separate_in_list[2] = time_separate_in_list[2].replace('AM', '')
    else:
        time_separate_in_list[2] = time_separate_in_list[2].replace('AM', '')
    new_time = ':'.join(time_separate_in_list)
    return new_time
    
    
print(time_conversion('12:45:54PM'))