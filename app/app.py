from flask import Flask, render_template, request
from database import get_wells
from plot import plot_wells

website = Flask(__name__)

@website.route("/")
def main_page():
	return render_template("index.html")

@website.route("/plot")
def plot():
	depth_min = request.args.get('depth_min', 500)
	grad_min = request.args.get('grad_min', 0.05)
	well_loc = get_wells(depth_min, grad_min)
	myjson = plot_wells(well_loc) 
	return render_template("plot_rich.html", alt_json=myjson)