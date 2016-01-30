#!/usr/bin/env python
from sys import exit

def throne_room():
	print "You hear heavy, machine controlled breathing."
	print "You can't see what it is, but you see a lightsaber on the mantle."
	print "What do you do?"
	
	print "1. Grab the lightsaber."
	print "2. Run back."
	print "3. Don't move."
	
	while True:
		choice = raw_input("> ")
		
		darth_moved = True
		if choice == "1":
			print "Oh no! Darth Vader has appeared and lit his lightsaber!"
			print "Prepare for battle!!!"
			
		elif choice == "2" and darth_moved:
			print "You got away, you nerfherder." 
			exit (0)
		elif choice == "3" and darth_moved:
			print "Bad choice."
			print "Darth Vader appeared and stabbed you from behind."
			print "Game over."
			exit (0)
		else:
			print "Pick an actual choice, Rebel!"
			
def trash_compactor():
	print "You walked into the trash compactor!" 
	print "The walls are closing in!!!"
	print "Do you flee, or be crushed?!"
	
	print "1. Flee."
	print "2. Stay."
	
	choice = raw_input ("> ")
	
	if "1" in choice:
		start()
	elif "2" in choice:
		dead("You've been squished.")
	else:
		print "Choose!"
		
def dead(why):
	print why, "Good job!"
	exit(0)
	
def start():
	print "You are in a dark hallway."
	print "There is a door to left and right."
	print "Which one do you take?"
	
	print "1. Left."
	print "2. Right."
		
	choice = raw_input("> ")
	
	if choice == "1":
		throne_room()
	elif choice == "2":
		trash_compactor()
	else:
		print "Pick a choice!"
		
start()