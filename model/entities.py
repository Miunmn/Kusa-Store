from sqlalchemy import Column, Integer, Float, String, Sequence, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import connector

class User(connector.Manager.Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    email = Column(String(50))
    name = Column(String(30))
    fullname = Column(String(30))
    username = Column(String(12))
    password = Column(String(15))

'''class Message(connector.Manager.Base):
    __tablename__ = 'messages'
    id = Column(Integer, Sequence('message_id_seq'), primary_key=True)
    content = Column(String(500))
    sent_on = Column(DateTime(timezone=True))
    user_from_id = Column(Integer, ForeignKey('users.id'))
    user_to_id = Column(Integer, ForeignKey('users.id'))
    user_from = relationship(User, foreign_keys=[user_from_id])
    user_to = relationship(User, foreign_keys=[user_to_id])'''

class Producto(connector.Manager.Base):
    __tablename__ = 'producto'
    id = Column(Integer, Sequence(name = 'producto_id_seq', start=101), primary_key=True)
    categoria = Column(String(50))
    nombre = Column(String(50))
    descripcion = Column(String(50))
    precio = Column(Float)
    #vista = Column(String(500))
    
