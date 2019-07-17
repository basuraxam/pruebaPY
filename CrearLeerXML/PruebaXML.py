import xml.etree.ElementTree as ET

# create the file structure
comprobar = ET.Element('Comprobador')
buscar1 = ET.SubElement(comprobar, 'buscar')
buscar1.set('web','www.zorin.es')
buscar1.set('valor','lite')
buscar1.set('id','zorin15lite')
buscar1.text = 'zorin 15 lite'

buscar2 = ET.SubElement(comprobar, 'buscar')
buscar2.set('web','www.linuxmint.es')
buscar2.set('valor','19.2')
buscar2.set('id','lmint192')
buscar2.text = 'linux mint 19.2'


# create a new XML file with the results
mydata = ET.tostring(comprobar)
myfile = open("comprobador.xml", "w")
myfile.write(mydata)

