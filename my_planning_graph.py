
from itertools import chain, combinations
from aimacode.planning import Action
from aimacode.utils import expr

from layers import BaseActionLayer, BaseLiteralLayer, makeNoOp, make_node


class ActionLayer(BaseActionLayer):

    def _inconsistent_effects(self, actionA, actionB):
        """ Return True if an effect of one action negates an effect of the other

        Hints:
            (1) `~Literal` can be used to logically negate a literal
            (2) `self.children` contains a map from actions to effects

        See Also
        --------
        layers.ActionNode
        """
        # TODO: implement this function
        for effectA in actionA.effects:
            for effectB in actionB.effects:
                if (effectA == ~effectB):
                    return True

        return False

    def _interference(self, actionA, actionB):
        """ Return True if the effects of either action negate the preconditions of the other 

        Hints:
            (1) `~Literal` can be used to logically negate a literal
            (2) `self.parents` contains a map from actions to preconditions
        
        See Also
        --------
        layers.ActionNode
        """
        # TODO: implement this function
        for effectA in actionA.effects:
            for preconditionB in actionB.preconditions:
                if (effectA == ~preconditionB):
                    return True

        for effectB in actionB.effects:
            for preconditionA in actionA.preconditions:
                if (effectB == ~preconditionA): 
                    return True
            
        return False        

    def _competing_needs(self, actionA, actionB):
        """ Return True if any preconditions of the two actions are pairwise mutex in the parent layer

        Hints:
            (1) `self.parent_layer` contains a reference to the previous literal layer
            (2) `self.parents` contains a map from actions to preconditions
        
        See Also
        --------
        layers.ActionNode
        layers.BaseLayer.parent_layer
        """
        # TODO: implement this function
        for preconditionA in actionA.preconditions:
            for preconditionB in actionB.preconditions:
                if(self.parent_layer.is_mutex(preconditionA,preconditionB)):
                   return True
                   
        return False

class LiteralLayer(BaseLiteralLayer):

    def _inconsistent_support(self, literalA, literalB):
        """ Return True if all ways to achieve both literals are pairwise mutex in the parent layer

        Hints:
            (1) `self.parent_layer` contains a reference to the previous action layer
            (2) `self.parents` contains a map from literals to actions in the parent layer

        See Also
        --------
        layers.BaseLayer.parent_layer
        """
        # TODO: implement this function
        for actionA in self.parents[literalA]:
            for actionB in self.parents[literalB]:
                if(self.parent_layer.is_mutex(actionA,actionB)):
                    continue
                else:
                    return False 
                   
        return True 

    def _negation(self, literalA, literalB):
        """ Return True if two literals are negations of each other """
        # TODO: implment this function
        if (literalA == ~literalB):
            return True
        
        return False


