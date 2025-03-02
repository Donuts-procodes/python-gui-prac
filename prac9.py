with open('file.txt','r') as f:
    print(f.read())
    
file_name='file.txt'
old_part='helloworld'
new_part='HELLO WORLD'

with open('file.txt','r') as f:
	data=f.read()

data=data.replace(old_part, new_part,1)

with open('file.txt','w') as f:
    f.write(data)
    
with open('file.txt','r') as f:
    print(f.read())