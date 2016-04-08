#!/usr/bin/python

import re

s = 'Apr  7 20:35:03 Ladderr CRON[24405]: (CRON) info (No MTA installed, discarding output'

m = re.match(r'(\w{3})  (\d{1}) (\d{2}):(\d{2}):(\d{2}) (\w*) (\w*)\[(\d*)\]', s)

month = m.group(1)
day = m.group(2)
hour = m.group(3)
minutes = m.group(4)
seconds = m.group(5)
hostname = m.group(6)
proccess = m.group(7)
message = m.group(8)

print month + day + hour + minutes + seconds + hostname + proccess + message
