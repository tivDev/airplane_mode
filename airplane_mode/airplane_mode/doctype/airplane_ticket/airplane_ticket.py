# Copyright (c) 2024, tiv and contributors
# For license information, please see license.txt

import frappe
import random
from frappe.model.document import Document


class AirplaneTicket(Document):
    
	def before_save(self):
		# Calculate the total amount of the airplane ticket.
		self.total_amount = self.flight_price + sum([ad_on.amount for ad_on in self.ad_ons])
		# call function
		self.check_capacity()
	
	def before_insert(self):
		# Generate a random seat number for the airplane ticket.
		# The seat number is a combination of a random number between 1 and 99
		# and a random uppercase letter from the set 'ABCDE'.
		self.seat = f"{random.randint(1,99)}{random.choice('ABCDE')}"

	def on_submit(self):
		# call function
		self.check_capacity

	def check_capacity(self):
		"""
		Check the capacity of the flight to book the ticket. 
		If the flight is full, throw an error.
		"""

		# Define the Doctypes
		doctype_airplane_flight = "Airplane Flight"
		doctype_airplane = "Airplane"
		doctype_airplane_ticket = "Airplane Ticket"

		# Get the flight details
		flight = self.flight
		get_airplane_flight = frappe.db.get_value(
			doctype_airplane_flight, flight, "airplane"
		)
		# Get the capacity of the airplane
		get_airplane = frappe.db.get_value(
			doctype_airplane, get_airplane_flight, "capacity"
		)
		# Get the list of tickets for the flight
		get_airplane_ticket = frappe.db.get_list(
			doctype_airplane_ticket,
			fields=["name", "docstatus"],
			filters={"flight": flight, "docstatus": 1},
		)
		# Check if the flight is full
		if get_airplane == len(get_airplane_ticket):
			frappe.throw(f"You cannot book flight '{flight}' because the flight is already full")