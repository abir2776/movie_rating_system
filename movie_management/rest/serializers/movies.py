from rest_framework import serializers

from movie_management.models import Movie, Rating

from core.models import User


class GlobalMovieSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField()
    author_name = serializers.SerializerMethodField()
    class Meta:
        model = Movie
        fields = [
            "author",
            "title",
            "image",
            "genre",
            "publish_date",
            "duration",
            "producer",
            "lead_actors",
            "rating",
            "author_name",
        ]

    def get_rating(self, obj):
        return obj.get_avg_rating()
    
    def get_author_name(self, obj):
        return obj.author.first_name + ' ' + obj.author.last_name


class ReviewRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = "__all__"
        
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("phone","email","first_name", "last_name")
