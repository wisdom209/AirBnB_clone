#!/usr/bin/python3
""""Defines User module"""
from models.base_model import BaseModel
from models import helper_functions


class User(BaseModel):
	"""
	assigns public class attributes that defines users

	Arguments:
				emails (str) - empty string
				password (str) - empty string
				first_name (str) - empty string
				last_name (str) - empty string
	"""
	email = ""
	password = ""
	first_name = ""
	last_name = ""

	def all():
		"""Get all instances"""
		return helper_functions.get_all("User")

	@staticmethod
	def count():
		"""Count all class instances"""
		return helper_functions.get_all_count(User)

	@staticmethod
	def show(class_name,instance_id):
		"""Show the needed instance"""
		return helper_functions.show_instance(class_name, instance_id)
