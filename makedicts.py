#!/usr/bin/env python
'''
################################################
convert a list of tuples to a row of dicts 
field name is used as key
################################################
'''

def makedicts(cursor, query, params=()):
    cursor.execute(query, params)
    colnames = [desc[0] for desc in cursor.description]
    rowdicts = [dict(zip(colnames,row))for row in cursor.fetchall()]
    return rowdicts

if __name__ == '__main__':
    import sqlite3
    conn = sqlite3.connect('dbase1')
    cursor = conn.cursor()
    try:
        cursor.execute('drop table people')
    except:
        pass
    cursor.execute('create table people (name char(20), job char(10), pay int(4))')
    cursor.execute('insert into people values (?,?,?)', ('Bob', 'dev', 50000))
    cursor.execute('insert into people values (?,?,?)', ('Sue', 'dev', 50000))
    cursor.execute('insert into people values (?,?,?)', ('Mose', 'guru', 50000))
    cursor.execute('insert into people values (?,?,?)', ('vincent', 'eng', 50000))
    cursor.execute('insert into people values (?,?,?)', ('brian', 'eng', 50000))
    query = 'select * from people'
    all_p = makedicts(cursor, query)

    count_line = 1
    for item in all_p:
        if count_line:
            print('-'*40)
            print('{}'.format("\t\t".join(item.keys())))
            print('-'*40)
            print('{}'.format("\t\t".join([str(x) for x in item.values()])))
            count_line = 0
        else:
            print('-'*40)
            print('{}'.format("\t\t".join([str(x) for x in item.values()])))

            