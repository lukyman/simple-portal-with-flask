"""empty message

Revision ID: f28113b4045e
Revises: 01cc5bf33c95
Create Date: 2018-05-09 14:59:22.155569

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'f28113b4045e'
down_revision = '01cc5bf33c95'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('portal_user', sa.Column('fullname', sa.String(length=120), nullable=False))
    op.drop_column('portal_user', 'firstname')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('portal_user', sa.Column('firstname', mysql.VARCHAR(length=120), nullable=False))
    op.drop_column('portal_user', 'fullname')
    # ### end Alembic commands ###
