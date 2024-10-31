from flask import Flask
from flask_graphql import GraphQLView
from graphene import Schema

from app.db.database import check_and_initialize_missions
from app.gql.mutation import Mutation
from app.gql.query import Query



app = Flask(__name__)
schema = Schema(query=Query, mutation=Mutation)

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
'graphql',
        schema=schema,
        graphiql=True
    )
)

if __name__ == '__main__':
    # check_and_initialize_missions()
    app.run(host="0.0.0.0", port=5000)
