from flask import Flask
from flask_graphql import GraphQLView
from graphene import ObjectType, String, Schema
class Query(ObjectType):
    status = String(description="status")
    def resolve_status(self, args, context, info):
        return "status"

def create_app():
    app = Flask(__name__)

    from app.server import bp as server_bp
    app.register_blueprint(server_bp)

    app.add_url_rule(
        "/graphql",
        view_func=GraphQLView.as_view("graphql", schema=Schema(query=Query))
    )

    return app
