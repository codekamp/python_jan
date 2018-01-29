some_var = 'some random value'
another_var = 99

def abc():
    something()

def something():
    print('value of world module is', __name__)



if __name__ == '__main__':
    print('I am running as script')
else:
    print('I am running as module')