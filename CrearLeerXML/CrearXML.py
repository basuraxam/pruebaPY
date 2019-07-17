import xml.etree.ElementTree as ET

elemento_1 = ET.Element('SistemasOperativos')
elemento_hijo_1 = ET.SubElement(elemento_1, 'Windows')
elemento_hijo_2 = ET.SubElement(elemento_1, 'Linux')
elemento_hijo_3 = ET.SubElement(elemento_1, 'MacOS')

archivo = open('SistemasOperativos.xml', 'a')

archivo.write(ET.tostring(elemento_1, encoding='utf-8').decode('utf-8'))
