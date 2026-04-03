from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

def create_user(
    username: str,
    password: str = None,
    email: str = None,
    first_name: str = None,
    last_name: str = None
) -> models.Model:
    user = User.objects.create_user(
        username=username,
        password=password
    )

    if email:
        user.email = email
    if first_name:
        user.first_name = first_name
    if last_name:
        user.last_name = last_name

    if password:
        user.set_password(password)

    user.save()
    return user


def get_user(user_id: int) -> models.Model:
    return User.objects.get(id=user_id)


def update_user(
    user_id: int,
    username: str = None,
    password: str = None,
    email: str = None,
    first_name: str = None,
    last_name: str = None
) -> models.Model:
    user = get_user(id=user_id)

    if username:
        user.username = username
    if email:
        user.email = email
    if first_name:
        user.first_name = first_name
    if last_name:
        user.last_name = last_name
    if password:
        user.set_password(password)

    user.save()
    return user
