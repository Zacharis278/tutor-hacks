from tutor import hooks

# Expose mysql port
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

# Adds non-default apps to the tutor-mfe plugin
hooks.Filters.CONFIG_DEFAULTS.add_items([
    (
        "MFE_AUTHORING_MFE_APP",
        {
            "name": "authoring",
            "repository": "https://github.com/edx/frontend-app-course-authoring",
            "port": 2001,
            "env": {
                "development": {
                    "EXAMS_BASE_URL": "http://exams.local.overhang.io:8740"
                }
            }
        },
    ),
])