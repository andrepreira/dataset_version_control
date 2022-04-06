"""item

Revision ID: 5cfbe522e071
Revises: ec780f464283
Create Date: 2022-03-31 21:49:08.741603

"""
from alembic import op
import sqlalchemy as sa

from sqlalchemy.sql.sqltypes import Float, DateTime
from sqlalchemy.schema import Sequence, Column, ForeignKey
from sqlalchemy.types import DateTime, DATE, JSON, Integer, Text, String
from sqlalchemy.sql import func


# revision identifiers, used by Alembic.
revision = '5cfbe522e071'
down_revision = 'ec780f464283'
branch_labels = None
depends_on = None


def upgrade():

    op.create_table(
        'item',
        Column('id',Integer, primary_key=True, autoincrement=True, nullable=False),
        Column('texto', Text()),
        Column('id_dataset', Integer, ForeignKey('dataset.id')),
        Column('nome', String(250))
    )

def downgrade():
    op.drop_table('item')
