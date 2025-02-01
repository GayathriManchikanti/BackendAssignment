from rest_framework import serializers
from .models import FAQ

class FAQSerializer(serializers.ModelSerializer):
    translated_question = serializers.SerializerMethodField()

    class Meta:
        model = FAQ
        fields = ["id", "question", "answer", "translated_question"]

    def get_translated_question(self, obj):
        request = self.context.get("request")
        lang = request.query_params.get("lang", "en") if request else "en"
        return obj.get_question(lang)
