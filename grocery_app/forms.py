from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField, FloatField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, URL
from grocery_app.models import ItemCategory, GroceryStore


class GroceryStoreForm(FlaskForm):
    """Form for adding/updating a GroceryStore."""

    title = StringField(
        "Store title", validators=[DataRequired(), Length(min=3, max=80)]
    )
    address = StringField(
        "Address", validators=[DataRequired(), Length(min=10, max=80)]
    )
    submit = SubmitField("Submit")

class GroceryItemForm(FlaskForm):
    """Form for adding/updating a GroceryItem."""

    name = StringField("Item name", validators=[DataRequired(), Length(min=3, max=30)])
    price = FloatField("Item price", validators=[DataRequired()])
    category = SelectField("Category", choices=ItemCategory.choices())
    photo_url = StringField(
        "Photo URL", validators=[DataRequired(), URL(require_tld=True)]
    )
    store = QuerySelectField(
        "Store", query_factory=lambda: GroceryStore.query, allow_blank=False
    )
    submit = SubmitField("Submit")