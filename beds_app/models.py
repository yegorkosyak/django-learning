import uuid
from django.db import models


class User(AbstractUser):
    """Custom User class"""

    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    phone_number = models.PhoneNumberField()
    password
    shelter_id
    active_at
    created_at
    updated_at
    deleted_at
    last_login_at

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
