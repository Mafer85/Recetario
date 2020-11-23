import graphene
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from ingredientes.models import Ingrediente, Receta

class RecetaNode(DjangoObjectType):
    class Meta:
        model = Receta
        filter_fields =['titulo','preparacion','ingrediente']
        interfaces = (relay.Node,)

class IngredienteNode(DjangoObjectType):
    class Meta:
        model = Ingrediente
        filter_fields ={
        'nombre':['exact','icontains','istartswith'],
        'descripcion': ['exact','icontains'],
        }
        interfaces = (relay.Node, )

class Query(graphene.ObjectType):
    ingrediente = relay.Node.Field(IngredienteNode)
    all_ingredientes = DjangoFilterConnectionField(IngredienteNode)

    receta = relay.Node.Field(RecetaNode)
    all_recetas = DjangoFilterConnectionField(RecetaNode)
