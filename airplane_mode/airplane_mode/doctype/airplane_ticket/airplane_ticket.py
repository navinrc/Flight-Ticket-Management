# Copyright (c) 2024, Navin R C and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe import _
import random

# airplane_ticket.py
class AirplaneTicket(Document):
	def calculate_total_amount(self):
		# Calculate total by adding Flight Price and all add-ons' Amounts
		total_add_ons = sum(add_on.amount for add_on in self.add_ons)
		self.total_amount = self.flight_price + total_add_ons

	def remove_duplicate_add_ons(self):
		# Remove duplicate add-ons based on the 'Item' field
		unique_add_ons = {}
		for add_on in self.add_ons:
			if add_on.item not in unique_add_ons:
				unique_add_ons[add_on.item] = add_on
		self.add_ons = list(unique_add_ons.values())

	def validate(self):
		self.calculate_total_amount()
		self.remove_duplicate_add_ons()

	# Generate seat number in the format "<random-integer><random-capital-letter-from-A-to-E>"
	def generate_seat_number(self):
		# Generate a random integer
		random_integer = random.randint(0, 9)

		# Generate a random capital letter from A to E
		random_letter = chr(random.randint(ord("A"), ord("E")))

		# Combine both to form the desired pattern
		self.seat = f"{random_integer}{random_letter}"

	def before_submit(self):
		# Check if the status is "Boarded"
		if self.status != "Boarded":
			# Raise an error to prevent submission
			frappe.throw(_("Cannot submit the document. Status must be 'Boarded' to submit."))

	def before_insert(self):
		self.generate_seat_number()
