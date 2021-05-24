"""create players

Revision ID: 016103da0466
Revises: 8a4f5964a7ec
Create Date: 2021-05-21 16:01:53.233662

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '016103da0466'
down_revision = '8a4f5964a7ec'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
    'players',
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('name', sa.String, nullable=False, unique=True),
    sa.Column('number', sa.Integer),
    sa.Column('age', sa.Integer),
    sa.Column('position', sa.String),
    sa.Column('nationality', sa.String),
    )


def downgrade():
    op.drop_table('players')
    
