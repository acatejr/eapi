"""Adjusted watershed_id to int in wgew raingage model

Revision ID: df72420ae702
Revises: a8834437c8f1
Create Date: 2021-04-25 14:14:55.066796

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'df72420ae702'
down_revision = 'a8834437c8f1'
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    pass
