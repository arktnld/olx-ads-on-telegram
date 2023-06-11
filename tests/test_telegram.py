import unittest
from olx_ads_on_telegram.telegram import get_last_msg, send_msg
from olx_ads_on_telegram.vars import TELEGRAM_BOT_TOKEN

class TestGetClient(unittest.TestCase):
    channel_invite_link = 'https://t.me/+LK3A0pKDCYBkZmIx'
    # session_name = 'session_name'
    base_url = "https://www.olx.com.br/estado-df?f=p&q="

    def test_send_msg(self):

        msg = "this a test message"
        channel = '@olxbgbr'
        reponse = send_msg(msg, channel, TELEGRAM_BOT_TOKEN)

        self.assertEqual(reponse.status_code, 200)
        self.assertEqual(reponse.json()['ok'], True)

    def test_get_last_msg(self):

        api_id = 25470833
        api_hash = '04d8e93a0863c1c2ebeda9f39c31663a'
        channel_username = 'olxbgbr'
        session_name = 'olx_ads_on_telegram/session_name'

        last_urls = get_last_msg(api_id, api_hash, session_name, channel_username)

        self.assertIsNotNone(last_urls)
        self.assertIsInstance(last_urls, list)


if __name__ == '__main__':
    unittest.main()
