import os
from flask import Flask
from flask_graphql import GraphQLView
from schema import schema

server = Flask(__name__)
server.add_url_rule(
    "/graphql",
    view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True)
)

@server.route("/")
def hello():
    return "ok!"

if __name__ == "__main__":
    server.run(host='0.0.0.0', port=5000)
