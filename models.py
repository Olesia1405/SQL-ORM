import sqlalchemy
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Publisher(Base):
    __tablename__ = "publisher"

    id_publisher = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    publisher_name = sqlalchemy.Column(sqlalchemy.String(length=100), nullable=False, unique=True)

    def __str__(self):
        return f'Publisher {self.id_publisher} : {self.publisher_name}'


class Book(Base):
    __tablename__ = "book"

    id_book = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    book_title = sqlalchemy.Column(sqlalchemy.String(length=100), nullable=False)
    id_publisher = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("publisher.id_publisher"), nullable=False)
    publisher = relationship(Publisher, backref="books")

    def __str__(self):
        return f'Book {self.id_book} : ({self.book_title}, {self.id_publisher})'


class Shop(Base):
    __tablename__ = "shop"

    id_shop = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    shop_name = sqlalchemy.Column(sqlalchemy.String(length=100), nullable=False)

    def __str__(self):
        return f'Shop {self.id_shop} : ({self.shop_name})'


class Stock(Base):
    __tablename__ = "stock"

    id_stock = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    stock_count = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    id_book = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("book.id_book"), nullable=False)
    id_shop = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("shop.id_shop"), nullable=False)
    book = relationship(Book, backref="stocks")
    shop = relationship(Shop, backref="stocks")

    def __str__(self):
        return f'Stock {self.id_stock} : ({self.stock_count}, {self.id_book}, {self.id_shop})'


class Sale(Base):
    __tablename__ = "sale"

    id_sale = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    sale_price = sqlalchemy.Column(sqlalchemy.Numeric, nullable=False)
    sale_date = sqlalchemy.Column(sqlalchemy.DateTime, nullable=False)
    sale_count = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    id_stock = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("stock.id_stock"), nullable=False)
    stock = relationship(Stock, backref="sales")

    def __str__(self):
        return f'Sale {self.id_sale} : ({self.sale_price}, {self.sale_date}, {self.sale_count}, {self.id_stock})'
