<<<<<<< HEAD
#import xml.etree.ElementTree as ET
from lxml import etree as ET
#Get the XML File Data
stream = open('G:\GIT\Mong-Project\simple.xml','r')
=======
import xml.etree.ElementTree as ET

#Get the XML File Data
stream = open('simple.xml','r')
>>>>>>> 2365c2d30d97c84943a9383e9df1aab456ffec9a

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
    