TEAM_NAME = "mighty_ducks" #Pick a team name
MEMBERS = ["mrf9n","jr5cf","kc4bf"]
'''
state = {
	"team-code": "eef8976e",
	"game": "sym",
	"opponent-name": "mighty-ducks",
	"prev-repetitions": 10, #Might be None if first game ever, or other number
	"last-opponent-play": 1, #0 or 1 depending on strategy played
	"last-outcome": 4, #Might be None if first game, or whatever outcome of play is
	"prospects": [
		[2,3],
		[5,4]
	]
}
'''
def decide(state):
	if state["prospects"][0][0]<state["prospects"][1][0] and state["prospects"][0][1]>state["prospects"][1][1]:
		cooperation = 0
		betray = 1
	else:
		cooperation = 1
		betray = 0	
	if state["prev-repetitions"]==None:
		history = {
		"opponent-play":[],
		"play":[betray]
		}
		save_data(history)
		return betray
	elif state["prev-repetitions"]==1:
		history = load_data()
		history["opponent-play"].append(state["last-opponent-play"])
		history["play"].append(cooperation)
		save_data(history)
		return cooperation
	else:
		history = load_data()
		history["opponent-play"].append(state["last-opponent-play"])
		if state["prospects"][cooperation][betray]>state["prospects"][betray][betray]:
			if history["opponent-play"][-1]!=history["play"][-1]: #either one betray
				history["play"].append(betray)
				save_data(history)
				return betray
			else:# history["opponent-play"][-1]==cooperation & both betray
				history["play"].append(cooperation)
				save_data(history)
				return cooperation
		else:
			# traditional tic for tat
			if history["opponent-play"][-1]==betray: #either one betray
				history["play"].append(betray)
				save_data(history)
				return betray
			else:# history["opponent-play"][-1]==cooperation & both betray
				history["play"].append(cooperation)
				save_data(history)
				return cooperation			

def get_move(state):
	if state["prospects"][0][0]>state["prospects"][1][0] and state["prospects"][0][1]>state["prospects"][1][1]:
		final_move=0
	elif state["prospects"][1][1]>state["prospects"][0][1] and state["prospects"][1][0]>state["prospects"][0][0]:
		final_move=1
	else:
		final_move=decide(state)
	return {
	"team-code": state["team-code"],
	"move": final_move
	}
