""" from https://github.com/keithito/tacotron """

import re


valid_symbols = [
    "0", "1", "2", "3", "4", "5", "AA_vn", "AE1", "AO1", "AW_vn", "B",
    "CH_vn", "D", "EE_vn", "EH1", "F", "G_vn", "HH", "IE_vn", "IY1",
    "IZ_vn", "K", "KH_vn", "KW_vn", "L",
    "M",
    "N",
    "NG",
    "NG_vn",
    "NH_vn",
    "OO_vn",
    "OW_vn",
    "OZ_vn",
    "O_vn",
    "P",
    "S",
    "S_vn",
    "T",
    "TH_vn",
    "TR_vn",
    "T_vn",
    "UO_vn",
    "UW1",
    "UW_vn",
    "UZ_vn",
    "V",
    "WA_vn",
    "WO_vn",
    "WU_vn",
    "Y",
    "YZ_vn",
    "Z",
    "u",
]

_valid_symbol_set = set(valid_symbols)


class CMUDict:
    def __init__(self, file_or_path, keep_ambiguous=True):
        if isinstance(file_or_path, str):
            with open(file_or_path, encoding='latin-1') as f:
                entries = _parse_cmudict(f)
        else:
            entries = _parse_cmudict(file_or_path)
        if not keep_ambiguous:
            entries = {word: pron for word, pron in entries.items() if len(pron) == 1}
        self._entries = entries

    def __len__(self):
        return len(self._entries)

    def lookup(self, word):
        return self._entries.get(word.upper())


_alt_re = re.compile(r'\([0-9]+\)')


# def _parse_cmudict(file):
#     cmudict = {}
#     for line in file:
#         if len(line) and (line[0] >= 'A' and line[0] <= 'Z' or line[0] == "'"):
#             parts = line.split('  ')
#             word = re.sub(_alt_re, '', parts[0])
#             pronunciation = _get_pronunciation(parts[1])
#             if pronunciation:
#                 if word in cmudict:
#                     cmudict[word].append(pronunciation)
#                 else:
#                     cmudict[word] = [pronunciation]
#     return cmudict

def _parse_cmudict(file):
    cmudict = {}
    for line in file:
        line = line.strip()
        if len(line) == 0:  # Bỏ qua các dòng trống
            continue
        
        parts = line.split('  ')  # Tách chuỗi tại 2 dấu cách liên tiếp
        
        if len(parts) < 2:  # Kiểm tra xem có đủ hai phần không
            continue  # Bỏ qua dòng này nếu không đủ dữ liệu
        
        word = re.sub(_alt_re, '', parts[0])  # Loại bỏ ký tự không hợp lệ trong từ
        pronunciation = _get_pronunciation(parts[1])  # Lấy phiên âm từ phần còn lại
        
        if pronunciation:  # Nếu phiên âm hợp lệ
            if word in cmudict:
                cmudict[word].append(pronunciation)
            else:
                cmudict[word] = [pronunciation]
    return cmudict



def _get_pronunciation(s):
    parts = s.strip().split(' ')
    for part in parts:
        if part not in _valid_symbol_set:
            return None
    return ' '.join(parts)
