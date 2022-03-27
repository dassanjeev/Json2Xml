'''
Author    : https://github.com/dassanjeev
Co Author : https://github.com/vijju000
         

'''
import xml.etree.cElementTree as e
import xml.dom.minidom as mindom
from xml.etree.ElementTree import tostring
import json as j



class JsonToXml:
    def __init__(self,rootName = "root"):
        self.rootName = rootName
        self.main = e.Element(self.rootName)
                
    def converter(self,path,savefile = True):
        with open(path) as json_format_file:
            d = j.load(json_format_file)
        def getDict(d,main):
            for key in d.keys():
                if type(d[key])!= list and type(d[key])!= dict:
                    e.SubElement(main,key).text = str(d[key])
                elif type(d[key])== dict:
                    main2 = e.SubElement(main,key)
                    getDict(d[key],main2)
                elif type(d[key])== list:
                    main3 = e.SubElement(main,key)
                    for value in d[key]:
                        getDict(value,main3)
        getDict(d,self.main)
        xml_p = mindom.parseString(tostring(self.main))
        pretty_xml = xml_p.toprettyxml()
        path = path+".xml"
        if savefile:
            with open(path, "w") as file:
                file.write(pretty_xml)
        return pretty_xml

    def converter2(self,d):
        def getDict(d,main):
            for key in d.keys():
                if type(d[key])!= list and type(d[key])!= dict:
                    e.SubElement(main,key).text = str(d[key])
                elif type(d[key])== dict:
                    main2 = e.SubElement(main,key)
                    getDict(d[key],main2)
                elif type(d[key])== list:
                    main3 = e.SubElement(main,key)
                    for value in d[key]:
                        getDict(value,main3)
        getDict(d,self.main)
        xml_p = mindom.parseString(tostring(self.main))
        pretty_xml = xml_p.toprettyxml()
        return pretty_xml

    
def main():
    obj = JsonToXml("Sanjeev")
    print(obj.converter(path = "C:/Users/dassa/Desktop/AI-ML L1/temp - Copy.json"))






