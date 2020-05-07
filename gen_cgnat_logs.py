#!/usr/bin/env python
import ipaddr
import random
import datetime

privip_range = ipaddr.IPv4Network('192.168.1.0/16')
pubip_range = ipaddr.IPv4Network('100.67.82.0/27')

with open('cgnat.log', 'a') as the_file:
	for i in range(150000):
		privip_rand = ipaddr.IPv4Address(random.randrange(int(privip_range.network)+1, int(privip_range.broadcast) - 1))
		privport_rand = random.randrange(1,65536)
		pubip_rand = ipaddr.IPv4Address(random.randrange(int(pubip_range.network)+1, int(pubip_range.broadcast) - 1))
		pubport_rand = random.randrange(1,65536)
		timestamp = datetime.datetime.now().strftime("%B %d %H:%M:%S")
		the_file.write('%s - %s:%s  ->  %s:%s \n' %(timestamp, privip_rand, privport_rand, pubip_rand, pubport_rand))


print 'Data Uploaded into file successfully!'
