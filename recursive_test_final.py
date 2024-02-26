import unittest
from recursive_floyd_final import floyd

N = 5
INF = 99999

class TestRecursiveFloyd(unittest.TestCase):
    """Test suite for the recursive Floyd-Warshall algorithm."""

    def test_recursive_floyd(self):
        """Test the recursive Floyd-Warshall algorithm."""
        input_graph = [
            [0, 2, INF, INF, INF],
            [INF, 0, 6, INF, INF],
            [INF, 7, 0, INF, INF],
            [INF, INF, 1, 0, 3],
            [1, 4, INF, INF, 0],
        ]

        error_input_graph = [
            [0, 2, INF, INF, INF],
            [INF, 0, 5, INF, INF], # [2][1] has been changed from 6 to 5
            [INF, 7, 4, INF, INF], # [2][2] has been changed from 0 to 4
            [INF, INF, 1, 0, 3],
            [1, 4, INF, INF, 0],
        ]

        expected_output = [
            [0, 2, 8, INF, INF],
            [INF, 0, 6, INF, INF],
            [INF, 7, 0, INF, INF],
            [4, 6, 1, 0, 3],
            [1, 3, 9, INF, 0],
        ]

        dist = floyd(input_graph)
        self.assertEqual(dist, expected_output)
        print("Test Passed! The input graph matches the expected output. \n")

        dist_error = floyd(error_input_graph)
        self.assertNotEqual(dist_error, expected_output)
        print("Test Passed! The input graph does not match the expected output. \n")

    def test_disconnected_graph(self):
        """Test the algorithm on a disconnected graph."""
        input_graph = [
            [0, INF, INF, INF, INF],
            [INF, 0, INF, INF, INF],
            [INF, INF, 0, INF, INF],
            [INF, INF, INF, 0, INF],
            [INF, INF, INF, INF, 0],
        ]

        expected_output = [
            [0, INF, INF, INF, INF],
            [INF, 0, INF, INF, INF],
            [INF, INF, 0, INF, INF],
            [INF, INF, INF, 0, INF],
            [INF, INF, INF, INF, 0],
        ]

        dist = floyd(input_graph)
        self.assertEqual(dist, expected_output)
        print("Test Passed! The input graph is not disconnected.\n")

if __name__ == '__main__':
    unittest.main()