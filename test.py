import unittest
import Testmodel

class TestHeal_MainWindow(unittest.TestCase):
    

    def test_insert_dates(self):
        self._MainWindow = Testmodel.Testmodel()

        self._MainWindow.insert_dates('name', 'Reception', 'Price', 'Datatime')

        _Insert = self._MainWindow.data_table()

        self.assertIn(['name', 'Reception', 'Price', 'Datatime'], _Insert)



if __name__ == '__main__':
    unittest.main()