#main.py
from pcom import *
import time
import datetime

log = Logger()
# log.suppress_communication_logs(True)

pcom = Pcom("172.20.9.15",5000,log)
log.Message("Communication has established")
log.Message("Command loop has started")
# log.ErrorMessage("Hosokawa-san lost the link with Tada-san")

address_list = [
"FFFE381A",
"FFFE3838",
"FFFE383A",
"FFFE385A",
"FFFE387A",
"FFFE389A",
"FFFE38BA",
"FFFE38D8",
"FFFE38DA",
"FFFE38FA",
"FFFE391A"
]

indexer:int
indexer = 0
for s in address_list:
    ans = pcom.send_and_receive("&0FDLA" + s + "W")

