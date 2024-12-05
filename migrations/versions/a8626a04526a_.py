"""empty message

Revision ID: a8626a04526a
Revises: c3e65428871a
Create Date: 2024-12-04 19:59:56.055672

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a8626a04526a'
down_revision = 'c3e65428871a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('places_folder', schema=None) as batch_op:
        batch_op.add_column(sa.Column('folder_name', sa.String(length=20), nullable=False))
        batch_op.drop_column('name')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('places_folder', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.VARCHAR(length=20), nullable=False))
        batch_op.drop_column('folder_name')

    # ### end Alembic commands ###