"""views

Revision ID: 47f97b83cee4
Revises: 17c3d2384711
Create Date: 2022-01-26 12:07:05.075977

"""
from alembic import op
import sqlalchemy as sa
import mindsdb.interfaces.storage.db



# revision identifiers, used by Alembic.
revision = '47f97b83cee4'
down_revision = '17c3d2384711'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('view',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('company_id', sa.Integer(), nullable=True),
    sa.Column('query', sa.String(), nullable=False),
    sa.Column('datasource_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['datasource_id'], ['datasource.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('view')
    # ### end Alembic commands ###
