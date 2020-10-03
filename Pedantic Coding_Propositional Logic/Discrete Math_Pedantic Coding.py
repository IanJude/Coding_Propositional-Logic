start_transaction = 'Cheese Burger Deluxe'.lower() # .lower() make the value to lowercase
add_ons1 = 'French Fries and Drinks'
add_ons2 = 'Sundae'
reply = 'Yes'.lower() # .lower()make the value to lowercase
reply1 = 'No'.lower() # .lower()make the value to lowercase
print('Menu:{} only'.format(start_transaction))
order = input('Enter your order: ') # Ask the user to input value
add4 = f'Here is your order {start_transaction}, {add_ons2} with receipt'
if order == start_transaction: # If the order is the same with the value of start_transaction, if not then else
    print(order)  # If equals to order print order
    print('Add ons: {}'.format(add_ons1)) #
    add = input('Add French Fries and Drinks?: ') # Ask input to the user if the user want to add fries (Yes/No)
    if add == reply: # If the user want to add fries
        if add == reply: # if the user answered yes
            add3 = input(f'Is this is really your order {start_transaction} with {add_ons1}?')
            if add3 == reply: # if the user answered yes
                print(f'Here is your order {start_transaction}, {add_ons1} with receipt')
                print('Thank You! We hope to see you again.')
            elif add3 == reply1: # If the user answered no
                    print(f'Here is your order {start_transaction}, {add_ons2} with receipt')
                    print('Thank You! We hope to see you again.')
    elif add == reply1: # If the user do not want to add fries
        print(f'Here is your order {start_transaction}, {add_ons2} with receipt')
        print('Thank You! We hope to see you again.')
else: # If the user do not want a cheese burger deluxe
    print('Order Again')



