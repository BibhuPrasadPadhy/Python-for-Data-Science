def Greeting_Function(greeting,name):
    return '{} {}'.format(greeting,name)

print(Greeting_Function('Hi','Bibhu'))
print('*'*100)
##-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def Greeting_Function(greeting = 'Hi',name = 'Bibhu'):
    return '{} {}'.format(greeting,name)

print(Greeting_Function('Hi','Bibhu'))
print(Greeting_Function('Hi','Prasad'))
print(Greeting_Function('Hello','Prasad'))
print(Greeting_Function('Hiya','Prasad'))
print(Greeting_Function('Hello'))
print(Greeting_Function('Hiya'))
print(Greeting_Function(name='Hello'))
print(Greeting_Function(name='Hiya'))

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def Greeting_Function(*args,**kwargs):
    print(args)
    print(kwargs)
    for i in kwargs:
        print(i,':',kwargs[i])

print(Greeting_Function('Bibhu','Prasad','Padhy',occupation='Engineer',Company='Infosys'))

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def Greeting_Function(*args,**kwargs):
    print(args)
    print(kwargs)
    for i in kwargs:
        print(i,':',kwargs[i])

name = ['Bibhu','Prasad','Padhy']
info = {'occupation' :'Engineer','Company':'Infosys'}

print(Greeting_Function(*name,**info))

