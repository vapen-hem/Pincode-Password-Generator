from password_generator3 import run_password
from pin_generator import run_pincode

#Error = re-run the code
while True:
    #Asks the user if they want to create a pin or a password
    wdyw = input('Do you want to create a password, or a pincode? :')
    print('-----------------------')
    #Runs password file
    if wdyw == 'password':
        run_password()
        break
    #Runs pincode file
    elif wdyw == 'pincode':
        run_pincode()
        break
    elif wdyw == 'break':
        break
    #Error message
    else:
        print('You have to type (  password  ) or (  pincode  )')
        print('-----------------------')
    


