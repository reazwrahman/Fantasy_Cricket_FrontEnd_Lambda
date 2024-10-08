"""empty message

Revision ID: 1f3bcb65d637
Revises: 
Create Date: 2022-01-15 10:51:58.993185

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1f3bcb65d637'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('gameDetails',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('game_title', sa.String(), nullable=True),
    sa.Column('match_id', sa.BigInteger(), nullable=True),
    sa.Column('game_status', sa.String(), nullable=True),
    sa.Column('squad_link', sa.String(), nullable=True),
    sa.Column('scorecard_link', sa.String(), nullable=True),
    sa.Column('points_per_run', sa.Float(), nullable=True),
    sa.Column('points_per_wicket', sa.Float(), nullable=True),
    sa.Column('game_start_time', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('squad_link')
    )
    op.create_index(op.f('ix_gameDetails_match_id'), 'gameDetails', ['match_id'], unique=True)
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('default', sa.Boolean(), nullable=True),
    sa.Column('permissions', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_roles_default'), 'roles', ['default'], unique=False)
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('confirmed', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    op.create_table('selectedSquad',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('match_id', sa.BigInteger(), nullable=True),
    sa.Column('selected_squad', sa.String(), nullable=True),
    sa.Column('captain', sa.String(), nullable=True),
    sa.Column('vice_captain', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_selectedSquad_match_id'), 'selectedSquad', ['match_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_selectedSquad_match_id'), table_name='selectedSquad')
    op.drop_table('selectedSquad')
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_roles_default'), table_name='roles')
    op.drop_table('roles')
    op.drop_index(op.f('ix_gameDetails_match_id'), table_name='gameDetails')
    op.drop_table('gameDetails')
    # ### end Alembic commands ###
