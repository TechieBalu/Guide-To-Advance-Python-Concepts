import json
from typing import List, Optional
import pydantic 
from icecream import ic
# from beartype.typing import Optional, List
class Book(pydantic.BaseModel):
    title: str
    author: str
    publisher: str
    price: float
    isbn_10: Optional[str]
    isbn_13: Optional[str]
    subtitle: Optional[str]
    # author2: Optional[Author]

    
    



def main() -> None:
    """Main function."""

    # Read data from a JSON file
    with open("./data.json") as file:
        data = json.load(file)
        # print(data)
        # Priting title
        # print(data[0]["title"])


        books: List[Book] = [Book(**item) for item in data]
        # print(books)
        ic(type(books))
        ic(books[0].title)
        ic(type(books[0]))

        # print(books[0])
        # print(books[0].dict(exclude={"price"}))
        # print(books[1].copy())


if __name__ == "__main__":
    main()