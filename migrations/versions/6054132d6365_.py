"""empty message

Revision ID: 6054132d6365
Revises: 
Create Date: 2023-10-23 21:58:02.426056

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6054132d6365'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reptiles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('common_name', sa.String(length=250), nullable=True),
    sa.Column('scientific_name', sa.String(length=250), nullable=True),
    sa.Column('native_habitat', sa.String(length=250), nullable=True),
    sa.Column('fun_fact', sa.Text(), nullable=True),
    sa.Column('conservation_status', sa.Enum('extinct', 'endangered', 'threatened', 'near_threatened', 'observed', 'accepted', name='conservationstatus'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reptiles')
    # ### end Alembic commands ###
