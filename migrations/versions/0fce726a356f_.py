"""empty message

Revision ID: 0fce726a356f
Revises: 3dbd7cdb8480
Create Date: 2024-12-04 19:17:55.688515

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0fce726a356f'
down_revision = '3dbd7cdb8480'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('places_folder',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('owner_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['owner_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('place',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('folder_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['folder_id'], ['places_folder.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('place_info',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('place_id', sa.Integer(), nullable=False),
    sa.Column('place_image', sa.String(length=255), nullable=True),
    sa.Column('place_desc', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['place_id'], ['place.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('place_info')
    op.drop_table('place')
    op.drop_table('places_folder')
    # ### end Alembic commands ###
