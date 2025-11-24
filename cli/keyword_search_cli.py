#!/usr/bin/env python3

import argparse
import json

def search_movies(query: str) -> None:
    print(f'Searching for: {query}')
    with open('data/movies.json', 'r') as f:
        movies = json.load(f)
        matches = []
        for movie in movies['movies']:
            if query in movie['title']:
                matches.append(movie)
        for movie in sorted(matches, key=lambda movie: movie['id'])[:5]:
            print(f"{movie['id']}. {movie['title']}")

def main() -> None:
    parser = argparse.ArgumentParser(description="Keyword Search CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    search_parser = subparsers.add_parser("search", help="Search movies using BM25")
    search_parser.add_argument("query", type=str, help="Search query")

    args = parser.parse_args()

    match args.command:
        case "search":
            search_movies(args.query)
        case _:
            parser.print_help()

if __name__ == "__main__":
    main()
