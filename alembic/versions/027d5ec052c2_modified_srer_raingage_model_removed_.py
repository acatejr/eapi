"""Modified SRER raingage model, removed xcoord and ycoord fields

Revision ID: 027d5ec052c2
Revises: a85526ff71f7
Create Date: 2021-04-29 00:57:09.480028

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '027d5ec052c2'
down_revision = 'a85526ff71f7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('srer_raingage', 'x_coord')
    op.drop_column('srer_raingage', 'y_coord')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('srer_raingage', sa.Column('y_coord', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('srer_raingage', sa.Column('x_coord', sa.INTEGER(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###