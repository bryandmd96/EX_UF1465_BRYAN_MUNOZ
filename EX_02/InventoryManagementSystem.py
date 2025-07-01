import re

inventory = {}

class InventoryManagement:
    """esta clase representa el inventario"""
    def __init__(self, product, quantity):
        """
        Inicializa los atributos
        Argumentos posicionales:
        product - str producto
        quantity - int cantidad de producto
        inventario - dir {product : quantity}
        """
        _product = product
        _quantity = quantity
        

    def add_product(self, product, quantity): # método agregar o actualizar producto y cantidad
        if f"{product}" in inventory:
            inventory[f"{product}"] = quantity
        else:
            inventory.update({f"{product}": quantity})

    def delete_product(self, product): # método eliminar o mensaje error
        inventory.pop(f"{product}", "Producto no encontrado para eliminar")

    def consult_product(self, product): # método consultar o mensaje error
        inventory.get(f"{product}", "Producto no existe en el inventario")

    def mod_quantity(self, product, new_quantity):
        if f"{product}" in inventory:
            inventory[f"{product}"] = f"{new_quantity}"
        else:
            print(f"El producto <{product}> no existe en el inventario")
        

    def find_product(self, text):
        text_search = r"text.*"
        resultados = {}
        for product_search, quantity_search in inventory.items():
            if re.search(text, product_search):
                resultados[product_search] = quantity_search
        return resultados
        

    def view_inventory(self, sort=False):
        order_items = sorted(inventory.items())
        for product_search, quantiy_search in order_items:
            print(f"{product_search}: {quantiy_search}")

tienda = InventoryManagement()
