import graphene
import ingredientes.schema

class Query(ingredientes.schema.Query, graphene.ObjectType):
    pass

schema =graphene.Schema(query=Query)
