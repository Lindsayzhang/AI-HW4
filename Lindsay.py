TEAM_NAME = "247AI" #Pick a team name
MEMBERS = ["hg5mc","wz4u","jw6qs", "jz5ez"]
history = {
	"opponent-play":[],
	"play":[]
}
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

def get_move(state):
	if state["game"]=="sym":
		if state["prospects"][0][0]>state["prospects"][1][1]:
			cooperation=0
			betray=1
		elif state["prospects"][0][0]<state["prospects"][1][1]:
			cooperation=1
			betray=0
		elif state["prospects"][0][1]<state["prospects"][1][0]:
			cooperation =  0
			betray = 1
		else:
			cooperation = 1
			betray=0
		if state["prev-repetitions"]==0:
			final_move=betray
		else:
			# A>B>??,D>C>?? 4 cases
			if state["prospects"][cooperation][cooperation]>=state["prospects"][cooperation][betray] \
			and state["prospects"][cooperation][betray]>state["prospects"][betray][betray] \
				and state["prospects"][cooperation][betray]>state["prospects"][betray][cooperation]:
				final_move = cooperation

			# B>A>??, C>D>?? 4 cases
			elif state["prospects"][cooperation][betray]>state["prospects"][cooperation][cooperation] \
			and state["prospects"][cooperation][cooperation]>state["prospects"][betray][betray] \
				and state["prospects"][cooperation][cooperation]>state["prospects"][betray][cooperation]:
				final_move = cooperation

			# A>D>??, D>A>?? 4 cases
			elif state["prospects"][cooperation][cooperation]>state["prospects"][betray][betray] \
				and state["prospects"][betray][betray]>state["prospects"][cooperation][betray] \
				and state["prospects"][betray][betray]>state["prospects"][betray][cooperation]:
				# if same, stay same
				if state["last-outcome"]==state["prospects"][cooperation][cooperation] \
					or state["last-outcome"]==state["prospects"][betray][betray]:
					final_move = state["last-opponent-play"]
				else:
					final_move = 1-state["last-opponent-play"]

			# B>C>??, C>B>?? 4 cases
			elif state["prospects"][cooperation][betray]>state["prospects"][betray][cooperation] \
				and state["prospects"][betray][cooperation]>state["prospects"][cooperation][cooperation] \
				and state["prospects"][betray][cooperation]>state["prospects"][betray][betray]:
				# if same, be different
				if state["last-outcome"]==state["prospects"][cooperation][cooperation] \
					or state["last-outcome"]==state["prospects"][betray][betray]:
					final_move = 1-state["last-opponent-play"]
				else:
					final_move = state["last-opponent-play"]				

			# BDAC, ACBD betray 4 cases
			elif state["prospects"][cooperation][betray]>state["prospects"][betray][betray]>state["prospects"][cooperation][cooperation]>state["prospects"][betray][cooperation] \
				or state["prospects"][cooperation][cooperation]>state["prospects"][betray][cooperation]>state["prospects"][cooperation][betray]>state["prospects"][betray][betray]:
				final_move = cooperation

			else: # 4 cases
				final_move = state["last-opponent-play"]

		return {
		"team-code": state["team-code"],
		"move": final_move
		}
