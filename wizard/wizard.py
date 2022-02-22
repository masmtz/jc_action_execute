# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError


class ChangeDate4013Wizard(models.TransientModel):
    _name = 'change.date.4013.wizard'
    _description = 'Wizard action for change date in 4013 records'

    date_doc = fields.Date()

    def change_date(self):
        prod_ids = self._context.get('active_ids')
        user = self.env.user
        if user.has_group('jc_action_execute.group_change_sacrificing_date'):
            if prod_ids and self.date_doc:
                for sid in prod_ids:
                    production = self.env['prodigia.mrp.production.jc'].browse(sid)
                    if production.state == 'done':
                        production.write({'date_sacrificing': self.date_doc,})
            else:
                raise UserError('No has seleccionado registros o fecha valida')
        else:
            raise UserError('No tienes permisos para ejecutar esta acción')
