from tutor import hooks

hooks.Filters.ENV_PATCHES.add_item(
    (
        "local-docker-compose-dev-services",
        """
mysql:
    ports:
    - "3306:3306"
""",
    )
)