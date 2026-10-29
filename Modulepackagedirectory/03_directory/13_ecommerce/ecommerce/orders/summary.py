def order_total(product, quantity):
    if product is None: raise ValueError("Product not found.")
    return product["price"] * quantity
