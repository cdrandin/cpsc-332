from django.db import models
from django.forms import ModelForm, Textarea


###
# Create post['table] like this ... 
# python manage.py sql dairy_farm
# python manage.py syncdb
###

class Herds(models.Model):
	location = models.CharField(max_length = 30)

	def __unicode__(self):
		return u'%s' % (self.location)

class HerdsForm(ModelForm):
	class Meta:
		model   = Herds 



class Cows(models.Model):
	born             = models.DateField(help_text  = "Please use format: <em>MM/DD/YYYY</em>.")
	acquired         = models.DateField(help_text  = "Please use format: <em>MM/DD/YYYY</em>.")
	source           = models.CharField(max_length = 20)
	breed            = models.CharField(max_length = 20)
	mom              = models.ForeignKey('Cows', related_name='mom_cow')
	dad              = models.ForeignKey('Cows', related_name='dad_cow')
	lineage_comments = models.TextField()
	date_remove      = models.DateField(help_text  = "Please use format: <em>MM/DD/YYYY</em>.")
	herd             = models.ForeignKey('Herds')
	birth_weight     = models.FloatField()
	location         = models.CharField(max_length = 20)

	def __unicode__(self):
		return u'%s %s %s' % (self.born, self.breed, self.herd)

class CowsForm(ModelForm):
	class Meta:
		model   = Cows 

class Vets(models.Model):
	tech_name= models.CharField(max_length = 30)
	address  = models.CharField(max_length = 50)
	city     = models.CharField(max_length = 20)
	state    = models.CharField(max_length = 30)
	zip_code = models.CharField(max_length = 10)

	def __unicode__(self):
		return u'%s %s' % (self.tech_name, self.address)

class VetsForm(ModelForm):
	class Meta:
		model   = Vets 


class Feedings(models.Model):
	herd        = models.ForeignKey('Herds')
	date        = models.DateField(help_text  = "Please use format: <em>MM/DD/YYYY</em>.")
	time        = models.TimeField(help_text  = "Please enter in military format.")
	food_source = models.IntegerField()
	quantity    = models.FloatField()
	waste       = models.FloatField()

	def __unicode__(self):
		return u'%s %s %s' % (self.herd, self.date, self.time)

class FeedingsForm(ModelForm):
	class Meta:
		model   = Feedings 


class Food_Sources(models.Model):
	comments = models.TextField()

	def __unicode__(self):
		return u'%s' % (self.comments)

class Food_SourcesForm(ModelForm):
	class Meta:
		model   = Food_Sources 


class Consultations(models.Model):
	cow    = models.ForeignKey('Cows')
	date   = models.DateField(help_text  = "Please use format: <em>MM/DD/YYYY</em>.")
	weight = models.FloatField()
	vet    = models.ForeignKey('Vets')

	def __unicode__(self):
		return u'%s %s' % (self.cow, self.vet)

class ConsultationsForm(ModelForm):
	class Meta:
		model   = Consultations 


class Treatments(models.Model):
	dose = models.CharField(max_length = 20)
	type = models.CharField(max_length = 20)

	def __unicode__(self):
		return u'%s %s' % (self.dose, self.type)

class TreatmentsForm(ModelForm):
	class Meta:
		model   = Treatments 


class Milkings(models.Model):
	cow      = models.ForeignKey('Cows')
	date     = models.DateField(help_text  = "Please use format: <em>MM/DD/YYYY</em>.")
	quantity = models.FloatField()
	comments = models.TextField()

	def __unicode__(self):
		return u'%s %s %s' % (self.cow, self.date, self.quantity)

class MilkingsForm(ModelForm):
	class Meta:
		model   = Milkings 


class Suppliers(models.Model):
	phone    = models.CharField(max_length = 10)
	address  = models.CharField(max_length = 50)
	city     = models.CharField(max_length = 20)
	state    = models.CharField(max_length = 30)
	zip_code = models.CharField(max_length = 10)

	def __unicode__(self):
		return u'%s %s' % (self.phone, self.address)

class SuppliersForm(ModelForm):
	class Meta:
		model   = Suppliers 


class Food_Purchases(models.Model):
	date          = models.DateField(help_text  = "Please use format: <em>MM/DD/YYYY</em>.")
	delivery_cost = models.FloatField()
	supplier      = models.ForeignKey('Suppliers')

	def __unicode__(self):
		return u'%s %s %s' % (self.date, self.delivery_cost, self.supplier)

class Food_PurchasesForm(ModelForm):
	class Meta:
		model   = Food_Purchases 


class Feed(models.Model):
	food_purchase = models.ForeignKey('Food_Purchases')
	protein       = models.FloatField()
	quantity      = models.FloatField()
	cost          = models.FloatField()
	amount        = models.FloatField()

	def __unicode__(self):
		return u'%s %s %s' % (self.food_purchase, self.protein, self.cost)

class FeedForm(ModelForm):
	class Meta:
		model   = Feed 