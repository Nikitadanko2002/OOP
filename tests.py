import unittest
from matrix import SquareMatrix


class SquareMatrixTests(unittest.TestCase):
    def test_calculate_determinant(self):
        # Тестирование расчета определителя матрицы для квадратной матрицы 2x2
        matrix_2x2 = SquareMatrix(2)
        matrix_2x2.matrix = [[2, 3], [4, 5]]
        determinant_2x2 = matrix_2x2.calculate_determinant()
        self.assertEqual(determinant_2x2, -2)

        # Тестирование расчета определителя матрицы для квадратной матрицы 3x3
        matrix_3x3 = SquareMatrix(3)
        matrix_3x3.matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        determinant_3x3 = matrix_3x3.calculate_determinant()
        self.assertEqual(determinant_3x3, 0)

    def test_calculate_transpose(self):
        # Тестирование формирования транспонированной матрицы для квадратной матрицы 2x2
        matrix_2x2 = SquareMatrix(2)
        matrix_2x2.matrix = [[1, 2], [3, 4]]
        transpose_matrix_2x2 = matrix_2x2.calculate_transpose()
        expected_matrix_2x2 = [[1, 3], [2, 4]]
        self.assertEqual(transpose_matrix_2x2.matrix, expected_matrix_2x2)

        # Тестирование формирования транспонированной матрицы для квадратной матрицы 3x3
        matrix_3x3 = SquareMatrix(3)
        matrix_3x3.matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        transpose_matrix_3x3 = matrix_3x3.calculate_transpose()
        expected_matrix_3x3 = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
        self.assertEqual(transpose_matrix_3x3.matrix, expected_matrix_3x3)

    def test_calculate_rank(self):
        # Тестирование расчета ранга матрицы для квадратной матрицы 2x2
        matrix_2x2 = SquareMatrix(2)
        matrix_2x2.matrix = [[1, 2], [3, 4]]
        rank_2x2 = matrix_2x2.calculate_rank()
        self.assertEqual(rank_2x2, 2)

        # Тестирование расчета ранга матрицы для квадратной матрицы 3x3
        matrix_3x3 = SquareMatrix(3)
        matrix_3x3.matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        rank_3x3 = matrix_3x3.calculate_rank()
        self.assertEqual(rank_3x3, 3)


if __name__ == "__main__":
    unittest.main()

