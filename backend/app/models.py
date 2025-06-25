from datetime import datetime
from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from werkzeug.security import generate_password_hash, check_password_hash
from app import db

class Profile(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    daily_cost: so.Mapped[float] = so.mapped_column(sa.Float(2))
    daily_smokes: so.Mapped[int] = so.mapped_column(sa.Integer)

    users: so.WriteOnlyMapped['User'] = so.relationship(
        back_populates='user_profile')

    def __repr__(self):
        return '<Profile {}>'.format(self.users)


class User(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True,
                                                unique=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True,
                                             unique=True)
    quit_date: so.Mapped[datetime] = so.mapped_column(sa.DateTime)
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))
    profile_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(Profile.id),
                                                  index=True)

    user_profile: so.Mapped['Profile'] = so.relationship(
        back_populates='users')

    def __repr__(self):
        return '<{}, {}>'.format(self.username, self.quit_date)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)