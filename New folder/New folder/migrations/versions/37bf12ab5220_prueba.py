"""Prueba

Revision ID: 37bf12ab5220
Revises: c15681da044f
Create Date: 2021-06-02 19:59:18.185730

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '37bf12ab5220'
down_revision = 'c15681da044f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('prueba')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('prueba',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='prueba_pkey')
    )
    # ### end Alembic commands ###
