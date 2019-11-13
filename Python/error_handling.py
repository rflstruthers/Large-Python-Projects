
def getInfo():
    var1 = input('\nPlease provide the first numeric value: ')
    var2 = input('\nPlease provide the second numeric value: ')
    return var1,var2


def compute():
    go = True
    while go:
        var1,var2 = getInfo()
        try: #try this block of code
            var3 = int(var1) + int(var2)
            go = False #if no error, exit while loop
        except ValueError as e: #if there is a ValueError, run this block of code and print origional error message
            print('{}: \n\nYou did not provide a numeric value!'.format(e))
        except: #if there is any other kind of error, run this block of code
            print('\n\nOops, you provided invalid input!')
    print('{} + {} = {}'.format(var1,var2,var3))
    








if __name__ == '__main__':
    compute()
