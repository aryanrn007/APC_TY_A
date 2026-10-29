from ecommerce.products.catalog import get_product
from ecommerce.products.inventory import available_stock
from ecommerce.customers.records import get_customer
from ecommerce.orders.order import create_order
from ecommerce.orders.summary import order_total
from ecommerce.payments.payment import make_payment
from ecommerce.payments.invoice import create_invoice

customer_id, product_id, quantity = 101, 1, 2
product = get_product(product_id)
print("Customer:", get_customer(customer_id))
print("Product:", product)
print("Available stock:", available_stock(product_id))
order = create_order(customer_id, product_id, quantity)
amount = order_total(product, quantity)
payment = make_payment(amount, "UPI")
invoice = create_invoice("ORD001", amount)
print("Order:", order)
print("Payment:", payment)
print("Invoice:", invoice)
