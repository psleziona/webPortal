"""empty message

Revision ID: c465b2cf6eae
Revises: 
Create Date: 2021-02-03 09:35:29.325031

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c465b2cf6eae'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task', sa.Column('handled_by', sa.Integer(), nullable=True))
    op.drop_constraint(None, 'task', type_='foreignkey')
    op.create_foreign_key(None, 'task', 'user', ['handled_by'], ['id'])
    op.drop_column('task', 'author')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task', sa.Column('author', sa.INTEGER(), nullable=True))
    op.drop_constraint(None, 'task', type_='foreignkey')
    op.create_foreign_key(None, 'task', 'user', ['author'], ['id'])
    op.drop_column('task', 'handled_by')
    # ### end Alembic commands ###