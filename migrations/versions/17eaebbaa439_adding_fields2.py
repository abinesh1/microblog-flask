"""adding fields2

Revision ID: 17eaebbaa439
Revises: 0c751aa529fb
Create Date: 2020-01-08 19:19:13.980233

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '17eaebbaa439'
down_revision = '0c751aa529fb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=240), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
