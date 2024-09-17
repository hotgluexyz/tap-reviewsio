from singer_sdk import typing as th

reviewer_attr_object = th.ObjectType(
    th.Property("attribute_id", th.StringType),
    th.Property("type", th.StringType),
    th.Property("label", th.StringType),
    th.Property("options", th.ArrayType(th.StringType)),
    th.Property("value", th.StringType),
)
author_object = th.ObjectType(
    th.Property("name", th.StringType),
    th.Property("location", th.StringType),
    th.Property("attributes", th.ArrayType(reviewer_attr_object)),
)
videos_object = th.ObjectType(
    th.Property("thumbnail", th.StringType),
    th.Property("video", th.StringType),
)
author_reply_object = th.ObjectType(
    th.Property("name", th.StringType),
    th.Property("avatar", th.StringType),
)
reply_object = th.ObjectType(
    th.Property("comments", th.StringType),
    th.Property("date_created", th.DateTimeType),
    th.Property("author", author_reply_object),
)
company_stats_object = th.ObjectType(
    th.Property("review_count", th.NumberType),
    th.Property("average_rating", th.NumberType),
)
stats_attr_object = th.ObjectType(
    th.Property("id", th.StringType),
    th.Property("type", th.StringType),
    th.Property("label", th.StringType),
    th.Property("options", th.ArrayType(th.StringType)),
    th.Property("question", th.StringType),
    th.Property("count", th.NumberType),
    th.Property("average_rating", th.NumberType),
)
stats_object = th.ObjectType(
    th.Property("company", company_stats_object),
    th.Property("attributes", th.ArrayType(stats_attr_object)),
    th.Property("ratings", th.ArrayType(th.NumberType)),
)
filterable_review_attrs = th.ObjectType(
    th.Property("id", th.StringType),
    th.Property("type", th.StringType),
    th.Property("label", th.StringType),
    th.Property("options", th.ArrayType(th.ObjectType(
        th.Property("label", th.StringType),
        th.Property("values", th.StringType),
    ))),
)
filters_object = th.ObjectType(
    th.Property("review_attributes", th.ArrayType(filterable_review_attrs)),
    th.Property("attributes", th.ArrayType(filterable_review_attrs)),
)
review_properties = [
    th.Property("type", th.StringType),
    th.Property("type_label", th.StringType),
    th.Property("source", th.StringType),
    th.Property("rating", th.IntegerType),
    th.Property("title", th.StringType),
    th.Property("comments", th.StringType),
    th.Property("author", author_object),
    th.Property("date_created", th.DateTimeType),
    th.Property("time_ago", th.StringType),
    th.Property("order_id", th.StringType),
    th.Property("sku", th.StringType),
    th.Property("helpful_count", th.NumberType),
    th.Property("attributes", th.ArrayType(reviewer_attr_object)),
    th.Property("photos", th.ArrayType(th.StringType)),
    th.Property("unpublished_photos", th.ArrayType(th.StringType)),
    th.Property("videos", th.ArrayType(videos_object)),
    th.Property("tags", th.ArrayType(th.StringType)),
    th.Property("replies", th.ArrayType(videos_object)),
    th.Property("stats", stats_object),
    th.Property("review_count", th.NumberType),
    th.Property("results_count", th.NumberType),
    th.Property("average_rating", th.NumberType),
    th.Property("verdict", th.StringType),
    th.Property("store_name", th.StringType),
    th.Property("filters", filters_object),
]
review_object = th.ObjectType(
    *review_properties
)
