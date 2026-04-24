
due = 50
accepted = [25, 10, 5]




while due > 0:                  #while "due" is more than 0 ask for more money
    print(f"amount due: {due}")
    coin = int(input("insert coin "))  #make input an integer


    if coin in accepted:        #checks if input is in the accepted list
        due -= coin             #due = due - coing

print(f"change owed: {abs(due)}")
25