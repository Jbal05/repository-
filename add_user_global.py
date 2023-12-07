var = 42
def ask_me() :
     num = int(input("enter number"))
     return(num)

def add_global(num) :
    global var
    var = var + num
    return(var )

def main() :
    global var
    number1 - ask me ()
    number2 - ask me ()
    sum +- add global (ask_me())
    sum +- add_global (ask_me())
    sum +- add_global (var)
    print("sum:", sum)
    print("global:", var)

if __name__ == '__main__':
    main()
