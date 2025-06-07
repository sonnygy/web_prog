from django.db import models

class Comment(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'text': self.text,
            'rating': self.rating,
            'created_at': self.created_at.isoformat()
        }