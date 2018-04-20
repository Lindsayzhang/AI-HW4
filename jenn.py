import random
import json

TEAM_NAME = "mighty_ducks"  # Pick a team name
MEMBERS = ["mrf9n", "jr5cf", "kc4bf"]

state = {
    "team-code": "eef8976e",
    "game": "sym",
    "opponent-name": "mighty-ducks",
    "prev-repetitions": 10,  # Might be None if first game ever, or other number
    "last-opponent-play": 1,  # 0 or 1 depending on strategy played
    "last-outcome": None,  # Might be None if first game, or whatever outcome of play is
    "prospects": [
        [12, 3],
        [1, 9]
    ]
}

history = {
    "opponent-play": [],
    "play": [],
    "score": 0
}

def tit42tat(state, play):
    global history
    if state["last-outcome"] == None:
        #print("tit42tat")
        history["play"].append(play)
        history["opponent-play"].append(state["last-opponent-play"])
        #print(history)
        return play
    elif len(history["opponent-play"]) == 1:
        history["play"].append(play)
        history["opponent-play"].append(state["last-opponent-play"])
        #print(history)
        return play
    #random check
    if len(history["opponent-play"]) > 4 and len(history["opponent-play"])%5 ==0 and state["prospects"][play][play%1]:
        if history["play"][-1] == 0:
            p = 1
        else:
            p = 0
        print("h", p, "play", play)
        history["play"].append(p)
        history["opponent-play"].append(state["last-opponent-play"])
        #print(history)
        return p
    if history["opponent-play"][-1] == state["last-opponent-play"]:
        p = state["last-opponent-play"]
        history["play"].append(p)
        history["opponent-play"].append(state["last-opponent-play"])
        #print("same")
        return p
    else:
        history["play"].append(play)
        history["opponent-play"].append(state["last-opponent-play"])
        #print(history)
        return play




def decide(state):
    #global history
    #history["score"] += state["last-outcome"]
    if state["prospects"][0][0] > state["prospects"][1][0]:
        #dominant strategy to play 0
        if state["prospects"][0][1] > state["prospects"][1][1]:
            return 0
        #mixed strategy, play best outcome first with tit 4 2 tat strategy
        elif state["prospects"][0][1] < state["prospects"][1][1]:
            play = tit42tat(state, 0)
            #print("top")
            return play
    elif state["prospects"][0][0] < state["prospects"][1][0]:
        if state["prospects"][0][1] < state["prospects"][1][1]:
            return 1
        #mixed strategy, play best outcome first with tit 4 2 tat strategy
        elif state["prospects"][0][1] > state["prospects"][1][1]:
            play = tit42tat(state, 1)
            #print("bottom")
            return play


def get_move(state):
    '''if state["prospects"][0][0] > state["prospects"][1][0] and state["prospects"][0][1] > state["prospects"][1][1]:
        final_move = 0
    elif state["prospects"][1][1] > state["prospects"][0][1] and state["prospects"][1][0] > state["prospects"][0][0]:
        final_move = 1
    else:
        final_move = decide(state)
    print(final_move)'''
    play = decide(state)
    return {
        "team-code": state["team-code"],
        "move": play
    }


###################################
if __name__ == "__main__":  #
    global hmm
    hmm = state
    myscore = 0
    oppscore = 0
    i = 0
    while i < 10:
        myplay = get_move(state)
        other = int(input('Opponent plays: '))
        hmm["last-opponent-play"] = other
        hmm["last-outcome"] = hmm["prospects"][myplay["move"]][other]
        myscore += hmm["last-outcome"]
        opprospect = hmm["prospects"]
        temp = opprospect[0][1]
        opprospect[0][1] = opprospect[1][0]
        opprospect[1][0] = temp
        oppscore += opprospect[myplay["move"]][other]
        print("me: ",myplay["move"]," score: ", myscore,"\nopponent: ",other, " score: ", oppscore)
        i += 1

###################################
