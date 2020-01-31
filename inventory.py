inverntoryDict = {
    "balls": 5,
    "Cones": 10,
    "Jerseys": 23
} 

inverntoryDictFoxford = {
    "balls": 154,
    "Cones": 49865,
    "Jerseys": 154
} 

def FindStock(dict1, item):
    ''' This method finds the stock in the inventory
    params: dict = inventroyDict
            items =item to choose in dict
            return stock of the item
     '''
    for values in dict1:
        if values == item:
            return dict1[values]

itemToCheck = "Cones"
ballStock = FindStock(inverntoryDictFoxford, itemToCheck)
print(ballStock)