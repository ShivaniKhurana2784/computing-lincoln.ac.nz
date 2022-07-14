from asyncio import events
from flask import render_template, request, redirect
from app import app, db
from app.models import Members, Events, Event_Stage, Teams

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/athletic', methods=['GET'])
def athletic():
    members = Members.query.all()
    return render_template('athletic.html', members=members)


@app.route('/details', methods=['POST'])
def details():
    team_id = request.form.get('member')
    events = Events.query.filter_by(NZTeam=team_id).all()
    for k in events:
        event_stage = Event_Stage.query.filter_by(EventID=k.id).all()
    print(event_stage)
    return render_template('upcoming_events.html', events=events, event_stage=event_stage)


@app.route('/admin')
def admin():
    return render_template('admin/index.html')

@app.route('/admin/add_member', methods=['GET', 'POST'])
def add_member():
    if request.method == 'POST':
        form = request.form
        team_id = form.get('teams')
        first_name = form.get('fname')
        last_name = form.get('lname')
        city = form.get('city')
        birthdate = form.get('date')
        if team_id or first_name or last_name or city or birthdate:
            entry = Members(TeamID = team_id, FirstName = first_name, LastName=last_name, City=city, Birthdate=birthdate)
            db.session.add(entry)
            db.session.commit()
        return render_template('admin/add_member.html')
    
    if request.method == 'GET':
        teams_ids = Teams.query.all()
        return render_template('admin/add_member.html', teams_ids=teams_ids)


@app.route('/admin/add_team', methods=['GET', 'POST'])
def add_team():
    if request.method == 'POST':
        form = request.form
        team_name = form.get('teamname')
        print(team_name, '----------')
        if team_name:
            teams = Teams(TeamName = team_name)
            db.session.add(teams)
            db.session.commit()
        return render_template('admin/add_team.html')
    
    if request.method == 'GET':
        return render_template('admin/add_team.html')


@app.route('/admin/add_event', methods=['GET', 'POST'])
def add_event():
    if request.method == 'POST':
        form = request.form
        eventname = form.get('eventname')
        sport = form.get('sport')
        teams = form.get('teams')
        if eventname or sport or teams:
            entry = Events(EventName = eventname, Sport=sport, NZTeam=teams)
            db.session.add(entry)
            db.session.commit()
        return render_template('admin/add_event.html')
    
    if request.method == 'GET':
        teams_ids = Teams.query.all()
        return render_template('admin/add_event.html', teams_ids=teams_ids)


@app.route('/admin/add_event_stage', methods=['GET', 'POST'])
def add_event_stage():
    if request.method == 'POST':
        form = request.form
        eventname = form.get('eventname')
        sport = form.get('sport')
        teams = form.get('teams')
        if eventname or sport or teams:
            entry = Event_Stage(EventName = eventname, Sport=sport, NZTeam=teams)
            db.session.add(entry)
            db.session.commit()
        return render_template('admin/add_event_stage.html')
    
    if request.method == 'GET':
        event_ids = Events.query.all()
        return render_template('admin/add_event_stage.html', event_ids=event_ids)


# Report calculations
@app.route('/admin/reports', methods=['GET', 'POST'])
def reports():
    members = Members.query.all()
    return render_template('admin/reports.html')

@app.route('/admin/reports/<int:id>', methods=['GET', 'POST'])
def reportsByathlete(id):
    print('++++++++++++++',id)
    members = Members.query.all()
    return render_template('admin/reports_by_athlete.html')

# @app.errorhandler(Exception)
# def error_page(e):
#     return "of the jedi"