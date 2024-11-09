// Copyright (c) 2024, Navin R C and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airplane Ticket", {
	refresh(frm) {},
	flight_price(frm) {
		frm.trigger("update_total_amount");
	},
	update_total_amount(frm) {
		let items_price = 0;
		for (let item of frm.doc.add_ons) {
			items_price += item.amount;
		}

		const amount = frm.doc.flight_price + items_price;
		frm.set_value("total_amount", amount);
	},
});

frappe.ui.form.on("Airplane Ticket Add-on Item", {
	amount(frm) {
		// trigger fn
		frm.trigger("update_total_amount");
	},
	add_ons_remove(frm) {

		frm.trigger("update_total_amount");
	}
});
