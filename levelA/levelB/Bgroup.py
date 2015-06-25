from __future__ import absolute_import

from ..Agroup import levelA1fun, levelA2fun

def levelB1fun():
    print('\n--------------inside function levelB1fun')
    print('called from module {}'.format(__name__))
    print('\n--------------exit function levelB1fun')

def levelB2fun():
    print('\n--------------inside function levelB2fun')
    print('called from module {}'.format(__name__))
    levelA1fun()
    levelA2fun()
    levelB1fun()
    print('\n--------------exit function levelB2fun')
    
    
