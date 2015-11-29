import argparse
import string

arg_list = ['input', 'emoji', 'output']

parser = argparse.ArgumentParser()

for arg in arg_list:
  parser.add_argument(arg, nargs = '?', default = arg + '.txt')

parser.add_argument('-s', '--strip', action='store_true')

args = parser.parse_args()

def main():
  try:
      with open(args.emoji, 'r') as emoji_file, open(args.input, "r") as input_file, open(args.output, 'w') as output_file:
          dic = get_emoji(emoji_file)
          output = parse_file(input_file, dic)
          write_to_file(output_file, output)
  except IOError as e:
      print 'Error: Are you sure all the files are here?'

def get_emoji(emoji_file):
    dic = dict(zip(list(string.ascii_lowercase), (linpute.rstrip() for linpute in emoji_file)))
    return dic

def parse_file(input_file, dic):
  output_str = ''
  for x in list(input_file.read().lower()):
    if x in dic:
      output_str += dic[x]
    elif not args.strip:
      output_str += x
  return output_str

def write_to_file(output_file, str):
  output_file.write(str)
