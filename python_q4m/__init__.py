# -*- coding: utf-8 -*-
import python_q4m

__author__  = "Tatsuhiko Kubo (cubicdaiya@gmail.com)"
__version__ = "0.0.5"
__license__ = "GPL2"
__doc__     = """
This module is simple Q4M operation wrapper developed by pixiv Inc. for asynchronous upload system

Simple example of usage is followings

   >>> from python_q4m.q4m import *
   >>> class QueueTable(Q4M):
   >>>     def __init__(self, con):
   >>>         super(self.__class__, self).__init__(con)
   >>>         self.table   = 'queue_table'
   >>>         self.columns = ['id',
   >>>                         'msg',
   >>>                        ]
   >>> try:
   >>>    con = MySQLdb.connect(host='localhost',
   >>>                          db=dbname,
   >>>                          user=username,
   >>>                          passwd=password,
   >>>                         )
   >>>    q = QueueTable(con)
   >>>    q.enqueue([1, 'msg'])
   >>>    while q.wait() == 0:
   >>>        time.sleep(1);
   >>>     res = q.dequeue()
   >>>     print res['id']
   >>>     print res['msg']
   >>>     q.end()
   >>>     con.close()
   >>> except MySQLdb.Error, e:
   >>>     print 'Error %d: %s' % (e.args[0], e.args[1])
   >>>     q.abort()
   >>>     con.close()

And it is necessary to create following table for above example.

CREATE TABLE `queue_table` (`id` int(11) NOT NULL, `msg` text NOT NULL) ENGINE=QUEUE;

"""
