from __future__ import absolute_import
import os,site
home_dir=os.getenv('HOME')
site.addsitedir('%s/repos' % home_dir)

from importtest.levelA.levelB.Bgroup import levelB2fun

if __name__ == "__main__":
    print('\n-------- inside main program')
    levelB2fun()
    print('\n-------- exit main program')

    
