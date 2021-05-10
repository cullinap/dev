#!/bin/bash
echo running ex13.db

rm ex13.db
sqlite3 ex13.db < code.sql
sqlite3 ex13.db < ex13a.sql

