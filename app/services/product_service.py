from os import name

from app.extensions import db
from app.models.product import Product
from app.exceptions import ProductNotFoundError, ProductExistsError


class ProductService:

    @staticmethod
    def create_product(product_name, serial_number):
        if Product.query.filter_by(serial_number=serial_number).first():
            raise ProductExistsError("Product with this serial number already exists")

        product = Product(
            product_name=product_name,
            serial_number=serial_number,
            stock_quantity=0
        )

        db.session.add(product)
        db.session.commit()

        return product

    @staticmethod
    def get_all_products():
        return Product.query.all()

    @staticmethod
    def get_product(product_id):
        product = Product.query.get(product_id)
        if not product:
            raise ProductNotFoundError("Product not found")
        return product

    @staticmethod
    def update_product(product_id, product_name, serial_number):
        product = Product.query.get(product_id)
        if not product:
            raise ProductNotFoundError("Product not found")
        if Product.query.filter_by(serial_number=serial_number).first():
            raise ProductExistsError("Product with this serial number already exists")
        product.product_name = product_name
        product.serial_number = serial_number
        db.session.commit()
        return product

    @staticmethod
    def delete_product(product_id):
        product = Product.query.get(product_id)
        if not product:
            raise ProductNotFoundError("Product not found")

        db.session.delete(product)
        db.session.commit()
