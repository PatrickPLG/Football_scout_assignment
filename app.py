# Importering af bibloteker og filer
from flask import Flask, render_template, request
from player import Attacker, Goalkeeper, Defender, Midfielder

app = Flask(__name__)

# Lister som opbevare dataene
goalkeepers = [Goalkeeper("Nicki Chi", 23, "Trolp FC", 18)]
defenders = [Defender("Alexander Jul", 25, "Tripa FC", 32)]
midfielders = [Midfielder("Adam Sul", 19, "Okaype FC", 200)]
attackers = [Attacker("Jacob Lund", 21, "Yeppep FC", 8)]

# Startsiden/index
@app.route('/')
def index():
    # Retunere index.html, med de forskellige lister
    return render_template('index.html', goalkeepers=goalkeepers, defenders=defenders, midfielders=midfielders, attackers=attackers)

# Siden /create
@app.route('/create', methods=['POST', 'GET'])
def create():
    # Hvis der postes noget data
    if request.method == 'POST':
        # Opretter variablen choice, som tager fat i værdierne fra inputtet fra CreateType
        choice = request.form.get('CreateType')
        # Tjekker om inputtet er lig med "Attacker", "Defender" osv.
        # Den retunere derefter siden som passer med inputtet
        if choice == "Attacker":
            return render_template('createattacker.html', page=createattacker)
        elif choice == "Defender":
            return render_template('createdefender.html', page=createdefender)
        elif choice == "Midfielder":
            return render_template('createmidfielder.html', page=createmidfielder)
        elif choice == "Goalkeeper":
            return render_template('creategoalkeeper.html', page=creategoalkeeper)
    # Hvis der ikke bliver postet noget data
    # Så retunere den create.html
    else:
        return render_template('create.html')

# Siden /createattacker
@app.route('/createattacker', methods=['POST', 'GET'])
def createattacker():
    # Hvis der postes noget data
    # Sæt de forskellige parameter som klassen attacker bruger
    # Lig med værdierne i inputsne og retunere index.html
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        team = request.form['team']
        goals = request.form['goals']
        attackers.append(Attacker(name, int(age), team, int(goals)))
        return render_template('index.html', goalkeepers=goalkeepers, defenders=defenders, midfielders=midfielders, attackers=attackers)
    # Hvis der ikke postes noget data
    # Retunere createattacker.html
    else:
        return render_template('createattacker.html')

# Siden /creategoalkeeper
@app.route('/creategoalkeeper', methods=['POST', 'GET'])
def creategoalkeeper():
    # Hvis der postes noget data
    # Sæt de forskellige parameter som klassen goalkeeper bruger
    # Lig med værdierne i inputsne og retunere index.html
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        team = request.form['team']
        saves = request.form['saves']
        goalkeepers.append(Goalkeeper(name, int(age), team, int(saves)))
        return render_template('index.html', goalkeepers=goalkeepers, defenders=defenders, midfielders=midfielders, attackers=attackers)
    # Hvis der ikke postes noget data
    # Retunere creategoalkeeper.html
    else:
        return render_template('creategoalkeeper.html')

# Siden /createdefender
@app.route('/createdefender', methods=['POST', 'GET'])
def createdefender():
    # Hvis der postes noget data
    # Sæt de forskellige parameter som klassen defender bruger
    # Lig med værdierne i inputsne og retunere index.html
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        team = request.form['team']
        blocked = request.form['blocked']
        defenders.append(Defender(name, int(age), team, int(blocked)))
        return render_template('index.html', goalkeepers=goalkeepers, defenders=defenders, midfielders=midfielders, attackers=attackers)
    # Hvis der ikke postes noget data
    # Retunere createdefender.html
    else:
        return render_template('createdefender.html')

# Siden /createmidfielder
@app.route('/createmidfielder', methods=['POST', 'GET'])
def createmidfielder():
    # Hvis der postes noget data
    # Sæt de forskellige parameter som klassen midfielder bruger
    # Lig med værdierne i inputsne og retunere index.html
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        team = request.form['team']
        passes = request.form['passes']
        midfielders.append(Midfielder(name, int(age), team, int(passes)))
        return render_template('index.html', goalkeepers=goalkeepers, defenders=defenders, midfielders=midfielders, attackers=attackers)
    # Hvis der ikke postes noget data
    # Retunere createmidfielder.html
    else:
        return render_template('createmidfielder.html')

