from rest_framework import serializers
from .models import Text_Snippet,Tags



class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ['id', 'title']



class TextSnippetSerializer(serializers.ModelSerializer):
    tags = TagsSerializer(many=True)

    class Meta:
        model = Text_Snippet
        fields = ['id', 'title', 'text', 'timestamp', 'created_user', 'tags']
        
    def create(self, validated_data):
        tags_data = validated_data.pop('tags')
        print(tags_data,'tags_data')
        snippet = Text_Snippet.objects.create(**validated_data)
        
        # loop is to check weather tag title exist if so create a new tag 

        for tag in tags_data:
            print(tag['title'])
            tags, _ = Tags.objects.get_or_create(title=tag['title'])
            print(tags, _)
            snippet.tags.add(tags)

        return snippet
    
    def update(self, instance, validated_data):
        tags_data = validated_data.pop('tags')
        print('tags_data',tags_data,validated_data)
        instance.title = validated_data.get('title', instance.title)
        instance.text = validated_data.get('text', instance.text)
        instance.save()

        for tag in tags_data:
            tag_title = tag['title']
            tags, _ = Tags.objects.get_or_create(title=tag_title)
            instance.tags.add(tags)

        validated_data['timestamp'] = instance.timestamp
        validated_data['created_user'] = instance.created_user

        existing_tags = instance.tags.all()
        serializer = TagsSerializer(existing_tags, many=True)
        validated_data['tags'] = serializer.data

        return validated_data


