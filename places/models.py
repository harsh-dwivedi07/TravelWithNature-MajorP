from django.db import models
from datetime import datetime 

# Create your models here.
class placing(models.Model):

    place_name = models.CharField(max_length=100)
    place_mainimg = models.ImageField(upload_to='dynamic_pic')
    place_img1 = models.ImageField(upload_to='dynamic_pic',blank=True)
    place_img2 = models.ImageField(upload_to='dynamic_pic',blank=True)
    place_img3 = models.ImageField(upload_to='dynamic_pic',blank=True)
    place_img4 = models.ImageField(upload_to='dynamic_pic',blank=True)

    state_choice = (
	    ('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands'),
        ('Andhra Pradesh', 'Andhra Pradesh'),
        ('Arunachal Pradesh', 'Arunachal Pradesh'),
        ('Assam', 'Assam'),
        ('Bihar', 'Bihar'),
	    ('Chandigarh', 'Chandigarh'),
        ('Chhattisgarh', 'Chhattisgarh'),
	    ('Dadra & Nagar Haveli and Daman & Diu', 'Dadra & Nagar Haveli and Daman & Diu'),
        ('Delhi', 'Delhi'),
        ('Goa', 'Goa'),
        ('Gujarat', 'Gujarat'),
        ('Haryana', 'Haryana'),
        ('Himachal Pradesh', 'Himachal Pradesh'),
 	    ('Jammu and Kashmir', 'Jammu and Kashmir'),
        ('Jharkhand', 'Jharkhand'),
        ('KKarnataka', 'Karnataka'),
        ('Keral', 'Kerala'),
        ('Lakshadweep', 'Lakshadweep'),
        ('Ladakh', 'Ladakh'),
        ('Madhya Pradesh', 'Madhya Pradesh'),
        ('Maharashtra', 'Maharashtra'),
        ('Manipur', 'Manipur'),
        ('Meghalaya', 'Meghalaya'),
        ('Mizoram', 'Mizoram'),
        ('Nagaland', 'Nagaland'),
        ('Odisha', 'Odisha'),
        ('Punjab', 'Punjab'),
	    ('Puducherry', 'Puducherry'),
        ('Rajasthan', 'Rajasthan'),
        ('Sikkim', 'Sikkim'),
        ('Tamil Nadu', 'Tamil Nadu'),
        ('Telangana', 'Telangana'),
        ('Tripura', 'Tripura'),
        ('Uttar Pradesh', 'Uttar Pradesh'),
        ('Uttrakhand', 'Uttarakhand'),
        ('West Bengal', 'West Bengal'),

       
    )

    place_city =  models.CharField(max_length=100)
    place_state= models.CharField(choices=state_choice, max_length=100)

    place_smdesc = models.TextField(max_length=180)
    place_desc = models.TextField()

    cs_available=models.BooleanField(default=False)
    cs_img=models.ImageField(upload_to='dynamic_pic',blank=True)
    cs_name =  models.CharField(max_length=100,blank=True)

    gnd_choice = (
	    ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    )
    cs_gender= models.CharField(choices=gnd_choice, max_length=100,blank=True)

    cs_number=models.CharField(max_length=10,blank=True)
    cs_address=  models.CharField(max_length=100,blank=True)
    cs_proff=  models.CharField(max_length=100,blank=True)
    created_date=models.DateTimeField(default=datetime.now,blank=True)


class Comment(models.Model):
    cur=models.ForeignKey(placing, related_name="comments",on_delete=models.CASCADE )
    name=models.CharField(max_length=150)
    body=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)
    analy=models.CharField(max_length=100,default='Neutral')
    def __str__(self):
        return '%s - %s' %(self.cur.place_name,self.name)