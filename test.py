state = {
	"team-code": "eef8976e",
	"game": "sym",
	"opponent-name": "mighty-ducks",
	"prev-repetitions": None, #Might be None if first game ever, or other number
	"last-opponent-play": 1, #0 or 1 depending on strategy played
	"last-outcome": 4, #Might be None if first game, or whatever outcome of play is
	"prospects": [
		[4,3],
		[5,2]
	]
}

load_data = {
	"opponent-play":[],
	"play":[]
}

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
		return betray
	elif state["prev-repetitions"]==1:
		history = load_data
		history["opponent-play"].append(state["last-opponent-play"])
		history["play"].append(cooperation)
		return cooperation
	else:
		history["opponent-play"].append(state["last-opponent-play"])
		if (history["opponent-play"][-1]==betray and history["play"][-1]==cooperation):
			history["play"].append(betray)
			return betray
		else:# history["opponent-play"][-1]==cooperation & both betray
			history["play"].append(cooperation)
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

print(get_move(state))