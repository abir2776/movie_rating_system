from django.db import models


class Status(models.TextChoices):
    DRAFT = "DRAFT", "Draft"
    ACCEPTED = "ACCEPTED", "Accepted"
    PENDING = "PENDING", "Pending"


class MovieGenre(models.TextChoices):
    ACTION = "ACTION", "Action"
    ADVENTURE = "ADVENTURE", "Adventure"
    ANIMATION = "ANIMATION", "Animation"
    BIOGRAPHY = "BIOGRAPHY", "Biography"
    COMEDY = "COMEDY", "Comedy"
    CRIME = "CRIME", "Crime"
    DOCUMENTARY = "DOCUMENTARY", "Documentary"
    DRAMA = "DRAMA", "Drama"
    FAMILY = "FAMILY", "Family"
    FANTASY = "FANTASY", "Fantasy"
    HISTORY = "HISTORY", "History"
    HORROR = "HORROR", "Horror"
    MUSIC = "MUSIC", "Music"
    MYSTERY = "MYSTERY", "Mystery"
    ROMANCE = "ROMANCE", "Romance"
    SCIENCE_FICTION = "SCIENCE_FICTION", "Science Fiction"
    SPORT = "SPORT", "Sport"
    THRILLER = "THRILLER", "Thriller"
    WAR = "WAR", "War"
    WESTERN = "WESTERN", "Western"


class ReviewRating(models.IntegerChoices):
    ONE_STAR = 1, "★☆☆☆☆"
    TWO_STARS = 2, "★★☆☆☆"
    THREE_STARS = 3, "★★★☆☆"
    FOUR_STARS = 4, "★★★★☆"
    FIVE_STARS = 5, "★★★★★"
