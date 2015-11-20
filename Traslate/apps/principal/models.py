from django.db import models

class Languaje(models.Model):
	name = models.CharField(max_length = 20)
	def __str__(self):
		return self.name

class Word(models.Model):
	word = models.CharField(max_length = 30)
	def __str__(self):
		return self.word

class Traslate(models.Model):
	origin_languaje = models.ForeignKey(Languaje, null = False, blank = True, related_name='o_languaje')
	dest_languaje = models.ForeignKey(Languaje, null = False, blank = True, related_name='d_languaje')
	origin_word = models.ForeignKey(Word, null = False, blank = True, related_name='o_word')
	dest_word = models.ForeignKey(Word, null = False, blank = True, related_name='d_word')
	def __str__(self):
		return str(self.origin_word)+' '+str(self.dest_word)