#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os.path
import sqlite3
import tempfile

import click

sql = """create table if not exists users(
    id integer primary key autoincrement,
    name varchar(30)
    )
"""

DB_PATH = os.path.join(tempfile.gettempdir(), "test.db")


@click.group()
def cli():
    pass


@cli.command(short_help="initialize database and tables")
def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    conn.close()


@cli.command(short_help="fill records to database")
@click.option("--total", "-t", default=300, help="fill data for example")
def fill_data(total):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    for i in range(total):
        cur.execute("insert into users (name) values (?)", ["name" + str(i)])

    conn.commit()
    conn.close()


if __name__ == "__main__":
    cli()
