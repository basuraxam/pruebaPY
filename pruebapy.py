import requests
import sys

def download(url):

	r=requests.get(url)

	if r.status_code != 200:
		sys.stderr.write("error")
		return None

	return r.text

if __name__ == '__main__':
	url = "https://sourceforge.net/projects/zorin-os/files/15"
	r = download(url)
	if r:
		sys.stdout.write(r[:1000000])
	else:
		sys.stdout.write("Nothing was retrieved.")
