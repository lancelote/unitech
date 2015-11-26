unitech project
===============

Development
-----------

Some Django settings are stored as environment variables. One should set them
before running development server / tests. Check the list below for reference.

Environment Variables
~~~~~~~~~~~~~~~~~~~~~

There are four different suites of settings and requirements:

1. `development`
2. `testing`
3. `production`
4. `staging`

Feel free to change environment variable name according to working
environment. For example purposes `development` name will be used below.

+----------------------------+--------------------------------+
| Variable Name              | Value                          |
+============================+================================+
| `DJANGO_SETTINGS_MODULE`   | `unitech.settings.development` |
+----------------------------+--------------------------------+
| `SECRET_KEY`               | `abcd1234...`                  |
+----------------------------+--------------------------------+
