import graphene
import graphql_jwt

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
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
