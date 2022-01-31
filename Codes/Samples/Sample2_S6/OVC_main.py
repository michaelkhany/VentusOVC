""" 
 -------------------------------------------------------------
 Project:      Objective Visionary Core System (v.beta)
 version:      v.20220111b
 Supervisor:   ENG. Michael B.Khani
 Developers:   et al.  
        Configurations
 Properties:   2x Camera Input Images, Target Sample
 Output:       Target recognition data, Distance estimation data
 -------------------------------------------------------------"""


import os
from datetime import datetime
from typing import NewType

# ....
# (your dependencies here)

import ovcm_log

# ...

# Preparing the environment
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
clearConsole()

print('Objective Visionary Core System (v.beta)');

while (True):
    #To estimate the duration time form now
    start_time = datetime.now()

    clearConsole()
    runTimeBug =""
    try:
        # ....
        # (your code runs here)


        print("Hi")
        ovcm_log.printIt_CL("Test process started:",ovcm_log.bcolors.CGREEN)
        ovcm_log.printIt("Processing done.")


        # ....
    except ValueError:
        runTimeBug ="Not suitable value"
    except:
        runTimeBug ="Unknown bug."
    #Log the error:
    if (len(runTimeBug) >=1):
        print("\n\tStatus: Error({0})".format(runTimeBug))
    else:
        print("\n\t Status: Normal")
    #To estimate the duration time til now
    end_time = datetime.now()
    time_diff = (end_time - start_time)
    execution_time = time_diff.total_seconds() * 1000
    print("\n\tRun-time Duration {0}".format(execution_time))
