"""Adding wgew and srer models

Revision ID: 657e446e66fd
Revises: 8983d881617f
Create Date: 2021-05-14 23:47:09.016250

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '657e446e66fd'
down_revision = '8983d881617f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('srer_raingage',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('station_code', sa.String(length=25), nullable=True),
    sa.Column('current_station_name', sa.String(length=25), nullable=True),
    sa.Column('latitude', sa.Numeric(precision=15, scale=5), nullable=True),
    sa.Column('longitude', sa.Numeric(precision=15, scale=5), nullable=True),
    sa.Column('created', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_srer_raingage_id'), 'srer_raingage', ['id'], unique=False)
    op.create_table('wgew_raingage',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('watershed_id', sa.Integer(), nullable=True),
    sa.Column('gage_id', sa.Integer(), nullable=True),
    sa.Column('east', sa.Integer(), nullable=True),
    sa.Column('north', sa.Integer(), nullable=True),
    sa.Column('latitude', sa.Numeric(precision=15, scale=5), nullable=True),
    sa.Column('longitude', sa.Numeric(precision=15, scale=5), nullable=True),
    sa.Column('elevation', sa.Integer(), nullable=True),
    sa.Column('err', sa.Numeric(precision=5, scale=1), nullable=True),
    sa.Column('created', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_wgew_raingage_id'), 'wgew_raingage', ['id'], unique=False)
    op.create_table('srer_precipevent',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.Column('month', sa.Integer(), nullable=True),
    sa.Column('precip', sa.Numeric(precision=15, scale=5), nullable=True),
    sa.Column('created', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated', sa.DateTime(timezone=True), nullable=True),
    sa.Column('raingage_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['raingage_id'], ['srer_raingage.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_srer_precipevent_id'), 'srer_precipevent', ['id'], unique=False)
    op.create_table('wgew_precipevent',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('event_date', sa.DateTime(timezone=True), nullable=True),
    sa.Column('event_time', sa.Time(timezone=True), nullable=True),
    sa.Column('duration', sa.Numeric(precision=15, scale=5), nullable=True),
    sa.Column('depth', sa.Numeric(precision=15, scale=5), nullable=True),
    sa.Column('time_est', sa.String(length=2), nullable=True),
    sa.Column('created', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated', sa.DateTime(timezone=True), nullable=True),
    sa.Column('raingage_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['raingage_id'], ['wgew_raingage.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_wgew_precipevent_id'), 'wgew_precipevent', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_wgew_precipevent_id'), table_name='wgew_precipevent')
    op.drop_table('wgew_precipevent')
    op.drop_index(op.f('ix_srer_precipevent_id'), table_name='srer_precipevent')
    op.drop_table('srer_precipevent')
    op.drop_index(op.f('ix_wgew_raingage_id'), table_name='wgew_raingage')
    op.drop_table('wgew_raingage')
    op.drop_index(op.f('ix_srer_raingage_id'), table_name='srer_raingage')
    op.drop_table('srer_raingage')
    # ### end Alembic commands ###
