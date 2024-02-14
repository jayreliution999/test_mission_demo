# -*- coding: utf-8 -*-

from odoo import models, fields, api


class TaskChecklist(models.Model):
    _name = 'task.checklist'

    name = fields.Char(string='Name')
    description = fields.Text(string='Description')
