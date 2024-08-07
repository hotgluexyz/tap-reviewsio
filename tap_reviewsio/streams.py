"""Stream type classes for tap-reviewsio."""

from pathlib import Path

from singer_sdk import typing as th

from tap_reviewsio.client import reviewsioStream


class MerchantReviews(reviewsioStream):
    """Merchant Reviews Stream."""

    name = "merchant_reviews"
    path = "merchant/reviews"
    primary_keys = ["store_review_id"]
    replication_key = None
    records_jsonpath = "$.reviews[*]"

    schema = th.PropertiesList(
        th.Property("store_review_id", th.IntegerType),
        th.Property("title", th.StringType),
        th.Property("comments", th.StringType),
        th.Property("date_created", th.DateTimeType),
        th.Property("rating", th.IntegerType),
        th.Property("user_id", th.IntegerType),
        th.Property("store_branch_id", th.IntegerType),
        th.Property("invitation_id", th.IntegerType),
        th.Property("order_number", th.StringType),
        th.Property("timeago", th.StringType),
        th.Property("date_formatted", th.StringType),
        th.Property(
            "reviewer",
            th.ObjectType(
                th.Property("first_name", th.StringType),
                th.Property("last_name", th.StringType),
                th.Property("verified_buyer", th.StringType),
                th.Property("address", th.StringType),
                th.Property("email", th.StringType),
            ),
        ),
        th.Property(
            "ratings",
            th.ArrayType(
                th.ObjectType(
                    th.Property("name", th.StringType),
                    th.Property("score", th.StringType),
                ),
            ),
        ),
        th.Property("branch",
            th.ObjectType(
                th.Property("name", th.StringType),
                th.Property("description", th.StringType),
                th.Property("image", th.StringType),
            ),
        ),
        th.Property("images", th.CustomType({"type": ["array", "string"]})),
        th.Property(
            "tags",
            th.ArrayType(
                th.ObjectType(
                    th.Property("tag", th.StringType),
                ),
            ),
        ),
        th.Property(
            "replies",
            th.ArrayType(
                th.ObjectType(
                    th.Property("user_id", th.IntegerType),
                    th.Property("store_review_id", th.IntegerType),
                    th.Property("comments", th.StringType),
                    th.Property("user_type", th.StringType),
                    th.Property("date_created", th.DateTimeType),
                ),
            ),
        )
    ).to_dict()


class ProductReviews(reviewsioStream):
    """Product Reviews Stream."""

    name = "product_reviews"
    path = "product/reviews/all"
    primary_keys = ["product_review_id"]
    replication_key = None
    records_jsonpath = "$.reviews[*]"
    schema = th.PropertiesList(
        th.Property("product_review_id", th.IntegerType),
        th.Property("product_make", th.StringType),
        th.Property("order_id", th.StringType),
        th.Property("name", th.StringType),
        th.Property("sku", th.StringType),
        th.Property("review", th.StringType),
        th.Property("rating", th.IntegerType),
        th.Property("date_created", th.DateTimeType),
        th.Property("votes", th.IntegerType),
        th.Property("timeago", th.StringType),
        th.Property("product", th.StringType),
        th.Property(
            "reviewer",
            th.ObjectType(
                th.Property("user_id", th.IntegerType),
                th.Property("first_name", th.StringType),
                th.Property("last_name", th.StringType),
                th.Property("verified_buyer", th.StringType),
                th.Property("address", th.StringType),
                th.Property("profile_picture", th.StringType),
                th.Property("gravatar", th.StringType),
                th.Property("email", th.StringType),
                th.Property("name_formatted", th.IntegerType),
            ),
        ),
        th.Property(
            "ratings",
            th.ArrayType(
                th.ObjectType(
                    th.Property("name", th.StringType),
                    th.Property("score", th.StringType),
                ),
            ),
        ),
        # th.Property("images", th.ArrayType),
        # th.Property("tags", th.ArrayType),
        # th.Property("replies", th.ArrayType),
    ).to_dict()
