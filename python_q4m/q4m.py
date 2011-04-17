# -*- coding: utf-8 -*-

import MySQLdb

class Q4M(object):

    def __init__(self, con):
        self.con = con

    def abort(self):
        cur = self.con.cursor()
        cur.execute('SELECT queue_abort()')
        ret = cur.fetchone()[0]
        cur.close()
        return ret

    def wait(self, tm = None):
        cur = self.con.cursor()
        sql = 'SELECT queue_wait(\'' + self.table + '\'%s)'
        sql = self._set_tm(sql, tm)
        cur.execute(sql)
        ret = cur.fetchone()[0]
        cur.close()
        return ret

    def end(self):
        cur = self.con.cursor()
        cur.execute('SELECT queue_end()')
        ret = cur.fetchone()[0]
        cur.close()
        return ret
        
    def enqueue(self, values) :
        cur         = self.con.cursor()
        columns_str = ','.join(self.columns)
        values_str  = ','.join([ MySQLdb.escape_string('%s') for i in range(len(self.columns))])
        cur.execute('INSERT INTO ' + self.table +
                    '(' + columns_str + ') VALUES(' + values_str + ')',
                    values)
        cur.close()

    def dequeue(self):
        cur = self.con.cursor(MySQLdb.cursors.DictCursor)
        res = cur.execute('SELECT * from ' + self.table)
        if res > 1:
            raise MySQLdb.Error(res, "dequeued row is not one.")
        elif res == 0:
            raise MySQLdb.Error(res, "queue is empty.")
        return cur.fetchone()

    def _set_tm(self, sql, tm):
        if tm is not None and isinstance(tm, int) :
            sql = sql % (', ' + str(tm))
        else:
            sql = sql % ''
        return sql
        
