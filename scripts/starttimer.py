import time
print(">> start_timer()")
tempfile = open(".orangepytimer.temp","w")
tempfile.write(f"{time.time()}")
tempfile.close()
print("<< timer started")
