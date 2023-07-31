class OwnException(Exception):
    pass


class LevelError(OwnException):
    def __init__(self, user_level, admin_level):
        self.user_level = user_level
        self.admin_level = admin_level

    def __str__(self):
        return 'Access denied! Your access level should be lower than admin access level'


class NotAllowedError(OwnException):
    def __init__(self, name, id_):
        self.name = name
        self.id_ = id_

    def __str__(self):
        return 'Access denied! User not found.'


class AdminNotFoundError(OwnException):
    def __str__(self):
        return 'Access denied! Admin not found! Use enter command to login to the system.'
    