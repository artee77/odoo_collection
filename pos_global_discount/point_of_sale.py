from openerp.osv import fields, osv

class pos_config(osv.osv):
    _inherit = "pos.config"
    
    _columns = {
        'discount': fields.float('Discount', help="Select the amount above which password is required"),
        'password_discount': fields.char('Discount Password'),
    }
pos_config()