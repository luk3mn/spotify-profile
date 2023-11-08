"""empty message

Revision ID: 484aaa379aab
Revises: 0d8041499fc8
Create Date: 2023-11-07 11:00:56.823263

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '484aaa379aab'
down_revision = '0d8041499fc8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tb_track', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image_url', sa.String(length=200), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tb_track', schema=None) as batch_op:
        batch_op.drop_column('image_url')

    # ### end Alembic commands ###
