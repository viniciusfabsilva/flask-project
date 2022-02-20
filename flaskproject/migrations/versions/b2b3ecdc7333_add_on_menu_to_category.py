"""add on_menu to category

Revision ID: b2b3ecdc7333
Revises: 
Create Date: 2022-02-19 21:00:07.702884

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b2b3ecdc7333'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('category', sa.Column('on_menu', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('category', 'on_menu')
    # ### end Alembic commands ###