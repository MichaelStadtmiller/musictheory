import musicalbeeps


# Happy Birthday
def simple_happy_birthday(player):
	player.play_note("G", 0.15)
	player.play_note("G", 0.15)
	player.play_note("A", 0.3)
	player.play_note("G", 0.3)
	player.play_note("C5", 0.3)
	player.play_note("B", 0.3)


# https://musescore.com/static/musescore/scoredata/g/fb883a87216d44cc1c50b0737761621656548b6d/score_0.png?no-cache=1610714686
happy_birthday = {
	'sig': '4/4',
	'bpm': 131,
	'notes': [
		('G', '8'),
		('G', '8'),
		('A', '4'),
		('G', '4'),
		('C5', '4'),
		('B', '4'),
	]
}

mary_had_a_little_lamb = {
	'sig': '2/4',
	'bpm': 120,
	'notes': [
		('E', '4'),
		('D', '4'),
		('C', '4'),
		('D', '4'),
		('E', '4'),
		('E', '4'),
		('E', '2'),
	]
}

basic_notes = {
	'1': 1.0,  # whole note
	'2': 0.5,  # half note
	'4': 0.25,  # quarter note
	'8': 0.125,  # eight note
	'16': 0.0625,  # sixteenth note
}


def play_song(player, song):
	# player: the musicalbeeps player object
	# song: the mapping of the song
	beats_meas, beat_note = map(int, (song['sig'].split('/')))  # which note gets the beat

	# get the beats in the right key signature (4: quarter note = 1s, 8: eight note = 1s)
	sig_notes = get_signature_notes(beat_note)
	bps = int(song['bpm']) / 60  # beats per second
	for note in song['notes']:
		player.play_note(note[0], sig_notes[note[1]] / bps)


def get_signature_notes(beat_note):
	sig_notes = {}
	for n in basic_notes:
		sig_notes[n] = basic_notes[n] * beat_note
	return sig_notes


if __name__ == "__main__":
	player = musicalbeeps.Player(volume=0.2, mute_output=False)

	# simple_happy_birthday(player)
	# get_signature_notes(4)
	# play_song(player, mary_had_a_little_lamb)
	play_song(player, happy_birthday)
