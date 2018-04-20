TEAM_NAME = "247AI" #Pick a team name
MEMBERS = ["hg5mc","wz4u","jw6qs","jz5ez"]

state = {
	"team-code": "eef8976e",
	"game": "sym",
	"opponent-name": "mighty-ducks",
	"prev-repetitions": 10, #Might be None if first game ever, or other number
	"last-opponent-play": 1, #0 or 1 depending on strategy played
	"last-outcome": 4, #Might be None if first game, or whatever outcome of play is
	"prospects": [
		[5,2],
		[4,3]
	]
}
		

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

		print("cooperation: ", cooperation)
		print("betray: ", betray)

		# A>B>??,D>C>?? 4 cases
		if state["prospects"][cooperation][cooperation]>=state["prospects"][cooperation][betray] \
		and state["prospects"][cooperation][betray]>=state["prospects"][betray][betray] \
			and state["prospects"][cooperation][betray]>=state["prospects"][betray][cooperation]:
			print("1st")
			final_move = cooperation

		# B>A>??, C>D>?? 4 cases
		elif state["prospects"][cooperation][betray]>=state["prospects"][cooperation][cooperation] \
		and state["prospects"][cooperation][cooperation]>=state["prospects"][betray][betray] \
			and state["prospects"][cooperation][cooperation]>=state["prospects"][betray][cooperation]:
			print("2nd")
			final_move = cooperation

		# A>D>??, D>A>?? 4 cases
		elif state["prospects"][cooperation][cooperation]>=state["prospects"][betray][betray] \
			and state["prospects"][betray][betray]>=state["prospects"][cooperation][betray] \
			and state["prospects"][betray][betray]>=state["prospects"][betray][cooperation]:
			print("3rd")
			if state["prev-repetitions"]==0:
				final_move=cooperation
			# if same, stay same
			elif state["last-outcome"]==state["prospects"][cooperation][cooperation] \
				or state["last-outcome"]==state["prospects"][betray][betray]:
				final_move = state["last-opponent-play"]
			else:
				final_move = 1-state["last-opponent-play"]

		# B>C>??, C>B>?? 4 cases
		elif state["prospects"][cooperation][betray]>=state["prospects"][betray][cooperation] \
			and state["prospects"][betray][cooperation]>=state["prospects"][cooperation][cooperation] \
			and state["prospects"][betray][cooperation]>=state["prospects"][betray][betray]:
			print("4th")
			if state["prev-repetitions"]==0:
				final_move=cooperation
			# if same, be different
			elif state["last-outcome"]==state["prospects"][cooperation][cooperation] \
				or state["last-outcome"]==state["prospects"][betray][betray]:
				final_move = 1-state["last-opponent-play"]
			else:
				final_move = state["last-opponent-play"]				

		# BDAC, ACBD betray 4 cases
		elif state["prospects"][cooperation][betray]>=state["prospects"][betray][betray]>=state["prospects"][cooperation][cooperation]>=state["prospects"][betray][cooperation] \
			or state["prospects"][cooperation][cooperation]>=state["prospects"][betray][cooperation]>=state["prospects"][cooperation][betray]>=state["prospects"][betray][betray]:
			print("5th")
			final_move = cooperation

		else: # 4 cases
			print("6th")
			if state["prev-repetitions"]==0:
				final_move=betray
			else:
				final_move = state["last-opponent-play"]

		return {
		"team-code": state["team-code"],
		"move": final_move
		}

if __name__ == "__main__":  #
    global hmm
    hmm = state
    myscore = 0
    oppscore = 0
    i = 0
    while i < 10:
        myplay = get_move(hmm)
        other = int(input('Opponent plays: '))
        hmm["last-opponent-play"] = other
        hmm["prev-repetitions"]+=1
        hmm["last-outcome"] = hmm["prospects"][myplay["move"]][other]
        myscore += hmm["last-outcome"]
#        opprospect = hmm["prospects"]
#        print(hmm["prospects"])
#        temp = opprospect[0][1]
#        opprospect[0][1] = opprospect[1][0]
#        opprospect[1][0] = temp
        oppscore += hmm["prospects"][other][myplay["move"]]
        print(hmm["prospects"])
        print("me: ",myplay["move"]," score: ", myscore,"\nopponent: ",other, " score: ", oppscore)
        i += 1