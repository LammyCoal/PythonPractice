# This program uses map() filter() and reduce() to process data
from functools import reduce


# List of songs with their durations (in minutes)
playlist = [('What Was I Made For?', 3.42), ('Just Like That', 5.05), ('Song 3', 6.55), ('Leave The Door Open', 4.02), ('I Can\'t Breath', 4.47), ('Bad Guy', 3.14)]

def filtering(songs):
    return songs[1] > float(5.00)
answer = filter(filtering, playlist)
print(list(answer))

duration = playlist[0][1]
int_minutes = int(duration)
seconds = int_minutes * 60
total_minutes = seconds  + ((duration-int_minutes) * 100)
print(total_minutes)



def convertion(songs):
    return duration * 60

convert = map(convertion, playlist)
print(list(convert))

def add_duration(total, songs):
    return total + songs[1]

answer = reduce(add_duration, playlist,0)
print(answer)







