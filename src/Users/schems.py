from .models import User, GlobalRole, Profile
from app import ma


class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User
        include_fk = True

    id = ma.auto_field()
    username = ma.auto_field()
    email = ma.auto_field()
