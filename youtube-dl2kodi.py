#!/usr/bin/python

import codecs
import getopt
import json
import os
import sys
from datetime import datetime
from xml.dom import minidom
from xml.etree.ElementTree import Element, SubElement, tostring, ElementTree
from io import BytesIO

if len(sys.argv) != 2:
    print("usage: youtube-dl2kodi <FILENAME>")
    sys.exit(1)

filemovie = '.'.join(sys.argv[1].split('.')[:-1]) # strip .mkv when run via --exec
filemoviedir = os.path.dirname(filemovie);
filemovie = os.path.splitext(filemovie)[0]
filemovieext = os.path.splitext(filemovie)[1]
filejson = filemovie + ".info.json"
filenfo = filemovie + ".nfo"
tvshownfo = os.path.join(filemoviedir , "tvshow.nfo")

with open(filejson) as data_file:
    data = json.load(data_file)

#tvshow/channel
root_tvshow = Element("tvshow")
title_tvshow = SubElement(root_tvshow, "title")
uniqueid_show = SubElement(root_tvshow, "uniqueid")

title_tvshow.text  = data['uploader']
uniqueid_show.text = data['uploader_id']
uniqueid_show.set("type", data['extractor'])
uniqueid_show.set("default", "true")

##episodedetails
aired_date = datetime.strptime(data['upload_date'], '%Y%m%d').strftime('%Y-%m-%d')
root = Element("episodedetails")
title = SubElement(root, "title")
showtitle = SubElement(root, "showtitle")
aired = SubElement(root, "aired")
plot = SubElement(root, "plot")
thumb =  SubElement(root, "thumb")
season = SubElement(root, "season")
uniqueid = SubElement(root, "uniqueid")

title.text = data['fulltitle']
showtitle.text = data['uploader']
aired.text = aired_date
plot.text = data['description']
thumb.text = data['thumbnail']
season.text = "0"
uniqueid.text = data['id']
uniqueid.set("type", data['extractor'])
uniqueid.set("default", "true")

root_t =  ElementTree(root)
e = BytesIO()
root_t.write(e, encoding='utf-8', xml_declaration=True)

with open(filenfo, "bw") as f:
      f.write(e.getvalue())
# os.remove(filejson)

root_tvshow_t = ElementTree(root_tvshow)
s = BytesIO()
root_tvshow_t.write(s, encoding='utf-8', xml_declaration=True)

if not os.path.isfile(tvshownfo):
    with open(tvshownfo, "wb") as f:
      f.write(s.getvalue())
