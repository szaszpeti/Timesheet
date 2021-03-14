from django.db import models

from django.contrib.auth.models import User

class Entry(models.Model):
    
    entry_date = models.DateTimeField(auto_now_add=True)
    entry_location = models.CharField(max_length=50)
    entry_wtglocalnumber = models.CharField(max_length=3)
    entry_wtgnumber = models.CharField(max_length=50)
    entry_technician_one = models.ForeignKey(User, on_delete=models.CASCADE)
    entry_technician_two = models.CharField(max_length=50)
    entry_technician_three = models.CharField(max_length=50, blank=True)
    entry_notes = models.TextField(blank=True)
    
    
    
    TRAVEL_OFFICE_WTG = 'Travel Office --> WTG'
    TRAVEL_WTG_OFFICE = 'Travel WTG --> Office'
    TRAVEL_HOTEL_WTG = 'Travel Hotel --> WTG'
    TRAVEL_WTG_HOTEL = 'Travel WTG --> Hotel'
    TRAVEL_EXTRA = 'Travel Extra'
    WORK_PREPARATION = 'Work Preparation'
    UT_INSPECTION = 'UT Inspection'
    STANDBY_WEATHER = 'Standby Weather'
    STANDBY_WTG_DISORDER = 'Standby WTG Disorder'
    CLEANING = 'Cleaning'
    OTHER = 'Other'
    
    
    
    ACTIVITY = [(TRAVEL_OFFICE_WTG, 'Travel Office --> WTG '),
                         (TRAVEL_WTG_OFFICE, 'Travel WTG --> Office'),
                         (TRAVEL_HOTEL_WTG, 'Travel Hotel --> WTG'),
                         (TRAVEL_WTG_HOTEL, 'Travel WTG --> Hotel'),
                         (TRAVEL_EXTRA, 'Travel Extra'),
                         (WORK_PREPARATION, 'Work Preparation'),
                         (UT_INSPECTION, 'UT Inspection'),
                         (STANDBY_WEATHER, 'Standby Weather'),
                         (STANDBY_WTG_DISORDER, 'Standby WTG Disorder'),
                         (CLEANING, 'Cleaning'),
                          (OTHER, 'Other'),
                         
                         ]



    entry_activity_1 = models.CharField(choices=ACTIVITY, max_length=50)
    entry_time_start_1 = models.TimeField(null=True,blank=True, auto_now=False, auto_now_add=False)
    entry_time_end_1 = models.TimeField(null=True,blank=True, auto_now=False, auto_now_add=False)
    entry_note_1 = models.CharField(max_length=200, blank=True)
    
    entry_activity_2 = models.CharField(choices=ACTIVITY, max_length=50)
    entry_time_start_2 = models.TimeField(null=True,blank=True, auto_now=False, auto_now_add=False)
    entry_time_end_2 = models.TimeField(null=True,blank=True, auto_now=False, auto_now_add=False)
    entry_note_2 = models.CharField(max_length=200, blank=True)
    
    entry_activity_3 = models.CharField(choices=ACTIVITY, max_length=50)
    entry_time_start_3 = models.TimeField(null=True,blank=True, auto_now=False, auto_now_add=False)
    entry_time_end_3 = models.TimeField(null=True,blank=True, auto_now=False, auto_now_add=False)
    entry_note_3 = models.CharField(max_length=200, blank=True)
    
    entry_activity_4 = models.CharField(choices=ACTIVITY, max_length=50)
    entry_time_start_4 = models.TimeField(null=True,blank=True, auto_now=False, auto_now_add=False)
    entry_time_end_4 = models.TimeField(null=True,blank=True, auto_now=False, auto_now_add=False)
    entry_note_4 = models.CharField(max_length=200, blank=True)
    
    entry_activity_5 = models.CharField(choices=ACTIVITY, max_length=50)
    entry_time_start_5 = models.TimeField(null=True,blank=True, auto_now=False, auto_now_add=False)
    entry_time_end_5 = models.TimeField(null=True,blank=True, auto_now=False, auto_now_add=False)
    entry_note_5 = models.CharField(max_length=200, blank=True)
    
    entry_activity_6 = models.CharField(choices=ACTIVITY, max_length=50)
    entry_time_start_6 = models.TimeField(null=True,blank=True, auto_now=False, auto_now_add=False)
    entry_time_end_6 = models.TimeField(null=True,blank=True, auto_now=False, auto_now_add=False)
    entry_note_6 = models.CharField(max_length=200,blank=True)
   
    
    class Meta:
        verbose_name_plural = "entries"
        
    def __str__(self):
        return f'{self.entry_location + " - " + self.entry_wtgnumber}'
    
    

    
    
