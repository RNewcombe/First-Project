#Stock
FoodDict = {
    "Bread": 65,
    "Biscuits": 43,
    "Pasta": 31
} 

DrinkDict = {
    "Minerals": 40,
    "Beer": 18,
    "Water": 55
}
#Method
def CheckStock(stock, item):
    for values in stock:
        if values == item:
            return stock[values]
#Call
itemToCheck = "Pasta"
FoodStock = CheckStock(FoodDict, itemToCheck)
print(FoodStock)

itemToCheck = "Beer"
DrinkStock = CheckStock(DrinkDict, itemToCheck)
print(DrinkStock)