import arcade
from engine.math import Vector2
from engine.physics import PhysicsEngine
from engine.game_object import GameObject

class GameWindow(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "My Physics Engine")
        arcade.set_background_color(arcade.color.DARK_SLATE_GRAY)
        
        # Инициализация нашего движка
        self.physics_engine = PhysicsEngine()
        self.game_objects = []
        
        self.setup()
    
    def setup(self):
        """Настройка сцены"""
        # Создаём тестовые объекты
        ball = GameObject(
            position=Vector2(400, 300),
            velocity=Vector2(2, 3),
            mass=1.0,
            radius=20,
            color=arcade.color.RED
        )
        self.game_objects.append(ball)
        
        # Статичный объект
        static_obj = GameObject(
            position=Vector2(200, 100),
            velocity=Vector2(0, 0),
            mass=0,  # mass=0 означает статичный объект
            radius=30,
            color=arcade.color.BLUE
        )
        self.game_objects.append(static_obj)
    
    def on_draw(self):
        """Отрисовка кадра"""
        self.clear()
        
        # Рисуем все объекты
        for obj in self.game_objects:
            obj.draw()
        
        # Отладочная информация
        arcade.draw_text(
            f"Objects: {len(self.game_objects)} | FPS: {arcade.get_fps():.1f}",
            10, 10, arcade.color.WHITE, 14
        )
    
    def on_update(self, delta_time):
        """Обновление физики"""
        # Обновляем физику для всех объектов
        self.physics_engine.update(self.game_objects, delta_time)
    
    def on_mouse_press(self, x, y, button, modifiers):
        """Создаём новый объект по клику"""
        if button == arcade.MOUSE_BUTTON_LEFT:
            new_ball = GameObject(
                position=Vector2(x, y),
                velocity=Vector2(0, 0),
                mass=1.0,
                radius=15,
                color=arcade.color.GREEN
            )
            self.game_objects.append(new_ball)

if __name__ == "__main__":
    window = GameWindow()
    arcade.run()