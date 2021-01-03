import unittest
from app import hello
import testing.mysqld
from sqlalchemy import create_engine
from pytest_mysql import factories

# prevent generating brand new db every time.  Speeds up tests.
#MYSQLD_FACTORY = testing.mysqld.MysqldFactory(cache_initialized_db=True, port=3306)


mysql_my_proc = factories.mysql_proc(
    port=3306)
mysql_my = factories.mysql('mysql_my_proc')

class TestHelloApp(unittest.TestCase):

  @classmethod
  def setUpClass(cls):
      mysql_my_proc = factories.mysql_proc(port=3306)
      mysql_my = factories.mysql('mysql_my_proc')

#      cls.mysql = MYSQLD_FACTORY()
#      cls.db_conn = create_engine(cls.mysql.url()).connect()

#  def setUp(self):
#      self.mysql.start()
#      self.db_conn.execute("""CREATE TABLE `foo` (blah)""")

  def test_hello(self):
    self.assertEqual(hello(), '{"items": [{"itemName":"ToothBrush","itemPrice":145.5},{"itemName":"soap","itemPrice":45.5},{"itemName":"Men Wallet","itemPrice":3345.5}]}')

if __name__ == '__main__':
  unittest.main()
