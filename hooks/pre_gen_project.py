import re
import sys

PACKAGE_NAME_REGEX = r"^[a-z][a-z0-9_]*$"

package_name = "{{ cookiecutter.package_name }}"

if not re.match(PACKAGE_NAME_REGEX, package_name):
    print(
        f"ERROR: {package_name!r} is not a valid Python package name. "
        "It must start with a lowercase letter and contain only lowercase "
        "letters, digits, and underscores. Adjust 'project_name' and retry."
    )
    sys.exit(1)
