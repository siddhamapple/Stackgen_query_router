from core.exceptions import RouterError
from router.query_router import route_query


def main():
    print("StackGen Query Router (type 'exit' to quit)\n")

    while True:
        query = input(">> ")

        if query.lower() == "exit":
            break

        try:
            response = route_query(query)
            print(response)
        except RouterError:
            print("I cannot answer this question.")


if __name__ == "__main__":
    main()
