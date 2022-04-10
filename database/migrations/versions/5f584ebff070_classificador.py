"""classificador

Revision ID: 5f584ebff070
Revises: 5cfbe522e071
Create Date: 2022-03-31 21:54:37.149006

"""
from alembic import op
import sqlalchemy as sa

from sqlalchemy.sql.sqltypes import Float, DateTime
from sqlalchemy.schema import Sequence, Column, ForeignKey
from sqlalchemy.types import DateTime, DATE, JSON, Integer, Text, String
from sqlalchemy.sql import func


# revision identifiers, used by Alembic.
revision = '5f584ebff070'
down_revision = '5cfbe522e071'
branch_labels = None
depends_on = None


def upgrade():

    op.create_table(
        'classificador',
        Column('id',Integer, primary_key=True, autoincrement=True, nullable=False),
        Column('nome', String(250)),
        Column('tipo', String(250)),
        Column('path', Text()),
    )


def downgrade():
    op.drop_table('classificador')
