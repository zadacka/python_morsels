import re


def sum_timestamps_alex(timestamps):
    minutes = 0
    seconds = 0
    for timestamp in timestamps:
        hms_match = re.match(r"^(?P<hours>\d*):(?P<minutes>\d+):(?P<seconds>\d+)$", timestamp)
        ms_match = re.match(r"^(?P<minutes>\d+):(?P<seconds>\d+)$", timestamp)
        if hms_match:
            minutes += int(hms_match.group('hours')) * 60 + int(hms_match.group('minutes'))
            seconds += int(hms_match.group('seconds'))
        elif ms_match:
            minutes += int(ms_match.group('minutes'))
            seconds += int(ms_match.group('seconds'))
        else:
            raise ValueError(f"Could not find a hh:mm:ss or mm:ss format match for: {timestamp}")

    hours = (minutes + seconds // 60) // 60
    minutes = (minutes + seconds // 60) % 60
    seconds = seconds % 60

    if hours:
        return f"{hours:}:{minutes:02}:{seconds:02}"
    elif minutes:
        return f"{minutes:}:{seconds:02}"
    else:
        return f"0:{seconds:02}"


#############################################################
# Now for Trey's Solution....
############################################################

def parse_time(time_string):
    # optional group syntax: (? ..... )?
    # this is EXACTLY what I wanted to do ... but I didn't know how to do it!
    TIME_RE = re.compile(r"^(?:(\d+):)?(\d+):(\d+)$")
    hours, minutes, seconds = re.match(TIME_RE, time_string).groups()
    # ^- hours may be None, in which case we want to short circuit it to 0
    return int(hours or 0) * 3600 + int(minutes) * 60 + int(seconds)


def format_time(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    if hours:
        return f"{hours:01}:{minutes:02}:{seconds:02}"
    else:
        return f"{minutes:01}:{seconds:02}"


def sum_timestamps(timestamps):
    total_seconds = 0
    # for some reason I thought that Trey's hints were recommending that we handle minutes, seconds separately
    # my *original* plan was to convert everything to seconds ... which was the really nice way that Trey did this
    for timestamp in timestamps:
        total_seconds += parse_time(timestamp)
    return format_time(total_seconds)
