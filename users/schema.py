from django.contrib.auth import get_user_model
from graphql import GraphQLError

import graphene
from graphene.types.structures import NonNull
from graphene_django import DjangoObjectType


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()
        # only_fields = ["id", "username", "password", "email"]
        # exclude = ["password"]


class Query(graphene.ObjectType):
    user = graphene.Field(UserType, username=graphene.String(required=True))
    me = graphene.Field(UserType)

    def resolve_me(self, info):
        user = info.context.user

        if not user.is_authenticated:
            raise GraphQLError("Not logged in")

        return user

    def resolve_user(self, info, username):
        user = info.context.user

        if not user.is_authenticated:
            raise GraphQLError("Not logged in")

        return get_user_model().objects.get(username=username)


class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)

    def mutate(self, info, username, password, email):
        User = get_user_model()

        user = info.context.user

        if not user.is_authenticated:
            raise GraphQLError("Not logged in")

        user = User.objects.create_user(
            username=username,
            password=password,
            email=email,
        )

        return CreateUser(user=user)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
