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
	txtfind = "Lite"
	txtfind = "Core"
	r = download(url)
	if r:
		web = r[:10000000]
		q = web.find(txtfind)
		if (q==-1):
			sys.stdout.write("No existe...")
		else:
			sys.stdout.write("Encontrado...")

		#sys.stdout.write(r[:1000000])
	else:
		sys.stdout.write("No existe.")
