from olx_ads_on_telegram.helper import build_msg, filter_found_urls
import unittest

class TestFunctions(unittest.TestCase):

    def test_build_msg(self):
        input_list = ["$100", "Product Title", "12345", "State ", "City", "https://example.com"]

        expected_output = f"*$100*\n\nProduct Title\n\n_City, State  12345_\n\n[link](https://example.com)"

        self.assertEqual(build_msg(input_list), expected_output)

    def test_filter_found_urls(self):
        input_urls = ['https://example.com/abc', 'https:// example.com/def', 'https://test.com/']
        input_keys = ['example', 'abc']

        expected_output = ['https://test.com/']

        self.assertEqual(filter_found_urls(input_urls, input_keys), expected_output)

if __name__ == '__main__':
    unittest.main()

