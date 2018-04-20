TEAM_NAME = "247AI" #Pick a team name
MEMBERS = ["hg5mc","wz4u","jw6qs","jz5ez"]

import json

state = {
	"team-code": "eef8976e",
	"game": "sym",
	"opponent-name": "mighty-ducks",
	"prev-repetitions":0, #Might be None if first game ever, or other number
	"last-opponent-play": 1, #0 or 1 depending on strategy played
	"last-outcome": 4, #Might be None if first game, or whatever outcome of play is
	"prospects": [
		[5,2],
		[4,3]
	]
}


def get_move(state):
	if state["game"]=="sym":
		# decide which (0/1) is cooperation
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

		# A>B>C>D, ABDC,DCAB, DCBA (4 cases), e.g. [[4,3],[2,1]], we directly cooperate
		if state["prospects"][cooperation][cooperation]>=state["prospects"][cooperation][betray] \
		and state["prospects"][cooperation][betray]>=state["prospects"][betray][betray] \
			and state["prospects"][cooperation][betray]>=state["prospects"][betray][cooperation]:
			print("1st")
			final_move = cooperation

		# B>A>C>D, BADC, CDAB, CDBA (4 cases), e.g. [[3,4],[1,2]], we directly cooperate
		elif state["prospects"][cooperation][betray]>=state["prospects"][cooperation][cooperation] \
		and state["prospects"][cooperation][cooperation]>=state["prospects"][betray][betray] \
			and state["prospects"][cooperation][cooperation]>=state["prospects"][betray][cooperation]:
			print("2nd")
			final_move = cooperation

		# A>D>B>C, ADCB, DABC, DACB (4 cases), e.g. [[4,1],[2,3]]
		elif state["prospects"][cooperation][cooperation]>=state["prospects"][betray][betray] \
			and state["prospects"][betray][betray]>=state["prospects"][cooperation][betray] \
			and state["prospects"][betray][betray]>=state["prospects"][betray][cooperation]:
			print("3rd")
			# if the first round, we cooperate
			if state["prev-repetitions"]==0:
				final_move=cooperation
			# if last time, our choice is the same as opponent, choose what we chose last time to stay the same with opponent
			elif state["last-outcome"]==state["prospects"][cooperation][cooperation] \
				or state["last-outcome"]==state["prospects"][betray][betray]:
				final_move = state["last-opponent-play"]
			# if last time, our choice is different from opponent's choice, choose another one to stay the same with opponent
			else:
				final_move = 1-state["last-opponent-play"]

		# B>C>A>D, BCDA, CBAD, CBDA (4 cases), e.g. [[2,4],[3,1]]
		elif state["prospects"][cooperation][betray]>=state["prospects"][betray][cooperation] \
			and state["prospects"][betray][cooperation]>=state["prospects"][cooperation][cooperation] \
			and state["prospects"][betray][cooperation]>=state["prospects"][betray][betray]:
			print("4th")
			# if the first round, we cooperate			
			if state["prev-repetitions"]==0:
				final_move=cooperation
			# if last time, our choice is the same as opponent, choose another one to be different from opponent
			elif state["last-outcome"]==state["prospects"][cooperation][cooperation] \
				or state["last-outcome"]==state["prospects"][betray][betray]:
				final_move = 1-state["last-opponent-play"]
			# if last time, our choice is different from opponent, choose what we chose last time to be different from opponent				
			else:
				final_move = state["last-opponent-play"]				

		# BDAC, ACBD, CADB, DBCA, (4 cases) e.g. [[4,2],[3,1]], we directly cooperate
		elif state["prospects"][cooperation][betray]>=state["prospects"][betray][betray]>=state["prospects"][cooperation][cooperation]>=state["prospects"][betray][cooperation] \
			or state["prospects"][cooperation][cooperation]>=state["prospects"][betray][cooperation]>=state["prospects"][cooperation][betray]>=state["prospects"][betray][betray]:
			print("5th")
			final_move = cooperation

		# ACDB, CABD, DBAC, BDCA (4 cases) e.g. [[4,1],[3,2]], tit for tat
		else: 
			print("6th")
			file_name="AI.json"
			if state["prev-repetitions"]==0:
				final_move=betray
				history = {
					"oppoplay":[],
					"ourplay":[]
				}
				with open(file_name,'w') as file_object:
					json.dump(history, file_object)
				history["ourplay"].append(final_move)
				history = json.dumps(history)
			else:
				with open(file_name,'r') as file_object:
					history=json.load(file_object)
				history["oppoplay"].append(state["last-opponent-play"])
				if state["prev-repetitions"]>=5:
					a = 0
					for i in range(5):
						if history["oppoplay"][-1-i]!=history["ourplay"][-1-i]:
							a+=1
					if a==5 and history["ourplay"][-1]==cooperation:
						final_move = cooperation
					else:
						final_move = state["last-opponent-play"]
				else: 
					final_move = state["last-opponent-play"]
				history["ourplay"].append(final_move)
				history = json.dumps(history)

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