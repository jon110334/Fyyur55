"""empty message

Revision ID: 3488725c51a5
Revises: 62055d0f8ccf
Create Date: 2020-11-19 20:26:11.650215

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3488725c51a5'
down_revision = '62055d0f8ccf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Venue', sa.Column('seeking_description', sa.String(length=500), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Venue', 'seeking_description')
    # ### end Alembic commands ###
