import json

def input_for_variables(n,variable_name):

	for i in range(n):
		ele = input()
		variable_name.append(ele)


file_names = []
object_names = []
x = []
y = []
z = []
rx = []
ry = []
rz = []
data = {}
final_data = {}
variable_key = ['File name','Object name','x','y','z','rx','ry','rz']

number_of_elements = int(input('Provide the number of elements : '))

print ("Enter ",number_of_elements," File names : ")
input_for_variables(number_of_elements,file_names)

print ("Enter ",number_of_elements," Object names : ")
input_for_variables(number_of_elements,object_names)

print ("Enter ",number_of_elements," values for x : ")
input_for_variables(number_of_elements,x)

print ("Enter ",number_of_elements," values for y : ")
input_for_variables(number_of_elements,y)

print ("Enter ",number_of_elements," values for z : ")
input_for_variables(number_of_elements,z)

print ("Enter ",number_of_elements," values for rx : ")
input_for_variables(number_of_elements,rx)

print ("Enter ",number_of_elements," values for ry : ")
input_for_variables(number_of_elements,ry)

print ("Enter ",number_of_elements," values for rz : ")
input_for_variables(number_of_elements,rz)

for i in range(number_of_elements):
	variable_values = [file_names[i],object_names[i],x[i],y[i],z[i],rx[i],ry[i],rz[i]]
	data = dict(zip(variable_key,variable_values))
	final_data[i+1] = data

print(final_data)

j=json.dumps(final_data,indent = 6)

with open('Data to be stored into.json','w')as f:
	f.write(j)
	f.close()
