# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProjectTask(models.Model):
    _inherit = 'project.task'

    @api.depends('checklist_ids')
    def task_progress(self):
        for rec in self:
            total_length = self.env['task.checklist'].search_count([])
            checklist_length = len(rec.checklist_ids)
            if total_length != 0:
                rec.task_progress = (checklist_length * 100) / total_length

    checklist_ids = fields.Many2many('task.checklist', string='Checklist')
    task_progress = fields.Float(compute=task_progress,string='Task Progress', store=True, default=0.0)
    max_rate = fields.Integer(string='Max Rate', default=100)


