import uuid
from sqlalchemy.dialects.postgresql import UUID

from app.extensions import db

class Product(db.Model):
    __tablename__ = "product"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    product_name = db.Column(db.String(255), nullable=False)
    serial_number = db.Column(db.String(100), unique=True, nullable=False)
    stock_quantity = db.Column(db.Integer, nullable=False, default=0)

    def to_dict(self):
        return {
            "id": str(self.id),
            "product_name": self.product_name,
            "serial_number": self.serial_number,
            "stock_quantity": self.stock_quantity
        }
