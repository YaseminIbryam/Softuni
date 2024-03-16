# import re
#
# text = input()
# regex = r'\b_[a-zA-Z0-9]+\b'
# matches = re.findall(regex, text)
# print(','.join([match[1:] for match in matches]))

import re

sentence = input()
pattern = r"\b_([A-Za-z0-9]+)\b"
variables = re.findall(pattern, sentence)
print(",".join(variables))