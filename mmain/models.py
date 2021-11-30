from django.db import models

# Create your models here.
class Testimonial(models.Model):
    
    cname = models.CharField(max_length=100)
    cimg = models.ImageField(upload_to='dynamic_pic')
    cdesc = models.TextField()

class TopPlace(models.Model):
    state_choice = (
	    ('AND', 'Andaman and Nicobar Islands'),
        ('AP', 'Andhra Pradesh'),
        ('ARP', 'Arunachal Pradesh'),
        ('AS', 'Assam'),
        ('BI', 'Bihar'),
	    ('CH', 'Chandigarh'),
        ('CHH', 'Chhattisgarh'),
	    ('DD', 'Dadra & Nagar Haveli and Daman & Diu'),
        ('DL', 'Delhi'),
        ('GO', 'Goa'),
        ('GU', 'Gujarat'),
        ('HR', 'Haryana'),
        ('HP', 'Himachal Pradesh'),
 	    ('JK', 'Jammu and Kashmir'),
        ('JH', 'Jharkhand'),
        ('KR', 'Karnataka'),
        ('KRL', 'Kerala'),
        ('LD', 'Lakshadweep'),
        ('LH', 'Ladakh'),
        ('MP', 'Madhya Pradesh'),
        ('MH', 'Maharashtra'),
        ('MN', 'Manipur'),
        ('MG', 'Meghalaya'),
        ('MZ', 'Mizoram'),
        ('NG', 'Nagaland'),
        ('OD', 'Odisha'),
        ('PJ', 'Punjab'),
	    ('PD', 'Puducherry'),
        ('RS', 'Rajasthan'),
        ('SI', 'Sikkim'),
        ('TN', 'Tamil Nadu'),
        ('TG', 'Telangana'),
        ('TR', 'Tripura'),
        ('UP', 'Uttar Pradesh'),
        ('UK', 'Uttarakhand'),
        ('WB', 'West Bengal'),

       
    )
    place_name = models.CharField(max_length=100)
    place_img = models.ImageField(upload_to='dynamic_pic')
    place_desc = models.TextField(max_length=120)
    place_city =  models.CharField(max_length=100)
    place_state= models.CharField(choices=state_choice, max_length=100)