from n1 import requiredTime
if __name__ == '__main__':
    # Подготовка тестов
    _distances = [ [10.0, 10.0], [11.0, 330.0, 11.22], [3.0], [55121.22, 991.2] ]           # Длины отрезков на пути
    _speeds = [ [2.0,2.0], [1.0, 2.1111111, 9.000000001], [3.0], [991299.0, 128484828.0]]   # Ограничитель скорости на отрезке
    _accelerations = [2.0, 1.0, 3.0, 5.0]                                                   # Изменение скорости машины при разгоне/торможении
    Tests = zip(_distances, _speeds, _accelerations)

    # Тестим
    for distances, speeds, acceleration in Tests:
        print(
            requiredTime(distances, speeds, acceleration)
        )
