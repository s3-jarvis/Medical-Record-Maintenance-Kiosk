import os 
import logging
from logging.handlers import RotatingFileHandler
    
cnt =2 

directory = "PID_{}".format(cnt)
    
# Parent Directories 
parent_dir = 'C:/Users/Srinivas U Bhat/Desktop'
    
# Path 
paths = os.path.join(parent_dir, directory) 
    
# Create the directory 
# 'PID_number' 
os.makedirs(paths) 
print("Directory '% s' created" % directory) 


logger1 = logging.getLogger('general_logger')
logger2 = logging.getLogger('some_other_logger')

folder1 = "C:/Users/Srinivas U Bhat/Desktop/{}/Doctor_Report.log".format(directory)
folder2 = "C:/Users/Srinivas U Bhat/Desktop/{}/Symptoms.log".format(directory)

print("Folder one :",folder1)
print("Folder one :",folder2)

log_handler1 = logging.FileHandler(folder1, 'w')
log_handler2 = logging.FileHandler(folder2, 'w')

logger1.addHandler(log_handler1)
logger2.addHandler(log_handler2)

logger1.warning("this will be logged to Doctor's report ")
logger2.warning("this will be logged to Symptoms file")