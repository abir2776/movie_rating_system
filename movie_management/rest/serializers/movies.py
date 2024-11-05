from rest_framework import serializers

from movie_management.models import Movie, Rating


class GlobalMovieSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField()

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
        ]

    def get_rating(self, obj):
        return obj.get_avg_rating()


class ReviewRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = "__all__"
