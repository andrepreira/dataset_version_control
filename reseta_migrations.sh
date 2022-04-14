#!/bin/bash

cd ./database

alembic downgrade -5

alembic upgrade +5