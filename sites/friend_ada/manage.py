#!/usr/bin/env python
import os
import sys
from pathlib import Path

def main():
    # pridaj koreň repa (web-factory/) do sys.path, aby sa našiel "shared"
    repo_root = Path(__file__).resolve().parents[2]
    sys.path.insert(0, str(repo_root))

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "friend_ada.settings.dev")

    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)

if __name__ == "__main__":
    main()
