import json
from players import *
from copy import deepcopy
import numpy as np

empty_board = [
    [BLANK, BLANK, BLANK],
    [BLANK, BLANK, BLANK],
    [BLANK, BLANK, BLANK]
]

players = ["X", "O"]
current_player = "X"

all_states = []
previous_states = []
current_states = [empty_board]

def locate_blank_cells(state):
    locations = []
    for i in range(3):
        for j in range(3):
            if state[i][j] == BLANK:
                locations.append((i, j))
    return locations

def remove_reflections(states):
    reflections_removed = states.copy()
    removed_indexes = []
    for i, state in enumerate(states):
        for test_state in states[:i]:
            if i not in removed_indexes:
                pop_index = i - (len(states) - len(reflections_removed))
                #print(f"DEBUG - remove_reflections - I: {i}; Len: {len(reflections_removed)}; Pop Index {pop_index}")
                # VERTICAL REFLECTION
                for x in range(3):
                    if not (state[x][0] == test_state[x][2] and state[x][1] == test_state[x][1]):
                        break
                else:
                    reflections_removed.pop(pop_index)
                    removed_indexes.append(i)
                    continue

                # HORIZONTAL REFLECTION
                for x in range(3):
                    if not (state[0][x] == test_state[2][x] and state[1][x] == test_state[1][x]):
                        break
                else:
                    reflections_removed.pop(pop_index)
                    removed_indexes.append(i)
    return reflections_removed

def remove_rotations(states):
    rotations_removed = states.copy()
    removed_indexes = []
    for i, state in enumerate(states):
        for test_state in states[:i]:
            if i not in removed_indexes:
                pop_index = i - (len(states) - len(rotations_removed))
                rotation = deepcopy(test_state)
                remove_state = False
                for x in range(4):
                    rotation = list(zip(*rotation[::1]))
                    if np.array_equal(state, rotation):
                        remove_state = True
                if remove_state:
                    rotations_removed.pop(pop_index)
                    removed_indexes.append(i)
    return rotations_removed

for turn in range(9):
    all_states.append(current_states)
    previous_states = [deepcopy(state) for state in current_states]
    current_states = []

    current_player = players[(players.index(current_player) + 1) % len(players)]

    print(f"PROGRESS - Turn: {turn}; Player: {current_player}; Previous States: {len(previous_states)}")

    for previous_state in previous_states:
        blank_cells = locate_blank_cells(previous_state)
        for cell in blank_cells:
            state = deepcopy(previous_state)
            state[cell[0]][cell[1]] = current_player
            current_states.append(state)

    current_states = remove_reflections(current_states)
    current_states = remove_rotations(current_states)

with open("gamestates.json", "w") as f:
    json.dump(all_states, f)
print("Done!")
