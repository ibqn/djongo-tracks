import graphene
from tracks.schema import Query as TracksQuery


class Query(TracksQuery, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
