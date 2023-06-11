import unittest
from olx_ads_on_telegram.olx import request_ads, request_info

class TestFunctions(unittest.TestCase):

    def test_request_ads(self):
        url = "https://www.olx.com.br/estado-df?f=p&q=" + "jogo%20tabuleiro" + "&sf=1"

        patterns = [ # Filter by category
            "https://df.olx.com.br/distrito-federal-e-regiao/artigos-infantis",
            "https://df.olx.com.br/distrito-federal-e-regiao/hobbies-e-colecoes"
        ]

        urls = request_ads(url, patterns)

        # Test if the output is a list
        self.assertIsInstance(urls, list)

    def test_request_info(self):
        url = "https://df.olx.com.br/distrito-federal-e-regiao/hobbies-e-colecoes/lego-speed-champions-76899-lamborghini-urus-huracan-1196270821"
        result = request_info(url)

        # Test if the output is a list with 6 elements
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 6)

if __name__ == '__main__':
    unittest.main()
