from typing import List, Any

import sys
import redis
from redis_lru import RedisLRU

from models import Author, Quote

client = redis.StrictRedis(host="localhost", port=6379, password=None)
cache = RedisLRU(client)


@cache
def find_by_tag(tag: str) -> list[str | None]:
    print(f"Find by {tag}")
    quotes = Quote.objects(tags__iregex=tag)
    result = [q.quote for q in quotes]
    return result


@cache
def find_by_author(author: str) -> list[list[Any]]:
    print(f"Find by {author}")
    authors = Author.objects(fullname__iregex=author)
    print(authors)
    result = {}
    for a in authors:
        quotes = Quote.objects(author=a)
        print(quotes)
        result[a.fullname] = [q.quote for q in quotes]
    return result


def parse_command(command: str) -> tuple[str, str]:
   
    parts = command.split(":")
    if len(parts) != 2:
        raise ValueError("Некоректний формат команди")
    return parts[0].strip(), parts[1].strip()

def main():
    
    while True:
        command = input("Введіть команду (name:, tag:, tags:, exit): ")
        if command.lower() == "exit":
            break
        try:
            command_type, value = parse_command(command)
            if command_type == "name":
                results = find_by_author(value)
           
                for author, quotes in results.items():
                    print(f"Автор: {author}")

                    for quote in quotes:
                        print(f"  - {quote}")
            elif command_type == "tag":
                results = find_by_tag(value)
                for quote in results:
                    print(f"- {quote}")
            elif command_type == "tags":
                tags = value.split(",")
                for t in tags:
                    results = find_by_tag(t)
                    for quote in results:
                        print(f"- {quote}")             
            else:
                print("Невідома команда")
        except ValueError as e:
            print(f"Помилка: {e}")

if __name__ == "__main__":
    main()