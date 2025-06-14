f = open('test.txt','w')
f.write("Hello World!")
f.close()
print(open('test.txt').read())

f = open('test.txt','w+')
f.write("Good Morning")
f.seek(3)
print(f.read())
f.close

f = open('test.txt')
text=f.read()
print(text)
f.close()
