"""empty message

Revision ID: 54c17052c8f4
Revises: d1a12773d8f3
Create Date: 2016-06-22 21:38:54.874481

"""

# revision identifiers, used by Alembic.
revision = '54c17052c8f4'
down_revision = 'd1a12773d8f3'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('match', sa.Column('team1_string', sa.String(length=32), nullable=True))
    op.add_column('match', sa.Column('team2_string', sa.String(length=32), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('match', 'team2_string')
    op.drop_column('match', 'team1_string')
    ### end Alembic commands ###