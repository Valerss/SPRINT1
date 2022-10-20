from calculator_val import Calculator

menu={'sum': 'arg1 and arg2', 'subtraction': 'arg1 and arg2', 'nroot': 'base and root'}
'''creating a dictionary with all calculator options. It will be called in the 
following function'''

def calc_gui ():
    '''In this function the user is guided through the calculator operations.
    the function is asking the user which operation to perform. In case of wrong
    input, the function presents the available operations and asks for new input '''
    print('please enter desired operation:')
    operation='true'

    while operation:
          operation=input()
          if operation in menu:
              print('ok, you selected '+operation+' please insert '+menu.get(operation))
              a= input()
              b= input()

              '''here we call the Calculator class from calculator_val module.
              The following 2 lines are an alternative method to invoke the
              Calculator functions. The other method was preferred due to its beauty'''
              #print('Calculator.'+operation+'('+a+','+b+')')
              #print(exec('Calculator.'+operation+'('+a+','+b+')'))

              obj = Calculator
              func = getattr(obj, operation)
              print(func(int(a), int(b)))

              print('please enter desired operation:')

          elif operation:
            print('this calculator cannot perform such operation')
            print('please choose between: '+str(menu.keys()))



