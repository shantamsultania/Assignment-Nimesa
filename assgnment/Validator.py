def valid_date(date):
    date_word = date.split("-")
    year = date_word[0]
    month = date_word[1]
    day = date_word[2]
    if len(date) != 10:
        return False
    if len(date_word) != 3:
        return False
    elif len(year) != 4:
        return False
    elif len(month) != 2:
        return False
    elif len(day) != 2:
        return False
    c = 0
    for i in date:
        if i == '-':
            c += 1
        if c > 2:
            return False

    return True


def valid_time(time):
    time_word = time.split(":")
    hours = time_word[0]
    min = time_word[1]
    sec = time_word[2]
    if len(time) != 8:
        return False
    if len(hours) != 2:
        return False
    elif len(min) != 2:
        return False
    elif len(sec) != 2:
        return False
    elif len(time_word) != 3:
        return False
    c = 0
    for i in time:
        if '0' <= i <= '9':
            continue
        else:
            if i == ':':
                c += 1
            if c > 2:
                return False

    return True
