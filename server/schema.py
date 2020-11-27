from datetime import datetime
import graphene
from graphene import relay

class Query(graphene.ObjectType):
    node = relay.Node.Field()
    status = graphene.String(description='API status')

    def resolve_status(self, info):
        """Displays simple api status message.
        """
        now = datetime.now()
        return '{}'.format(now.strftime('%I:%H:%S - %m.%d.%Y'))

schema = graphene.Schema(query=Query)
