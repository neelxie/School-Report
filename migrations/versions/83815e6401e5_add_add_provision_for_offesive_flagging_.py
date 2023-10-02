"""Add add provision for offesive flagging field for answers

Revision ID: 83815e6401e5
Revises: e018d0a634ed
Create Date: 2023-10-02 05:02:40.517941

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '83815e6401e5'
down_revision = 'e018d0a634ed'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('answers', sa.Column('offensive', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('answers', 'offensive')
    # ### end Alembic commands ###
