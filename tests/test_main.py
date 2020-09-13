'''
Tests for the main.py
'''
from main import make_graph
import unittest
import os


class TestMain(unittest.TestCase):

    def test_make_graph(self):
        '''Tests the make_graph function'''
        def test(percent: float, block: str, result: str):
            self.assertEqual(make_graph(percent, block), result,
                             f"{percent}% should return {result}")
        blocks = ["░▒▓█", "⚪⚫"]
        percents = [0, 100, 50, 50.001, 25, 75, 3.14,
                    9.901, 87.334, 87.333, 4.666, 4.667]
        graphGroup = [["░░░░░░░░░░░░░░░░░░░░░░░░░",
                       "█████████████████████████",
                       "████████████▒░░░░░░░░░░░░",
                       "████████████▓░░░░░░░░░░░░",
                       "██████▒░░░░░░░░░░░░░░░░░░",
                       "██████████████████▓░░░░░░",
                       "▓░░░░░░░░░░░░░░░░░░░░░░░░",
                       "██▒░░░░░░░░░░░░░░░░░░░░░░",
                       "██████████████████████░░░",
                       "█████████████████████▓░░░",
                       "█░░░░░░░░░░░░░░░░░░░░░░░░",
                       "█▒░░░░░░░░░░░░░░░░░░░░░░░"],
                      ["⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪",
                       "⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫",
                       "⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪",
                       "⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪",
                       "⚫⚫⚫⚫⚫⚫⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪",
                       "⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚪⚪⚪⚪⚪⚪",
                       "⚫⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪",
                       "⚫⚫⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪",
                       "⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚪⚪",
                       "⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚪⚪⚪",
                       "⚫⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪",
                       "⚫⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪"]]
        for i, graphs in enumerate(graphGroup):
            os.environ["INPUT_BLOCKS"] = blocks[i]
            for j, graph in enumerate(graphs):
                test(percents[j], blocks[i], graph)


if __name__ == '__main__':
    unittest.main()
