"""classificados

Revision ID: 2ef62ed22972
Revises: 951fff2e422c
Create Date: 2022-03-31 22:09:56.772787

"""
from alembic import op
import sqlalchemy as sa

from sqlalchemy.sql.sqltypes import Float, DateTime
from sqlalchemy.schema import Sequence, Column, ForeignKey
from sqlalchemy.types import DateTime, DATE, JSON, Integer, Text, String,Boolean
from sqlalchemy.sql import func

# revision identifiers, used by Alembic.
revision = '2ef62ed22972'
down_revision = '951fff2e422c'
branch_labels = None
depends_on = None

def upgrade():

    op.create_table(
        'classificados',
        Column('id',Integer, primary_key=True, autoincrement=True, nullable=False),
        Column('label', String(250)),
        Column('id_item', Integer, ForeignKey('item.id')),
        Column('id_versao', Integer, ForeignKey('versao.id')),
    )

def downgrade():
    op.drop_table('classificados')
