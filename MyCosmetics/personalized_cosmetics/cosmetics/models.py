from django.db import models

class MyCosmetics(models.Model):  # Renamed from UserPreference
    skin_type_choices = [
        ('oily', 'Oily'),
        ('dry', 'Dry'),
        ('combination', 'Combination'),
        ('normal', 'Normal'),
    ]
    
    skin_type = models.CharField(max_length=20, choices=skin_type_choices)
    age = models.PositiveIntegerField()
    concerns = models.TextField()

    def __str__(self):
        return f"{self.skin_type} - Age: {self.age}"


class CosmeticSuggestion(models.Model):
    user_preference = models.ForeignKey(MyCosmetics, on_delete=models.CASCADE)  # Updated ForeignKey
    suggested_products = models.TextField()

    def __str__(self):
        return f"Suggestions for {self.user_preference}"