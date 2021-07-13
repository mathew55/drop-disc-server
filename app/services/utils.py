from pathlib import Path

#Utility functions
def get_project_root() -> Path:
    return Path(__file__).parent.parent
