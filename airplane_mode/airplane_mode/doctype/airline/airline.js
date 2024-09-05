// Copyright (c) 2024, tiv and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airline", {
	/**
	 * Called when the form is refreshed.
	 * If the airline has a website, it adds a link to the form.
	 * @param {frappe.ui.form.Form} frm - The form object.
	 */
	refresh: function (frm) {
		// Get the website from the form.
		let website = frm.doc.website;

		// If the website is not empty.
		if (website) {
			frm.add_web_link(website);
		}
	},
});
