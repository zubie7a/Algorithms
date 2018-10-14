# https://app.codesignal.com/company-challenges/verkada/T5wpQMsHxSr2X3ESy
class ProductManager:
    # Change this from list in original statement to hash because better.
    # For look up it was always iterating the list and that's not efficient.
    products = {}
    def createProduct(self, id, title):
        # Return False if the product id already exists.
        if id in self.products:
            return False
        # Otherwise just create product and store it.
        product = {}
        product['id'] = id
        product['title'] = title
        self.products[id] = product
        return True

    def updateProduct(self, id, title):
        # Return False if the product id doesn't exist.
        if id not in self.products:
            return False
        # Otherwise just update it's title in the stored record.
        product = self.products[id]
        product['title'] = title
        self.products[id] = product
        return True

    def deleteProduct(self, id):
        # Return False if the product id doesn't exist.
        if id not in self.products:
            return False
        # Otherwise just retrieve it and delete it's stored record.
        del self.products[id]
        return True

    def findProductById(self, id):
        # product or null
        if id in self.products:
            return self.products[id]
        return None

    def findProductByTitle(self, title):
        # product or null
        for product in self.products.values():
            if product['title'] == title:
                return product
        return None

product_manager = ProductManager()

import json
from collections import OrderedDict
'''
    Input Example:
        [["createProduct","10","Product_10"], 
         ["createProduct","10","Product_10"], 
         ["updateProduct","10","New_Product_10"], 
         ["deleteProduct","9"], 
         ["findProductById","9"], 
         ["findProductById","10"], 
         ["findProductByTitle","Product_10"], 
         ["findProductByTitle","New_Product_10"]]
'''
def productManagement(operations):
    # Calls corresponding methods of productManager based on the input
    ans = []
    for operation in operations:
        if operation[0] == 'createProduct':
            res = product_manager.createProduct(operation[1], operation[2])
            ans.append(json.dumps(res))
        if operation[0] == 'updateProduct':
            res = product_manager.updateProduct(operation[1], operation[2])
            ans.append(json.dumps(res))
        if operation[0] == 'deleteProduct':
            res = product_manager.deleteProduct(operation[1])
            ans.append(json.dumps(res))
        if operation[0] == 'findProductById':
            res = product_manager.findProductById(operation[1])
            if res == None:
                ans.append('null')
            else:
                ans.append(json.dumps(OrderedDict(res), separators=(',', ':')))
        if operation[0] == 'findProductByTitle':
            res = product_manager.findProductByTitle(operation[1])
            if res == None:
                ans.append('null')
            else:
                ans.append(json.dumps(OrderedDict(res), separators=(',', ':')))
    return ans
