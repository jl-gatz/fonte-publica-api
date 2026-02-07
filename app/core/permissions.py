from enum import Enum


class Role(str, Enum):
    public = "public"
    contributor = "contributor"
    editor = "editor"
    admin = "admin"
