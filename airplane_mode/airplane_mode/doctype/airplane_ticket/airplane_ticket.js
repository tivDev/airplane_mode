// Copyright (c) 2024, tiv and contributors
// For license information, please see license.txt

frappe.ui.form.on('Airplane Ticket', {
	refresh: function (frm) {
		frm.add_custom_button(
		  "Assign Seat",
		  () => {
			frappe.prompt(
			  [{ fieldname: "seat", fieldtype: "Data", label: "Seat Number" }],
			  function (values) {
				frm.set_value("seat", values.seat);
			  },
			  "Select Seat",
			  "Set"
			);
		  },
		  "Action"
		);
	  },
});
