# Chapter 9: Dijkstra — Lab Report

## Student Information
- **Name:** Karla Cuevas
- **Date:** 05/10/2026
- **Course:** COSC 2436

## Algorithm Summary
Algorithm Analysis: Dijkstra's Algorithm

What type of graph does this program build? [Your answer — directed/undirected, weighted/unweighted]
Why must all edge weights be non-negative for Dijkstra's to work? [Your explanation]
Time Complexity (with simple array scan for min-node): O(?)
Time Complexity (with a min-heap/priority queue): O(?)
Core Data Structures

Structure	Variable Name	What It Stores
Adjacency dict	graph	
Cost table	costs	
Parent table	parents	
Visited list	processed	
Algorithm Trace

Given nodes A, B, C, D and edges A-B(1), A-C(4), B-C(2), B-D(6), C-D(3), trace Dijkstra's from A to D:

Iteration	Current Node	costs[A]	costs[B]	costs[C]	costs[D]	processed
Init	—					
1						
2						
3						
4						
Shortest path A to D: [Your answer]
Total cost: [Your answer]

Reflection Questions

Why does the algorithm initialize all node costs to infinity except the start node?

Why do we store edges in both directions (graph[a][b] and graph[b][a])? What would break if we only stored one direction?

The find_lowest_cost_node() function scans all nodes linearly. How would using a priority queue (min-heap) improve performance, and why does it matter for large graphs?

If a negative edge weight were introduced (e.g., A-B with weight -3), explain how Dijkstra's algorithm could produce an incorrect result. What algorithm handles negative weights?

How does the parents dictionary allow path reconstruction? Why do we reverse the path at the end?

What happens when the source and destination are in disconnected components of the graph? How does the code detect this?

