"""Stream type classes for tap-reviewsio."""

from abc import ABC
from singer_sdk import typing as th

from tap_reviewsio.client_v2 import ReviewsioV2Stream
from tap_reviewsio.objects import review_properties


class GenericReviewsV2Stream(ReviewsioV2Stream, ABC):
    """Generic Reviews Stream."""

    path = "reviews"
    primary_keys = ["id", "date_created"]
    replication_key = "date_created"
    records_jsonpath = "$.reviews[*]"


class ProductReviewsV2Stream(GenericReviewsV2Stream):
    """Product Reviews Stream."""

    name = "product_reviews_v2"
    review_type = "product_review"

    schema = th.PropertiesList(
        *review_properties,
        th.Property("product_review_id", th.IntegerType),
    ).to_dict()


class CompanyReviewsV2Stream(GenericReviewsV2Stream):
    """Product Reviews Stream."""

    name = "company_reviews_v2"
    review_type = "store_review"

    schema = th.PropertiesList(
        *review_properties,
        th.Property("store_review_id", th.IntegerType),
    ).to_dict()
