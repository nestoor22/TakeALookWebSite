import graphene

from lists.schema import AddShowToList, CreateList
from user.schema import SignIn, UserQuery, CreateUser, LogOut
from show.schema import ShowQuery, SetShowRate, DeleteShowRate
from boards.schema import BoardsQuery, CreateBoardMutation, SetLastVisitedBoard


class Query(BoardsQuery, ShowQuery, UserQuery):
    pass


class Mutation(graphene.ObjectType):
    sign_in = SignIn.Field()
    log_out = LogOut.Field()
    create_user = CreateUser.Field()
    create_board = CreateBoardMutation.Field()
    set_last_visited_board = SetLastVisitedBoard.Field()
    set_show_rate = SetShowRate.Field()
    delete_show_rate = DeleteShowRate.Field()
    create_list = CreateList.Field()
    add_show_to_list = AddShowToList.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
