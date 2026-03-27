from datetime import datetime

def can_retake(finish_time, current_time):
    # Define format of str to make object datetime
    format_str = '%Y %m %d %H %M %S'
    # finish time in format of str to make object datetime
    finish_time_str = finish_time[:4] + ' ' + finish_time[5:7] + ' ' + finish_time[8:10] + ' ' + finish_time[11:13] + ' ' + finish_time[14:16] + ' ' + finish_time[17:19]
    # current time in format of str to make object datetime
    current_time_str = current_time[:4] + ' ' + current_time[5:7] + ' ' + current_time[8:10] + ' ' + current_time[11:13] + ' ' + current_time[14:16] + ' ' + current_time[17:19]
    # finish time in object datetime
    finish_time_obj = datetime.strptime(finish_time_str, format_str)
    # current time in object datetime
    current_time_obj = datetime.strptime(current_time_str, format_str)
    # Calculate time difference
    dif_time = current_time_obj - finish_time_obj
    # Convert time difference to hours
    result = dif_time.total_seconds()/3600
    # Return value
    return True if result >= 48 else False

if __name__ == '__main__':
    print(can_retake("2026-03-23T08:00:00", "2026-03-25T14:00:00"))
    print('----')
    print(can_retake("2026-03-24T14:00:00", "2026-03-25T10:00:00"))
    print('----')
    print(can_retake("2026-03-23T09:25:00", "2026-03-25T09:25:00"))
    print('----')
    print(can_retake("2026-03-25T11:50:00", "2026-03-23T11:49:59"))

