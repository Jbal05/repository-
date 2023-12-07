def conversation ():
    print ("welcome to my conversation")
    print("do you like coding")

    answer = input ("answer yes or no"). lower()
    if answer == "yes":
        print("that's good")
    elif answer.lower() == "no":
        print("that sucks")
    else:
        print ("that's too bad!!")
    print("Thanks for talking with me")

def main():
    conversation()

if __name__ == "__main__":
    main()
