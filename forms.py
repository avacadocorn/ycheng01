# forms.py

from wtforms import Form, StringField, SelectField, validators


class SearchForm(Form):
    choices = [('Item', 'Item'),
               ('Store', 'Store'),
               ('Date_to_purchase', 'Date_to_purchase')]
    select = SelectField('Search for record:', choices=choices)
    search = StringField('')


class StoreForm(Form):

    item = StringField('Item')
    price = StringField('Price')
    quantity = StringField('Quantity')
    store_name = StringField('Store Name')
    address = StringField('Address')
    date_to_purchase = StringField('Date To Purchase')
    note = StringField('Note')
