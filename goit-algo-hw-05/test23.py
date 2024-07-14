
import re

def generator_numbers(text:str):
   
   numbers = re.findall(r"\d*\.?\d+",text)
   for n in numbers:
      yield float(n)
      



text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
# numbers = re.findall(r"\d*\.?\d+",text)
# print(numbers)
# for n in numbers:
#     print (n)


for i  in generator_numbers(text):
    print(i)