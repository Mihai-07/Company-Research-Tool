from langchain_tavily import TavilySearch

class Search:
    name: str = "Search the Internet"
    description: str = """
        Searches the internet for relevant information on a given query.
        It is particularly useful when you want to gather up-to-date
        information on a given topic.
    """

    @staticmethod
    def func(query: str):
        search = TavilySearch()
        return search.run(query)