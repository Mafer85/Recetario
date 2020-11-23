import graphene
import ingredientes.schema

classQuery(ingredientes.schema.Query, graphene.ObjectType):
pass
    schema =graphene.Schema(query=Query)
