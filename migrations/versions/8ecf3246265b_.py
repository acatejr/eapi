"""empty message

Revision ID: 8ecf3246265b
Revises: 1903f8551ebc
Create Date: 2018-03-24 21:07:31.006225

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8ecf3246265b'
down_revision = '1903f8551ebc'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('srer_precipevents',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('raingage_id', sa.Integer(), nullable=True),
        sa.Column('year', sa.Integer(), nullable=True),
        sa.Column('month', sa.Integer(), nullable=True),
        sa.Column('precip', sa.Numeric(precision=15, scale=5, decimal_return_scale=True), nullable=True),
        sa.Column('created', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
        sa.Column('updated', sa.DateTime(timezone=True), nullable=True),
        sa.ForeignKeyConstraint(['raingage_id'], ['srer_raingages.id'], ),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('srer_precipevents')

