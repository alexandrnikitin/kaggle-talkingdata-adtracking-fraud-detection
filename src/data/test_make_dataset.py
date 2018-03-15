import unittest
import csv
from io import StringIO

from .make_dataset import construct_line


class TestMakeDataset(unittest.TestCase):

    def test_construct_line(self):
        scsv = "ip,app,device,os,channel,click_time,attributed_time,is_attributed\n87540,12,1,13,497,2017-11-07 09:30:38,,0"
        f = StringIO(scsv)
        for row in csv.DictReader(f):
            self.assertEqual(construct_line(row), "-1 |i 87540 |a 12 |d 1 |o 13 |c 497\n")


if __name__ == '__main__':
    unittest.main()
