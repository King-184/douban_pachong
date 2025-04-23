from peewee import *
db = SqliteDatabase("movie.db")
# db = MySQLDatabase("spider", host="localhost", port=3306, user="root", passwd="root")
# 表结构实体
class Movie(Model):
    title = CharField(max_length=20)
    rating_num = FloatField()
    comment_num = TextField()
    class Meta:
        database = db  # This model use the "people.db" database
        table_name = 'douban_movie'
# 保存数据函数
def save_data():
    db.create_tables([Movie])
    movie = Movie(title=title, rating_num=rating_num, comment_num=comment_num)
    movie.save()