"""create attended_game

Revision ID: 01c0fcdeaa19
Revises: 016103da0466
Create Date: 2021-05-21 16:02:01.591575

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '01c0fcdeaa19'
down_revision = '016103da0466'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
    'attended_games',
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('user_id', sa.Integer),
    sa.Column('fixture_id', sa.Integer))

def downgrade():
    op.drop_table('attended_games')

