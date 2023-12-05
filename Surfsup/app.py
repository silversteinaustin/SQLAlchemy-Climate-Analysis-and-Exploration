# Import the dependencies.
from flask import Flask, jsonify
import numpy as np
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
app = Flask(__name__)

#################################################
# Database Setup
#################################################
@app.route("/")
def home():
    if __name__ == "__main__":
        app.run(debug=True)

# reflect an existing database into a new model

# reflect the tables


# Save references to each table


# Create our session (link) from Python to the DB


#################################################
# Flask Setup
#################################################



#################################################
# Flask Routes
#################################################
