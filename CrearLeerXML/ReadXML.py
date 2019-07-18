from xml.dom import minidom

 

mixml="""<conversation>

    <message line="1">

        <author>jose</author>

        <time>03:10</time>

    </message>

    <message line="2">

        <author>juan</author>

        <time>03:20</time>

    </message>

    <message line="3">

        <author>pepe</author>

        <time>03:20</time>

    </message>

</conversation>"""

 

xmldoc = minidom.parseString(mixml)

 

# obtenemos el atributo line de <message line="...">

print ("Atributo")

print ("----------------------")

itemlist = xmldoc.getElementsByTagName("message")

for i in itemlist:

    print (i.attributes["line"].value)

 

# obtenemos el valor del tag <text>

print

print ("Contenido")

print ("----------------------")

itemlist = xmldoc.getElementsByTagName("author")

for i in itemlist:

    print (i.firstChild.nodeValue)
