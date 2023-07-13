import json

STARTING_PROBABILITY = 50

gamestates = json.load(open("gamestates.json", "r"))
gamestate_objects = []

for i, turns in enumerate(gamestates):
    blank_cells = 9 - i
    gamestate_objects.append([])
    for state in gamestates[i]:
        choice_probabilities = [STARTING_PROBABILITY for x in range(blank_cells)]
        gamestate_object = {"gamestate" : state, "turns_taken" : i, "choices" : choice_probabilities}
        gamestate_objects[i].append(gamestate_object)

json.dump(gamestate_objects, open("gamestates_training.json", "w"))
