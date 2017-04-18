import requests

def checkthePagination(filename, url, **kwargs):


    r = requests.post(url, data = kwargs)
    with open(filename, 'w') as output_file:
        output_file.write(r.text.encode('utf-8'))

count = 1
dct = {

    'rid':'dota2',
    'ajax':'block_matches_current',
    'data[s]': count,
    'data[type]' :'gg'

}


if __name__ == '__main__':
    checkthePagination('kurqa.html', 'http://game-tournaments.com/dota-2', **dct)
