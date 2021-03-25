import graphene

class Query(graphene.ObjectType):
    status = graphene.String()

    def resolve_status(root, info):
        return "status"

schema = graphene.Schema(query=Query)