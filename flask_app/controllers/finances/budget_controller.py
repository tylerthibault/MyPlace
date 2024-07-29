from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.finances import budget_model


# ********* CREATE *********
@app.route('/finance/budget/new')
def budget_new():
    return render_template('/budget_new.html')

@app.route('/finance/budget/create', methods=['POST'])
def budget_create():
    data = {
        **request.form,
    }
    if not budget_model.Budget.validator(**data):
        return redirect('/finance/dashboard')
    
    budget_model.Budget.create_one(**data)
    return redirect('/finance/budgets')

# ********* READ *********
@app.route('/finance/budgets')
def budget_show():
    context = {
    'all_budgets' :  budget_model.Budget.get_all()
    }
    return render_template('/pages/budgets/budget_edit.html', **context)
    
@app.route('/finance/budgets/<int:id>/edit')
def budget_edit(id):
    context = {
        'budget' :  budget_model.Budget.get(id=id)
    }
    return render_template('/pages/budgets/budget_edit.html', **context)


# ********* UPDATE *********
@app.route('/finance/budgets/<int:id>/update', methods=['POST'])
def budget_update(id):
    data = {
        **request.form,
    }

    if not budget_model.Budget.validator(**data):
        return redirect(f'/budgets/{id}/edit')

    budget_model.Budget.update_one({'id':id}, **data)
    return redirect(f'/budgets/{id}/edit')

# ********* DELETE *********
@app.route('/finance/budgets/<int:id>/delete')
def budget_delete(id):
    budget_model.Budget.delete_one(id=id)
    return redirect('/budgets')