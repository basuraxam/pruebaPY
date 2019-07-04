
import urllib2

# google cada vez que generas la web pone codigo diferente por el caracter 258
#url = 'http://www.google.es'
url = 'https://sourceforge.net/projects/zorin-os/files/15/'
#fichero = './datos/googlecom.txt'
fichero = './datos/zorin.txt'

response   = urllib2.urlopen(url)
webContent = response.read()
webDatos   = webContent[0:10000000]

file1 = open(fichero, 'r')
fileContent = file1.read()
file1.close()

print ("COMPARACION 0")
if fileContent == webDatos:
    print ("Comp 0 - iguales")
else:
    print ("Comp 0 - diferente")


print ("COMPARACION 1")
if fileContent == webContent:
    print ("Comp 1 - iguales")
else:
    print ("Comp 1 - diferente")


print ("COMPARACION 2")

i=0
for cfile in fileContent:
    i=i+1   
    cweb = webDatos[i-1:i]
    if cfile != cweb:
        print ("Comp 2 - diferente")
        print (i)        
        print (cfile + " - " + cweb)
        #exit()

    if i==130008: exit()




#print(webContent[0:10000000])

#contenido = webContent[0:10000000]
#print(contenido)


#with open('./datos/diffgoogle.txt', 'w') as file_out:
#    for line in difference:
#        file_out.write(line)




#file1 = open('some_file_1.txt', 'r')
#file2 = open('some_file_2.txt', 'r')
#FO = open('some_output_file.txt', 'w')

#for line1 in file1:
#    for line2 in file2:
#        if line1 == line2:
#            FO.write("%s\n" %(line1))

#FO.close()
#file1.close()
#file2.close()

