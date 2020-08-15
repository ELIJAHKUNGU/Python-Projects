
import json

a = {
    'Name' : 'Max',
    ' Age' : 28,
    'Marks': (90,56,98,45,67),
    "pass" : True

}
with open('demo.json' , 'w') as fh:
    fh.write(json.dumps(a, indent=2))

