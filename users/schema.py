from django.contrib.auth import get_user_model
import sys

import graphene
from graphene.types.structures import NonNull
from graphene_django import DjangoObjectType
import graphene_django


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()
        # only_fields = ["id", "username", "password", "email"]
        # exclude = ["password"]


class Query(graphene.ObjectType):
    user = graphene.Field(UserType, id=graphene.ID(required=True))

    def resolve_user(self, info, id):
        return get_user_model().objects.get(id=id)


class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)
    ok = graphene.Boolean()
    message = graphene.String()

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)

    def mutate(self, info, username, password, email):
        User = get_user_model()

        try:
            user = User.objects.create_user(
                username=username, password=password, email=email
            )
            ok = True
            message = "Success: User created"
        except Exception as e:
            user = None
            ok = False
            message = "Error: User is not created"

        return CreateUser(user=user, ok=ok, message=message)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
