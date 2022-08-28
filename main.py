import time
import rotatescreen as rs

display = rs.get_primary_display()
angel_list = [0, 90, 180, 270]

while True:
    for i in angel_list:
        display.rotate_to(i)
        time.sleep(0.1)
