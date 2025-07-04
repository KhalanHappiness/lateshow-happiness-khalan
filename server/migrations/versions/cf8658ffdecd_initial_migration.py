"""Initial migration

Revision ID: cf8658ffdecd
Revises: 
Create Date: 2025-06-23 20:54:15.661292

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cf8658ffdecd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('episodes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.String(), nullable=True),
    sa.Column('number', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('guests',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('occupation', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('appearances',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('rating', sa.Integer(), nullable=True),
    sa.Column('episode_id', sa.Integer(), nullable=False),
    sa.Column('guest_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['episode_id'], ['episodes.id'], name=op.f('fk_appearances_episode_id_episodes')),
    sa.ForeignKeyConstraint(['guest_id'], ['guests.id'], name=op.f('fk_appearances_guest_id_guests')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('appearances')
    op.drop_table('guests')
    op.drop_table('episodes')
    # ### end Alembic commands ###
