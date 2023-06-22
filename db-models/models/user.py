from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class UserModel(models.Model):
    id = fields.IntField(pk=True)
    full_name = fields.TextField()
    email = fields.TextField()
    hashed_password = fields.TextField()

    def __str__(self):
        return self.full_name
        

UserSchema = pydantic_model_creator(UserModel)
