import graphene
from graphene_django import DjangoObjectType

from tracks.models import Track


class TrackType(DjangoObjectType):
    class Meta:
        model = Track


class Query(graphene.ObjectType):
    tracks = graphene.List(TrackType)

    def resolve_tracks(self, info):
        return Track.objects.all()


class CreateTrack(graphene.Mutation):
    track = graphene.Field(TrackType)

    class Arguments:
        title = graphene.String()
        description = graphene.String()
        url = graphene.String()

    def mutate(self, info, title, description, url):
        user = info.context.user

        if not user.is_authenticated:
            raise Exception("Not logged in")

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
            raise Exception("Not logged in")

        track = Track.objects.get(id=track_id)

        if track.posted_by != user:
            raise Exception("Not permitted to update this track")

        if title is not None:
            track.title = title

        if description is not None:
            track.description = description

        if url is not None:
            track.url = url

        track.save()

        return UpdateTrack(track=track)


class Mutation(graphene.ObjectType):
    create_track = CreateTrack.Field()
    update_track = UpdateTrack.Field()
