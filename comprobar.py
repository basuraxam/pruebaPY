#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import sys
import argparse

def download(url):

	r=requests.get(url)

	if r.status_code != 200:
		sys.stderr.write("error")
		return None

	return r.text

#----------------------------------------------------------------------------------------------------------------


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='%(prog)s is an ArgumentParser demo')

    parser.add_argument("-w","--web", help="Página web", default = "https://sourceforge.net/projects/zorin-os/files/15")
    parser.add_argument("-b","--buscar", help="Texto a buscar", default = "Lite")
    parser.add_argument("-t","--texto", help="Texto idenficativo", default = "Zorin 15 Lite")    
    parser.add_argument("-f","--file", help="Fichero con las webs y busquedas definidas", default = "")
    args = parser.parse_args()


    if args.file != "":
        sys.stdout.write("Parametro aun no disponible, sera ignorado ( %s ) \n" % args.file)        

    sys.stdout.write("Buscando: %s \n" % args.texto)

    r = download(args.web)
    if r:
	    TextoWeb = r[:10000000]
        
	    q = TextoWeb.find(args.buscar)
	    if (q==-1):
		    sys.stdout.write("No existe el texto a buscar. \n")
	    else:
		    sys.stdout.write("Texto encontrado en la web. \n")

	    #sys.stdout.write(r[:1000000])
    else:
	    sys.stdout.write("No existe la web. \n")

    try:
        input("Press enter to continue")
    except SyntaxError:
        pass


