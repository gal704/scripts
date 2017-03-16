import glob
import os
import sys

def handleMP4():
	try:
		import mutagen.mp4 as mp4
	except:
		print "Error importing mutagen.mp4 make sure you ran this script from bash"
		return None

	files = glob.glob("*.mp4")
	files_with_length = []
	
	current_directory = os.getcwd() + os.sep
	
	for i in xrange(len(files)):
		files[i] = current_directory + files[i]
	
	for file in files:
		try:
			audio = mp4.MP4(file)
			length = int(audio.info.length * 1000)
			files_with_length.append((file, length))
		except:
			print "Error handling MP4 files"

	return files_with_length

def handleMP3():
	try:
		import mutagen.mp3 as mp3
	except:
		print "Error importing mutagen.mp4 make sure you ran this script from bash"
		return None

	files = glob.glob("*.mp3")
	files_with_length = []
	
	current_directory = os.getcwd() + os.sep

	for i in xrange(len(files)):
		files[i] = current_directory + files[i]
	
	for file in files:
		try:
			audio = mp3.MP3(file)
			length = int(audio.info.length * 1000)
			files_with_length.append((file, length))
		except:
			print "Error handling MP4 files"
	return files_with_length

def CompareStrings(string1, string2):
	sizeToCompare = min(len(string1), len(string2))

	for i in xrange(sizeToCompare):
		if string1[i] != string2[i]:
			return False
	return True

def convertBashPathToWindowsPath(bashPath):

	if bashPath == None:
		return None

	if bashPath[0] != '/':
		return None
	
	if not CompareStrings(bashPath, "/mnt/"):
		return None
	return bashPath[5:6] + ':' + bashPath[6:]

def CreateXML(songs):
	try:
		from xml.etree.ElementTree import Element, SubElement, tostring
	except:
		print "Failed to import xml"
		return None

	url0 = "http://xspf.org/ns/0/"
	url1 = "http://www.videolan.org/vlc/playlist/ns/0/"
	url3 = "http://www.videolan.org/vlc/playlist/0"
	
	playlist = Element("playlist",{"xmlns":url0, "xmlns:vlc":url1, "version":"1"})

	title = SubElement(playlist, "title")
	
	title.text= "PlayList"

	tracklist = SubElement(playlist, "tracklist")
	track = []

	for i in xrange(len(songs)):
		track.append([SubElement(tracklist,"track")])
		track[i].append(SubElement(track[i][0], "location"))
		track[i][1].text = songs[i][0]
		track[i].append(SubElement(track[i][0], "duration"))
		track[i][2].text = str(songs[i][1])
		track[i].append(SubElement(track[i][0], "extension", {"application" : url3}))
		track[i].append(SubElement(track[i][3], "vlc:id"))
		track[i][4].text = str(i)

	extensions = SubElement(playlist, "extension", {"application" : url3})
	items = []
	for i in xrange(len(songs)):
			items.append(SubElement(extensions, "vlc:item", {"tid" 	: str(i)}))
	return tostring(playlist)

if __name__ == '__main__':
	
	outputFile = open(sys.argv[1] + ".xspf", "w")
	mp4files = handleMP4()
	mp3files = handleMP3()
	allFiles = []

	for file in mp4files:
		allFiles.append(("file:///" + convertBashPathToWindowsPath(file[0]), file[1]))

	for file in mp3files:
		allFiles.append(("file:///" + convertBashPathToWindowsPath(file[0]), file[1]))

	xml = CreateXML(allFiles)
	outputFile.write(xml)
	outputFile.close()
