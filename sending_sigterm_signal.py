from property import redis_server
import os,signal

r = redis_server
pid = int(r.lpop('pid'))
print(pid)

#terminating  the  process for request_processs.py 
def terminate_process(pid):
    try:
        if pid:
            os.kill(pid,signal.SIGTERM)
            print("process {} is terminated successfully!!!".format(pid))    
    except ProcessLookupError:
        print("No such processs is running")

terminate_process(pid)