def pizza_making(size,*toppings):
    print("\nMaking a "+str(size)+"-inch pizza with the following toppings")
    for topping in toppings:
        print("-"+topping)