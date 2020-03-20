from sqlalchemy import Column, ForeignKey, Integer, String, ForeignKeyConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.orm.collections import attribute_mapped_collection

from .base import Base

__ALL__ = ["EntityAttribute", "Entity", "EntityAttributeValue"]


class Entity(Base):
    __tablename__ = "entity"

    id = Column(Integer, primary_key=True, autoincrement=True)
    type_ = Column(String(50), primary_key=True)

    attributes = relationship(
        "EntityAttributeValue",
        collection_class=attribute_mapped_collection("attribute_id"),
        cascade="all, delete-orphan",
    )

    __mapper_args__ = {"polymorphic_identity": "entity", "polymorphic_on": type_}


class EntityAttribute(Base):
    __tablename__ = "entity_attribute"

    id = Column(String(50), primary_key=True)
    name = Column(String(50), nullable=False)


class EntityAttributeValue(Base):
    __tablename__ = "entity_attribute_value"

    entity_id = Column(Integer, primary_key=True)
    entity_type = Column(String(50), primary_key=True)
    attribute_id = Column(String(50), primary_key=True)
    value = Column(String(50), nullable=False)

    __table_args__ = (
        ForeignKeyConstraint([entity_id, entity_type], [Entity.id, Entity.type_]),
        {},
    )
