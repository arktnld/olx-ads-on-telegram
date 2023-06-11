#
# Script to send OLX ads to Telegram channels
#

import os
import olx_ads_on_telegram.telegram as telegram
import olx_ads_on_telegram.olx as olx
import olx_ads_on_telegram.helper as helper
from olx_ads_on_telegram.vars import *
import time

def run_search():
    for search_type in olx_search_types:
        olx_new_urls = []
        telegram_old_urls = telegram.get_last_msg(TELEGRAM_API_ID,
                                                  TELEGRAM_API_HASH,
                                                  telethon_session_name,
                                                  telegram_channel_list[search_type])

        for query in olx_list_queries[search_type]:
            search_url = base_url + query + most_recent_filter
            olx_found_urls = helper.filter_found_urls(
                    olx.request_ads(search_url, olx_category_filters[search_type]),
                    olx_search_exclude)

            # get unique urls
            olx_unique_urls = set(olx_found_urls) - set(telegram_old_urls)
            olx_new_urls += olx_unique_urls

        for new_url in set(olx_new_urls):
            info = olx.request_info(new_url)

            if info == None:
                continue

            print(f"sending {search_type}: {new_url}")

            message = helper.build_msg(info)

            time.sleep(5)
            telegram_channel_name = "@" + telegram_channel_list[search_type]
            telegram.send_msg(message, telegram_channel_name, TELEGRAM_BOT_TOKEN)

