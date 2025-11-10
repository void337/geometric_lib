def area(a, b): 
    '''
    Принимает стороны прямоугольника и возвращает площадь
        Параметры:
            a (int/float): первая сторона прямоугольника
            b (int/float): вторая сторона прямоугольника
        Возвращаемое значение:
            area (int/float): площадь прямоугольника
        Исключения:
            TypeError: если стороны не числа
            ValueError: если стороны отрицательные
    '''  
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Стороны должны быть числами")
    if a < 0 or b < 0:
        raise ValueError("Стороны не могут быть отрицательными")
    return a * b 

def perimeter(a, b): 
    '''
    Принимает стороны прямоугольника и возвращает периметр
        Параметры:
            a (int/float): первая сторона прямоугольника
            b (int/float): вторая сторона прямоугольника
        Возвращаемое значение:
            perimeter (int/float): периметр прямоугольника
        Исключения:
            TypeError: если стороны не числа
            ValueError: если стороны отрицательные
    ''' 
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Стороны должны быть числами")
    if a < 0 or b < 0:
        raise ValueError("Стороны не могут быть отрицательными")
    return 2*a + 2*b