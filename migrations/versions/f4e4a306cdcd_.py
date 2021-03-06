"""empty message

Revision ID: f4e4a306cdcd
Revises: 8edb48444054
Create Date: 2021-05-11 17:41:52.068409

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'f4e4a306cdcd'
down_revision = '8edb48444054'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('professor', 'reg_professor',
               existing_type=sa.Integer(),
               type_=sa.BigInteger(),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('professor', 'reg_professor',
               existing_type=sa.BigInteger(),
               type_=sa.Integer(),
               existing_nullable=True)
    # ### end Alembic commands ###
