import requests
import sys

def download(url):

	r=requests.get(url)

	if r.status_code != 200:
		sys.stderr.write("error")
		return None

	return r.text

if __name__ == '__main__':
	url = "http://elpais.com"
	r = download(url)
	if r:
		sys.stdout.write(r[:100])
	else:
		sys.stdout.write("Nothing was retrieved.")
