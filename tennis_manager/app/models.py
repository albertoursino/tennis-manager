from django.db import models


class User(models.Model):
    """Model for the user."""

    name = models.CharField(blank=False, max_length=50)
    surname = models.CharField(blank=False, max_length=50)

    def __str__(self: models.Model) -> str:
        """Return a string representation of the user."""
        return f"{self.name} {self.surname}"


class Field(models.Model):
    """Model for the field."""

    number = models.IntegerField(blank=False)

    def __str__(self: models.Model) -> str:
        """Return a string representation of the field."""
        return f"Field number {self.number}"


class Match(models.Model):
    """Model for the match."""

    users: User = models.ManyToManyField("User")
    field: Field = models.ForeignKey("Field", on_delete=models.SET_NULL, null=True)
    date = models.DateField(auto_now_add=True)

    class Meta:  # noqa: D106
        verbose_name_plural = "Matches"

    def __str__(self: models.Model) -> str:
        """Return a string representation of the match."""
        return f"Field number {self.field.number} used by: {', '.join(self.get_all_users())[:len(self.users)-2]}"

    def get_all_users(self: models.Model) -> list[User]:
        """Return the list of users of the match."""
        return list(self.users)
