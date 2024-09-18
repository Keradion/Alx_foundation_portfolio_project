from mezgebe import db 
from flask import render_template, flash, redirect, url_for, abort, request, Blueprint, current_app
from mezgebe.expenses.forms import NewExpenseForm
from mezgebe.models import Expense, User
from flask_login import current_user, login_required

expenses = Blueprint('expenses', __name__)


@expenses.route('/expense/new_expense',  methods=['GET', 'POST'])
@login_required
def add_expense():
    """ A Route To Handle a Process To Create a New Expense By a User """
    new_expense_form = NewExpenseForm()
    if new_expense_form.validate_on_submit():
        new_expense = Expense(amount=new_expense_form.amount.data,
                              description=new_expense_form.description.data,
                              user_id=current_user.id)
        db.session.add(new_expense)
        db.session.commit()
        flash('New expense added successfully', 'success')
        return redirect(url_for('main.home'))
    return render_template('expenseform.html', form=new_expense_form)


@expenses.route('/expense/<int:expense_id>')
@login_required
def expense(expense_id):
    """ Retrive an expense associated with a given expense_id """
    expense = Expense.query.filter_by(id=expense_id).all()
    return render_template('expense.html', expense=expense[0])



@expenses.route('/expense/<int:expense_id>/update', methods=['GET', 'POST'])
@login_required
def update_expense(expense_id):
    """ Update An Expense Associated With a Given expense_id """
    expense = Expense.query.filter_by(id=expense_id).all()
    if expense[0].user_id != current_user.id:
        abort(403)
    new_expense_form = NewExpenseForm()
    if new_expense_form.validate_on_submit():
        expense[0].amount = new_expense_form.amount.data
        expense[0].description = new_expense_form.description.data
        db.session.commit()
        flash('Expense has been updated successfully!', 'success')
        return redirect(url_for('expenses.expense', expense_id=expense[0].id))
    elif request.method == 'GET':
        new_expense_form.amount.data = expense[0].amount
        new_expense_form.description.data = expense[0].description
    return render_template('expenseform.html', form=new_expense_form)



@expenses.route('/expense/<int:expense_id>/delete', methods=['GET', 'POST'])
@login_required
def delete_expense(expense_id):
    """ Delete An Expense Associated With a Given expense_id """
    expense = Expense.query.filter_by(id=expense_id).all()
    if expense[0].user_id != current_user.id:
        abort(403)
    db.session.delete(expense[0])
    db.session.commit()
    flash('Expense has been deleted successfully!', 'success')
    return redirect(url_for('main.home'))
