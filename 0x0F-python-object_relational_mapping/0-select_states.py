#!/usr/bin/python3
'''Query with MySQLdb'''
import MySQLdb
import sys
if __name__ == "__main__":
        db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                              passwd=sys.argv[2], db=sys.argv[3])
        match = sys.argv[4]
        c = db.cursor()
        c.execute("""SELECT * FROM states ORDER BY id ASC""", {'name': sys.argv[4]})
        rows = c.fetchall()
        for row in rows:
            if match == row[1]:
                print(row)
                                                        
