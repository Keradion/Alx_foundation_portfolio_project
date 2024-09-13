from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class NewExpenseForm(FlaskForm):
    """
      Class Define Form / Fields To Handle Create New Expense
      Operation By The User

    """
    amount = StringField('Expense Amount', validators=[DataRequired()])
    description = TextAreaField('Expense Reason',  validators=[DataRequired()])
    submit_button = SubmitField('Add Expense')

