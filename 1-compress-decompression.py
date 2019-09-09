import sys

def decompress(string):
   block_start = string.find('[')
   if block_start == -1:
      return string
   block_end = -1
   opening_brackets = 0
   closing_brackets = 0

   for i in range(block_start, len(string)):
      if string[i] == '[':
         opening_brackets += 1
      elif string[i] == ']':
         closing_brackets += 1
         if opening_brackets == closing_brackets:
            block_end = i
            break 

   part = (int(string[:block_start]) * decompress(string[block_start + 1:block_end]))
   rest = decompress(string[block_end + 1:])
   return part + rest


if __name__ == '__main__':
   sys.stdout.write(decompress(sys.argv[1]))
