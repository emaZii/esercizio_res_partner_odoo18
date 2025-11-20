# -*- coding: utf-8 -*-
# from odoo import http


# class PixProductLabelCustom(http.Controller):
#     @http.route('/pix_product_label_custom/pix_product_label_custom', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pix_product_label_custom/pix_product_label_custom/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('pix_product_label_custom.listing', {
#             'root': '/pix_product_label_custom/pix_product_label_custom',
#             'objects': http.request.env['pix_product_label_custom.pix_product_label_custom'].search([]),
#         })

#     @http.route('/pix_product_label_custom/pix_product_label_custom/objects/<model("pix_product_label_custom.pix_product_label_custom"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pix_product_label_custom.object', {
#             'object': obj
#         })

