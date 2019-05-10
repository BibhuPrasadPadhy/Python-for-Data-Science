messageVar = 'Hello World,I am doing good :)'

print('*'*100)
print('Python Strings testing')
print('*'*100)
print(messageVar.upper())
print(messageVar.lower())
print(messageVar.count('o'))
print(messageVar.count('z'))
print(messageVar.index('o'))
# print(messageVar.index('z')) Throws an error not -1
print(messageVar.find('God'))
print(messageVar.find('doing'))
print(messageVar.rfind('doing'))
print(messageVar.replace('World','Universe'))

print('*'*100)
print('Python Strings Concatenation')
print('*'*100)


GreetingMessage = 'Hello'
Name = 'Michael'

print('Greeting:')
print(GreetingMessage,Name)
print(GreetingMessage+Name)

print('*'*100)
print('String Formatting')
print('*'*100)

Greeting = 'Hello'
Name = 'Michael'

print('{} {} , Welcome to our stream'.format(Greeting,Name))

print('*'*100)
print('String Formatting using F Strings')
print('*'*100)

message = f'{Greeting} {Name} ,Welcome to our stream'
print(message)

