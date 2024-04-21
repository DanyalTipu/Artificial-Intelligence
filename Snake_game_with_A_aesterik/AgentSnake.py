import copy
from queue import PriorityQueue

class AgentSnake():
    def __init__(self):
        pass
    
    def heuristic(self, state):
        # Heuristic function: Manhattan distance between snake head and food
        return abs(state.FoodPosition.X - state.snake.HeadPosition.X) + abs(state.FoodPosition.Y - state.snake.HeadPosition.Y)

    def SearchSolution(self, state):
        visited = set()
        queue = PriorityQueue()
        queue.put((0, state, []))  # (priority, state, plan)
        
        while not queue.empty():
            _, current_state, current_plan = queue.get()
            
            if current_state.snake.HeadPosition.X == current_state.FoodPosition.X and current_state.snake.HeadPosition.Y == current_state.FoodPosition.Y:
                return current_plan
            
            if (current_state.snake.HeadPosition.X, current_state.snake.HeadPosition.Y) in visited:
                continue
            
            visited.add((current_state.snake.HeadPosition.X, current_state.snake.HeadPosition.Y))
            
            # Generate possible moves
            for move in [0, 3, 6, 9]:  # Up, Down, Right, Left
                new_state = copy.deepcopy(current_state)
                new_plan = current_plan + [move]
                new_state.snake.HeadDirection.Update(0, 0)  # Reset direction
                if move == 0:
                    new_state.snake.HeadDirection.Y = -1
                elif move == 6:
                    new_state.snake.HeadDirection.Y = 1
                elif move == 3:
                    new_state.snake.HeadDirection.X = 1
                elif move == 9:
                    new_state.snake.HeadDirection.X = -1
                
                new_state.snake.moveSnake(new_state)
                
                cost = len(new_plan) + self.heuristic(new_state)
                queue.put((cost, new_state, new_plan))
                
        return []  # If no solution is found
