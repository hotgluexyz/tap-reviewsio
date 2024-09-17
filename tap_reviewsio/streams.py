"""Stream type classes for tap-reviewsio."""

from abc import ABC
from singer_sdk import typing as th

from tap_reviewsio.client import ReviewsioStream
from tap_reviewsio.objects import review_properties

class GenericReviewsStream(ReviewsioStream, ABC):
    """Generic Reviews Stream."""

    path = "reviews"
    replication_key = "date_created"
    records_jsonpath = "$.reviews[*]"

    schema = th.PropertiesList(
        *review_properties
    ).to_dict()


class ProductReviewsStream(GenericReviewsStream):
    """Product Reviews Stream."""

    name = "product_reviews_"
    review_type = "product_review"


class CompanyReviewsStream(GenericReviewsStream):
    """Product Reviews Stream."""

    name = "company_reviews_"
    review_type = "store_review"
