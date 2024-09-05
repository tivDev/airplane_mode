# Copyright (c) 2024, tiv and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
from frappe.website.website_generator import WebsiteGenerator


class AirplaneFlight(WebsiteGenerator,Document):
	def before_submit(self):
		self.status = "Completed"
