# 3D Parallel Hill Climbing Evolutionary Robot

![](https://github.com/SofianR2/mybots/blob/Final/CSAL%20Teaser%20GIF%20Final.gif)



Put Video Here

## Fitness and Morphospace

Fitness Function: The fitness function simply has the robot move in the x direction.

Morphospace: This body creates shapes by extending in either the x, y, or z direction from any previous links, allowing for many possible shapes and sizes. While the fitness function mostly allows for shimmying/hopping forward, it sometimes bounces when the figure is generated with legs/arms. 

The bodies mutates based on the direction the last body was generated, as it affects how the next joints need to be lined up. For instance, if moving in the same direction, the next joint will be offset by the full length of the body in that direction, while when changing directions, the next joint will be offset by the dimensions of the new link in the old direction plus the dimensions of the new link in the new direction (ex. offset x by x/2 when coming from the x direction and y by y/2 when going to the y direction). The specifics of body generation and mutation are described below. 

## Body Generation

As detailed below, links and joints are stored in lists. Send_Cube() which adds links to the simulation is run over each link in the list, and Send_Joint() which adds joints to the simulation is run over each joint in the list, ultimately making a robot. This is repeated for each generation, taking into account any mutations to the robot. 

![image](https://user-images.githubusercontent.com/103147652/224840520-6b693645-5cdf-4bc9-a0c1-1c8b9d2ad5e9.png)


## Body Mutation

The diagram below shows how mutation works.
The robot starts with two links and extends in the x, y, or z direction from any of the existing links. Each link keeps track of which direction it grew from so it can generate a new link from itself properly (with regards to dimensions/coordinates). Each link also keeps track of its occupied faces to prevent links growing from the same face twice or links growing back into their parent. The body has a capacity of 12 links, and when this capacity is reached, the robot stops growing and instead mutates by deleting the last added link. A new random link is then able to grow randomly from any of the existing links. 

![image](https://user-images.githubusercontent.com/103147652/224819166-bd374676-e55e-452c-8142-0d8a8848ae80.png)

## Sensor Assignment
Sensors are generated/assigned by keeping track of which links need sensors, in a list of 0s and 1s, with 1s representing sensors. Additionally, the index of this list coorelates to the name of the sensor in question. Motors are assigned to every link by iterating over the list of links. 

![image](https://user-images.githubusercontent.com/103147652/224837539-681611e4-14e2-43c3-9a78-5ba3e92da195.png)

## Selection - Parallel Hill Climber

Evolution takes place through parallel hill climbing, which involves looking at a population of samples which are all subject to certain mutations. In this robot, the mutations are changing the robot's fitness values (how well it moves in the x direction), creating new links, and eventually removing the newest link. 

If a child has a better fitness value than its parent, it replaces the parent and becomes the next in line to mutate and evolve. This process of mutating and evolving an entire population (below) spans for several generations, which essentially means we repeat this process to further increase fitness via more mutations. 

![image](https://user-images.githubusercontent.com/103147652/224863060-e5fa7d2b-408e-4656-9135-a99448b192bc.png)

## Results and Conclusions

Here are some examples of robots before and after they were evolved:

![image](https://user-images.githubusercontent.com/103147652/224865811-11c03045-3a5c-4b18-a74b-7ca1c24b4e03.png)
![image](https://user-images.githubusercontent.com/103147652/224865701-93930962-d06f-4316-91e0-fced3391b0d5.png)


## Visualization of Results
### 10 seeds x 500 generations x 10 population = 50,000 simulations
![Figure_1](https://user-images.githubusercontent.com/103147652/224849475-b6fa0add-d7cc-466d-b8d6-61e913f30c9a.png)

After evolving for 500 generations, we can see that evolution occurs much more rapidly in earlier generations, and eventually plateaus in later generations. It can also be seen that evolution typically stopped or plateaued if there was an extreme improvement in fitness, which makes sense as we essentially "skip" the earlier levels of fitness by having one big jump. 

If we do not set a limit to the number of links we generate, we may be able to see better fitness values, although the program may become computationally taxing, depending on the number of generations.

## Code/Files to Look At:

Search.py - runs the parallel hill climber using multiple seeds (randomization that can be replicated) and graphs the fitness results of the robot

parallelHillClimber.py - generates the list of parents and children to mutate/evolve, actually evolves them, and shows the best result

solution.py - the actual "robots" and where they are generated - AddNewLinkAndJoint() adds new links and joints to add to the link and joint lists, and BuildBody() goes through these lists and actually creates the links and joints. The Mutate() function is where mutations occur such as extending the robot's body or removing a link from the body. 



## Steps to run the program: 
Open Command Prompt/Git Bash and move to a local directory where you want to add the git repo using the cd command. cd (insert directory name here)

Clone the repository using the following command: git clone https://github.com/SofianR2/mybots.git

Select the repository using the following command: cd https://github.com/SofianR2/mybots.git

Check your current branch using the following command: git branch

If the branch highlighted is not finalProject, input the following commands to change to this branch: git fetch origin Final

git checkout Final

Make sure to run the command git pull to ensure that the code is the latest available.

Now type the command python search.py to run the simulation.* 

*If this doesn’t work, try running python3 search.py instead

### Credits:
Explosion Effect - https://www.youtube.com/watch?v=Q7KmAe8_jZE
Video Music - https://www.youtube.com/watch?v=6eWIffP2M3Y

[Inspiration from Karl Sims and Ludobots]
