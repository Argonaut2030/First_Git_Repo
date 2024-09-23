dict = [
  {
    '03.11.2022': {
      'EUR': {
        'sale': 39.4,
        'purchase': 38.4
      },
      'USD': {
        'sale': 39.9,
        'purchase': 39.4
      }
    }
  },
  {
    '02.11.2022'
  }
]

currency = 'EUR'
data = '02.11.2022'
dict[-1][data][currency] = {'sale': 38, 'purchase': 29}
print(dict)