

def log(event, task_id, conn):
    with conn.cursor() as cur:
        match event:
            case "edit":
                print("i work")
                cur.execute(
                    'INSERT INTO history (task_id, "time", description) VALUES (%s, NOW(), %s);',
                    (task_id, event)
                )
                return "Success"
            case "delete":
                cur.execute(
                    'INSERT INTO history (task_id, "time", description) VALUES (%s, NOW(), %s);',
                    (task_id,  event)
                )
                return "Success"
            case _:
                return "Invalid event"