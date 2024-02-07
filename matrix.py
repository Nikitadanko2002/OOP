class SquareMatrix:
    def __init__(self, size : int):
        self.size = size
        self.matrix = [[0] * size for _ in range(size)]


    def input_matrix(self):
        print("Введите элементы матрицы:")
        for i in range(self.size):
            for j in range(self.size):
                self.matrix[i][j] = float(input(f"Элемент [{i + 1}][{j + 1}]: "))

    def calculate_determinant(self):
        if self.size == 1:
            return self.matrix[0][0]
        elif self.size == 2:
            return self.matrix[0][0] * self.matrix[1][1] - self.matrix[0][1] * self.matrix[1][0]
        else:
            determinant = 0
            for j in range(self.size):
                submatrix = self.get_submatrix(0, j)
                determinant += ((-1) ** j) * self.matrix[0][j] * submatrix.calculate_determinant()
            return determinant

    def calculate_transpose(self):
        transpose_matrix = SquareMatrix(self.size)
        for i in range(self.size):
            for j in range(self.size):
                transpose_matrix.matrix[i][j] = self.matrix[j][i]
        return transpose_matrix

    def calculate_rank(self) -> int:
        rank = self.size
        for row in self.matrix:
            if all(element == 0 for element in row):
                rank -= 1
        return rank

    def display_matrix(self):
        print("Матрица:")
        for row in self.matrix:
            print(row)

    def get_submatrix(self, row_index: int, col_index: int):
        submatrix = SquareMatrix(self.size - 1)
        for i in range(self.size):
            if i == row_index:
                continue
            for j in range(self.size):
                if j == col_index:
                    continue
                submatrix.matrix[i - (i > row_index)][j - (j > col_index)] = self.matrix[i][j]
        return submatrix

