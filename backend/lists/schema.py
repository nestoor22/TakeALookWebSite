import graphene

from graphene_django import DjangoObjectType

from .models import ShowsList, ListShowRelation
from boards.models import BoardLists


class ShowsListRelationType(DjangoObjectType):
    class Meta:
        model = ListShowRelation


class ShowsListType(DjangoObjectType):
    class Meta:
        model = ShowsList

    shows_on_list = graphene.List(ShowsListRelationType)

    @staticmethod
    def resolve_shows_on_list(parent, info):
        return ListShowRelation.objects.filter(list_id=parent.id)


class CreateList(graphene.Mutation):
    id = graphene.Int()

    class Arguments:
        list_name = graphene.String()
        board_id = graphene.Int()

    @staticmethod
    def mutate(parent, info, list_name, board_id):
        user_id = info.context.session.get('_auth_user_id')
        list_instance = ShowsList.objects.create(name=list_name, owner_id=user_id)
        BoardLists.objects.create(board_id=board_id, list_id=list_instance.id)

        return CreateList(id=list_instance.id)


class AddShowToList(graphene.Mutation):
    id = graphene.Int()

    class Arguments:
        list_id = graphene.Int()
        show_id = graphene.Int()

    @staticmethod
    def mutate(parent, info, list_id, show_id):
        show_on_list_instance = ListShowRelation.objects.create(
            list_id=list_id, show_id=show_id
        )
        return AddShowToList(id=show_on_list_instance.id)


class ShowsListsQuery(graphene.ObjectType):
    shows_list = graphene.List(ShowsListType)

    @staticmethod
    def resolve_shows_list(parent, info):
        user_id = info.context.session.get('_auth_user_id')
        return ShowsList.objects.filter(owner_id=user_id)
