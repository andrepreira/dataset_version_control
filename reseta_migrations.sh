#!/bin/bash

cd ./database

alembic downgrade -6

alembic upgrade +6