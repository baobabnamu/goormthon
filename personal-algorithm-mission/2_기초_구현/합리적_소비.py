N = int(input())
products = {}
for _ in range(N):
	productName, productPrice = input().split()
	productPrice = int(productPrice)
	products[productName] = productPrice
	
min_product = min(products, key=lambda x: products[x])
max_product = max(products, key=lambda x: products[x])

print(max_product, products.get(max_product))
print(min_product, products.get(min_product))