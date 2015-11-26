unitech project
===============

Development
-----------

Some Django settings are stored as environment variables. One should set them
before running development server / tests. Check the list below for reference.

Environment Variables
~~~~~~~~~~~~~~~~~~~~~

+----------------------------+--------------------------------+
| Variable Name              | Value                          |
+============================+================================+
| `DJANGO_SETTINGS_MODULE`   | `unitech.settings.development` |
|                            | `unitech.settings.testing`     |
|                            | `unitech.settings.production`  |
|                            | `unitech.settings.staging`     |
+----------------------------+--------------------------------+
| `SECRET_KEY`               | `abcd1234...`                  |
+----------------------------+--------------------------------+

