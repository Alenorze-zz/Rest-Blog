from rest_framework.serializers import (
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField
)


from posts.models import Post



class PostCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'publish'
        ]


post_detail_url = HyperlinkedIdentityField(
        view_name='posts-api:detail',
        lookup_field='slug'
        )


class PostDetailSerializer(ModelSerializer):
    url = post_detail_url
    user = SerializerMethodField()
    image = SerializerMethodField()
    html = SerializerMethodField()
    class Meta:
        model = Post
        fields = [
            'url',
            'id',
            'user',
            'title',
            'slug',
            'content',
            'html',
            'publish',
            'image',
        ]

    def get_html(self, obj):
        return obj.get_markdown()

    def get_user(self, obj):
        return str(obj.user.username)

    def get_image(self, obj):
        try:
            image = obj.image.url
        except:
            image = None
        return image



class PostListSerializer(ModelSerializer):
    url = post_detail_url
    user = SerializerMethodField()
    class Meta:
        model = Post
        fields = [
            'url',
            'user',
            'title',
            'content',
            'publish',
        ]

    def get_user(self, obj):
        return str(obj.user.username)
