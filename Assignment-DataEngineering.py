d = spark.table("skit.metadata_2")
display(d)

def create_table(table_name, columns):
    str = ""
    for col, dtype in columns.items():
        str += f"{col} {dtype}, "
    str = str.rstrip(", ")
    create_table_query = f"CREATE OR REPLACE TABLE {table_name} ({str})"
    spark.sql(create_table_query)

table_name = []
columns = {}

distinct_rows = d.select("RawTable","CurratedTableName","PresentationLayerTable").distinct().collect()


print(distinct_rows)
for row in distinct_rows: 
    table_name.append(row["RawTable"])
    if "CurratedTableName" in row:
        table_name.append(row["CurratedTableName"])
    if "PresentationLayerTable" in row:
        table_name.append(row["PresentationLayerTable"])
for x in table_name:
    columns = {}
    if d.filter(d.RawTable == x).count() > 0:
        for row in d.filter(d.RawTable == x).collect():
            columns[row["RawColumn"]] = row["RawTableDatatype"] 
        create_table(x, columns)
    elif d.filter(d.CurratedTableName == x).count() > 0:
        for row in d.filter(d.CurratedTableName == x).collect():
            columns[row["CurratedTableColumn"]] = row["CurratedTableColumnDatatype"] 
        create_table(x, columns)
    elif d.filter(d.PresentationLayerTable == x).count() > 0:
        for row in d.filter(d.PresentationLayerTable == x).collect():
            columns[row["PresentationLayerColumn"]] = row["PresentationLayerColumnDatatype"] 
        create_table(x, columns)
