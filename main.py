import sqlalchemy
from sqlalchemy.orm import sessionmaker
from create_tables import create_tables
from models import Publisher, Book, Shop, Stock, Sale

DSN = "postgresql://postgres:postgres@localhost:5432/Home_Work6"
engine = sqlalchemy.create_engine(DSN)

# Создаем таблицы
create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()


def get_shops(publisher_input):
    query = session.query(Book.book_title, Shop.shop_name, Sale.sale_price, Sale.sale_date) \
        .select_from(Shop) \
        .join(Stock) \
        .join(Book) \
        .join(Publisher) \
        .join(Sale)

    if publisher_input.isdigit():
        result = query.filter(Publisher.id_publisher == int(publisher_input)).all()
    else:
        result = query.filter(Publisher.publisher_name == publisher_input).all()

    for book_title, shop_name, sale_price, sale_date in result:
        print(f"{book_title: <40} | {shop_name: <10} | {sale_price: <8} | {sale_date.strftime('%d-%m-%Y')}")


if __name__ == '__main__':
    publisher_input = input("Введите имя или ID издателя: ")
    get_shops(publisher_input)

session.close()
