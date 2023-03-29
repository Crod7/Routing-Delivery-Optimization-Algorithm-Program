
# This function takes a number and converts it to a string representing the time. ex: 8.5 ---> 8:30am
def intConvertToTime(time):

    seconds = time * 60 * 60
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)

    return "%02d:%02d:%02d"%(hours, minutes, seconds)