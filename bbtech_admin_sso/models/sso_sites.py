# -*- coding: utf-8 -*-
import json
from base64 import b64encode

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

from odoo import fields, models, api
from datetime import *


class SSOSites(models.Model):
    _name = 'sso.sites'
    _description = 'SSO Sites'

    name = fields.Char(required=True)
    site_url = fields.Char(required=True)
    db_name = fields.Many2one('tbc_saas',required=True)

    _sql_constraints = [
        ('db_name', 'unique(db_name)', 'DB Name already exists!')
    ]

    def go_to_website(self):
        data = {
            'login': self.env.user.login,
            'site_from': self.env['ir.config_parameter'].sudo().get_param('web.base.url'),
            'date_time': datetime.today().strftime("%d/%m/%Y,%H:%M:%S")
        }
        group_id = 'admin'
        url = 'www.texasbook.com'
        encode_data = json.dumps(data).encode("utf-8")
        key = b64encode((group_id + url).encode())
        cipher = AES.new(key, AES.MODE_CBC)
        ct_bytes = cipher.encrypt(pad(encode_data, AES.block_size))
        iv = b64encode(cipher.iv).decode()
        ct = b64encode(ct_bytes).decode()
        token = b64encode(json.dumps(
            {'iv': iv, 'ciphertext': ct}).encode("utf-8")).decode()
        return {
            "url": self.site_url.rstrip('/') + "/singlesignon/" + token,
            "type": "ir.actions.act_url",
        }
