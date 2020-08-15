import json


with open('demo.json' , 'r') as fh:
    #print(fh.read())


    #To know the type of the Json File
    json_str=fh.read()
    json_value=json.loads(json_str)
    print(type(json_value))
    #what if we just want Name
    print(json_value['Name'])
