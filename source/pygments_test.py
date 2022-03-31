# python pygments_test.py 

from pygments.styles import get_all_styles
from pygments.lexers import get_all_lexers

def get_styles():
  # get a list of supported styles
  styles = list(get_all_styles())
  print(styles)

def get_languages():
  # get a list of supported highlighters
  lexers = get_all_lexers()
  for lexer in lexers:
    print("-  " + lexer[0] + "\n")
    print("  -  " + "\n  -  ".join(lexer[1]) + "\n")

get_languages()