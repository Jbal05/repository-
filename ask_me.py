def user_selection(num) :
    ans = input ("Enter selection")
    if ans == "q":
        return false
    returm true

def main () :
    run_me = true
    while run_me:
          run_me = user_selection ()

if __name__ == '__main__':
    main()