class PlanningGraph:
    def __init__(self, problem, state, serialize=True, ignore_mutexes=False):
        """
        Parameters
        ----------
        problem : PlanningProblem
            An instance of the PlanningProblem class

        state : tuple(bool)
            An ordered sequence of True/False values indicating the literal value
            of the corresponding fluent in problem.state_map

        serialize : bool
            Flag indicating whether to serialize non-persistence actions. Actions
            should NOT be serialized for regression search (e.g., GraphPlan), and
            _should_ be serialized if the planning graph is being used to estimate
            a heuristic
        """
        self._serialize = serialize
        self._is_leveled = False
        self._ignore_mutexes = ignore_mutexes
        self.goal = set(problem.goal)

        # make no-op actions that persist every literal to the next layer
        no_ops = [make_node(n, no_op=True) for n in chain(*(makeNoOp(s) for s in problem.state_map))]
        self._actionNodes = no_ops + [make_node(a) for a in problem.actions_list]
        
        # initialize the planning graph by finding the literals that are in the
        # first layer and finding the actions they they should be connected to
        literals = [s if f else ~s for f, s in zip(state, problem.state_map)]
        layer = LiteralLayer(literals, ActionLayer(), self._ignore_mutexes)
        layer.update_mutexes()
        self.literal_layers = [layer]
        self.action_layers = []

    def level_cost(self, graph, goal):
        """
        # from pseudocode/heuzristics.md
        The level cost is a helper function used by MaxLevel and LevelSum. The level cost of a goal is equal to the level number of the first literal layer in the planning graph where the goal literal appears.

        function LevelCost(graph, goal) 
        returns a value  
        
        inputs:
        graph, a leveled planning graph  
        goal, a literal that is a goal in the planning graph  
  
        for each layer i in graph.literalLayers do
            if goal in layer i then return i 

        """
        
        for i, layer in enumerate(graph.literal_layers):
            if goal in layer:
                return i

        
    def h_levelsum(self):
        """ Calculate the level sum heuristic for the planning graph

        The level sum is the sum of the level costs of all the goal literals
        combined. The "level cost" to achieve any single goal literal is the
        level at which the literal first appears in the planning graph. Note
        that the level cost is **NOT** the minimum number of actions to
        achieve a single goal literal.
        
        For example, if Goal_1 first appears in level 0 of the graph (i.e.,
        it is satisfied at the root of the planning graph) and Goal_2 first
        appears in level 3, then the levelsum is 0 + 3 = 3.

        Hints
        -----
          (1) See the pseudocode folder for help on a simple implementation
          (2) You can implement this function more efficiently than the
              sample pseudocode if you expand the graph one level at a time
              and accumulate the level cost of each goal rather than filling
              the whole graph at the start.

        See Also
        --------
        Russell-Norvig 10.3.1 (3rd Edition)

        # from pseudocode/heuzristics.md
        
        The level sum heuristic, following the subgoal independence assumption, 
        returns the sum of the level costs of the goals; this can be inadmissible 
        but works well in practice for problems that are largely decomposable.

        —AIMA Chapter 10

        ---
        function LevelSum(_graph_) returns a value  
        inputs:
        graph, an initialized (unleveled) planning graph  
  
        costs = []  
        graph.fill()  /* fill the planning graph until it levels off */
        for each  goal in graph.goalLiterals do
            costs.append(LevelCost(graph, goal))  
    
        return sum(costs)          
        """
        # TODO: implement this function
        costs = []
        self.fill()
        for goal in self.goal:
            costs.append(self.level_cost(self, goal))
        
        return sum(costs)

    def h_maxlevel(self):
        """ Calculate the max level heuristic for the planning graph

        The max level is the largest level cost of any single goal fluent.
        The "level cost" to achieve any single goal literal is the level at
        which the literal first appears in the planning graph. Note that
        the level cost is **NOT** the minimum number of actions to achieve
        a single goal literal.

        For example, if Goal1 first appears in level 1 of the graph and
        Goal2 first appears in level 3, then the levelsum is max(1, 3) = 3.

        Hints
        -----
          (1) See the pseudocode folder for help on a simple implementation
          (2) You can implement this function more efficiently if you expand
              the graph one level at a time until the last goal is met rather
              than filling the whole graph at the start.

        See Also
        --------
        Russell-Norvig 10.3.1 (3rd Edition)

        Notes
        -----
        WARNING: you should expect long runtimes using this heuristic with A*
        
        # from pseudocode/heuzristics.md
        The max-level heuristic simply takes the maximum level cost of any of the goals; this is admissible, but not necessarily accurate.

        —AIMA Chapter 10
        ---
        function MaxLevel(_graph_) returns a value  
        inputs:
        graph, an initialized (unleveled) planning graph  
  
        costs = []  
        graph.fill()  /* fill the planning graph until it levels off */
        
        for each goal in graph.goalLiterals do
            costs.append(LevelCost(graph, goal))  
        
        return max(costs)  
        
        """
        # TODO: implement maxlevel heuristic
        costs = []
        self.fill()
        for goal in self.goal:
            costs.append(self.level_cost(self, goal))
        
        return max(costs)

    def h_setlevel(self):
        """ Calculate the set level heuristic for the planning graph

        The set level of a planning graph is the first level where all goals
        appear such that no pair of goal literals are mutex in the last
        layer of the planning graph.

        Hints
        -----
          (1) See the pseudocode folder for help on a simple implementation
          (2) You can implement this function more efficiently if you expand
              the graph one level at a time until you find the set level rather
              than filling the whole graph at the start.

        See Also
        --------
        Russell-Norvig 10.3.1 (3rd Edition)

        Notes
        -----
        WARNING: you should expect long runtimes using this heuristic on complex problems
        
        # from pseudocode/heuzristics.md
        The set-level heuristic finds the level at which all the literals in the conjunctive goal appear in the planning graph without any pair of them being mutually exclusive.

        —AIMA Chapter 10

        ---
        function SetLevel(graph) returns a value  
        inputs:
        graph, an initialized (unleveled) planning graph  
  
        graph.fill()  /* fill the planning graph until it levels off */
        
        for layer i in graph.literalLayers do
            allGoalsMet <- true          
            for each goal in graph.goalLiterals do 
                if goal not in layer i then allGoalsMet <- false 
            if not allGoalsMet then continue  
          
            goalsAreMutex <- false  
            for each goalA in _graph.goalLiterals_ do 
                for each goalB in _graph.goalLiterals_ do 
                    if layer i.isMutex(goalA, goalB) then goalsAreMutex <- true  
            if not goalsAreMutex then return i
        
        """
        # TODO: implement setlevel heuristic
        self.fill()
        for i, layer in enumerate(self.literal_layers):
            
            all_goals_met = True
            for goal in self.goal:
                if goal not in layer:
                    all_goals_met = False
            if not all_goals_met: 
                continue
                
            goals_are_mutex = False
            for goalA in self.goal:
                for goalB in self.goal:
                    if layer.is_mutex(goalA,goalB): 
                        goals_are_mutex = True
            if not goals_are_mutex:
                return i
            
        return False

    ##############################################################################
    #                     DO NOT MODIFY CODE BELOW THIS LINE                     #
    ##############################################################################

    def fill(self, maxlevels=-1):
        """ Extend the planning graph until it is leveled, or until a specified number of
        levels have been added

        Parameters
        ----------
        maxlevels : int
            The maximum number of levels to extend before breaking the loop. (Starting with
            a negative value will never interrupt the loop.)

        Notes
        -----
        YOU SHOULD NOT THIS FUNCTION TO COMPLETE THE PROJECT, BUT IT MAY BE USEFUL FOR TESTING
        """
        while not self._is_leveled:
            if maxlevels == 0: break
            self._extend()
            maxlevels -= 1
        return self

    def _extend(self):
        """ Extend the planning graph by adding both a new action layer and a new literal layer

        The new action layer contains all actions that could be taken given the positive AND
        negative literals in the leaf nodes of the parent literal level.

        The new literal layer contains all literals that could result from taking each possible
        action in the NEW action layer. 
        """
        if self._is_leveled: return

        parent_literals = self.literal_layers[-1]
        parent_actions = parent_literals.parent_layer
        action_layer = ActionLayer(parent_actions, parent_literals, self._serialize, self._ignore_mutexes)
        literal_layer = LiteralLayer(parent_literals, action_layer, self._ignore_mutexes)

        for action in self._actionNodes:
            # actions in the parent layer are skipped because are added monotonically to planning graphs,
            # which is performed automatically in the ActionLayer and LiteralLayer constructors
            if action not in parent_actions and action.preconditions <= parent_literals:
                action_layer.add(action)
                literal_layer |= action.effects

                # add two-way edges in the graph connecting the parent layer with the new action
                parent_literals.add_outbound_edges(action, action.preconditions)
                action_layer.add_inbound_edges(action, action.preconditions)

                # # add two-way edges in the graph connecting the new literaly layer with the new action
                action_layer.add_outbound_edges(action, action.effects)
                literal_layer.add_inbound_edges(action, action.effects)

        action_layer.update_mutexes()
        literal_layer.update_mutexes()
        self.action_layers.append(action_layer)
        self.literal_layers.append(literal_layer)
        self._is_leveled = literal_layer == action_layer.parent_layer
