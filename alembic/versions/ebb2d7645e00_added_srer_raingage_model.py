"""Added SRER raingage model

Revision ID: ebb2d7645e00
Revises: f633e16dd3b1
Create Date: 2021-04-29 00:25:56.236933

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ebb2d7645e00'
down_revision = 'f633e16dd3b1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('srer_raingage',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('station_code', sa.String(length=25), nullable=True),
    sa.Column('current_station_name', sa.String(length=25), nullable=True),
    sa.Column('x_coord', sa.Integer(), nullable=True),
    sa.Column('y_coord', sa.Integer(), nullable=True),
    sa.Column('latitude', sa.Numeric(precision=15, scale=5), nullable=True),
    sa.Column('longitude', sa.Numeric(precision=15, scale=5), nullable=True),
    sa.Column('created', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_srer_raingage_id'), 'srer_raingage', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_srer_raingage_id'), table_name='srer_raingage')
    op.drop_table('srer_raingage')
    # ### end Alembic commands ###
