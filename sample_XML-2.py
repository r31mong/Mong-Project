import xmltodict

#get the XML file date
stream = open('G:\GIT\Mong-Project\simple.xml','r')

#Parse the XML file into an 'OrderedDict'
xml = xmltodict.parse(stream.read())

for e in xml["breakfast_menu"]["food"]:
    print(e)
