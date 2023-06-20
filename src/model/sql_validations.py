class SQLValidations:

    # retorna apenas 1 coluna
    check_empty_table = "SELECT COUNT(*) FROM %s"
