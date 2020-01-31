'''Stock'''

FoodDict = {
    "bread": 65,
    "biscuits": 43,
    "pasta": 3
} 

DrinkDict = {
    "minerals": 40,
    "beer": 8,
    "water": 55
}

'''Method'''

def CheckStock(stock, item):
    for values in stock:
        if values == item:
              return stock[values]
                
'''Call'''

# print(FoodDict)
# print(DrinkDict)

itemToCheck = input("Enter Food Stock: ")
FoodStock = CheckStock(FoodDict, itemToCheck)
print(itemToCheck, FoodStock)
if FoodStock < 10:
    print("Order more " +itemToCheck+ "!")

itemToCheck = input("Enter Drink Stock: ")
DrinkStock = CheckStock(DrinkDict, itemToCheck)
print(itemToCheck, DrinkStock)
if DrinkStock < 10:
    print("Order more " +itemToCheck+ "!")