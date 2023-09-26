"""Add new ranked by column

Revision ID: 58ecd8b9b28e
Revises: 97ab39cd1158
Create Date: 2023-09-26 20:08:06.949138

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '58ecd8b9b28e'
down_revision = '97ab39cd1158'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('questions', sa.Column('ranked_by', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'questions', 'user_accounts', ['ranked_by'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'questions', type_='foreignkey')
    op.drop_column('questions', 'ranked_by')
    # ### end Alembic commands ###
