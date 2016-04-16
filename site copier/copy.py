import sys
import urllib2
import re
import os

MAX_LEVELS = 20

def help():
	print "Usage:"
	print "    " + sys.argv[0] + " base_url_address"

def is_exist(path):
	return os.path.isfile(path)

def create_file(name, data):
	try:
		new_file = open(name, "w")
	except:
		print "Failed to open file named:" + name

	new_file.write(data)
	new_file.close()

def get_relative_urls(source_code):
	urls = re.findall('href="(?!(?:mailto|http))([^"]*)"', source_code)
	return urls

def get_source_code(url):
	response = urllib2.urlopen(url)
	page_source = response.read()
	return page_source

def get_file_name(url):
	return url[url.rfind('/')+1:]

def crawl_and_copy(first_url):
	urls = []
	base_url = first_url[:-1 * len(get_file_name(first_url))]
	urls.append((first_url, 0))
	while(len(urls)):
		current_file_touple = urls.pop()
		current_file = current_file_touple[0]
		current_level = current_file_touple[1]
		if not is_exist(get_file_name(current_file)):
			source_code = get_source_code(current_file)
			file_name = get_file_name(current_file)
			create_file(file_name, source_code)
			if current_level < MAX_LEVELS:
				relative_urls = get_relative_urls(source_code)
				for i in relative_urls:
					urls.append(((base_url + i), current_level + 1))


def main():
	if len(sys.argv) != 2:
		help()
		exit()

	first_url = sys.argv[1]
	crawl_and_copy(first_url)
	# source = get_source_code(first_url)
	# file_name = get_file_name(first_url)
	# print "file name:" + file_name
	# print "base url:" + first_url[:-1 * len(get_file_name(first_url))]
	# urls = re.findall('href="(?!(?:mailto|http))([^"]*)"', source)
	# print urls

	pass

if __name__ == '__main__':
	main()