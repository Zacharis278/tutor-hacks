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

# custom webpack for learner dash
# jank just to get this working for now
hooks.Filters.ENV_PATCHES.add_item(
    (
        "mfe-webpack-dev-config",
        """
const path = require('path');
const config = module.exports

config.resolve.modules = [
  path.resolve(__dirname, './src'),
  'node_modules',
];

config.module.rules[0].exclude = /node_modules\/(?!(query-string|split-on-first|strict-uri-encode|@edx))/;

module.exports = config;
"""
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
                    "EXAMS_BASE_URL": "http://exams.local.overhang.io:8740",
                    "BASE_URL": "http://apps.local.overhang.io:2001"
                }
            }
        },
    ),
    (
        "MFE_LEARNER_DASHBOARD_MFE_APP",
        {
            "name": "dashboard",
            "repository": "https://github.com/edx/frontend-app-learner-dashboard",
            "port": 1996,
            "env": {
                "development": {
                    "BASE_URL": "http://apps.local.overhang.io:1996",
                    "FAVICON_URL": "https://edx-cdn.org/v3/default/favicon.ico",
                },
            },
        },
    ),
])