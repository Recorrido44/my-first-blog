import sys
# sys.path.insert(0,"/home/claudia/djangovirtual/myvenv/lib/python3.6/site-packages/jedi/third_party/typeshed/third_party/2and3")
sys.path.insert(0,"/usr/local/lib/python2.7/dist-packages")

import pymysql
pymysql.version_info = (1, 3, 13, "final", 0)
pymysql.install_as_MySQLdb()