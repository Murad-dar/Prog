import math
from typing import Dict, List, Tuple

class RoomCalculator:
    """Класс для расчета площади помещений"""
    
    def __init__(self):
        self.rooms_data = []
    
    def calculate_room_area(self, length: float, width: float, height: float = 2.7) -> Dict:
        """
        Расчет площади комнаты
        Args:
            length: длина комнаты (м)
            width: ширина комнаты (м) 
            height: высота комнаты (м)
        Returns:
            Dict с результатами расчета
        """
        floor_area = length * width
        wall_area = 2 * (length + width) * height
        total_area = floor_area + wall_area
        volume = length * width * height
        
        return {
            'type': 'Комната',
            'dimensions': f'{length}×{width}×{height}',
            'floor_area': round(floor_area, 2),
            'wall_area': round(wall_area, 2),
            'total_area': round(total_area, 2),
            'volume': round(volume, 2)
        }
    
    def calculate_apartment_area(self, rooms: List[Dict]) -> Dict:
        """
        Расчет общей площади квартиры
        Args:
            rooms: список комнат с параметрами
        Returns:
            Dict с результатами расчета
        """
        total_floor_area = 0
        total_wall_area = 0
        total_volume = 0
        room_count = len(rooms)
        
        for room in rooms:
            area_data = self.calculate_room_area(
                room['length'], room['width'], room.get('height', 2.7)
            )
            total_floor_area += area_data['floor_area']
            total_wall_area += area_data['wall_area']
            total_volume += area_data['volume']
        
        return {
            'type': 'Квартира',
            'room_count': room_count,
            'floor_area': round(total_floor_area, 2),
            'wall_area': round(total_wall_area, 2),
            'total_area': round(total_floor_area + total_wall_area, 2),
            'volume': round(total_volume, 2)
        }
    
    def calculate_building_area(self, floors: int, apartments_per_floor: int, 
                              avg_apartment_area: float) -> Dict:
        """
        Расчет площади многоэтажного дома
        Args:
            floors: количество этажей
            apartments_per_floor: квартир на этаже
            avg_apartment_area: средняя площадь квартиры (м²)
        Returns:
            Dict с результатами расчета
        """
        total_apartments = floors * apartments_per_floor
        total_residential_area = total_apartments * avg_apartment_area
        
        # Добавляем площадь общих помещений (лестницы, коридоры) - 20% от жилой площади
        common_area = total_residential_area * 0.2
        total_area = total_residential_area + common_area
        
        # Примерный объем здания (высота этажа 3м)
        building_volume = total_area * 3 * floors
        
        return {
            'type': 'Многоэтажный дом',
            'floors': floors,
            'apartments': total_apartments,
            'residential_area': round(total_residential_area, 2),
            'common_area': round(common_area, 2),
            'total_area': round(total_area, 2),
            'volume': round(building_volume, 2)
        }
