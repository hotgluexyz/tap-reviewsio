"""REST client handling, including reviewsioStream base class."""

import requests
from pathlib import Path
from typing import Any, Dict, Optional

from singer_sdk.streams import RESTStream
from singer_sdk.authenticators import APIKeyAuthenticator


SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")


class ReviewsioV2Stream(RESTStream):
    """reviewsio stream class."""

    url_base = "https://api.reviews.co.uk/"

    records_jsonpath = "$[*]"
    per_page = 100

    @property
    def authenticator(self) -> APIKeyAuthenticator:
        """Return a new authenticator object."""
        return APIKeyAuthenticator.create_for_stream(
            self, key="apikey", value=self.config.get("apikey"), location="header"
        )

    @property
    def http_headers(self) -> dict:
        """Return the http headers needed."""
        headers = {}
        if "user_agent" in self.config:
            headers["User-Agent"] = self.config.get("user_agent")
        if "store" in self.config:
            headers["store"] = self.config.get("store")
        return headers

    def get_next_page_token(
        self, response: requests.Response, previous_token: Optional[Any]
    ) -> Optional[Any]:
        """Return a token for identifying next page or None if no more pages."""
        res_json = response.json()
        previous_token = previous_token or 1
        if len(res_json.get('reviews', [])) == self.per_page:
            next_page_token = previous_token + 1
            return next_page_token

    def get_url_params(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        """Return a dictionary of values to be used in URL parameterization."""
        params: dict = {}
        params["per_page"] = self.per_page
        if next_page_token:
            params["page"] = next_page_token
        elif next_page_token == 0:
            params["page"] = 1
        if self.replication_key:
            params["sort"] = "date_asc"
            params["dateFrom"] = self.replication_key
        params["type"] = self.review_type
        return params


