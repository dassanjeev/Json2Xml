from Json2xml import JsonToXml

#you can change the main element of your xml
#obj = JsonToXml("mainElement")
obj = JsonToXml()
#you can use the file method
obj.converter(path = "you file location",savefile = True)
#or you can use the json object method where you pass a dict object
json = {
  "Name" : "Rani",
  "Designation" : "PHP Developer",
  "Salary" : 98000,
  "Age":27,
  "Projects" :{"Topic":"Smart Ambulance","Category":"Android Application","Months":{"Test":"Smart Ambulance","tes2":"Android Application","tes3":2}}
}

obj.converter2(json)

#Note both the function return pretty_xml which can be printed
