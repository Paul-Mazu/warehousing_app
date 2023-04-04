import psycopg2
from cli.data import personnel, stock

conn = psycopg2.connect(
    host='localhost',
    database='warehouse',
    user='postgres',
    password='1123:Qwe'
)

cur = conn.cursor()

cur.execute("insert into warehouse(name) values ('Warehouse 1'), ('Warehouse 2'), ('Warehouse 3'),('Warehouse 4');")

items_to_insert = []
for item in stock:
    items_to_insert.append(
        (
            item.get('state'),
            item.get('category'),
            item.get('warehouse'),
            item.get('date_of_stock')
        )
    )

cur.executemany(
    "insert into item(state, category, warehouse_id, date_of_stock) values (%s, %s, %s, %s);", items_to_insert)

def transform_personnel(lst, head=None):
    flattened = []
    for el in lst:
        flattened.append(
                (el['user_name'], el['password'], head)
            )
        if "head_of" in el:
            flattened.extend(transform_personnel(el["head_of"], el['user_name']))   
    return flattened

transformed_personnel = transform_personnel(personnel)
cur.executemany("insert into employee(user_name, password, lead_by) values (%s, crypt(%s, gen_salt('bf')), %s)", transformed_personnel)


conn.commit()
cur.close()
conn.close()



