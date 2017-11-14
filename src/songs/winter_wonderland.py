from models.music import Chord

lyrics = {
    'bridge1': "In the meadow we can build a snowman,\nWe'll pretend that he is Parson Brown\nHe'll say: Are you married? We'll say: No man,\nBut you can do the job when you're in town.",
    'bridge2': "In the meadow we can build a snowman,\nWe'll pretend that he's a circus clown\nWe'l have lots of fun with mr. Snowman\nUntil the other children knock him down.",
    'outro': 'Walking in a winter wonderland.\nWalking in a winter wonderland.',
    'verse1': "Sleigh bells ring, are you listening?\nIn the lane, snow is glistening\nA beautiful sight, we're happy tonight.\nWalking in a winter wonderland.",
    'verse2': 'Gone away is the bluebird,\nHere to stay is a new bird\nHe sings a love song, while we stroll along\nWalking in a winter wonderland.',
    'verse3': "Later on, we'll conspire,\nAs we dream by the fire\nTo face unafraid, the plans that we've made,\nWalking in a winter wonderland."}

structure = [
    ("Intro", "intro", None),
    ("Verse 1", "verse", "verse1"),
    ("Verse 2", None, "verse2"),
    ("Bridge 1", "bridge", "bridge1"),
    ("Verse 3", None, "verse3"),
    ("Bridge 2", None, "bridge2"),
    ("Verse 4", None, "verse3"),
    ("Outro", "outro", None)
]

harmony = {
    'verse': [
        Chord('G', '', 1), Chord('G', '', 2), Chord('G', 'dim7', 2),
        Chord('D', '7', 1), Chord('D', '7', 1), Chord('D', '7', 2), Chord('C', '7', 2),
        Chord('B', 'm7', 2), Chord('E', '7', 2), Chord('A', '7', 2), Chord('D', '7', 2)
    ],
    'bridge': [
        Chord('B', '7', 2), Chord('E', '7', 2), Chord('B', '7', 2), Chord('E', '7', 2),
        Chord('B', '7', 2), Chord('E', '7', 2), Chord('B', '7', 2), Chord('A', '7', 2),
        Chord('D', '7', 2), Chord('G', '7', 2), Chord('D', '7', 2), Chord('G', '7', 2),
        Chord('B', 'm7', 2), Chord('E', '7', 2), Chord('A', '7', 1)
    ],
    "intro": [],
    "outro": []
}
