# import re

inventory = {}

class InventoryManagement:
    """esta clase representa el inventario"""
    def __init__(self):
        """
        Inicializa los atributos
        Argumentos posicionales:
        product - str producto
        quantity - int cantidad de producto
        inventario - dir {product : quantity}
        """
        self._product = ""
        self._quantity = 0
        self._inventory = {}
        

    def add_product(self, product, quantity): # método agregar o actualizar producto y cantidad
        
        if f"{product}" in self._inventory:
            self._inventory[f"{product}"] = self._inventory[f"{product}"] + quantity
        else:
            self._inventory.update({f"{product}": quantity})

    def delete_product(self, product): # método eliminar o mensaje error
        self._inventory.pop(f"{product}", "Producto no encontrado para eliminar")

    def consult_product(self, product): # método consultar o mensaje error
        return self._inventory.get(product, "Producto no existe en el inventario")
        

    def mod_quantity(self, product, new_quantity):
        if f"{product}" in self._inventory:
            self._inventory[f"{product}"] = f"{new_quantity}"
        else:
            print(f"El producto <{product}> no existe en el inventario")
        

    def find_product(self, text):
    
        print("-- coincidencias --")

        for product_search, quantity_search in self._inventory.items():
            if text in product_search:
                print(f"{product_search} : {quantity_search}")
                
        print("------------------")

        

    def view_inventory(self, sort=False):
        if sort == False:
            print("--- INVENTARIO ---")
            for product_search, quantity_search in self._inventory.items():
                print(f"{product_search}: {quantity_search}")
            print("------------------")
        else:
            print("--- INVENTARIO ---")
            
            for product_search, quantity_search in sorted(self._inventory.items()):
                print(f"{product_search}: {quantity_search}")
            print("------------------")

tienda = InventoryManagement()
tienda.add_product("Manzanas", 10)
tienda.add_product("Peras", 5)
tienda.add_product("Manzanas", 5)
print("Consultar Manzanas:", tienda.consult_product("Manzanas"))
tienda.view_inventory()
tienda.delete_product("Peras")
print("Inventario después de eliminar Peras:")
tienda.view_inventory(False)

