import decimal

from django.db import models

from common.models import BaseModelWithUID

from .choices import MovieGenre, ReviewRating, Status


class Movie(BaseModelWithUID):
    author = models.ForeignKey("core.User", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True)
    genre = models.CharField(
        max_length=20, choices=MovieGenre.choices, blank=True, null=True
    )
    publish_date = models.DateField()
    duration = models.DurationField()
    producer = models.CharField(max_length=155)
    lead_actors = models.CharField(max_length=255)
    status = models.CharField(
        max_length=20, choices=Status.choices, default=Status.PENDING
    )

    def __str__(self):
        return f"UID: {self.uid}, Title: {self.title}"
    
    def get_avg_rating(self):
        ratings = self.rating_set.aggregate(models.Avg("rating"))
        
        return ratings.get("rating__avg")


class Rating(BaseModelWithUID):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey("core.User", on_delete=models.CASCADE)
    rating = models.IntegerField(choices=ReviewRating.choices)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"UID: {self.uid}, Movie: {self.movie}, User: {self.user}, Rating: {self.rating}"
