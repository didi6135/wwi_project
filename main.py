from flask import Flask
from flask_graphql import GraphQLView
from graphene import Schema


app = Flask(__name__)
# schema = Schema(query=Query, mutation=Mutation)

# app.add_url_rule(
#     '/graphql',
#     view_func=GraphQLView.as_view(
# 'graphql',
#         schema=schema,
#         graphiql=True
#     )
# )

if __name__ == '__main__':
    # init_db()
    app.run()