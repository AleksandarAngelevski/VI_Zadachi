from searching_framework import *
class House(Problem):
    
    #direction: True - right || False - left
    def __init__(self, initial,allowed, goal=None,):
        self.allowed = allowed
        super().__init__(initial, goal)
    def is_allowed(self,player_state):
        if(player_state not in self.allowed):
            return False    
        return True
    
    def goal_test(self, state):#state ((player_x, player_y), (house_x,house_y,direction))
        return state[0] == (state[1][0],state[1][1])
    def check_valid_player(self,player_state):#state ((player_x, player_y), (house_x,house_y,direction))
        return True  if 0<=player_state[0]<5 and 0<=player_state[1]<9 else False
    def check_valid_house(self,house_state):
        return True  if 0<=house_state[0]<=4 and house_state[1]==8 else False
    def actions(self, state):
        return self.successor(state).keys()
    def result(self, state, action):
        
        return self.successor(state)[action]
    def move_house(self,house_state):#state ((player_x, player_y), (house_x,house_y,direction))
        if(house_state[2]==True):
            new_state = (house_state[0]+1,house_state[1],house_state[2])
            if(self.check_valid_house(new_state)):
                return new_state
            else:
                new_state = (house_state[0]-1,house_state[1],False)
        else:
            new_state = (house_state[0]-1,house_state[1],house_state[2])
            if(self.check_valid_house(new_state)):
                return new_state
            else:
                new_state = (house_state[0]+1,house_state[1],True)

        return new_state

    def h(self,node):
        return (node.state[1][1] - node.state[0][1])/2
        # state = node.state
        # player = state[0]
        # y = player[1]
        
        # return (8 - y)/2
    def successor(self, state):
        #state ((player_x, player_y), (house_x,house_y,direction))
        succ={}
        house_state = state[1]
        player_state = state[0]
        moves = ['Stoj', 'Gore 1', 'Gore 2', 'Gore-desno 1', 'Gore-desno 2', 'Gore-levo 1', 'Gore-levo 2']
        state_delta = [(0,0),(0,1),(0,2),(1,1),(2,2),(-1,1),(-2,2)]
        new_house_state = self.move_house(house_state)
        for move, change in zip(moves,state_delta):
            new_player_state = (player_state[0]+change[0],player_state[1]+change[1])
            new_state =(new_player_state,new_house_state)
            
            if(self.is_allowed(new_player_state) or new_player_state == (new_house_state[0],new_house_state[1])):
                succ[move] = new_state

        return succ



if __name__ == '__main__':


    #state ((player_x, player_y), (house_x,house_y,direction))
    #direction: True - right || False - left
    allowed = [(1,0), (2,0), (3,0), (1,1), (2,1), (0,2), (2,2), (4,2), (1,3), (3,3), (4,3), (0,4), (2,4), (2,5), (3,5), (0,6), (2,6), (1,7), (3,7)]
    
    chovek = input()
    chovek = list(map(int,chovek.split(',')))
    kukjichka = input()
    kukjichka = list(map(int,kukjichka.split(',')))
    nasoka = True if input()=="desno" else False
    kukjichka.append(nasoka)
    kukjichka_state = tuple(kukjichka)
    sostojba = (tuple(chovek),kukjichka_state)
    problem = House(sostojba,allowed)
    p =astar_search(problem,problem.h)
    if(p is not None):
        print(p.solution())
    else:
        print("No solution")
