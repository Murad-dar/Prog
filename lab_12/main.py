import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import sys
import os

# Добавляем путь к пакету
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from heating_package import RoomCalculator, ThermalCalculator, ReportGenerator

class HeatingCalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор отопления помещений")
        self.root.geometry("800x700")
        self.root.resizable(True, True)
        
        # Инициализация калькуляторов
        self.room_calc = RoomCalculator()
        self.thermal_calc = ThermalCalculator()
        self.report_gen = ReportGenerator()
        
        # Переменные для хранения результатов
        self.calculation_result = None
        self.thermal_result = None
        self.cost_result = None
        
        self.setup_ui()
    
    def setup_ui(self):
        """Создание пользовательского интерфейса"""
        
        # Главный контейнер с прокруткой
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Заголовок
        title_label = ttk.Label(main_frame, text="Калькулятор отопления помещений", 
                               font=('Arial', 16, 'bold'))
        title_label.pack(pady=(0, 20))
        
        # Notebook для вкладок
        notebook = ttk.Notebook(main_frame)
        notebook.pack(fill=tk.BOTH, expand=True)
        
        # Вкладка расчета площади
        self.area_frame = ttk.Frame(notebook)
        notebook.add(self.area_frame, text="Расчет площади")
        self.setup_area_tab()
        
        # Вкладка теплового расчета
        self.thermal_frame = ttk.Frame(notebook)
        notebook.add(self.thermal_frame, text="Тепловой расчет")
        self.setup_thermal_tab()
        
        # Вкладка результатов
        self.results_frame = ttk.Frame(notebook)
        notebook.add(self.results_frame, text="Результаты")
        self.setup_results_tab()
    
    def setup_area_tab(self):
        """Настройка вкладки расчета площади"""
        
        # Тип помещения
        type_frame = ttk.LabelFrame(self.area_frame, text="Тип помещения")
        type_frame.pack(fill=tk.X, padx=5, pady=5)
        
        self.room_type = tk.StringVar(value="room")
        ttk.Radiobutton(type_frame, text="Комната", variable=self.room_type, 
                       value="room", command=self.on_room_type_change).pack(anchor=tk.W)
        ttk.Radiobutton(type_frame, text="Квартира", variable=self.room_type, 
                       value="apartment", command=self.on_room_type_change).pack(anchor=tk.W)
        ttk.Radiobutton(type_frame, text="Многоэтажный дом", variable=self.room_type, 
                       value="building", command=self.on_room_type_change).pack(anchor=tk.W)
        
        # Контейнер для параметров
        self.params_frame = ttk.LabelFrame(self.area_frame, text="Параметры")
        self.params_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.setup_room_params()
        
        # Кнопка расчета
        calc_button = ttk.Button(self.area_frame, text="Рассчитать площадь", 
                                command=self.calculate_area)
        calc_button.pack(pady=10)
    
    def setup_room_params(self):
        """Настройка параметров для комнаты"""
        # Очистка предыдущих виджетов
        for widget in self.params_frame.winfo_children():
            widget.destroy()
        
        if self.room_type.get() == "room":
            # Параметры комнаты
            ttk.Label(self.params_frame, text="Длина (м):").grid(row=0, column=0, sticky=tk.W, padx=5, pady=2)
            self.length_var = tk.DoubleVar(value=5.0)
            ttk.Entry(self.params_frame, textvariable=self.length_var, width=10).grid(row=0, column=1, padx=5, pady=2)
            
            ttk.Label(self.params_frame, text="Ширина (м):").grid(row=1, column=0, sticky=tk.W, padx=5, pady=2)
            self.width_var = tk.DoubleVar(value=4.0)
            ttk.Entry(self.params_frame, textvariable=self.width_var, width=10).grid(row=1, column=1, padx=5, pady=2)
            
            ttk.Label(self.params_frame, text="Высота (м):").grid(row=2, column=0, sticky=tk.W, padx=5, pady=2)
            self.height_var = tk.DoubleVar(value=2.7)
            ttk.Entry(self.params_frame, textvariable=self.height_var, width=10).grid(row=2, column=1, padx=5, pady=2)
            
        elif self.room_type.get() == "apartment":
            # Параметры квартиры
            ttk.Label(self.params_frame, text="Количество комнат:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=2)
            self.room_count_var = tk.IntVar(value=3)
            ttk.Entry(self.params_frame, textvariable=self.room_count_var, width=10).grid(row=0, column=1, padx=5, pady=2)
            
            ttk.Label(self.params_frame, text="Средняя длина комнаты (м):").grid(row=1, column=0, sticky=tk.W, padx=5, pady=2)
            self.avg_length_var = tk.DoubleVar(value=4.5)
            ttk.Entry(self.params_frame, textvariable=self.avg_length_var, width=10).grid(row=1, column=1, padx=5, pady=2)
            
            ttk.Label(self.params_frame, text="Средняя ширина комнаты (м):").grid(row=2, column=0, sticky=tk.W, padx=5, pady=2)
            self.avg_width_var = tk.DoubleVar(value=3.5)
            ttk.Entry(self.params_frame, textvariable=self.avg_width_var, width=10).grid(row=2, column=1, padx=5, pady=2)
            
            ttk.Label(self.params_frame, text="Высота потолков (м):").grid(row=3, column=0, sticky=tk.W, padx=5, pady=2)
            self.height_var = tk.DoubleVar(value=2.7)
            ttk.Entry(self.params_frame, textvariable=self.height_var, width=10).grid(row=3, column=1, padx=5, pady=2)
            
        elif self.room_type.get() == "building":
            # Параметры здания
            ttk.Label(self.params_frame, text="Количество этажей:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=2)
            self.floors_var = tk.IntVar(value=9)
            ttk.Entry(self.params_frame, textvariable=self.floors_var, width=10).grid(row=0, column=1, padx=5, pady=2)
            
            ttk.Label(self.params_frame, text="Квартир на этаже:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=2)
            self.apt_per_floor_var = tk.IntVar(value=4)
            ttk.Entry(self.params_frame, textvariable=self.apt_per_floor_var, width=10).grid(row=1, column=1, padx=5, pady=2)
            
            ttk.Label(self.params_frame, text="Средняя площадь квартиры (м²):").grid(row=2, column=0, sticky=tk.W, padx=5, pady=2)
            self.avg_apt_area_var = tk.DoubleVar(value=65.0)
            ttk.Entry(self.params_frame, textvariable=self.avg_apt_area_var, width=10).grid(row=2, column=1, padx=5, pady=2)
    
    def on_room_type_change(self):
        """Обработчик изменения типа помещения"""
        self.setup_room_params()
    
    def setup_thermal_tab(self):
        """Настройка вкладки теплового расчета"""
        
        # Климатические условия
        climate_frame = ttk.LabelFrame(self.thermal_frame, text="Климатические условия")
        climate_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Label(climate_frame, text="Климат:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=2)
        self.climate_var = tk.StringVar(value="moderate")
        climate_combo = ttk.Combobox(climate_frame, textvariable=self.climate_var, 
                                   values=["cold", "moderate", "warm"], 
                                   state="readonly", width=12)
        climate_combo.grid(row=0, column=1, padx=5, pady=2)
        
        # Качество изоляции
        insulation_frame = ttk.LabelFrame(self.thermal_frame, text="Теплоизоляция")
        insulation_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Label(insulation_frame, text="Качество изоляции:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=2)
        self.insulation_var = tk.StringVar(value="standard")
        insulation_combo = ttk.Combobox(insulation_frame, textvariable=self.insulation_var,
                                      values=["excellent", "good", "standard", "poor"],
                                      state="readonly", width=12)
        insulation_combo.grid(row=0, column=1, padx=5, pady=2)
        
        # Дополнительные параметры
        additional_frame = ttk.LabelFrame(self.thermal_frame, text="Дополнительные параметры")
        additional_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Label(additional_frame, text="Тип помещения:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=2)
        self.thermal_room_type = tk.StringVar(value="standard")
        room_type_combo = ttk.Combobox(additional_frame, textvariable=self.thermal_room_type,
                                     values=["standard", "corner_room", "cold_climate", "warm_climate"],
                                     state="readonly", width=15)
        room_type_combo.grid(row=0, column=1, padx=5, pady=2)
        
        # Расчет стоимости
        cost_frame = ttk.LabelFrame(self.thermal_frame, text="Расчет стоимости отопления")
        cost_frame.pack(fill=tk.X, padx=5, pady=5)
        
        self.calculate_cost_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(cost_frame, text="Рассчитать стоимость", 
                       variable=self.calculate_cost_var,
                       command=self.toggle_cost_params).pack(anchor=tk.W)
        
        self.cost_params_frame = ttk.Frame(cost_frame)
        self.cost_params_frame.pack(fill=tk.X, padx=20)
        
        ttk.Label(self.cost_params_frame, text="Часов работы в день:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=2)
        self.hours_per_day_var = tk.DoubleVar(value=8.0)
        ttk.Entry(self.cost_params_frame, textvariable=self.hours_per_day_var, width=8).grid(row=0, column=1, padx=5, pady=2)
        
        ttk.Label(self.cost_params_frame, text="Тариф (руб/кВт·ч):").grid(row=1, column=0, sticky=tk.W, padx=5, pady=2)
        self.tariff_var = tk.DoubleVar(value=4.5)
        ttk.Entry(self.cost_params_frame, textvariable=self.tariff_var, width=8).grid(row=1, column=1, padx=5, pady=2)
        
        # Кнопка расчета
        calc_thermal_button = ttk.Button(self.thermal_frame, text="Рассчитать тепловую мощность", 
                                       command=self.calculate_thermal)
        calc_thermal_button.pack(pady=10)
    
    def toggle_cost_params(self):
        """Показать/скрыть параметры расчета стоимости"""
        if self.calculate_cost_var.get():
            self.cost_params_frame.pack(fill=tk.X, padx=20)
        else:
            self.cost_params_frame.pack_forget()
    
    def setup_results_tab(self):
        """Настройка вкладки результатов"""
        
        # Текстовое поле для результатов
        self.results_text = tk.Text(self.results_frame, wrap=tk.WORD, font=('Courier', 10))
        scrollbar = ttk.Scrollbar(self.results_frame, orient=tk.VERTICAL, command=self.results_text.yview)
        self.results_text.configure(yscrollcommand=scrollbar.set)
        
        self.results_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Кнопки для сохранения отчетов
        buttons_frame = ttk.Frame(self.results_frame)
        buttons_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=5, pady=5)
        
        ttk.Button(buttons_frame, text="Сохранить в DOCX", 
                  command=self.save_docx_report).pack(side=tk.LEFT, padx=5)
        ttk.Button(buttons_frame, text="Сохранить в XLSX", 
                  command=self.save_xlsx_report).pack(side=tk.LEFT, padx=5)
        ttk.Button(buttons_frame, text="Очистить результаты", 
                  command=self.clear_results).pack(side=tk.RIGHT, padx=5)
    
    def calculate_area(self):
        """Расчет площади помещения"""
        try:
            if self.room_type.get() == "room":
                length = self.length_var.get()
                width = self.width_var.get()
                height = self.height_var.get()
                
                if length <= 0 or width <= 0 or height <= 0:
                    raise ValueError("Размеры должны быть положительными")
                
                self.calculation_result = self.room_calc.calculate_room_area(length, width, height)
                
            elif self.room_type.get() == "apartment":
                room_count = self.room_count_var.get()
                avg_length = self.avg_length_var.get()
                avg_width = self.avg_width_var.get()
                height = self.height_var.get()
                
                if room_count <= 0 or avg_length <= 0 or avg_width <= 0 or height <= 0:
                    raise ValueError("Все параметры должны быть положительными")
                
                # Создаем список комнат
                rooms = []
                for i in range(room_count):
                    rooms.append({
                        'length': avg_length,
                        'width': avg_width,
                        'height': height
                    })
                
                self.calculation_result = self.room_calc.calculate_apartment_area(rooms)
                
            elif self.room_type.get() == "building":
                floors = self.floors_var.get()
                apt_per_floor = self.apt_per_floor_var.get()
                avg_apt_area = self.avg_apt_area_var.get()
                
                if floors <= 0 or apt_per_floor <= 0 or avg_apt_area <= 0:
                    raise ValueError("Все параметры должны быть положительными")
                
                self.calculation_result = self.room_calc.calculate_building_area(
                    floors, apt_per_floor, avg_apt_area)
            
            self.update_results_display()
            messagebox.showinfo("Успех", "Расчет площади выполнен успешно!")
            
        except ValueError as e:
            messagebox.showerror("Ошибка", f"Ошибка в данных: {str(e)}")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Произошла ошибка: {str(e)}")
    
    def calculate_thermal(self):
        """Расчет тепловой мощности"""
        try:
            if self.calculation_result is None:
                messagebox.showwarning("Предупреждение", 
                                     "Сначала выполните расчет площади!")
                return
            
            # Устанавливаем параметры климата и изоляции
            self.thermal_calc.set_climate_conditions(self.climate_var.get())
            self.thermal_calc.set_insulation_quality(self.insulation_var.get())
            
            # Получаем площадь для расчета
            if 'floor_area' in self.calculation_result:
                area = self.calculation_result['floor_area']
            elif 'total_area' in self.calculation_result:
                area = self.calculation_result['total_area']
            else:
                raise ValueError("Не найдена площадь для расчета")
            
            # Определяем высоту потолков
            if hasattr(self, 'height_var'):
                ceiling_height = self.height_var.get()
            else:
                ceiling_height = 2.7
            
            # Расчет тепловой мощности
            self.thermal_result = self.thermal_calc.calculate_heating_power(
                area, self.thermal_room_type.get(), ceiling_height)
            
            # Расчет стоимости, если требуется
            if self.calculate_cost_var.get():
                power_kw = self.thermal_result['recommended_power'] / 1000
                hours = self.hours_per_day_var.get()
                tariff = self.tariff_var.get()
                
                self.cost_result = self.thermal_calc.calculate_heating_cost(
                    power_kw, hours, 30, tariff)
            else:
                self.cost_result = None
            
            self.update_results_display()
            messagebox.showinfo("Успех", "Тепловой расчет выполнен успешно!")
            
        except ValueError as e:
            messagebox.showerror("Ошибка", f"Ошибка в данных: {str(e)}")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Произошла ошибка: {str(e)}")
    
    def update_results_display(self):
        """Обновление отображения результатов"""
        self.results_text.delete(1.0, tk.END)
        
        result_text = "РЕЗУЛЬТАТЫ РАСЧЕТА\n"
        result_text += "=" * 50 + "\n\n"
        
        # Результаты расчета площади
        if self.calculation_result:
            result_text += "РАСЧЕТ ПЛОЩАДИ ПОМЕЩЕНИЯ\n"
            result_text += "-" * 30 + "\n"
            result_text += f"Тип помещения: {self.calculation_result['type']}\n"
            
            if 'dimensions' in self.calculation_result:
                result_text += f"Размеры: {self.calculation_result['dimensions']} м\n"
            
            if 'room_count' in self.calculation_result:
                result_text += f"Количество комнат: {self.calculation_result['room_count']}\n"
            
            if 'floors' in self.calculation_result:
                result_text += f"Этажей: {self.calculation_result['floors']}\n"
                result_text += f"Квартир: {self.calculation_result['apartments']}\n"
            
            if 'floor_area' in self.calculation_result:
                result_text += f"Площадь пола: {self.calculation_result['floor_area']} м²\n"
            
            if 'wall_area' in self.calculation_result:
                result_text += f"Площадь стен: {self.calculation_result['wall_area']} м²\n"
            
            if 'residential_area' in self.calculation_result:
                result_text += f"Жилая площадь: {self.calculation_result['residential_area']} м²\n"
                result_text += f"Площадь общих помещений: {self.calculation_result['common_area']} м²\n"
            
            result_text += f"Общая площадь: {self.calculation_result['total_area']} м²\n"
            result_text += f"Объем: {self.calculation_result['volume']} м³\n\n"
        
        # Результаты теплового расчета
        if self.thermal_result:
            result_text += "РАСЧЕТ ТЕПЛОВОЙ МОЩНОСТИ\n"
            result_text += "-" * 30 + "\n"
            result_text += f"Площадь для расчета: {self.thermal_result['area']} м²\n"
            result_text += f"Базовая мощность: {self.thermal_result['base_power']} Вт\n"
            result_text += f"Скорректированная мощность: {self.thermal_result['adjusted_power']} Вт\n"
            result_text += f"Рекомендуемая мощность: {self.thermal_result['recommended_power']} Вт "
            result_text += f"({self.thermal_result['recommended_power']/1000:.1f} кВт)\n"
            result_text += f"Удельная мощность: {self.thermal_result['power_per_m2']} Вт/м²\n\n"
            
            result_text += "КОЭФФИЦИЕНТЫ РАСЧЕТА\n"
            result_text += "-" * 20 + "\n"
            result_text += f"Коэффициент климата: {self.thermal_result['climate_coeff']}\n"
            result_text += f"Коэффициент теплоизоляции: {self.thermal_result['insulation_coeff']}\n"
            result_text += f"Коэффициент высоты: {self.thermal_result['height_coeff']}\n\n"
        
        # Результаты расчета стоимости
        if self.cost_result:
            result_text += "РАСЧЕТ СТОИМОСТИ ОТОПЛЕНИЯ\n"
            result_text += "-" * 30 + "\n"
            result_text += f"Мощность оборудования: {self.cost_result['power_kw']} кВт\n"
            result_text += f"Месячное потребление: {self.cost_result['monthly_consumption']} кВт·ч\n"
            result_text += f"Стоимость в месяц: {self.cost_result['monthly_cost']} руб.\n"
            result_text += f"Стоимость за сезон: {self.cost_result['yearly_cost']} руб.\n"
            result_text += f"Тариф: {self.cost_result['tariff']} руб./кВт·ч\n\n"
        
        self.results_text.insert(1.0, result_text)
    
    def save_docx_report(self):
        """Сохранение отчета в формате DOCX"""
        if not self.calculation_result:
            messagebox.showwarning("Предупреждение", "Нет данных для сохранения!")
            return
        
        try:
            filename = filedialog.asksaveasfilename(
                defaultextension=".docx",
                filetypes=[("Word документы", "*.docx"), ("Все файлы", "*.*")],
                title="Сохранить отчет как..."
            )
            
            if filename:
                self.report_gen.set_data(self.calculation_result, 
                                       self.thermal_result, 
                                       self.cost_result)
                saved_path = self.report_gen.generate_docx_report(filename)
                messagebox.showinfo("Успех", f"Отчет сохранен: {saved_path}")
                
        except ImportError:
            messagebox.showerror("Ошибка", 
                               "Для сохранения в DOCX требуется установить пакет python-docx:\n"
                               "pip install python-docx")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Ошибка при сохранении: {str(e)}")
    
    def save_xlsx_report(self):
        """Сохранение отчета в формате XLSX"""
        if not self.calculation_result:
            messagebox.showwarning("Предупреждение", "Нет данных для сохранения!")
            return
        
        try:
            filename = filedialog.asksaveasfilename(
                defaultextension=".xlsx",
                filetypes=[("Excel файлы", "*.xlsx"), ("Все файлы", "*.*")],
                title="Сохранить отчет как..."
            )
            
            if filename:
                self.report_gen.set_data(self.calculation_result, 
                                       self.thermal_result, 
                                       self.cost_result)
                saved_path = self.report_gen.generate_xlsx_report(filename)
                messagebox.showinfo("Успех", f"Отчет сохранен: {saved_path}")
                
        except ImportError:
            messagebox.showerror("Ошибка", 
                               "Для сохранения в XLSX требуется установить пакет openpyxl:\n"
                               "pip install openpyxl")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Ошибка при сохранении: {str(e)}")
    
    def clear_results(self):
        """Очистка результатов"""
        self.results_text.delete(1.0, tk.END)
        self.calculation_result = None
        self.thermal_result = None
        self.cost_result = None

def main():
    """Главная функция приложения"""
    root = tk.Tk()
    app = HeatingCalculatorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
