import os
import subprocess
import json
import sys
files =  os.listdir("../.././songs")
song_metadata = []


out_file = open("test.json", "w")
files_length = len(files);
current_percentage = 1
print current_percentage
for x in range(0, len(files)):
    file_path = files[x]

    title = ""
    artist = ""
    album = ""
    p = subprocess.Popen("ffmpeg -i '../.././songs/"+ file_path +"' -f ffmetadata", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in p.stdout.readlines():
	line = line.replace('"', "'").strip().replace('\n', '')
	if "title" in line:
	    if title == "":
		temp_array = line.split(':')
		title = temp_array[1].strip().replace('\n', '')
	if "artist" in line:
	    if artist == "":
		temp_array = line.split(':')
		artist = temp_array[1].strip().replace('\n', '')

	if "album" in line and "artist" not in line:
	    if album == "":
		temp_array = line.split(':')
		album = temp_array[1].strip().replace('\n', '')
    if title == "":
	title = file_path
    temp_dict = {'location': file_path, 'metadata': {'title': title, 'artist': artist, 'album': album}}
    song_metadata.append(temp_dict)
    temp_percentage = int(float(x)/files_length * 100)
    if temp_percentage + 1 > current_percentage:
	current_percentage = temp_percentage + 1
	print current_percentage


json.dump(song_metadata, out_file, indent=4)
out_file.close()