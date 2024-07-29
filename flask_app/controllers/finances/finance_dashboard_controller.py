from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.finances import budget_model


@app.route('/finance/dashboard')
def finance_dashboard():
    # context = {
    #     'current_budget': budget_model.Budget.get('is_active' = 1)
    # }
    return render_template('/finances/dashboard.html')
