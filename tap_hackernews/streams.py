"""Stream type classes for tap-hackernews."""

from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_hackernews.client import hackernewsStream

SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")

class ItemsStream(hackernewsStream):
    """Define custom stream."""
    name = "items"
    path = "/item/28888175.json"
    primary_keys = ["id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "items.json"


