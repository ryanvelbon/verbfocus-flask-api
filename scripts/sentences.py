# from pkgs.lang.text_proc import fix_casing, fix_punctuation, fix_spacing, fix_syntax, validate_syntax, validate_chars

from pkgs.lang import file_proc as fp
import io
import os

filepath = os.path.join(os.path.dirname(__file__), 'dummy_tr.txt')

# print(filepath)


f = io.open(filepath, mode="r", encoding="utf-8")



# text = f.read()

# print(text)



# print(f.read())


# print(f.read())



fp.stats(f)


