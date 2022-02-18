import time
import sys
import webbrowser as wb
minutes = sys.argv[1]
webopen = sys.argv[2]
seconds = 60 #that is is the number of seconds in a minute
conversion = float(minutes) * seconds
minutes = conversion
time.sleep(minutes)
wb.open(f"{webopen}", new=1)