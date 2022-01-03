import xml.etree.ElementTree as ET

#Get the XML File Data
stream = open('simple.xml','r')

#Parse the data into an ElementTree Object
xml = ET.parse(stream)

#Get the 'root' Element object from ElementTree
root = xml.getroot()

#Iterate through each child of the root Element
for e in root:
    #print the stringifield version of the element
    print(ET.tostring(e))
    print("")

    #print the 'ID' attribute of the Element Object
    print(e.get("Id"))
    