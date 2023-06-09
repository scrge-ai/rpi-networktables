# ROBOT IP: 10.0.8.2

import sys
import time
from networktables import NetworkTables

# To see messages from networktables, you must setup logging
import logging

logging.basicConfig(level=logging.DEBUG)

if len(sys.argv) != 2:
    print("Error: specify an IP to connect to!")
    exit(0)

ip = sys.argv[1]

NetworkTables.initialize(server=ip)


def valueChanged(key, value, isNew):
    print("valueChanged: key: '%s'; value: %s; isNew: %s" % (key, value, isNew))


#NetworkTables.addEntryListener(valueChanged)
NetworkTables.initialize(server=ip)
table = NetworkTables.getTable("testTable")
#robotTime = table.getNumber("test", 0)

while True:
    print(table.getNumber("test", 0))
