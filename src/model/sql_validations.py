class SQLValidations:

    # retorna apenas 1 coluna
    check_empty_table = "SELECT 1 FROM %s LIMIT 1"
