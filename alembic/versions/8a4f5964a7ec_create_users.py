"""create users

Revision ID: 8a4f5964a7ec
Revises: 
Create Date: 2021-05-21 16:01:02.187129

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8a4f5964a7ec'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
    'users',
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('email', sa.String, nullable=False, unique=True),
    sa.Column('name', sa.String),
    sa.Column('password', sa.String, nullable=False))


def downgrade():
    op.drop_table('users')
