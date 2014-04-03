PacmanProject
=============

This is an Artificial Inteligence project. That uses the known project Pac-Man to test the implementation of the Search Algorithms --- algoritmos de b ́squeda informada y no informada-- 
The main goal of the Pac-Man project is to apply the AI tecnics to play Pac-Man, is not about the construction of the game.

The file **search.py** contains all the search algorithsms, we can divide them in to big groups informed search or uninformed search:

## BFS (Breadth-First Search)
///COOODEE
	input : a problem definition p
	output: a solution or failure
	fringe:FIFO queue

	foreach s ∈ p.initials() do
		if p.goal(s) then return solution(node(s, _, _, 0))
		fringe.push(n(s, _, _, 0))
	end
	expanded := ∅
	while true do
		if fringe.empty () then return failure
		n := fringe.pop()
		expanded.push(n)
		foreach a ∈ p.actions(n.state) do
			ns := successor (p, n, a)
			if ns ∈ fringe and ns ∈ expanded then
				if p.goal(ns .state) then return solution(ns )
				fringe.push(ns )
			end
		end
	end
///CODEEEEFIN

Fringe is a FIFO queue, so the search in the graph expands first the superficials nodes (the closer to the initial node). So the search described by this algorithm is a wide search for levels.


## UCS (Uniform-Cost Search)

///CODE
	input : a problem definition p
	output: a solution or failure
	fringe: Priority queue ordered by path-cost

	foreach s ∈ p.initials() do
		fringe.push(n(s, _, _, 0))
	end
	expanded := ∅
	while true do
		if fringe.empty () then return failure
		n := fringe.pop()
		if p.goal(n.state) then return solution(n)
		expanded.push(n)
		foreach a ∈ p.actions(n.state) do
			ns := successor (p, n, a)
			if ns ∈ fringe and ns ∈ expanded then
				fringe.push(ns )
			else if ns is in fringe with higher cost then
				replace that fringe node with ns
			end
		end
	end

///CODEFIN



## DFS (Depth-First Search)

///CODE
	input : a problem definition p
	output: a solution or failure
	fringe:LIFO queue

	foreach s ∈ p.initials() do
		if p.goal(s) then return solution(node(s, _, _, 0))
		fringe.push(n(s, _, _, 0))
	end
	expanded := ∅
	while true do
		if fringe.empty () then return failure
		n := fringe.pop()
		expanded.push(n)
			foreach a ∈ p.actions(n.state) do
			ns := successor (p, n, a)
			if ns ∈ fringe and ns ∈ expanded then
				if p.goal(ns .state) then return solution(ns )
				fringe.push(ns )
			end
		end
	end

///CODEFIN

## DLS (Depth-Limited Search)

///CODE
	input : a problem definition p, a limit k
	output: a solution, failure or cutoff
	fringe: LIFO queue
	
	foreach s ∈ p.initials() do
		if p.goal(s) then return solution(node(s, _, _, 0, 0))
		fringe.push(n(s, _, _, 0, 0))
	end
	expanded := ∅
	cut := false
	while true do
		if fringe.empty () then return cut? cutoff : failure
		n := fringe.pop()
		if n.depth = k then cut := true
		else
			expanded.push(n)
			foreach a ∈ p.actions(n.state) do
				ns := successor (p, n, a)
				if ns ∈ fringe and ns ∈ expanded then
					if p.goal(ns .state) then return solution(ns )
					fringe.push(ns )
				end
			end
		end
	end

///CODEFIN

## IDS (Iterative Deepening Search)

///CODE

	input : a problem definition p
	output: a solution or failure

	for depth = 0 to ∞ do
		result := DLS(p, depth)
		if result =cutoff then return result
	end

///CODEFIN

## DFS (Depth-First Search)

///CODE
///CODEFIN

