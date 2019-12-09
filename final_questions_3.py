def funcOne():
    lstNames = []
    userName = getName()
    lstNames.append(userName)
    return lstNames


def getName():
    go = True
    while go:
        userName = input("\nPlease type in your username:\n>>> ")
        if userName == '':
            print("\nUsernames must not be empty!")
        else:
            print("\nWelcome back {}!".format(userName).title())
            go = False
    return userName

if __name__ == "__main__":
    funcOne()
