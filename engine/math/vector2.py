import math

class Vector2:
    """2D вектор для математики движка"""
    
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        """Сложение векторов"""
        return Vector2(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        """Вычитание векторов"""
        return Vector2(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        """Умножение на скаляр"""
        return Vector2(self.x * scalar, self.y * scalar)
    
    def __truediv__(self, scalar):
        """Деление на скаляр"""
        return Vector2(self.x / scalar, self.y / scalar)
    
    def length(self):
        """Длина вектора"""
        return math.sqrt(self.x**2 + self.y**2)
    
    def normalize(self):
        """Нормализация вектора (длина = 1)"""
        length = self.length()
        if length > 0:
            return Vector2(self.x / length, self.y / length)
        return Vector2(0, 0)
    
    def dot(self, other):
        """Скалярное произведение"""
        return self.x * other.x + self.y * other.y
    
    def distance_to(self, other):
        """Расстояние до другого вектора"""
        return (self - other).length()
    
    def __repr__(self):
        return f"Vector2({self.x:.2f}, {self.y:.2f})"