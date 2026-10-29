def create_order(customer_id, product_id, quantity):
    if quantity <= 0: raise ValueError("Quantity must be positive.")
    return {"customer_id": customer_id, "product_id": product_id, "quantity": quantity}
