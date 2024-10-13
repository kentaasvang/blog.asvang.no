#!./venv/bin/python3


if __name__ == "__main__":
    import pathlib
    from datetime import datetime

    MIGRATION_PATH = "data/migrations/"

    migration_name = input("Enter migration name: ")
    migration_name = migration_name.replace(" ", "_")
    migration_name = f"{datetime.now().isoformat()}_{migration_name}"
    migration_path = pathlib.Path(MIGRATION_PATH, migration_name)
    migration_path.mkdir(exist_ok=False)

    up_sql = migration_path / "up.sql"
    down_sql = migration_path / "down.sql"

    up_sql.touch()
    down_sql.touch()

    print(f"Created migration: {migration_path}")
