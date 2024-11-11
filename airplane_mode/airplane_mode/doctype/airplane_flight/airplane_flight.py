# Copyright (c) 2024, Navin R C and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator


class AirplaneFlight(WebsiteGenerator):
	def before_submit(self):
		# Check if the status is "Boarded"
		self.status = "Completed"