from matrix import SquareMatrix


class ConsoleApplication:
    def __init__(self):
        self.matrix = SquareMatrix(3)

    def display(self):
        print("Меню команд:")
        print("1. Ввод матрицы")
        print("2. Расчет определителя матрицы")
        print("3. Формирование транспонированной матрицы")
        print("4. Расчет ранга матрицы")
        print("5. Вывод текущего объекта матрицы")
        print("6. Выход")

    def run(self):
        while True:
            self.display()
            choice = input("Введите номер команды: ")

            if choice == "1":
                size = int(input("Введите размер матрицы: "))
                self.matrix = SquareMatrix(size)
                self.matrix.input_matrix()
            elif choice == "2":
                if self.matrix:
                    determinant = self.matrix.calculate_determinant()
                    print(f"Определитель матрицы: {determinant}")
                else:
                    print("Матрица не задана.")
            elif choice == "3":
                if self.matrix:
                    transpose_matrix = self.matrix.calculate_transpose()
                    print("Транспонированная матрица:")
                    transpose_matrix.display_matrix()
                else:
                    print("Матрица не задана.")
            elif choice == "4":
                if self.matrix:
                    rank = self.matrix.calculate_rank()
                    print(f"Ранг матрицы: {rank}")
                else:
                    print("Матрица не задана.")
            elif choice == "5":
                if self.matrix:

                    self.matrix.display_matrix()
                else:
                    print("Матрица не задана.")
            elif choice == "6":
                break

            else:
                print("Некорректный номер команды. Попробуйте еще раз.")
