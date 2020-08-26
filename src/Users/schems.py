from .models import User, GlobalRole, Profile
from app import ma


class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User
        include_fk = True
