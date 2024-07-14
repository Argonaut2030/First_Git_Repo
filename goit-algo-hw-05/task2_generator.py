
from typing import Callable
import re

# створюємо функцію, яка знаходить в тексті числа та повертає їх  списком
def generator_numbers(text:str):
   
   numbers = re.findall(r"\d*\.?\d+",text)
   for n in numbers:
      yield float(n)
      
# функція підрахунку загальної суми ЗП

def sum_profit (text: str, func: Callable):
   total = 0
   for i in func(text):
     total += i
   return total  

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")