import urllib2

url = 'https://sourceforge.net/projects/zorin-os/files/15/'

response = urllib2.urlopen(url)
webContent = response.read()

with open('./datos/zorin.txt', 'w') as file_out:
    file_out.write(webContent)

#print(webContent[0:300000])
