"""empty message

Revision ID: 8c3ae3af51c7
Revises: 0fce726a356f
Create Date: 2024-12-04 19:29:49.288852

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8c3ae3af51c7'
down_revision = '0fce726a356f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('places_folder', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(length=20), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('places_folder', schema=None) as batch_op:
        batch_op.drop_column('name')

    # ### end Alembic commands ###
