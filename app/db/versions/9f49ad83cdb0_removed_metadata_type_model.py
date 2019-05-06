"""Removed metadata type model

Revision ID: 9f49ad83cdb0
Revises: d0a0f5baeae8
Create Date: 2019-05-06 16:13:07.365087

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '9f49ad83cdb0'
down_revision = 'd0a0f5baeae8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('type_string', table_name='metadata_type')
    op.drop_table('metadata_type')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('metadata_type',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('type_string', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('mapped_type_string', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('decoder_class', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('created_at_runtime_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('updated_at_runtime_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('type_string', 'metadata_type', ['type_string'], unique=True)
    # ### end Alembic commands ###