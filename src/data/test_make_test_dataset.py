import unittest
import csv
from io import StringIO

from .make_test_dataset import construct_line


class TestMakeTestDataset(unittest.TestCase):

    def test_construct_line(self):
        scsv = "click_id,ip,app,device,os,channel,click_time\n0,5744,9,1,3,107,2017-11-10 04:00:00"
        f = StringIO(scsv)
        for row in csv.DictReader(f):
            self.assertEqual(construct_line(row), "'0 |i 5744 |a 9 |d 1 |o 3 |c 107\n")


if __name__ == '__main__':
    unittest.main()
