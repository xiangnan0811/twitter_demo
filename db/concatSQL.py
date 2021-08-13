def get_insert_and_update_sql(fields, table, not_update_key: str = ''):
    """
    以 item 的字段信息组装插入或更新sql
    :param fields:             item对应的字段 默认不包含 item_type 字段
    :param table:              入库表名
    :param not_update_key:     不更新的字段（id、create_time以外的不进行更新的字段）
    :return:                   组装成的sql
    """
    insert_keys = list(x for x in fields if x != 'item_type')
    insert_values = list(map(lambda x: f'%({x})s', insert_keys))
    update_keys = [x for x in insert_keys if x != "id" and x != "create_time"]
    if not_update_key != '':
        update_keys.remove(not_update_key)
    update_values = list(map(lambda x: f"{x}=values({x})", update_keys))
    sql = f"""
        INSERT INTO {table}({', '.join(insert_keys)})
        VALUES ({', '.join(insert_values)})
        ON DUPLICATE KEY UPDATE {', '.join(update_values)}
    """
    return sql


def get_insert_ignore_sql(fields, table):
    """
    以 item 字段组装插入sql
    :param fields:             item对应的字段 默认不包含 item_type 字段
    :param table:              入库表名
    :return:                   组装成的sql
    """
    insert_keys = list(x for x in fields if x != 'item_type')
    insert_values = list(map(lambda x: f'%({x})s', insert_keys))
    sql = f"""
        INSERT IGNORE INTO {table}({', '.join(insert_keys)})
        VALUES ({', '.join(insert_values)})
    """
    return sql
