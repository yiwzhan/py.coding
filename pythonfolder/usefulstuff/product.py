lis1=[]
def list_product(list):
    product = 1
    for i in list:
        u=int(i)
        product = product * u
    return product

product_result = list_product(lis1)
print(product_result)