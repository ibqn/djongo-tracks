from users.schema import UserType
import graphene
from graphene_django import DjangoObjectType
from graphql import GraphQLError

from tracks.models import (
    Track,
    Like,
)


class TrackType(DjangoObjectType):
    class Meta:
        model = Track


class LikeType(DjangoObjectType):
    class Meta:
        model = Like


class Query(graphene.ObjectType):
    tracks = graphene.List(TrackType)
    likes = graphene.List(LikeType)

    def resolve_tracks(self, info):
        return Track.objects.all()

    def resolve_likes(self, info):
        return Like.objects.all()


class CreateTrack(graphene.Mutation):
    track = graphene.Field(TrackType)

    class Arguments:
        title = graphene.String()
        description = graphene.String()
        url = graphene.String()

    def mutate(self, info, title, description, url):
        user = info.context.user

        if not user.is_authenticated:
            raise GraphQLError("Not logged in")

        track = Track(
            title=title,
            description=description,
            url=url,
            posted_by=user,
        )
        track.save()

        return CreateTrack(track=track)


class UpdateTrack(graphene.Mutation):
    track = graphene.Field(TrackType)

    class Arguments:
        track_id = graphene.ID(required=True)
        title = graphene.String()
        description = graphene.String()
        url = graphene.String()

    def mutate(self, info, track_id, title, description, url):
        user = info.context.user

        if not user.is_authenticated:
            raise GraphQLError("Not logged in")

        track = Track.objects.get(id=track_id)

        if track.posted_by != user:
            raise GraphQLError("Not permitted to update this track")

        if title is not None:
            track.title = title

        if description is not None:
            track.description = description

        if url is not None:
            track.url = url

        track.save()

        return UpdateTrack(track=track)


class DeleteTrack(graphene.Mutation):
    track_id = graphene.ID()

    class Arguments:
        track_id = graphene.ID(required=True)

    def mutate(self, info, track_id):
        user = info.context.user

        if not user.is_authenticated:
            raise GraphQLError("Not logged in")

        track = Track.objects.get(id=track_id)

        if track.posted_by != user:
            raise GraphQLError("Not permitted to delete this track")

        track.delete()

        return DeleteTrack(track_id=track_id)


class CreateLike(graphene.Mutation):
    # user = graphene.Field(UserType)
    # track = graphene.Field(TrackType)
    like = graphene.Field(LikeType)

    class Arguments:
        track_id = graphene.ID(required=True)

    def mutate(self, info, track_id):
        user = info.context.user

        if not user.is_authenticated:
            raise GraphQLError("Not logged in")

        track = Track.objects.get(id=track_id)

        if track.posted_by != user:
            raise GraphQLError("Not permitted to delete this track")

        like = Like.objects.create(user=user, track=track)

        # return CreateLike(user=user, track=track)
        return CreateLike(like=like)


class Mutation(graphene.ObjectType):
    create_track = CreateTrack.Field()
    update_track = UpdateTrack.Field()
    delete_track = DeleteTrack.Field()
