from typing import List

from ecommerce.products import models


async def gel_all_products(database) -> List[models.Product]:
    products = database.query(models.Product).all()
    return products


async def create_new_product(request, database) -> models.Product:
    new_product = models.Product(
        name=request.name,
        quantity=request.quantity,
        description=request.description,
        price=request.price,
        category_id=request.category_id
    )
    database.add(new_product)
    database.commit()
    database.refresh(new_product)
    return new_product


async def create_new_category(request, database) -> models.Category:
    new_category = models.Category(name=request.name)
    database.add(new_category)
    database.commit()
    database.refresh(new_category)

    return new_category
