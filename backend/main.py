from app import create_app
from flask import (Flask, render_template, jsonify, request, redirect, session, flash, Markup)
from sqlalchemy import MetaData


app = create_app()




if __name__ == '__main__': 
    app.run(debug=True)