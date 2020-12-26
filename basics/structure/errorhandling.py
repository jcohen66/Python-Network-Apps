for i in range(5):
    try:
        print(i / 1)
    except NameError:
        print("You have a name error in your code.")
    except ZeroDivisionError as e:
        print(e, "--> Divistion by 0 is not allowed, sorry!")
    except ValueError:
        print("Wrong value!")
    except:
        print("Error")
    else:
        print("No exceptions rased by the try")
    finally:
        print("The rest of the code ...")

    try:
        print(4 / 0)
    except NameError:
        print("Name Error!")
    finally:
        print("I don't care, I'm getting printed either way!")

