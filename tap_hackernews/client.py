"""REST client handling, including hackernewsStream base class."""

import copy
import requests
from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable

from memoization import cached

from singer_sdk.helpers.jsonpath import extract_jsonpath
from singer_sdk.streams import RESTStream


SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")


class hackernewsStream(RESTStream):
    """hackernews stream class."""

    records_jsonpath = "$[*]"  # Or override `parse_response`.
    next_page_token_jsonpath = "$.next_page"  # Or override `get_next_page_token`.

    @property
    def url_base(self) -> str:
        """Return the API URL root, configurable via tap settings."""
        return self.config["api_url"]

    @property
    def start_item(self) -> str:
        """Return the ID of the start item, configurable via tap settings."""
        return self.config["start_item"]

    def max_item() -> str:
        """Return the maximum unit ID at the start of the run."""
        max_item_no = requests.get('https://hacker-news.firebaseio.com/v0/maxitem.json')
        return max_item_no.json()


