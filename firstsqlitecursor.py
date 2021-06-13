import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    emails = pieces[1]
    temporary=emails.split('@')
    email=temporary[1]
    print(email)


    cur.execute('SELECT count FROM Counts WHERE org = ? ', (email,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (email,))
        print('inserted new ')
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (email,))
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts GROUP BY org ORDER BY count DESC LIMIT 10 '
listofemails = []
listofcounts = []
for row in cur.execute(sqlstr):
    listofemails.append(row[0])
    listofcounts.append(row[1])
print('before  data aggregation')
for i in range(0,len(listofemails)):
    print(str(listofemails[i]) + '-' + str(listofcounts[i]))
columnnames = 'PRAGMA table_info(Counts)'
for row in cur.execute(columnnames):
    print("the following table names exist in this database emaildb:")
    print(row[1])
"""must check down below to get the hang of a classic algorithm"""
#
#
#
# temporary = None
#
# for i in range(0,len(listofemails)) :
#     for j in range(len(listofemails) - 1, 0, -1):
#        try:
#             if listofemails[i] == listofemails[j]:
#                 listofemails.pop(j)
#                 listofcounts[i] = listofcounts[i] + listofcounts[j]
#             else:
#                 continue
#        finally:
#            print("aggregating data")
#
# print('after data aggregation')
# print(listofcounts)
# print(listofemails)
#
# cur.close()
