"""empty message

Revision ID: 66a64868bce4
Revises:
Create Date: 2024-03-30 01:43:18.370633

"""

from typing import Sequence, Union

import sqlalchemy as sa
import sqlmodel
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "66a64868bce4"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "repository",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("provider_repo_id", sa.Integer(), nullable=True),
        sa.Column("name", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_repository_provider_repo_id"), "repository", ["provider_repo_id"], unique=False)
    op.create_table(
        "user",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("scope", sa.Enum("ADMIN", "USER", name="userscope"), nullable=False),
        sa.Column("provider_user_id", sa.Integer(), nullable=True),
        sa.Column("login", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("hashed_password", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "guideline",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("content", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("creator_id", sa.Integer(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(["creator_id"], ["user.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("guideline")
    op.drop_table("user")
    sa.Enum(name="userscope").drop(op.get_bind(), checkfirst=False)
    op.drop_index(op.f("ix_repository_provider_repo_id"), table_name="repository")
    op.drop_table("repository")
    # ### end Alembic commands ###
