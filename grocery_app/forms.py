from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField, FloatField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, URL


class GroceryStoreForm(FlaskForm):
    """Form for adding/updating a GroceryStore."""

    # TODO: Add the following fields to the form class:
    # - title - StringField
    # - address - StringField
    # - submit button
    title = StringField(u"Title", validators=[DataRequired()])
    address = StringField(u"Address", validators=[DataRequired()])
    submit = SubmitField("Submit")


class GroceryItemForm(FlaskForm):
    """Form for adding/updating a GroceryItem."""

    # TODO: Add the following fields to the form class:
    # - name - StringField
    # - price - FloatField
    # - category - SelectField (specify the 'choices' param)
    # - photo_url - StringField (use a URL validator)
    # - store - QuerySelectField (specify the `query_factory` param)
    # - submit button
    name = StringField("Name", validators=[DataRequired(), Length(min=3, max=40)])
    price = FloatField("Price")
    category = SelectField(
        "Category",
        choices=[
            ("PRODUCE", "Produce"),
            ("DELI", "Deli"),
            ("BAKERY", "Bakery"),
            ("PANTRY", "Pantry"),
            ("FROZEN", "Frozen"),
            ("OTHER", "Other"),
        ],
    )
    photo_url = StringField("Photo Url", validators=[DataRequired(), URL()])
    store = QuerySelectField("Store Name", query_factory=store_query)
    submit = SubmitField("Submit")
