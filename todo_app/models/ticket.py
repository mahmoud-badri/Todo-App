from odoo import models, fields

class Tickets(models.Model):
    _name = 'todo'
    _description = 'Tickets'

    name = fields.Char()
    number = fields.Integer()
    tag = fields.Binary()
    state = fields.Selection([
        ("new", "New"),
        ("doing", "Doing"),
        ("done", "Done"),
    ])
    file = fields.Binary()
    description = fields.Text()
