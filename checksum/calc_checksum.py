import os
import sys

MAX_DATA_READ	= 100*1024*1024

def help():
	print "\n\rUsage:\tpython " + sys.argv[0] + " input_file_to_calc_checksum_on"

def main():
	checksum = 0
	count = 0
	if len(sys.argv) != 2:
		help()
		return

	f = open(sys.argv[1], "rb")
	data = f.read(MAX_DATA_READ)
	while len(data) != 0:
		for i in data:
			checksum += ord(i)
		data = f.read(MAX_DATA_READ)
		print count
		print checksum
		count = count + 1
	print checksum

if __name__ == '__main__':
    main()