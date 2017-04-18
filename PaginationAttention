import requests


def check(filename, f):
  payload = {'rid':'dota2', 'ajax':'block_matches_current', 'data[s]': f, 'data[type]': 'gg'}
  r = requests.post('http://game-tournaments.com/dota-2', data = payload)
  with open(filename, 'w') as output_file:
      output_file.write(r.text.encode('utf-8'))
