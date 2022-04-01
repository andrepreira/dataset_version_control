"""versao

Revision ID: 951fff2e422c
Revises: 5f584ebff070
Create Date: 2022-03-31 22:06:29.179876

"""
from alembic import op
import sqlalchemy as sa

from sqlalchemy.sql.sqltypes import Float, DateTime
from sqlalchemy.schema import Sequence, Column, ForeignKey
from sqlalchemy.types import DateTime, DATE, JSON, Integer, Text, String,Boolean
from sqlalchemy.sql import func

# revision identifiers, used by Alembic.
revision = '951fff2e422c'
down_revision = '5f584ebff070'
branch_labels = None
depends_on = None

def upgrade():

    op.create_table(
        'versao',
        Column('id',Integer, primary_key=True, autoincrement=True, nullable=False),
        Column('nome', String(250)),
        Column('descricao', String(350)),
        Column('is_manual', Boolean),
        Column('id_classificador', Integer, ForeignKey('classificador.id')),
        Column('date', DateTime(timezone=True), server_default=func.now())
    )


def downgrade():
    op.drop_table('versao')
