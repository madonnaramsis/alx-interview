#!/usr/bin/python3
"""Lock boxes checker"""


def canUnlockAll(boxes):
    """
    Checks if all boxes can be unlocked
    """
    keys = [0]
    for key in keys:
        if key < len(boxes):
            for new_key in boxes[key]:
                if new_key not in keys and new_key < len(boxes):
                    keys.append(new_key)

    return (len(keys) == len(boxes) or len(boxes) == 0)
