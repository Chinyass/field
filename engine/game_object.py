import arcade
from .math.vector2 import Vector2

class GameObject:
    """Базовый класс для всех игровых объектов"""
    
    def __init__(self, position, velocity, mass, radius, color):
        self.position = position
        self.velocity = velocity
        self.mass = mass
        self.radius = radius
        self.color = color
    
    def draw(self):
        """Отрисовка объекта"""
        arcade.draw_circle_filled(
            self.position.x, self.position.y, 
            self.radius, self.color
        )
        
        # Отладочная линия показывающая направление скорости
        if self.velocity.length() > 0:
            direction = self.position + self.velocity.normalize() * self.radius
            arcade.draw_line(
                self.position.x, self.position.y,
                direction.x, direction.y,
                arcade.color.WHITE, 2
            )