from tortoise.fields import CharField

#from core.db import sql_connection
from datetime import datetime

from tortoise import fields
# from core.db import sql_connection
from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.fields import CharField
from tortoise.models import Model

#from devtools import debug

# from tortoise.contrib.pydantic import pydantic_model_creator, pydantic_queryset_creator
'''
def sql_table(con):
    cursorObj = con.cursor()

    cursorObj.execute(
        "CREATE TABLE User(email integer PRIMARY KEY, password text)")

    con.commit()


con = sql_connection()
sql_table(con)'''


class User(Model):
    # fields are null = False by default but i specified it for clarity
    id = fields.IntField(pk=True, index=True)
    username = fields.CharField(max_length=20, null=False, unique=True)
    email = fields.CharField(max_length=200, null=False, unique=True)
    password = fields.CharField(max_length=100, null=False)
    is_verified = fields.BooleanField(default=False)
    join_date = fields.DatetimeField(default=datetime.utcnow)

    def gall(self) -> tuple[CharField, CharField, CharField]:
        return self.username, self.email, self.password


class User_in_chat(Model):
    id = fields.IntField(pk=True, index=True)
    user_name = fields.CharField(max_length=20, nullable=False, unique=True)
    city = fields.CharField(max_length=100, null=False, default="Unspecified")
    region = fields.CharField(max_length=100, null=False, default="Unspecified")
    user_description = fields.TextField(null=True)
    #logo = fields.CharField(max_length=200, null=False, default="static.papi4.jpg")
    owner = fields.ForeignKeyField('models.User', related_name='user_ch')


# user_pydanticIn will be used to create users since it allows


# readOnly fields same for all the others
user_pydantic = pydantic_model_creator(User, name="User", exclude=("is_verified",))
user_pydanticIn = pydantic_model_creator(User, name="UserIn", exclude_readonly=True,
                                         exclude=("is_verified", 'join_date'))
user_pydanticOut = pydantic_model_creator(User, name="UserOut")

user_ch_pydantic = pydantic_model_creator(User_in_chat, name="User_in_chat")
user_ch_pydanticIn = pydantic_model_creator(User_in_chat, name="User_in_chatIn", exclude_readonly=True)

"""user = pydantic_model_creator(User)
user1 = pydantic_queryset_creator(User)

async def runn():
    print("aboba")
    await Tortoise.init(db_url="sqlite://mem", modules={"models": ["__main__"]})
    print("!@#$%^ ---- DB from tortoise: ")
    sql = get_schema_sql(Tortoise.get_connection("default"), safe=False)
    print(sql)
    print(await User.all().values("id", "username", "email", "password"))
   # await Tortoise.generate_schemas()
    date = datetime.utcnow
    #user = await User.create(username="2amogus", email="2amogus1337@mail.ru", password="12345")
    print("ass")
    #print(user_pydanticIn.dict(exlude_unset=True))
    print("!@#$%^ ---- DB from pydantic: ")
    #debug(User)
    user11 = await user1.from_queryset(User.all())
    print(user11.dict())

if __name__ == "__main__":
    run_async(runn())"""
