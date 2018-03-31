"""empty message

Revision ID: 1903f8551ebc
Revises: 234fdf965733
Create Date: 2018-03-24 20:43:03.109886

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1903f8551ebc'
down_revision = '234fdf965733'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('srer_raingages', sa.Column('created', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True))
    op.add_column('srer_raingages', sa.Column('latitude', sa.Numeric(precision=15, scale=5, decimal_return_scale=True), nullable=True))
    op.add_column('srer_raingages', sa.Column('longitude', sa.Numeric(precision=15, scale=5, decimal_return_scale=True), nullable=True))
    op.add_column('srer_raingages', sa.Column('updated', sa.DateTime(timezone=True), nullable=True))


def downgrade():
    op.drop_column('srer_raingages', 'updated')
    op.drop_column('srer_raingages', 'longitude')
    op.drop_column('srer_raingages', 'latitude')
    op.drop_column('srer_raingages', 'created')

