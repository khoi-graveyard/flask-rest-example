"""empty message

Revision ID: fcbacf23e544
Revises: 2888ec641fb6
Create Date: 2020-03-09 15:59:21.721146

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fcbacf23e544'
down_revision = '2888ec641fb6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.drop_constraint('user_email_key', 'user', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('user_email_key', 'user', ['email'])
    op.drop_index(op.f('ix_user_email'), table_name='user')
    # ### end Alembic commands ###
