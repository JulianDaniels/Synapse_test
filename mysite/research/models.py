from django.db import models

class Post(models.Model): #makes a table
	title = models.CharField(max_length=140)
	body = models.TextField()
	date = models.DateTimeField()
class RGs(models.Model):
	Capability = models.CharField(max_length=140)
	Capability_Status = models.PositiveIntegerField()
class Units(models.Model):
	RG = models.CharField(max_length=140)

class Bioscience(models.Model):
	results = models.CharField(max_length=150)
	ca = models.CharField(max_length=150)
	rg = models.CharField(max_length=150)	

class Bio(models.Model):
	survey_results = models.CharField(max_length=150)
	enterprise = models.CharField(max_length=150)
	operating_unit = models.CharField(max_length=150)	
	ca = models.CharField(max_length=150)
	rg = models.CharField(max_length=150)
	respondent = models.CharField(max_length=150)
	respondent_title = models.CharField(max_length=150)
	capability_status = models.CharField(max_length=150)
	people = models.CharField(max_length=150)
	tools = models.CharField(max_length=150)
	processes = models.CharField(max_length=150)
	equipment = models.CharField(max_length=150)
	facilities = models.CharField(max_length=150)
	supplies = models.CharField(max_length=150)
	catalogue = models.CharField(max_length=150)
	capability_group = models.CharField(max_length=150)
	capability_subgroup = models.CharField(max_length=150)
	capability = models.CharField(max_length=150)
	Capability_Status_rank = models.CharField(max_length=150)
	People_avg = models.CharField(max_length=150)
	Tools_avg = models.CharField(max_length=150)
	Processes_avg = models.CharField(max_length=150)
	Equipment_avg = models.CharField(max_length=150)
	Facilities_avg = models.CharField(max_length=150)
	Supplies_avg = models.CharField(max_length=150)
	average = models.CharField(max_length=150)

#make metadata -> easier to reference later

	def __str__(self):
	    return self.survey_results
      
