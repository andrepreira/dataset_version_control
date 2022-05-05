"""entidades

Revision ID: 3e68c1943f96
Revises: 2ef62ed22972
Create Date: 2022-04-29 09:51:52.742354

"""
from alembic import op
import sqlalchemy as sa

from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import DateTime, Integer, Text, String,Boolean,  Float
from sqlalchemy.sql import func

# revision identifiers, used by Alembic.
revision = '3e68c1943f96'
down_revision = '2ef62ed22972'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'entidades',
        Column('id',Integer, primary_key=True, autoincrement=True, nullable=False),
        Column('entidade', Text()),
        Column('tipo', Text()),
        Column('start_char', Float()),
        Column('end_char', Float()),
        Column('id_item', Integer, ForeignKey('item.id')),
        Column('id_versao', Integer, ForeignKey('versao.id')),
        Column('label', Text()),
        Column('date', DateTime(timezone=True), server_default=func.now())
    )


def downgrade():
    op.drop_table('entidades')
