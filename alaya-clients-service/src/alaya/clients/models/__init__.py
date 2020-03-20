from sqlalchemy import Column, Integer, String, Enum
import enum
from .base import Base
from .eav import *


class Contact(Entity):
    __tablename__ = "contact"

    id = Column(Integer, ForeignKey("entity.id"), primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    phone_number = Column(String(50), nullable=False)

    __mapper_args__ = {
        "polymorphic_identity": "contact",
    }


# class Address(Entity):
#     __tablename__ = "address"
#
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     address_line_1 = Column(String, nullable=False)
#     address_line_1 = Column(String, nullable=True)
#     city = Column(String, nullable=False)
#     state = Column(String, nullable=False)
#     country = Column(String, nullable=False)
#
#
# class ContactAddress(Base):
#     class AddressType(enum):
#         SHIPPING = 'shipping'
#         BILLING = 'billing'
#         MAILING = 'mailing'
#
#     contact_id = Column(Integer, ForeignKey("contact.id"))
#     address_id = Column(Integer, ForeignKey("address.id"))
#     address_type = Column(Enum(AddressType), required=True)
