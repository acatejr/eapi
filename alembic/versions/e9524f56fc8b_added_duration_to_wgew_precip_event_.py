"""Added duration to wgew precip event model

Revision ID: e9524f56fc8b
Revises: 4252bdb610b3
Create Date: 2021-04-25 14:00:07.714363

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e9524f56fc8b'
down_revision = '4252bdb610b3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('wgew_precipevent', sa.Column('duration', sa.Numeric(precision=15, scale=5), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('wgew_precipevent', 'duration')
    # ### end Alembic commands ###