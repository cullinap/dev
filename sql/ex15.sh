#!/bin/bash
echo running ex15.sh

rm -rf ex15.db
python ex15.py
sqlite3 ex15.db < code.sql
sqlite3 ex15.db < ex14.sql
sqlite3 ex15.db < ex15.sql

echo finished ex15.sh
