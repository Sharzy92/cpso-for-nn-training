from particleSwarmOptimization.particle import Particle


class PSO():


    def __init__(self,costFunc,x0,bounds,num_particles,maxiter):
        self.__num_dimensions=len(x0)
        self.__err_best_g=-1                   # best error for group
        self.__pos_best_g=[]                   # best position for group
        self.__maxiter = maxiter
        self.__num_particles = num_particles
        self.__bounds = bounds
        self.__costFunc = costFunc


        # establish the __swarm
        self.__swarm=[]
        for i in range(0,self.__num_particles):
            self.__swarm.append(Particle(x0, self.__num_dimensions))


    def setGlobalBest(self):
        # print i,err_best_g
        # cycle through particles in __swarm and evaluate fitness
        for j in range(0, self.__num_particles):
            self.__swarm[j].evaluate(self.__costFunc)

            # determine if current particle is the best (globally)
            if self.__swarm[j].err_i < self.__err_best_g or self.__err_best_g == -1:
                self.__pos_best_g = list(self.__swarm[j].position_i)
                self.__err_best_g = float(self.__swarm[j].err_i)


    def begin(self):
        # begin optimization loop
        i=0
        while i < self.__maxiter:
            self.setGlobalBest()

            # cycle through __swarm and update velocities and position
            for j in range(0,self.__num_particles):
                self.__swarm[j].update_velocity(self.__pos_best_g)
                self.__swarm[j].update_position(self.__bounds)
            i+=1
        self.printGlobalBest()


    def printGlobalBest(self):
        # print final results
        print('FINAL:')
        print(self.__pos_best_g)
        print(self.__err_best_g)