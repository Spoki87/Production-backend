from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from app.services.product_service import ProductService
from app.utils.response import success_response, error_response
from app.exceptions import ProductNotFoundError, ProductExistsError

products_bp = Blueprint("product", __name__)

@products_bp.before_request
@jwt_required()
def require_jwt():
    pass

@products_bp.route("/products", methods=["POST"])
def create_product():
    data = request.json

    try:
        product = ProductService.create_product(
            product_name=data.get("product_name"),
            serial_number=data.get("serial_number"),
        )
    except ProductExistsError as e:
        return error_response(str(e), 409)

    return success_response(product.to_dict(), status=201)

@products_bp.route("/products", methods=["GET"])
def get_products():
    products = ProductService.get_all_products()
    return success_response([p.to_dict() for p in products])

@products_bp.route("/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    try:
        product = ProductService.get_product(product_id)
    except ProductNotFoundError as e:
        return error_response(str(e), 404)

    return success_response(product.to_dict())

@products_bp.route("/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    try:
        ProductService.delete_product(product_id)
    except ProductNotFoundError as e:
        return error_response(str(e), 404)

    return success_response(message="Product deleted")
