from cafe_functions import *
# welcoming Message

print('---------------------','Hi, Welcome to YOUR Cafe','---------------------')

while True:
    print("            Please choose from the Options below:", '\n', '\n')
    print("0 ----------------------------- Exit", '\n')
    print("1-------------------------------Main Menu", '\n')
    exit_input = (input())
    # to caste it to int we can put   if int(exit_input)== 0:
    if exit_input== '0':
        print('Goodbye')
        break
    elif exit_input=='1':
        while True:
            print('0 -------------------- Exit.', '\n')
            print('1 ------------ view the Menu.','\n')
            print('2 --------------add an Item.', '\n')
            print('3-------------update an Item.', '\n')
            print('4------------to delete an Item', '\n')
            owner_input = input()
           #    # to caste it to int we can put   if int(owner_input)== 0:

            if owner_input== '0':
                print('will see you again')
                new_list = []
                break
            elif owner_input == '1': 
                read_file=''
                read_text_file(read_file)
               
            elif owner_input=='2':
                print(' You can add new products to the List.','\n')
                print('Please enter new product, you wish to add to the menu.','\n')
                add_product = input()
                products =add_text_file(add_product)
                print( add_product +' added successfully:','\n' )
            
                read_text_file(products)

                

                            # updating a product

            elif owner_input == '3':
               update_text_file()
                
            # Delete a product
            elif owner_input == '4':
                 #function_delt()

                delete_item()
            else:
                print("Please make a valid choise")
                # print('Please Enter 0 to Exit ')
                # print('Please Enter 1 to view the Menu ')
                # print('Please Enter 2 to view the Menu ')
                # print('Please Enter 3 to update the Menu OR 0 to Exit')
                # print('Please Enter 4 to delete a product')
    else:
        print("Please Choose 0 to exit or 1 to View the menu")
