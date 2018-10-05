class Sources:
    """
     News class to define Class objects
    """

    def __init__(self, id, name, description, url, category, country):
        """
        function to create/ initiate the sources class
        """
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.country = country


class Articles:
    """
    specifies the articles objects
    """

    def __init__(self, author, title, description, url, urlToImage, publishedAt):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt


# class Review:
#     all_reviews = []
#
#     def __init__(self, movie_id, title, imageurl, review):
#         self.movie_id = movie_id
#         self.title = title
#         self.imageurl = imageurl
#         self.review = review
#
#     def save_review(self):
#         Review.all_reviews.append(self)
#
#     @classmethod
#     def get_reviews(cls, id):
#
#         response = []
#
#         for review in cls.all_reviews:
#             if review.movie_id == id:
#                 response.append(review)
#
#         return response
