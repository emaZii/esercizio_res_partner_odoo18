# -*- coding: utf-8 -*-

from odoo import models, fields, api

class resPartner(models.Model):
    
    _inherit = 'res.partner'

    tipo_cliente = fields.Selection(
        
        selection = [
            ('privato','Privato'),
            ('azienda','Azienda'),
            ('vip', 'ClienteVip')
        ],
        
        string = "Tipo Cliente",
        required = True
    )
    
    num_identificativo = fields.Integer(
        string = "Numero Identificativo"
    )
    
    codice_cliente = fields.Char(
        string = "Codice Cliente",
        compute = "_compute_codice_cliente",
        store = True,
        readonly = True
    )
        
    data_creazione = fields.Date(
        compute='_compute_data_creazione',
        store=False)
    
    @api.depends('tipo_cliente','num_identificativo')
    def _compute_codice_cliente(self):
        for rec in self:
            if rec.tipo_cliente and rec.num_identificativo:
                rec.codice_cliente = f"{rec.tipo_cliente}-{rec.num_identificativo}"
            else:
                rec.codice_cliente = False
                
    @api.onchange('tipo_cliente', 'num_identificativo')
    def _onchange_codice_cliente(self):
        if self.tipo_cliente and self.num_identificativo:
            self.codice_cliente = f"{self.tipo_cliente}-{self.num_identificativo}"
        else:
            self.codice_cliente = False
    
    
    def _compute_data_creazione (self):
        for rec in self:
            rec.data_creazione = False
            if rec.create_date:
                rec.data_creazione = rec.create_date.date() 
            
    #@api.model
    def create(self, vals):
        partner = super().create(vals)
        if partner.tipo_cliente and partner.num_identificativo:
            partner.codice_cliente = f"{partner.tipo_cliente}-{partner.num_identificativo}"
        return partner

    def write(self, vals):
        res = super().write(vals)
        for partner in self:
            if 'tipo_cliente' in vals or 'num_identificativo' in vals:
                if partner.tipo_cliente and partner.num_identificativo:
                    partner.codice_cliente = f"{partner.tipo_cliente}-{partner.num_identificativo}"
                else:
                    partner.codice_cliente = False
        return res