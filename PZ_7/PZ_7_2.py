#Дана строка, содержащая полное имя файла, то есть имя диска, список каталогов (путь), собственно имя и расширение. Выделить из этой строки расширение файла (без предшествующей точки).

try:
  def extract_last_part_after_dot(full_path):
      last_dot = full_path.rfind('.')
      if last_dot != -1 and last_dot != len(full_path) - 1:
          extension = full_path[last_dot + 1:]
          for separator in ['?', '#', '/']:
              separator_pos = extension.find(separator)
              if separator_pos != -1:
                  extension = extension[:separator_pos]
          return extension
      return ""
  url = input('введите строку: ')
  result = extract_last_part_after_dot(url)
  print(f"Извлечено: '{result}'")
except Exception as e:
  print('nah')