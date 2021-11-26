"""Stream type classes for tap-reviewsio."""

from pathlib import Path

from singer_sdk import typing as th

from tap_reviewsio.client import reviewsioStream

# TODO: Delete this is if not using json files for schema definition
SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")
# TODO: - Override `UsersStream` and `GroupsStream` with your own stream definition.
#       - Copy-paste as many times as needed to create multiple stream types.


class MerchantReviews(reviewsioStream):
    """Merchant Reviews Stream."""

    name = "merchant_reviews"
    path = "merchant/reviews"
    primary_keys = ["store_review_id"]
    replication_key = None
    records_jsonpath = "$.reviews[*]"
    # Optionally, you may also use `schema_filepath` in place of `schema`:
    # schema_filepath = SCHEMAS_DIR / "users.json"
    schema = th.PropertiesList(
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
        th.Property(
            "branch",
            th.ArrayType(
                th.ObjectType(
                    th.Property("name", th.StringType),
                    th.Property("description", th.StringType),
                    th.Property("image", th.StringType),
                ),
            ),
        ),
        # th.Property("images", th.ArrayType),
        # th.Property("tags", th.ArrayType),
        # th.Property("replies", th.ArrayType),
    ).to_dict()


class ProductReviews(reviewsioStream):
    """Product Reviews Stream."""

    name = "product_reviews"
    path = "product/reviews/all"
    primary_keys = ["product_review_id"]
    replication_key = None
    records_jsonpath = "$.reviews[*]"
    schema = th.PropertiesList(
        th.Property("product_make", th.StringType),
        th.Property("order_id", th.StringType),
        th.Property("name", th.StringType),
        th.Property("sku", th.StringType),
        th.Property("review", th.StringType),
        th.Property("rating", th.IntegerType),
        th.Property("date_created", th.DateTimeType),
        th.Property("votes", th.StringType),
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
