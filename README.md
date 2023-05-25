# FishTycoonSpeciesTracker
A rudimentary GUI system to quickly and easily record new fish species and information about them in the classic "Fish Tycoon" game.


In Fish Tycoon, the goal of the game is to discover the 7 magical fish of Isola and thus save the island's ecosystem. One of the
most straight forward ways to do this is by breeding your existing fish to create hybrids, then breeding those hybrids with
other fish, and so on and so on. The game features over 400 different kinds of fish. In order to find the 7 magic fish, it is
useful to have a breeding log that records what fish are produced when breeding any given pair of fish together, however
manually keeping track of these breeding combinations can quickly become tedious, especially since there are at least some fish
which can be generated from more than one set of parents. This program aims to make a simple and quick to use graphical
interface which allows users to keep track of fish breeding combinations, as well as other information about each fish, such as
their price when sold, the required environmental research level needed to keep them alive indefinitely, and whether they are
a magic fish or not.

Core feature targets include:
1) Ability to save the program and resume it without losing information by storing fish object in a json file (DONE!)
3) Ability to add new fish species by selecting their parents from a list of existing fish in your database (DONE!)
4) Ability to view all information about any species in your database (DONE!)
5) Ability to add new fish species whos parents are not in the database by manually typing in the names of the parents (DONE!)
6) Ability to edit information about a fish already in the database (not started)
7) Ability to add additional parent combinations to fish already in the database if said fish can be created from more than one pair of parents (not started)
