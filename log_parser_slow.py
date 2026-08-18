#import time

#def parse_logs_slow(filename):
#    errors = []
#    with open(filename, 'r', encoding='utf-8') as file:
#        lines = file.readlines()
#        for i, line in enumerate(lines):
#            for word in ['ERROR', 'error', 'ОШИБКА']:
#                if word in line:
#                    errors.append(f"Строка {i}: {line.strip()}")
#                    break  
#    return errors
#start = time.time()
#result = parse_logs_slow('sample.log')
#print(f"Найдено ошибок: {len(result)}")
#print(f"Время выполнения: {time.time() - start:.2f} секунд")

# log_parser.py
import time

def parse_logs_slow(filename):
    """Медленная версия с вложенными циклами"""
    errors = []
    
    # Открываем файл
    with open(filename, 'r', encoding='utf-8') as file:
        # Читаем все строки в список (ПЛОХО для больших файлов!)
        lines = file.readlines()
        
        # Внешний цикл по строкам
        for i, line in enumerate(lines):
            # Внутренний цикл — ищем подстроки (вложенный!)
            for word in ['ERROR', 'error', 'ОШИБКА']:
                if word in line:
                    # Вложенный цикл по символам (ЕЩЁ МЕДЛЕННЕЕ!)
                    for char in line:
                        if char == '!':
                            errors.append(f"Строка {i}: {line.strip()}")
                            break
                    break
    
    return errors

start = time.time()
result = parse_logs_slow('sample.log')
print(f"Найдено ошибок: {len(result)}")
print(f"Время выполнения: {time.time() - start:.2f} секунд")