import unittest

def zigzag(matrix):
    if not matrix or not matrix[0]:
        return []
    
    n = len(matrix)
    m = len(matrix[0])
    result = []
    
    for d in range(n + m - 1):
        diagonal = []
        
        if d % 2 == 0:
            row = min(d, n - 1)
            col = d - row
            while row >= 0 and col < m:
                diagonal.append(matrix[row][col])
                row -= 1
                col += 1
        else:
            col = min(d, m - 1)
            row = d - col
            while row < n and col >= 0:
                diagonal.append(matrix[row][col])
                row += 1
                col -= 1
        
        result.extend(diagonal)
    
    return result


class TestZigzag(unittest.TestCase):

    def test_3x3_matrix(self):
        matrix = [
            [1,  2, 3],
            [4,  5, 6],
            [7,  8, 9],
        ]
        expected = [1, 2, 4, 7, 5, 3, 6, 8, 9]         
        self.assertEqual(zigzag(matrix), expected)
    
    def test_5x5_matrix(self):
        matrix = [
            [1,  2,  6,  7,  15],
            [3,  5,  8,  14, 16],
            [4,  9,  13, 17, 22],
            [10, 12, 18, 21, 23],
            [11, 19, 20, 24, 25]
        ]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]         
        self.assertEqual(zigzag(matrix), expected)
    
    def test_2x4_matrix(self):
        matrix = [
            [1, 5],
            [2, 6],
            [3, 7],
            [4, 8]
        ]
        expected = [1, 5, 2, 3, 6, 7, 4, 8]        
        self.assertEqual(zigzag(matrix), expected)
    
    def test_1x6_matrix(self):
        matrix = [[1, 2, 3, 4, 5, 6]]
        expected = [1, 2, 3, 4, 5, 6]
        self.assertEqual(zigzag(matrix), expected)
    
    def test_1x1_matrix(self):
        matrix = [[1]]
        expected = [1]
        self.assertEqual(zigzag(matrix), expected)
    
if __name__ == '__main__':
    unittest.main()