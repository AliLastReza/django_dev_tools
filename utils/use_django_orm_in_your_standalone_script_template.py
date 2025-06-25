#!/usr/bin/env python
"""
Standalone Django ORM script template.
"""

from __future__ import annotations

import os
import sys

import django

# Add the project root to the Python path
# TODO: Make sure "project_root" var value is your project's root.
project_root = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)
sys.path.append(project_root)

# ───────────────────────────── Django bootstrap ──────────────────────────────
# 1) TODO: Tell Django where the settings module is (edit the dotted path once).
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dj_project.settings")

# 2) Initialise Django; *import models only after this call*.
django.setup()

# TODO: write your code here, all your imports and django (orm) code should be after "django.setup()" line. For example:
if __name__ == "__main__":
    from pprint import pprint

    from django.contrib.auth.models import User

    pprint(User.objects.all()[:5].values())
