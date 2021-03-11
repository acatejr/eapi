from graphql.type.definition import (GraphQLArgument, GraphQLField,
                                     GraphQLNonNull, GraphQLObjectType)
from graphql.type.scalars import GraphQLString
from graphql.type.schema import GraphQLSchema


QueryRootType = GraphQLObjectType(
    name="QueryRoot",
    fields={
        "status": GraphQLField(
            type_=GraphQLString,
            resolve=lambda obj, inf,
        )
    }
)

MutationRootType = GraphQLObjectType(
    name="MutationRoot",
    fields={}
)

Schema = GraphQLSchema(QueryRootType, MutationRootType)