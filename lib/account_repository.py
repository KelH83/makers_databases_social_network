from lib.account import Account

class AccountRepository:
    def __init__(self, connection):
        self._connection = connection

    # CREATE

    def create(self, account):
        self._connection.execute('INSERT INTO accounts (email, user_name) VALUES (%s, %s)', [
                                account.email, account.user_name])
        return None
    
    # READ
    def all(self):
        rows = self._connection.execute('SELECT * from accounts')
        accounts = []
        for row in rows:
            item = Account(row["email"], row["user_name"])
            accounts.append(item)
        return accounts
    

    def find(self, account_email):
        rows = self._connection.execute(
            'SELECT * from accounts WHERE email = %s', [account_email])
        row = rows[0]
        return Account(row["email"], row["user_name"])
    
    # UPDATE
    def update(self, new_email, account_id):
        self._connection.execute('UPDATE accounts SET email = %s WHERE id = %s', [new_email, account_id])
        rows = self._connection.execute('SELECT * FROM accounts WHERE id = %s', [account_id])
        row = rows[0]
        return Account(row["email"], row["user_name"])
    
    # DELETE
    def delete(self, account_id):
        self._connection.execute(
            'DELETE FROM accounts WHERE id = %s', [account_id])
        return None