def stack_me_high(num1) :
     if num1 == 0 | 10:
          return num1
    print ("current count :" ,num1)
    num1 += 1
    stack_me_high (num1)

def main ():
     num1 = stack_me_high (1)
     print("current count :",num1)

if__name__== "__main__":
    main()
