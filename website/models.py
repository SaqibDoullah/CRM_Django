from django.db import models

# Create your models here. A Django model to store customer information.Each field represents a piece of data about the customer.
    
class Record(models.Model):
    # Automatically set the field to now when the object is first created
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Customer's first name, with a maximum length of 50 characters
    first_name = models.CharField(max_length=50)
    
    # Customer's last name, with a maximum length of 50 characters
    last_name = models.CharField(max_length=50)
    
    # Customer's email address, with a maximum length of 50 characters
    email = models.EmailField(max_length=50)
    
    # Customer's phone number, with a maximum length of 15 characters
    phone = models.CharField(max_length=15)
    
    # Customer's address, with a maximum length of 100 characters
    address = models.CharField(max_length=100)
    
    # Customer's city, with a maximum length of 50 characters
    city = models.CharField(max_length=50)
    
    # Customer's state, with a maximum length of 50 characters
    state = models.CharField(max_length=50)
    
    # Customer's zip code, with a maximum length of 20 characters
    zip_code = models.CharField(max_length=20)


    """
    Returns a string representation of the Record object.

    This method is used when the Record object is converted to a string.
    It concatenates the first_name and last_name fields of the Record object.

    Parameters:
    None

    Returns:
    str: A string representation of the Record object in the format "first_name last_name".
    """
    def __str__(self):
    
        return (f"{self.first_name} {self.last_name}")
