import urllib2,os
import urllib

def download_song_from_url(url):
	file_name = url.split('/')[-1]
	url = urllib.quote(url,":/")
	print url
	req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"}) 
	con = urllib2.urlopen( req )

	u = con
	f = open("./songs/"+file_name, 'wb')
	meta = u.info()
	file_size = int(meta.getheaders("Content-Length")[0])
	print "Downloading: %s Bytes: %s" % (file_name, file_size)
	
	file_size_dl = 0
	block_sz = 8192
	while True:
	    buffer = u.read(block_sz)
	    if not buffer:
	        break

	    file_size_dl += len(buffer)
	    f.write(buffer)
	    status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
	    status = status + chr(8)*(len(status)+1)
	    print status,

	f.close()

file_list = open("temp.txt","r")
for line in file_list:
	try:
		download_song_from_url(line.strip())
		print "Done."
		pass
	except Exception, e:
		# raise
		print e
	else:
		pass
	finally:
		pass