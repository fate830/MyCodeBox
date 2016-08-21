import json

data = [{'a':"A",'b':(2,4),'c':3.0}]  #list对象
print (data)
#print repr(data)

data_string = json.dumps(data)
print (data_string)