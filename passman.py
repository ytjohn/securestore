# -*- coding: utf-8 -*-
"""
    PyCharm	
    ~~~~~~

    :copyright: (c) 2011 by ytjohn
    :license: BSD, see LICENSE for more details.
"""

from securestore.tokens import tokens
import cmd

class CLI(cmd.Cmd):

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = 'todo> '
        key = u't<Ji`1}`<AkOq"Lfui~o@KtJ?@9K5cN(\)h>jyD20uze4NAJ{p6X=mPrp|Lo!/z'[:32]
        self.tok = tokens('tmp/tmp.db', key)

    def do_builddb(self, arg):
        self.tok.generatetable()

    def do_add(self, arg):
        if arg:
            password = arg
        else:
            password = raw_input('')
        id = self.tok.record(password)
        print id

    def do_update(self, arg):
        if arg:
            try:
                (id, password) = arg.split(' ')
            except ValueError:
                id = arg
                password = raw_input('')
        else:
            print "must provide id"
            return
        print self.tok.record(password, id)





    def do_show(self, arg):
        if arg:
            id =arg
        else:
            id = raw_input('Id?: ')
        print self.tok.get(id)

    def do_delete(self, arg):
        if arg:
            id = arg
        else:
            id = raw_input('Delete id: ')
        print self.tok.delete(id)





if __name__ == "__main__":

    c = CLI()
    c.cmdloop(intro='interactive shell')

#
#
#key = u't<Ji`1}`<AkOq"Lfui~o@KtJ?@9K5cN(\)h>jyD20uze4NAJ{p6X=mPrp|Lo!/z'[:32]
#print key
#print unicode(key)
#tok = tokens('tmp.db', key)
#
#tok.generatetable()
#
#id1 = tok.record('test1')
#print id1, 'test1'
#id2 = tok.record('test2')
#print id2, 'test2'
#id3 = tok.record('test3', 4)
#print id3, 'test3'
#
#print "now retrieving"
#
#print id1, tok.get(id1)
#print id2, tok.get(id2)
#print id3, tok.get(id3)
#
#print "now deleting an id"
#print tok.delete(1)
#print "and another"
#print tok.delete(5)
#
#
#
#
#
#
