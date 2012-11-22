# -*- coding: utf-8 -*-
"""
    PyCharm	
    ~~~~~~

    :copyright: (c) 2011 by ytjohn
    :license: BSD, see LICENSE for more details.
"""

import sqlite3
from Crypto.Cipher import AES

class TokenExceptions(Exception):
    pass

class tokens(object):

    def __init__(self, db, key):
        self.db = db
        self.key = key
        self.dbconn = sqlite3.connect(db)
        self.dbconn.text_factory = str
        if not self._tableexists('tokens'):
            self._generatetable('tokens')

    def _encrypttoken(self, token):
        cipher = AES.new(self.key, AES.MODE_CFB)
        return cipher.encrypt(token)

    def _decrypttoken(self, token):
        cipher = AES.new(self.key, AES.MODE_CFB)
        return cipher.decrypt(token)

    def get(self, id):
        enctoken = self._fetchtoken(id)
        if enctoken:
            token = self._decrypttoken(enctoken)
        else:
            token = False
        return token

    def record(self, token, id=None):
        if token == '':
            return False

        enctoken = self._encrypttoken(token)
        saved = self._savetoken(enctoken, id)
        return saved

    def delete(self, id):
        if self._deletetoken(id) == 1:
            return "deleted %s" % id
        else:
            return "unable to delete %s" % id

    def _generatetable(self, table='tokens'):
        sql = """CREATE TABLE tokens (
                    id integer primary key,
                    token text,
                    created datetime,
                    modified datetime
                    );"""
        t = (table,)
        c = self.dbconn.cursor()
        try:
            c.execute(sql)
            self.dbconn.commit()
        except sqlite3.OperationalError, e:
            return "error: table already exists"
        return True

    def _tableexists(self, table='tokens'):
        sql = "SELECT name FROM sqlite_master WHERE type='table' AND " \
              "name=?;"

        c = self.dbconn.cursor()
        t = (table,)
        c.execute(sql, t)
        row = c.fetchone()
        try:
            name = row[0]
        except TypeError:
            return False

        if name == 'tokens':
            return True



    def _fetchtoken(self, id):
        c = self.dbconn.cursor()
        t = (id,)
        c.execute('SELECT token FROM tokens WHERE id=?', t)
        token = c.fetchone()
        try:
            token = token[0]
        except TypeError:
            return False
        return token

    def _savetoken(self, token, id=None):
        """ save the encrypted token. If id is passed,
        udpates and existing token. Returns saved token id.
        """
        c = self.dbconn.cursor()
        if id:
            t = (token, id)
            sql = "UPDATE tokens set token=?, modified=datetime('now') WHERE" \
                  " id=?; "
            count = c.execute(sql, t).rowcount
            if count == 1:
                self.dbconn.commit()
            else:
                return False
        else:
            t = (token,)
            sql = 'INSERT INTO tokens (id, token, created, modified) VALUES' \
                  ' (NULL, ?,datetime(\'now\'),datetime(\'now\'));'
            count = c.execute(sql, t).rowcount
            if count == 1:
                id = c.lastrowid
                self.dbconn.commit()
            else:
                return False

        return id

    def _deletetoken(self, id):
        c = self.dbconn.cursor()
        t = (id,)
        count = c.execute('DELETE from tokens WHERE id=?', t).rowcount
        if count == 1:
            self.dbconn.commit()
        else:
            self.dbconn.rollback()
        return count
















