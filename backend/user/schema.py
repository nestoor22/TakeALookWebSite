import graphene

from django.contrib.auth import authenticate, login, logout
from graphene_django import DjangoObjectType
from graphene.types import Field, List

from .models import User


class UserType(DjangoObjectType):
    class Meta:
        model = User


class UserInput(graphene.InputObjectType):
    first_name = graphene.String()
    last_name = graphene.String()
    email = graphene.String()
    password = graphene.String()
    bio = graphene.String()
    favorite_show = graphene.String()
    city = graphene.String()
    country = graphene.String()
    birthday = graphene.Date()


class UserQuery(graphene.ObjectType):
    user = Field(UserType)
    users = List(UserType)
    user_name = Field(UserType)

    @staticmethod
    def resolve_user(parent, info):
        user_id = info.context.session.get('_auth_user_id')
        if not user_id:
            raise Exception('User is not logged in')
        return User.objects.get(id=user_id)

    @staticmethod
    def resolve_users(parent, info):
        return User.objects.all()

    @staticmethod
    def resolve_user_name(parent, info):
        user_id = info.context.session.get('_auth_user_id')
        if not user_id:
            return None

        return User.objects.get(id=user_id)


class CreateUser(graphene.Mutation):
    id = graphene.Int()

    class Arguments:
        user = UserInput(required=True)

    @staticmethod
    def mutate(parent, info, **kwargs):
        user_info = kwargs.get('user')
        password = user_info.pop('password')
        user = User.objects.create(**user_info)
        user.set_password(password)
        user.save()
        return CreateUser(id=user.id)


class SignIn(graphene.Mutation):
    id = graphene.Int()
    first_name = graphene.String()
    last_name = graphene.String()
    email = graphene.String()

    class Arguments:
        email = graphene.String()
        password = graphene.String()

    @staticmethod
    def mutate(parent, info, **kwargs):
        user = authenticate(
            username=kwargs.get('email'), password=kwargs.get('password')
        )

        if not user:
            raise Exception('Incorrect credentials')

        login(info.context, user)
        return SignIn(
            id=user.id,
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
        )


class LogOut(graphene.Mutation):
    ok = graphene.Boolean()

    @staticmethod
    def mutate(parent, info):
        logout(info.context)
        return LogOut(ok=True)
