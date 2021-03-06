from scapy.all import *

class ping_host_scan:
	def __init__(self,scan_ip_prefix=None,scan_file_name=None):
		self.scan_ip_prefix = scan_ip_prefix
		self.scan_file_name = scan_file_name
	def scan_host(self):
		for addr in range(0,254):
			response = sr1(IP(dst = (self.scan_ip_prefix + str(addr)))/ICMP(),timeout = 0.1,verbose = 0)
			if response == None:
				pass
			else:
				print("%s [UP]" % (self.scan_ip_prefix + str(addr)))
	def scan_file(self):
		file = open(self.scan_file_name,"r")
		for addr in file:
			response = sr1(IP(dst = addr.strip())/ICMP(),timeout = 0.1,verbose = 0)
			if response == None:
				pass
			else:
				print("%s [UP]" % (addr.strip()))


# A = ping_scan(scan_file_name="iplist.txt")
# A.scan_file()