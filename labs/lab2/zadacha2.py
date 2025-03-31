from searching_framework import Problem, astar_search
class Lavirint(Problem):
    def __init__(self, initial,walls,size, goal=None):
        super().__init__(initial, goal)
        self.walls = walls
        self.size = size
    def result(self, state, action):
        return self.successor(state)[action]
    def actions(self, state):
        return self.successor(state).keys()
    def goal_test(self, state):
        return self.goal == state
    def successor(self, state): 
        succ = dict()
        directions = ["Gore","Desno 2","Desno 3","Dolu","Levo"]
        delta = [(0,1),(2,0),(3,0),(0,-1),(-1,0)]
        for dir, change in zip(directions,delta):
            new_state = (state[0]+change[0],state[1]+change[1])
            if(not self.into_wall(state,new_state) and not self.out_of_board(new_state)):
                succ[dir] = new_state
        return succ
    def out_of_board(self,state):
        if(0<= state[0]<self.size and 0<=state[1]<self.size):
            return False
        

        return True
    def into_wall(self,old_state,new_state):
        for wall in self.walls:
               
            if(new_state == wall):
                return True
            if(new_state[1] == wall[1] and old_state[0]<=wall[0]<=new_state[0]):
                return True
            
        return False    
            
        


    def h(self,node):
        return (abs(node.state[0] - self.goal[0]) + abs(node.state[1] - self.goal[1]))/3

if __name__ == '__main__':
    # your code here
    size = int(input())
    num_of_walls = int(input())
    wall_coordinates = list()
    for i in range(num_of_walls):
        wall_coordinates.append(tuple(map(int,input().split(','))))
    wall_coordinates = tuple(wall_coordinates)
    man_coordinates = tuple(map(int,input().split(',')))
    house_coordinates = tuple(map(int,input().split(',')))
    initial_state = man_coordinates
    
    house_problem = Lavirint(initial_state,wall_coordinates,size,house_coordinates)
    hp_res = astar_search(house_problem,house_problem.h) 
    if hp_res is not None:
        print(hp_res.solution())
