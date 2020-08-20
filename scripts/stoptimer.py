import time
try:
    newtime = time.time()
    tempfile = open(".orangepytimer.temp","r")
    oldtime = float(tempfile.read())
    tempfile.close()
    print(">> stop_timer()")
    print(f"<< {round(newtime-oldtime,2)}s")
    tempfile = open(".orangepytimer.temp","w")
    tempfile.close()
except:
    print(">> stop_timer()")
    print("<< error - timer not started")