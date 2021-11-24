"""reviewsio tap class."""

from typing import List

from singer_sdk import Tap, Stream
from singer_sdk import typing as th  # JSON schema typing helpers

from tap_reviewsio.streams import (
    reviewsioStream,
    ProductReviews,
    MerchantReviews
)

#       OR rewrite discover_streams() below with your custom logic.
STREAM_TYPES = [
    ProductReviews,
    MerchantReviews
]


class TapReviewsio(Tap):
    """reviewsio tap class."""
    name = "tap-reviewsio"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "apikey",
            th.StringType,
            required=True,
            description="The api key to authenticate against the API service"
        ),
        th.Property(
            "store",
            th.StringType,
            required=True,
            description="The name of the store"
        ),
        th.Property(
            "start_date",
            th.DateTimeType,
            description="The earliest record date to sync"
        )
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]

if __name__=="__main__":
    TapReviewsio.cli()