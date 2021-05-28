"""create fixtures

Revision ID: 65475570a85d
Revises: 01c0fcdeaa19
Create Date: 2021-05-21 16:02:08.286569

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '65475570a85d'
down_revision = '01c0fcdeaa19'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
    'fixtures',
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('fixture_id', sa.Integer),
    sa.Column('date', sa.Date),
    sa.Column('awaygoals', sa.String),
    sa.Column('awayname', sa.String),
    sa.Column('awaylogo', sa.String),
    sa.Column('homegoals', sa.String),
    sa.Column('homename', sa.String),
    sa.Column('homelogo', sa.String))


def downgrade():
    op.drop_table('fixtures')
    

