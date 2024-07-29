from flask_app import app
from flask_app.controllers import routes_controller, user_controller
from flask_app.controllers.finances import budget_controller, finance_dashboard_controller
 

# keep this at the bottom of this file!!
if __name__=="__main__":	 
    app.run(debug=True)	