"""Add new columns for finished and cleaned

Revision ID: 60949d7a6054
Revises: 4f2b1efa0aaf
Create Date: 2023-09-21 20:36:06.899855

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '60949d7a6054'
down_revision = '4f2b1efa0aaf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('questions', sa.Column('finished', sa.Boolean(), nullable=True))
    op.add_column('questions', sa.Column('cleaned', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('questions', 'cleaned')
    op.drop_column('questions', 'finished')
    # ### end Alembic commands ###
