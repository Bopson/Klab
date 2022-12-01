item = [ {'name': 'Bike', 'price':100}, 
{'name': 'TV', 'price':200}, {'name': 'Album', 'price':10}, 
{'name': 'Book', 'price':5}, {'name': 'Phone', 'price':500},
 {'name': 'Computer', 'price':1000}]

from operator import itemgetter
cheapSortedList = sorted(item, key=itemgetter('price')) 
print("The cheapest one is: ",cheapSortedList[0])
expensiveSortedList = sorted(item, key=itemgetter('price'), reverse=True) 
print("The most expensive one is: ",expensiveSortedList[0])

total = sum(d['price'] for d in item)

print("The full price of all products is: ",total)
item2=[i for i in item if not (i['price'] <= 10)]
new_total = sum(d['price'] for d in item2)
print("The full price of all products without those having a price less than 10 dollars: ",new_total)