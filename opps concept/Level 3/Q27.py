# Question 27
# Create a Library class and a SearchService class. Make the library USE-A the search service.

class SearchService:
    def search(self, name):
        print("SearchService:", name)

class Library:
    def __init__(self, name):
        self.name = name

    def use_service(self, service):
        service.search(self.name)

obj = Library("Example")
obj.use_service(SearchService())
