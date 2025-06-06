"""Initial migration

Revision ID: 4a364dbb8dab
Revises: 
Create Date: 2025-03-29 13:59:33.243069

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = '4a364dbb8dab'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('llm_request_traces',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('trace_id', sa.String(length=64), nullable=False),
    sa.Column('model_id', sa.String(length=64), nullable=False),
    sa.Column('backend_name', sa.String(length=64), nullable=False),
    sa.Column('request_time', sa.DateTime(), nullable=False),
    sa.Column('response_time', sa.DateTime(), nullable=True),
    sa.Column('duration', sa.Float(), nullable=True),
    sa.Column('request_json', sa.Text(), nullable=True),
    sa.Column('response_json', sa.Text(), nullable=True),
    sa.Column('prompt_tokens', sa.Integer(), nullable=True),
    sa.Column('completion_tokens', sa.Integer(), nullable=True),
    sa.Column('total_tokens', sa.Integer(), nullable=True),
    sa.Column('cached_tokens', sa.Integer(), nullable=True),
    sa.Column('error', sa.Text(), nullable=True),
    sa.Column('status', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('idx_backend_time', 'llm_request_traces', ['backend_name', 'request_time'], unique=False)
    op.create_index('idx_request_model', 'llm_request_traces', ['model_id', 'request_time'], unique=False)
    op.create_index('idx_status_time', 'llm_request_traces', ['status', 'request_time'], unique=False)
    op.create_index(op.f('ix_llm_request_traces_backend_name'), 'llm_request_traces', ['backend_name'], unique=False)
    op.create_index(op.f('ix_llm_request_traces_model_id'), 'llm_request_traces', ['model_id'], unique=False)
    op.create_index(op.f('ix_llm_request_traces_request_time'), 'llm_request_traces', ['request_time'], unique=False)
    op.create_index(op.f('ix_llm_request_traces_trace_id'), 'llm_request_traces', ['trace_id'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_llm_request_traces_trace_id'), table_name='llm_request_traces')
    op.drop_index(op.f('ix_llm_request_traces_request_time'), table_name='llm_request_traces')
    op.drop_index(op.f('ix_llm_request_traces_model_id'), table_name='llm_request_traces')
    op.drop_index(op.f('ix_llm_request_traces_backend_name'), table_name='llm_request_traces')
    op.drop_index('idx_status_time', table_name='llm_request_traces')
    op.drop_index('idx_request_model', table_name='llm_request_traces')
    op.drop_index('idx_backend_time', table_name='llm_request_traces')
    op.drop_table('llm_request_traces')
    # ### end Alembic commands ###
