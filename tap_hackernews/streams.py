"""Stream type classes for tap-hackernews."""

from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable

from singer_sdk import typing as th  # JSON Schema typing helpers
import requests
from tap_hackernews.client import hackernewsStream

SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")

# class MaxItemStream(hackernewsStream):
#     """The max item available."""
#     name = "maxitem"
#     path = "/maxitem.json"
#     primary_keys = ["maxitem"]
#     replication_key = None
#     schema = th.PropertiesList(
#         th.Property(
#             "maxitem",
#             th.NumberType,
#         ),
#     ).to_dict()

#     def get_child_context(self, record: dict, context: Optional[dict]) -> dict:
#         """Return a context dictionary for child streams."""
#         return {
#             "item_id": hackernewsStream.max_item()
#         }

class ItemsStream(hackernewsStream):
    """Define custom stream."""

    # parent_stream_type = MaxItemStream 
    # 
    item_id = hackernewsStream.max_item() 

    name = "items"
    path = "/item/{item_id}.json"

    primary_keys = ["item_id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "items.json"

    def get_next_page_token(self, response, previous_token) -> Optional[Any]:
        """Return a token for identifying next page or None if no more pages."""

        current_page = response.json().get('item')
        if not current_page:
            return
