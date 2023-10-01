import time

def focus_timer(minutes):
    seconds = minutes * 60
    end_time = time.time() + seconds
    
    while time.time() < end_time:
        remaining_time = int(end_time - time.time())
        minutes = remaining_time // 60
        seconds = remaining_time % 60
        timer = '{:02d}:{:02d}'.format(minutes, seconds)
        print('Remaining Time:', timer, end='\r')
        time.sleep(1)
    
    print('Focus Timer Completed!')

# 设置专注时长为25分钟
focus_timer(25)
