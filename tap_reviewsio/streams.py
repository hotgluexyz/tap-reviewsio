"""Stream type classes for tap-reviewsio."""

from abc import ABC
from singer_sdk import typing as th

from tap_reviewsio.client import ReviewsioStream
from tap_reviewsio.objects import review_properties


class GenericReviewsStream(ReviewsioStream, ABC):
    """Generic Reviews Stream."""

    path = "reviews"
    primary_keys = ["id", "date_created"]
    replication_key = "date_created"
    records_jsonpath = "$.reviews[*]"


class ProductReviewsStream(GenericReviewsStream):
    """Product Reviews Stream."""

    name = "product_reviews"
    review_type = "product_review"

    schema = th.PropertiesList(
        *review_properties,
        th.Property("product_review_id", th.IntegerType),
    ).to_dict()


class CompanyReviewsStream(GenericReviewsStream):
    """Product Reviews Stream."""

    name = "company_reviews"
    review_type = "store_review"

    schema = th.PropertiesList(
        *review_properties,
        th.Property("store_review_id", th.IntegerType),
    ).to_dict()
