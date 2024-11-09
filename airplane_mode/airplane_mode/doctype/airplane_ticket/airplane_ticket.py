# Copyright (c) 2024, Navin R C and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe import _


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

	def before_submit(self):
		# Check if the status is "Boarded"
		if self.status != "Boarded":
			# Raise an error to prevent submission
			frappe.throw(_("Cannot submit the document. Status must be 'Boarded' to submit."))
