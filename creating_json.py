import json

data=[
	{
		"file_name": "C:/Users/Ayush/Desktop/c programming/untitled1.py",
		"object_name": "Cube",
		"x": 1,
		"y":5,
		"z": 1,
		"Rx": 10,
		"Ry":20,
	    "Rz": 30
	},
	{ 

		"file_name": "C:/Java programming/untitled1.text",
		"object_name": "Sphere",
		"x": 123,
		"y":5112,
		"z": 23,
		"Rx": 810,
		"Ry":323,
		"Rz": 2
	}
]

j=json.dumps(data)

with open('Data to be stored into.json','w')as f:
	f.write(j)
	f.close()