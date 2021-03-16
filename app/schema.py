import graphene
from tracks.schema import (
    Query as TrackQuery,
    Mutation as TrackMutation,
)

from users.schema import (
    Query as UserQuery,
    Mutation as UserMutation,
)


class Query(TrackQuery, UserQuery, graphene.ObjectType):
    pass


class Mutation(TrackMutation, UserMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
