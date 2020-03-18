import requests


class BrakingBad:

    @staticmethod
    def quote():
        req = requests.get('https://breaking-bad-quotes.herokuapp.com/v1/quotes')
        quote = req.json()
        return quote

    @staticmethod
    def list_quotes(num):
        req = requests.get('https://breaking-bad-quotes.herokuapp.com/v1/quotes/' + str(num))
        list_quotes = req.json()
        return list_quotes


