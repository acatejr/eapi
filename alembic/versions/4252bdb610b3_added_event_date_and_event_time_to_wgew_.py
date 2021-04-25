"""Added event_date and event_time to wgew precip event model

Revision ID: 4252bdb610b3
Revises: 34fe8c5bea4c
Create Date: 2021-04-25 13:58:41.432065

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4252bdb610b3'
down_revision = '34fe8c5bea4c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('wgew_precipevent', sa.Column('event_date', sa.DateTime(timezone=True), nullable=True))
    op.add_column('wgew_precipevent', sa.Column('event_time', sa.Time(timezone=True), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('wgew_precipevent', 'event_time')
    op.drop_column('wgew_precipevent', 'event_date')
    # ### end Alembic commands ###