# Siden /delete
@app.route('/delete', methods=['POST', 'GET'])
def delete():
    # Hvis der postes noget data
    if request.method == 'POST':
        # Opretter variablen choice, som tager fat i værdierne fra inputtet fra deleteplayer
        choice = request.form.get('deleteplayer')
        # Tjekker om den første karakter i choice er lig med det given bogstav
        # Hvis den er det laves der er en varibel kaldet get_index som tager alt det efter det 
        # Første bogstav. Herefter tjekker den igennem listen og finder der hvor den spiller man skal
        # Findes id og fjerner derefter den spiller.
        if choice[0] == "g":
            get_index = choice[1:]
            index = 0
            for x in range(len(goalkeepers)):
                if goalkeepers[x].id == int(get_index):
                    index = x
            print(index)
            goalkeepers.pop(int(index))
        elif choice[0] == "d":
            get_index = choice[1:]
            index = 0
            for x in range(len(defenders)):
                if defenders[x].id == int(get_index):
                    index = x
            defenders.pop(int(index))
        elif choice[0] == "m":
            get_index = choice[1:]
            index = 0
            for x in range(len(midfielders)):
                if midfielders[x].id == int(get_index):
                    index = x
            midfielders.pop(int(index))
        elif choice[0] == "a":
            get_index = choice[1:]
            index = 0
            for x in range(len(attackers)):
                if attackers[x].id == int(get_index):
                    index = x
            attackers.pop(int(index))
        return render_template('index.html', goalkeepers=goalkeepers, defenders=defenders, midfielders=midfielders, attackers=attackers)
    # Hvis der ikke postes noget data
    # Retunere delete.html
    else:
        return render_template('delete.html', goalkeepers=goalkeepers, defenders=defenders, midfielders=midfielders, attackers=attackers)
    
@app.route('/update', methods=['POST', 'GET'])
def update():
    # Hvis der postes noget data
    if request.method == 'POST':
        # Opretter variablen choice, som tager fat i værdierne fra inputtet fra updateplayer
        choice = request.form.get('updateplayer')

        # Laver variabler som henter værdierne fra deres tilknutne inputs
        update_name = request.form['update_name']
        update_age = request.form['update_age']
        update_team = request.form['update_team']
        update_value = request.form['update_value']
        
        # Tjekker om den første karakter i choice er lig med det given bogstav
        # Hvis den er det laves der er en varibel kaldet get_index som tager alt det efter det 
        # Første bogstav. Herefter tjekker den igennem listen og finder der hvor den spiller man skal
        # Findes id. Der tjekkes der efter om der mangler noget input i nogle felter, og hvis det mangler noget
        # Sættes det bare lig med den gamle værdi, men hvis der er en ny, sættes det til den nye værdi.
        if choice[0] == "g":
            get_index = choice[1:]
            index = 0
            for x in range(len(goalkeepers)):
                if goalkeepers[x].id == int(get_index):
                    index = x
            if update_name == '':
                goalkeepers[index].name = goalkeepers[index].name
            else:
                goalkeepers[index].name = update_name
            if update_age == '':
                goalkeepers[index].age = goalkeepers[index].age
            else:
                goalkeepers[index].age = update_age
            if update_team == '':
                goalkeepers[index].team = goalkeepers[index].team
            else:
                goalkeepers[index].team = update_team
            if update_value == '':
                goalkeepers[index].saves = goalkeepers[index].saves
            else:
                goalkeepers[index].saves = update_value

        elif choice[0] == "d":
            get_index = choice[1:]
            index = 0
            for x in range(len(defenders)):
                if defenders[x].id == int(get_index):
                    index = x
            if update_name == '':
                defenders[index].name = defenders[index].name
            else:
                defenders[index].name = update_name
            if update_age == '':
                defenders[index].age = defenders[index].age
            else:
                defenders[index].age = update_age
            if update_team == '':
                defenders[index].team = defenders[index].team
            else:
                defenders[index].team = update_team
            if update_value == '':
                defenders[index].blocked = defenders[index].blocked
            else:
                defenders[index].blocked = defenders
        elif choice[0] == "m":
            get_index = choice[1:]
            index = 0
            for x in range(len(midfielders)):
                if midfielders[x].id == int(get_index):
                    index = x
            if update_name == '':
                midfielders[index].name = midfielders[index].name
            else:
                midfielders[index].name = update_name
            if update_age == '':
                midfielders[index].age = midfielders[index].age
            else:
                midfielders[index].age = update_age
            if update_team == '':
                midfielders[index].team = midfielders[index].team
            else:
                midfielders[index].team = update_team
            if update_value == '':
                midfielders[index].passes = midfielders[index].passes
            else:
                midfielders[index].passes = update_value
        elif choice[0] == "a":
            get_index = choice[1:]
            index = 0
            for x in range(len(attackers)):
                if attackers[x].id == int(get_index):
                    index = x
            if update_name == '':
                attackers[index].name = attackers[index].name
            else:
                attackers[index].name = update_name
            if update_age == '':
                attackers[index].age = attackers[index].age
            else:
                attackers[index].age = update_age
            if update_team == '':
                attackers[index].team = attackers[index].team
            else:
                attackers[index].team = update_team
            if update_value == '':
                attackers[index].goals = attackers[index].goals
            else:
                attackers[index].goals = update_value
        return render_template('index.html', goalkeepers=goalkeepers, defenders=defenders, midfielders=midfielders, attackers=attackers)
    # Hvis der ikke postes noget data
    # Retunere delete.html
    else:
        return render_template('update.html', goalkeepers=goalkeepers, defenders=defenders, midfielders=midfielders, attackers=attackers)

    

app.run(debug=True, host='0.0.0.0', port=81)