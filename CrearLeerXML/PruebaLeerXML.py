from xml.dom import minidom

xmldoc = minidom.parse("comprobador.xml")
itemlist = xmldoc.getElementsByTagName("buscar")

for i in itemlist:

	print (i.attributes["id"].value)
	print (i.attributes["valor"].value)
	print (i.attributes["web"].value)
	print (i.firstChild.nodeValue)
