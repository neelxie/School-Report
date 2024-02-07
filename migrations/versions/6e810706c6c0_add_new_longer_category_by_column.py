"""Add new longer category by column

Revision ID: 6e810706c6c0
Revises: 3383891b5c33
Create Date: 2024-01-25 08:33:34.028290

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6e810706c6c0'
down_revision = '3383891b5c33'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_accounts', sa.Column('new_category', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_accounts', 'new_category')
    # ### end Alembic commands ###