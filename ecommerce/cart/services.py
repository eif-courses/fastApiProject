from ecommerce.cart.models import Cart, CartItems
from ecommerce.products.models import Product
from ecommerce.user.models import User


async def add_items(cart_id, product_id, database):
    cart_items = CartItems(cart_id=cart_id, product_id=product_id)
    database.add(cart_items)
    database.commit()
    database.refresh(cart_items)


async def add_to_cart(product_id, database):
    # Patikrinti ar yra produktas

    product_info = database.query(Product).get(product_id)

    if not product_id:
        pass
    # out of stock

    user_info = database.query(User).filter(User.email == "g@example.com").first()
    cart_info = database.query(Cart).filter(Cart.user_id == user_info.id).first()

    if not cart_info:
        new_cart = Cart(user_id=user_info.id)
        database.add(new_cart)
        database.commit()
        database.refresh(new_cart)
        await add_items(cart_info.id, product_info.id, database)
    else:
        await add_items(cart_info.id, product_info.id, database)

    return {"status": "Item added to cart"}
