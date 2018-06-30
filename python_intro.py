if 3 > 2:
    print('It works!')

def hi(name):
    if name == 'Larisa':
        print('Hey Larisa!')
    elif name =='Sonja':
        print('Hey Sonja!')
    else:
        print('Hey who are you?')

hi('George')

def hi(name):
    print('Hi ' + name + '!')

girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']
for name in girls:
    hi(name)
    print('Next girl')
