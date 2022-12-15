from xml.dom import minidom

# otwieramy plik w parserze
DOMTree = minidom.parse('dane_xml.xml')
print(DOMTree.toxml())
cNodes = DOMTree.childNodes
print(cNodes[0].getElementsByTagName("osoba")[0].toxml())
print(cNodes[0].getElementsByTagName("osoba")[1].toxml())
