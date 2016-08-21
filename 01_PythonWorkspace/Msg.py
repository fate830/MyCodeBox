import json

class MyMsg(object):
    begin = 'ATSMSG'
    version = "1.0"
    end = '\n\r\n\r'
    
    def __init__(self):
        self.begin = 'ATSMSG'
        self.version = "1.0"
        self.end = '\n\r\n\r'
        
    def __repr__(self):
        return 'MyMsg:%s,%s,%s' % (self.begin, self.version, self.end)

class MySCSMsg(MyMsg):
    cmd = "REG_SVR"
    def __repr__(self):
        return 'MyMsg:%s,%s,%s,%s' % (self.begin, self.version, self.cmd, self.end)
                 
def convert_to_builtin_type(obj): 
    print ('default(%s)' % repr(obj)) # 把MyObj对象转换成dict类型的对象
    d = {}
    d['__class__'] = obj.__class__.__name__
    d['__module__'] = obj.__module__
    d.update(obj.__dict__)
    return d

print (MyMsg())
print (MySCSMsg())

obj = MyMsg()
#try:    
print (json.dumps(obj, default=convert_to_builtin_type))
#except TypeError, err:
#    print (err)