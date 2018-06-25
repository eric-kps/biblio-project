# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Book(models.Model):
    _name = 'biblio.book'
    _description = 'Book'

    name = fields.Char('Title')
    subtitle = fields.Char('Sub-title')
    isbn = fields.Char('ISBN')
    tag_ids = fields.Many2many('biblio.tag', string='Tags')
    author_id = fields.Many2many('res.partner', string='Author')
    coauthor_ids = fields.Many2many('res.partner', string='Co-Authors')
    summary = fields.Text('Summary')


class BookTag(models.Model):
    _name = 'biblio.tag'
    _description = 'Book Tag'

    name = fields.Char('Name')
    color = fields.Integer('Color')
    description = fields.Text('Description')

class Author(models.Model):
    _inherit = 'res.partner'
