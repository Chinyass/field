from ..math.vector2 import Vector2

class PhysicsEngine:
    """Простой физический движок"""
    
    def __init__(self):
        self.gravity = Vector2(0, -300)  # пиксели/секунду²
        self.damping = 0.99  # замедление для симуляции трения
    
    def update(self, game_objects, delta_time):
        """Обновление физики для всех объектов"""
        for obj in game_objects:
            if obj.mass > 0:  # Только для динамических объектов
                self._apply_physics(obj, delta_time)
        
        # Проверка столкновений
        self._check_collisions(game_objects)
    
    def _apply_physics(self, obj, delta_time):
        """Применяем физику к объекту"""
        # F = ma, но a = F/m, а F_gravity = m * g
        # поэтому a = g (ускорение не зависит от массы)
        acceleration = self.gravity
        
        # Интегрирование: v = v0 + a*t
        obj.velocity = obj.velocity + acceleration * delta_time
        
        # Применяем damping (трение)
        obj.velocity = obj.velocity * self.damping
        
        # Интегрирование: x = x0 + v*t
        obj.position = obj.position + obj.velocity * delta_time
        
        # Обработка столкновений с границами экрана
        self._handle_screen_bounds(obj)
    
    def _handle_screen_bounds(self, obj):
        """Обработка столкновений с границами экрана"""
        # Правая граница
        if obj.position.x + obj.radius > 800:
            obj.position.x = 800 - obj.radius
            obj.velocity.x = -obj.velocity.x * 0.8  # упругость
        
        # Левая граница
        if obj.position.x - obj.radius < 0:
            obj.position.x = obj.radius
            obj.velocity.x = -obj.velocity.x * 0.8
        
        # Верхняя граница
        if obj.position.y + obj.radius > 600:
            obj.position.y = 600 - obj.radius
            obj.velocity.y = -obj.velocity.y * 0.8
        
        # Нижняя граница
        if obj.position.y - obj.radius < 0:
            obj.position.y = obj.radius
            obj.velocity.y = -obj.velocity.y * 0.8
    
    def _check_collisions(self, game_objects):
        """Простая проверка столкновений между шарами"""
        for i in range(len(game_objects)):
            for j in range(i + 1, len(game_objects)):
                obj1 = game_objects[i]
                obj2 = game_objects[j]
                
                # Расстояние между центрами
                distance = obj1.position.distance_to(obj2.position)
                min_distance = obj1.radius + obj2.radius
                
                if distance < min_distance:
                    self._resolve_collision(obj1, obj2)
    
    def _resolve_collision(self, obj1, obj2):
        """Обработка столкновения двух шаров"""
        # Вектор от obj1 к obj2
        collision_vector = obj2.position - obj1.position
        distance = collision_vector.length()
        
        if distance == 0:
            return
            
        # Нормализованный вектор столкновения
        collision_normal = collision_vector.normalize()
        
        # Разделяем объекты чтобы они не пересекались
        overlap = (obj1.radius + obj2.radius) - distance
        separation = collision_normal * (overlap / 2)
        
        if obj1.mass > 0:
            obj1.position = obj1.position - separation
        if obj2.mass > 0:
            obj2.position = obj2.position + separation
        
        # TODO: Здесь можно добавить обмен импульсами
        # для более реалистичной физики