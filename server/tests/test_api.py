import pytest
from graphene.test import Client
from server import schema

# @pytest.fixture
# def client():
#     client = Client(schema)
#     return client

#     # db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
#     # flaskr.app.config['TESTING'] = True
#     # with flaskr.app.test_client() as client:
#     #     with flaskr.app.app_context():
#     #         flaskr.init_db()
#     #     yield client
#     # os.close(db_fd)
#     # os.unlink(flaskr.app.config['DATABASE'])

def test_api_status():
    """Test the api's status query.
    """
    client = Client(schema.schema)
    executed = client.execute('''{ status }''', context={})
    assert executed == {
        'data': {
            'status': 'ok'
        }
    }

