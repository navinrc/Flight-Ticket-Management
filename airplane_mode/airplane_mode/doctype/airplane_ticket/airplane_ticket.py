# Copyright (c) 2024, Navin R C and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe import _
import random


class AirplaneTicket(Document):
	def validate(self):
		self.remove_duplicates()

	#!hate this logic as its removing rows without user intimation, recheck on submission
	def remove_duplicates(self):
		unique_values = set()
		unique_rows = []

		for row in self.add_ons:
			if row.item not in unique_values:
				unique_values.add(row.item)
				unique_rows.append(row)

		self.add_ons = unique_rows

	# <random-integer><random-capital-alphabet-from-A-to-E> - 89E, 21A
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

