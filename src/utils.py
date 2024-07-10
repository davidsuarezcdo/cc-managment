def log(icon: str, message: str = ''):
  if not message:
     return print(icon)

  print(icon, message)

def line_separator(length: int = 30):
   print('=' * length)
