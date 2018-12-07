def has_role(author, role_name):
    return any(item.name == role_name for item in author.roles)
