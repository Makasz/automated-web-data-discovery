import unicodedata


def normalize_output(string):
    string = str(unicodedata.normalize('NFD', string.lower())
                 .encode('ascii', 'ignore'))[1:]
    return string[1:-1]


def month_pl_to_digital(date):
    day, month, year = date.split(' ')
    if len(day) == 1:
        day = '0' + day
    for pol, digital in month_pl_to_digital_dict.items():
        month = month.replace(pol, digital)
    return ''.join([year, month, day])


name_to_url_dict = {'ł': 'l',
                    'ó': 'o',
                    'ń': 'n',
                    ' ': '-',
                    'ź': 'z'}

month_pl_to_digital_dict = {
    'stycznia': '01',
    'lutego': '02',
    'marca': '03',
    'kwietnia': '04',
    'maja': '05',
    'czerwca': '06',
    'lipca': '07',
    'sierpnia': '08',
    'września': '09',
    'października': '10',
    'listopada': '11',
    'grudnia': '12'
}

websites = [
    {'url': 'http://londoneater.com/', 'category': 'blog', 'lang': 'EN'},
    {'url': 'http://eatlikeagirl.com/', 'category': '', 'lang': 'EN'},
    {'url': 'https://cheesenbiscuits.blogspot.com/', 'category': '', 'lang': 'EN'},
    {'url': 'https://www.belleaukitchen.com/', 'category': '', 'lang': 'EN'},
]
