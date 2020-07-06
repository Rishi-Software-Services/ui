from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("UI"),
			"items": [
				{
					"type": "doctype",
					"name": "ui doc",
					"onboard": 1,
				},
				
			]
		},
		
	]
