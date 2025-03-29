from .models import User



class StaticColumnNamesMap:
    """
    ## Статические имена столбцов.

    Класс, содержащий статические имена столбцов, которые могут использоваться в различных частях приложения.

    Attributes:
        ID (str): Имя столбца для идентификатора.
        CREATED_AT (str): Имя столбца для даты и времени создания записи.
        UPDATED_AT (str): Имя столбца для даты и времени последнего обновления записи.
    """
    ID = 'id'
    CREATED_AT = 'created_at'
    UPDATED_AT = 'updated_at'



class UserTableColumnsMap(StaticColumnNamesMap):
    """
    ## Имена столбцов таблицы пользователей.

    Класс, наследующий статические имена столбцов и добавляющий имена столбцов, специфичных для таблицы пользователей.

    Attributes:
        USERNAME (str): Имя столбца для имени пользователя.
        EMAIL (str): Имя столбца для электронной почты пользователя.
        FIRST_NAME (str): Имя столбца для имени пользователя.
        LAST_NAME (str): Имя столбца для фамилии пользователя.
        IS_ACTIVE (str): Имя столбца для статуса активности пользователя.
    """
    USERNAME = User.username.key
    EMAIL = User.email.key
    FIRST_NAME = User.first_name.key
    LAST_NAME = User.last_name.key
    IS_ACTIVE = User.is_active.key