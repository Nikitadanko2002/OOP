#


number = float #Абстрактный тип number

class SquareMatrix:

    def __init__(self, size: int):
        """
                    Конструктор класса "Квадратная матрица".

                    Параметры:
                    - size: int - размерность матрицы
        """
        self.__size = size
        self.matrix = [[0] * size for _ in range(size)]

    def input_matrix(self):
        """
                Метод для ввода элементов матрицы с клавиатуры.
        """
        for i in range(self.__size):
            for j in range(self.__size):
                self.matrix[i][j] = number(input(f"Элемент [{i + 1}][{j + 1}]: "))

    def calculate_determinant(self) -> number:
        """
                Метод для вычисления определителя матрицы.

                Возвращает:
                - float - значение определителя
        """
        if self.__size == 1:
            return self.matrix[0][0]
        elif self.__size == 2:
            return self.matrix[0][0] * self.matrix[1][1] - self.matrix[0][1] * self.matrix[1][0]
        else:
            determinant = 0
            for j in range(self.__size):
                submatrix = self.get_submatrix(0, j)
                determinant += ((-1) ** j) * self.matrix[0][j] * submatrix.calculate_determinant()
            return determinant

    def calculate_transpose(self) -> "SquareMatrix":
        """
                Метод для вычисления транспонированной матрицы.

                Возвращает:
                - SquareMatrix - транспонированная матрица
        """
        transpose_matrix = SquareMatrix(self.__size)
        for i in range(self.__size):
            for j in range(self.__size):
                transpose_matrix.matrix[i][j] = self.matrix[j][i]
        return transpose_matrix

    def calculate_rank(self) -> int:
        """
                Метод для вычисления ранга матрицы.

                Возвращает:
                - int - значение ранга
        """
        rows = len(self.matrix)
        cols = len(self.matrix[0])

        rank = 0

        for row in range(rows):
            non_zero_found = False

            for col in range(cols):
                if self.matrix[row][col] != 0:
                    non_zero_found = True
                    break

            if non_zero_found:
                rank += 1

                for r in range(row + 1, rows):
                    multiplier = self.matrix[r][col] / self.matrix[row][col]

                    for c in range(cols):
                        self.matrix[r][c] -= multiplier * self.matrix[row][c]

        return rank

    def display_matrix(self):
        """
                Метод для вывода матрицы на экран.
        """
        for row in self.matrix:
            print(row)

    def get_submatrix(self, row_index: int, col_index: int):
        """
               Метод для получения подматрицы путем удаления указанной строки и столбца.

               Параметры:
               - row_index: int - индекс удаляемой строки
               - col_index: int - индекс удаляемого столбца

               Возвращает:
               - SquareMatrix - подматрица
        """
        submatrix = SquareMatrix(self.__size - 1)
        for i in range(self.__size):
            if i == row_index:
                continue
            for j in range(self.__size):
                if j == col_index:
                    continue
                submatrix.matrix[i - (i > row_index)][j - (j > col_index)] = self.matrix[i][j]
        return submatrix
