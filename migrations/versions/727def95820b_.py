"""empty message

Revision ID: 727def95820b
Revises: 
Create Date: 2024-04-26 19:48:41.931806

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '727def95820b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('groupss', schema=None) as batch_op:
        batch_op.alter_column('group_id',
               existing_type=mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_general_ci', length=40),
               type_=sa.NVARCHAR(length=40),
               existing_nullable=False)
        batch_op.alter_column('group_title',
               existing_type=mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_general_ci', length=100),
               type_=sa.NVARCHAR(length=100),
               existing_nullable=True)
        batch_op.alter_column('user_id',
               existing_type=mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_general_ci', length=40),
               type_=sa.NVARCHAR(length=40),
               existing_nullable=False)
        batch_op.alter_column('color',
               existing_type=mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_general_ci', length=10),
               type_=sa.NVARCHAR(length=10),
               existing_nullable=True)

    with op.batch_alter_table('tags', schema=None) as batch_op:
        batch_op.alter_column('tag_id',
               existing_type=mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_general_ci', length=40),
               type_=sa.NVARCHAR(length=40),
               existing_nullable=False)
        batch_op.alter_column('tag_title',
               existing_type=mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_general_ci', length=100),
               type_=sa.NVARCHAR(length=100),
               existing_nullable=True)
        batch_op.alter_column('tag_color',
               existing_type=mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_general_ci', length=10),
               type_=sa.NVARCHAR(length=10),
               existing_nullable=True)
        batch_op.alter_column('user_id',
               existing_type=mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_general_ci', length=40),
               type_=sa.NVARCHAR(length=40),
               existing_nullable=False)
        batch_op.alter_column('group_id',
               existing_type=mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_general_ci', length=40),
               type_=sa.NVARCHAR(length=40),
               existing_nullable=False)

    with op.batch_alter_table('tasks', schema=None) as batch_op:
        batch_op.alter_column('task_id',
               existing_type=mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_general_ci', length=40),
               type_=sa.NVARCHAR(length=40),
               existing_nullable=False)
        batch_op.alter_column('task_title',
               existing_type=mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_general_ci', length=100),
               type_=sa.NVARCHAR(length=100),
               existing_nullable=True)
        batch_op.alter_column('task_description',
               existing_type=mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_general_ci', length=500),
               type_=sa.NVARCHAR(length=500),
               existing_nullable=True)
        batch_op.alter_column('tag_id',
               existing_type=mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_general_ci', length=40),
               type_=sa.NVARCHAR(length=40),
               existing_nullable=False)
        batch_op.alter_column('user_id',
               existing_type=mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_general_ci', length=40),
               type_=sa.NVARCHAR(length=40),
               existing_nullable=False)

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_general_ci', length=40),
               type_=sa.NVARCHAR(length=40),
               existing_nullable=False)
        batch_op.alter_column('email',
               existing_type=mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_general_ci', length=100),
               type_=sa.NVARCHAR(length=100),
               existing_nullable=True)
        batch_op.alter_column('password',
               existing_type=mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_general_ci', length=100),
               type_=sa.NVARCHAR(length=100),
               existing_nullable=True)
        batch_op.alter_column('name',
               existing_type=mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_general_ci', length=256),
               type_=sa.NVARCHAR(length=256),
               existing_nullable=True)
        batch_op.alter_column('bio',
               existing_type=mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_general_ci', length=2000),
               type_=sa.NVARCHAR(length=2000),
               existing_nullable=True)
        batch_op.alter_column('location',
               existing_type=mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_general_ci', length=200),
               type_=sa.NVARCHAR(length=200),
               existing_nullable=True)
        batch_op.alter_column('image',
               existing_type=mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_general_ci', length=200),
               type_=sa.NVARCHAR(length=200),
               existing_nullable=True)
        batch_op.alter_column('type_account',
               existing_type=mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_general_ci', length=10),
               type_=sa.NVARCHAR(length=10),
               existing_nullable=True)
        batch_op.alter_column('external_id',
               existing_type=mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_general_ci', length=40),
               type_=sa.NVARCHAR(length=40),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('external_id',
               existing_type=sa.NVARCHAR(length=40),
               type_=mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_general_ci', length=40),
               existing_nullable=True)
        batch_op.alter_column('type_account',
               existing_type=sa.NVARCHAR(length=10),
               type_=mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_general_ci', length=10),
               existing_nullable=True)
        batch_op.alter_column('image',
               existing_type=sa.NVARCHAR(length=200),
               type_=mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_general_ci', length=200),
               existing_nullable=True)
        batch_op.alter_column('location',
               existing_type=sa.NVARCHAR(length=200),
               type_=mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_general_ci', length=200),
               existing_nullable=True)
        batch_op.alter_column('bio',
               existing_type=sa.NVARCHAR(length=2000),
               type_=mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_general_ci', length=2000),
               existing_nullable=True)
        batch_op.alter_column('name',
               existing_type=sa.NVARCHAR(length=256),
               type_=mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_general_ci', length=256),
               existing_nullable=True)
        batch_op.alter_column('password',
               existing_type=sa.NVARCHAR(length=100),
               type_=mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_general_ci', length=100),
               existing_nullable=True)
        batch_op.alter_column('email',
               existing_type=sa.NVARCHAR(length=100),
               type_=mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_general_ci', length=100),
               existing_nullable=True)
        batch_op.alter_column('user_id',
               existing_type=sa.NVARCHAR(length=40),
               type_=mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_general_ci', length=40),
               existing_nullable=False)

    with op.batch_alter_table('tasks', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.NVARCHAR(length=40),
               type_=mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_general_ci', length=40),
               existing_nullable=False)
        batch_op.alter_column('tag_id',
               existing_type=sa.NVARCHAR(length=40),
               type_=mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_general_ci', length=40),
               existing_nullable=False)
        batch_op.alter_column('task_description',
               existing_type=sa.NVARCHAR(length=500),
               type_=mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_general_ci', length=500),
               existing_nullable=True)
        batch_op.alter_column('task_title',
               existing_type=sa.NVARCHAR(length=100),
               type_=mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_general_ci', length=100),
               existing_nullable=True)
        batch_op.alter_column('task_id',
               existing_type=sa.NVARCHAR(length=40),
               type_=mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_general_ci', length=40),
               existing_nullable=False)

    with op.batch_alter_table('tags', schema=None) as batch_op:
        batch_op.alter_column('group_id',
               existing_type=sa.NVARCHAR(length=40),
               type_=mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_general_ci', length=40),
               existing_nullable=False)
        batch_op.alter_column('user_id',
               existing_type=sa.NVARCHAR(length=40),
               type_=mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_general_ci', length=40),
               existing_nullable=False)
        batch_op.alter_column('tag_color',
               existing_type=sa.NVARCHAR(length=10),
               type_=mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_general_ci', length=10),
               existing_nullable=True)
        batch_op.alter_column('tag_title',
               existing_type=sa.NVARCHAR(length=100),
               type_=mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_general_ci', length=100),
               existing_nullable=True)
        batch_op.alter_column('tag_id',
               existing_type=sa.NVARCHAR(length=40),
               type_=mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_general_ci', length=40),
               existing_nullable=False)

    with op.batch_alter_table('groupss', schema=None) as batch_op:
        batch_op.alter_column('color',
               existing_type=sa.NVARCHAR(length=10),
               type_=mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_general_ci', length=10),
               existing_nullable=True)
        batch_op.alter_column('user_id',
               existing_type=sa.NVARCHAR(length=40),
               type_=mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_general_ci', length=40),
               existing_nullable=False)
        batch_op.alter_column('group_title',
               existing_type=sa.NVARCHAR(length=100),
               type_=mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_general_ci', length=100),
               existing_nullable=True)
        batch_op.alter_column('group_id',
               existing_type=sa.NVARCHAR(length=40),
               type_=mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_general_ci', length=40),
               existing_nullable=False)

    # ### end Alembic commands ###
