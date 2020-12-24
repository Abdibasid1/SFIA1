from application import app, db
from application.models import Boxer, Club
from application.forms import BoxerForm, ClubForm
from flask import render_template, request, redirect, url_for

@app.route("/")
@app.route("/home")
def home():
    all_boxers = Boxer.query.all() 
    all_clubs = Club.query.all()
#   return render_template("index.html", title="Home", all_boxers=all_boxers)
    return render_template("index.html", title="Home", all_boxers=all_boxers, all_clubs=all_clubs)


@app.route("/addboxer", methods=["GET","POST"])
def addboxer():
    form = BoxerForm()
    if request.method == "POST":
        if form.validate_on_submit():
            new_boxer = Boxer(
                firstname=form.firstname.data,
                lastname=form.lastname.data,
                weightclass=form.weightclass.data,
                email=form.email.data,
                club=form.club.data)
            db.session.add(new_boxer)
            db.session.commit()
            return redirect(url_for("home"))
    return render_template("addboxer.html", title="Add a boxer", form=form)

@app.route("/club", methods=["GET", "POST"])
def club():
    form = ClubForm()
#    boxer = Boxer.query.filter_by(boxer_id=boxer_id).first()
    if request.method == "POST":
        if form.validate_on_submit():
            new_club = Club(
                clubname=form.clubname.data,
                clublocation=form.clublocation.data,
                email=form.email.data,
                clubmanager=form.clubmanager.data)
            db.session.add(new_club)
            db.session.commit()
            return redirect(url_for("home"))
    return render_template("club.html", form=form, title="Update Club")


@app.route("/update/<int:boxer_id>", methods=["GET", "POST"])
def update(boxer_id):
    form = BoxerForm()
    boxer = Boxer.query.filter_by(id=boxer_id).first()
    if request.method == "POST":
        if boxer is not None: 
            boxer.firstname = form.firstname.data
            boxer.lastname = form.lastname.data
            boxer.weightclass = form.weightclass.data
            boxer.email = form.email.data
            db.session.commit()
            return redirect(url_for("home"))
        return "not found"
    
    return render_template("update.html", form=form, title="Update boxer", boxer=boxer)

@app.route("/delete/<int:boxer_id>", methods=["GET", "POST"])
def delete(boxer_id):
#    club = Clubs.query.filter_by(boxer_id=boxer_id).first()
    boxer = Boxer.query.filter_by(id=boxer_id).first()
    if boxer is not None:
        db.session.delete(boxer)
        db.session.commit()
        return redirect(url_for("home"))
    return "not found" 

@app.route("/deleteclub/<int:club_id>", methods=["GET", "POST"])
def deleteclub(club_id):
    club = Club.query.filter_by(id=club_id).first()
    if club is not None:
        db.session.delete(club)
        db.session.commit()
        return redirect(url_for("home"))
    return "not found" 















