import sqlite3

class SqliteDB:
    def __init__(self):
        self.database = 'database.db'
        try:
            conn = sqlite3.connect(self.database)
            conn.execute('CREATE TABLE IF NOT EXISTS requests (id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT, email TEXT, problem TEXT, solved BOOL)')
            print("[+] - Created the requests table!")
        except:
            print("[x] - Error creating the requests table!")
        finally:
            conn.close()
    
    def create_request(self, name, email, problem):
        try:
            conn = sqlite3.connect(self.database)
            cur = conn.cursor()
            cur.execute('INSERT INTO requests (name,email,problem,solved) VALUES (?,?,?,?)',(name,email,problem,False))
            conn.commit()
            print("[+] - Successfully added new request into database!")
        except:
            conn.rollback()
            print("[x] - Error adding new request into database.")
        finally:
            conn.close()
        

    def read_requests(self):
        try:
            conn = sqlite3.connect(self.database)
            cur = conn.cursor()
            cur.execute('SELECT * FROM requests WHERE solved=False')
            rows = cur.fetchall()
            print("[~] - Successfully fetched all requests!")
            return rows
        except:
            conn.rollback()
            print("[x] - Error fetching requests.")
        finally:
            conn.close()

    def update_request(self, id):
        try:
            conn = sqlite3.connect(self.database)
            cur = conn.cursor()
            cur.execute('UPDATE requests SET solved = True WHERE id = ?', (id))
            conn.commit()
            print("[~] - Successfully updated request!")
        except:
            conn.rollback()
            print("[x] - Error updating requests.")
        finally:
            conn.close()

    def delete_request(self, id):
        try:
            conn = sqlite3.connect(self.database)
            cur = conn.cursor()
            cur.execute('DELETE FROM requests WHERE id = ?', (id))
            conn.commit()
            print("[-] - Successfully deleted request!")
        except:
            conn.rollback()
            print("[x] - Error deleting request.")
        finally:
            conn.close()