import asyncio
import sys
from typing import Callable

from dotenv import load_dotenv

from app.db.connection import get_engine
from app.db.seed import migrate_schema, seed_collection, seed_dict


def migrate(args: list[str]):
    drop = len(args) == 1 and args[0] == "drop"
    asyncio.run(migrate_schema(get_engine(), drop))


commands: dict[str, Callable] = {
    "migrate": migrate,
    "seed_dict": lambda args: asyncio.run(seed_dict(args)),
    "seed_coll": lambda args: asyncio.run(seed_collection(args)),
}


def main():
    cmd, *args = sys.argv[1:]
    if cmd not in commands:
        print(f"Command {cmd!r} not found")
        return

    commands[cmd](args)


if __name__ == "__main__":
    load_dotenv()
    main()
