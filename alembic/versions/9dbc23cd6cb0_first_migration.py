"""First migration

Revision ID: 9dbc23cd6cb0
Revises: 
Create Date: 2021-04-19 16:38:15.853410

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9dbc23cd6cb0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('raingages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_raingages_id'), 'raingages', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_raingages_id'), table_name='raingages')
    op.drop_table('raingages')
    # ### end Alembic commands ###