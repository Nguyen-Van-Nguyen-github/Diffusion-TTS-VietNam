""" from https://github.com/keithito/tacotron """

import re
from unidecode import unidecode
from .numbers import normalize_numbers


_whitespace_re = re.compile(r'\s+')

_abbreviations = [(re.compile('\\b%s\\.' % x[0], re.IGNORECASE), x[1]) for x in [
    ('vn', 'việt nam'),
    ('tphcm', 'thành phố hồ chí minh'),
    ('hn', 'hà nội'),
    ('đbscl', 'đồng bằng sông cửu long'),
    ('hđnd', 'hội đồng nhân dân'),
    ('ubnd', 'ủy ban nhân dân'),
    ('dhqg', 'đại học quốc gia'),
    ('dhct', 'đại học cần thơ'),
    ('gd&dt', 'giáo dục và đào tạo'),
    ('dn', 'doanh nghiệp'),
    ('vnd', 'việt nam đồng'),
    ('qh', 'quốc hội'),
    ('ctn', 'chủ tịch nước'),
    ('ttcp', 'thủ tướng chính phủ'),
    ('bxd', 'bộ xây dựng'),
    ('byt', 'bộ y tế'),
    ('bqp', 'bộ quốc phồng'),
    ('btttt', 'bộ thông tin và truyền thông'),

    ('gv', 'giáo viên'),
    ('hs', 'học sinh'),
    ('sv', 'sinh viên'),
    ('pgs', 'phó giáo sư'),
    ('gs', 'giáo sư'),
    ('ts', 'tiến sĩ'),
    ('thcs', 'trung học cơ sở'),
    ('thpt', 'trung học phổ thông'),
    ('đh', 'đại học'),
    ('cđ', 'cao đẳng'),

    ('cđ', 'cao đẳng'),
    ('kh&cn', 'khoa học và công nghệ'),
    ('đtvt', 'điện tử viễn thông'),
    ('khxh', 'khoa học xã học'),
    ('khtn', 'khoa họctự nhiên'),
    ('vtv', 'đài truyền hình việt nam'),
    ('blv', 'bình luận viên'),
]]


def expand_abbreviations(text):
    for regex, replacement in _abbreviations:
        text = re.sub(regex, replacement, text)
    return text


def expand_numbers(text):
    return normalize_numbers(text)


def lowercase(text):
    return text.lower()


def collapse_whitespace(text):
    return re.sub(_whitespace_re, ' ', text)


def convert_to_ascii(text):
    return unidecode(text)


def basic_cleaners(text):
    text = lowercase(text)
    text = collapse_whitespace(text)
    return text


def transliteration_cleaners(text):
    text = convert_to_ascii(text)
    text = lowercase(text)
    text = collapse_whitespace(text)
    return text


def english_cleaners(text):
    text = convert_to_ascii(text)
    text = lowercase(text)
    text = expand_numbers(text)
    text = expand_abbreviations(text)
    text = collapse_whitespace(text)
    return text
