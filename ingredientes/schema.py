from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene:django.filter import DjangoFilterConnectionField

from ingredientes.models import Ingrediente, Receta

class IngredienteNode(DjangoObjectType):
    Class Meta:
        model = Ingrediente
        filter_fields =['nombre','descripcion']
        interfaces = (relay.Node,)

class RecetaNode(DjangoObjectType):
    class Meta:
        model = Receta
        filter_fields ={
        'titulo':['exact','icontains','istartswith'],
        'preparacion': ['exact','icontains'],
        'ingrediente':['exact'],
        'ingrediente_name':['exact']
        }interfaces=(relay.Node,)

class Query(graphene.ObjectType):
    ingrediente = relay.Node.Field(IngredienteNode)
    all_ingredientes = DjangoFilterConnectionField(IngredienteNode)

    receta = relay.Node.Field(RecetaNode)
    all_recetas = DjangoFilterConnectionField(RecetaNode)
