

def intConvertToTime(time):
    
    seconds = time * 60 * 60
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)

    return "%02d:%02d:%02d"%(hours, minutes, seconds)

def timeConvertToInt(stringTime):
    hour = stringTime[0: -6]
    minute = stringTime[3: -3]
    second = stringTime[6:]
    hour = int(hour)
    minute = int(minute)
    second = int(second)

    newTime = hour + (minute/60) + (second/3600)
    return round(newTime, 4)

def timePassing(time):

    print("time passes")