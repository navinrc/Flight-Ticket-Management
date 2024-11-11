import frappe

@frappe.whitelist(allow_guest=True)
def show_me():
    return frappe.render_template("templates/pages/show_me.html", context={})