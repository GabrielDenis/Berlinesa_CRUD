from peewee import *

# id(string 13, pk)
# sku(string 255, accept null)
# description(varchar 255)
# url.img(varchar 1024 url image)
# created_at(datetime/timestamp)
# price(numeric 8,2)
# name(varchar 90)

database = MySQLDatabase(
    'berlinesa_db',
    user='root',
    password='toor',
    host='localhost',
    port=3306
)

class Product(Model):
    id = CharField(max_length=13, primary_key=True)
    sku = CharField(max_length=256, null=True)
    description = CharField(max_length=256)
    url_img = CharField(max_length=1024)
    created_at = DateTimeField()
    price = FloatField()
    name = CharField(max_length=90)

    def __str__(self):
        return self.name

    class Meta:
        database = database
        table_name = 'products'