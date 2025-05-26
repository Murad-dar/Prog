from typing import Dict

class ThermalCalculator:
    """Класс для расчета тепловой мощности"""
    
    # Нормативные значения удельной мощности (Вт/м²)
    POWER_NORMS = {
        'standard': 100,        # Стандартные условия
        'corner_room': 120,     # Угловая комната
        'cold_climate': 150,    # Холодный климат
        'warm_climate': 80,     # Теплый климат
        'good_insulation': 70,  # Хорошая теплоизоляция
        'poor_insulation': 130  # Плохая теплоизоляция
    }
    
    def __init__(self):
        self.climate_coefficient = 1.0
        self.insulation_coefficient = 1.0
        
    def set_climate_conditions(self, climate_type: str):
        """Установка климатических условий"""
        climate_coeffs = {
            'cold': 1.3,        # Холодный климат
            'moderate': 1.0,    # Умеренный климат  
            'warm': 0.8         # Теплый климат
        }
        self.climate_coefficient = climate_coeffs.get(climate_type, 1.0)
    
    def set_insulation_quality(self, insulation_type: str):
        """Установка качества теплоизоляции"""
        insulation_coeffs = {
            'excellent': 0.7,   # Отличная изоляция
            'good': 0.8,        # Хорошая изоляция
            'standard': 1.0,    # Стандартная изоляция
            'poor': 1.3         # Плохая изоляция
        }
        self.insulation_coefficient = insulation_coeffs.get(insulation_type, 1.0)
    
    def calculate_heating_power(self, area: float, room_type: str = 'standard',
                              ceiling_height: float = 2.7) -> Dict:
        """
        Расчет требуемой тепловой мощности
        Args:
            area: площадь помещения (м²)
            room_type: тип помещения
            ceiling_height: высота потолков (м)
        Returns:
            Dict с результатами расчета
        """
        # Базовая мощность
        base_power = area * self.POWER_NORMS.get(room_type, 100)
        
        # Коррекция на высоту потолков
        height_coefficient = ceiling_height / 2.7
        
        # Итоговая мощность с учетом всех коэффициентов
        total_power = (base_power * height_coefficient * 
                      self.climate_coefficient * self.insulation_coefficient)
        
        # Рекомендуемая мощность с запасом 20%
        recommended_power = total_power * 1.2
        
        return {
            'area': area,
            'base_power': round(base_power, 0),
            'adjusted_power': round(total_power, 0),
            'recommended_power': round(recommended_power, 0),
            'power_per_m2': round(recommended_power / area, 1),
            'climate_coeff': self.climate_coefficient,
            'insulation_coeff': self.insulation_coefficient,
            'height_coeff': round(height_coefficient, 2)
        }
    
    def calculate_heating_cost(self, power_kw: float, hours_per_day: float = 8,
                             days_per_month: int = 30, tariff: float = 4.5) -> Dict:
        """
        Расчет стоимости отопления
        Args:
            power_kw: мощность в кВт
            hours_per_day: часов работы в день
            days_per_month: дней в месяце
            tariff: тариф за кВт·ч (руб)
        Returns:
            Dict с расчетом стоимости
        """
        monthly_consumption = power_kw * hours_per_day * days_per_month
        monthly_cost = monthly_consumption * tariff
        yearly_cost = monthly_cost * 7  # Отопительный сезон 7 месяцев
        
        return {
            'power_kw': power_kw,
            'monthly_consumption': round(monthly_consumption, 1),
            'monthly_cost': round(monthly_cost, 2),
            'yearly_cost': round(yearly_cost, 2),
            'tariff': tariff
        }