# 3D Parallel Hill Climbing Evolutionary Robot

![](https://github.com/SofianR2/mybots/blob/Final/CSAL%20Teaser%20GIF%20Final.gif)

## Overview Video

https://user-images.githubusercontent.com/103147652/225114677-c35de801-6305-4df2-9d9d-7f451ef6ab8d.mp4


## Fitness and Morphospace
*Note: I spoke with Sam regarding confusion on Assignment 8 which caused a misimplementation and was told this new implementation was acceptable for this project.* 

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

## Results

Here are some examples of unevolved and evolved robots:
### Unevolved - 0 generations, 1 population
![image](https://user-images.githubusercontent.com/103147652/224865811-11c03045-3a5c-4b18-a74b-7ca1c24b4e03.png)
![image](https://user-images.githubusercontent.com/103147652/225115426-999d9254-b5c2-4774-8587-be86d74a373a.png)
![image](https://user-images.githubusercontent.com/103147652/225115500-b1881809-65af-4d88-981c-6a69645b1056.png)
![image](https://user-images.githubusercontent.com/103147652/225115532-ea7f7b10-6da4-4220-a8ef-b6215f0e2833.png)
![image](https://user-images.githubusercontent.com/103147652/225115549-9ad07c79-fee9-420b-b720-dff58b97d6f6.png)
![image](https://user-images.githubusercontent.com/103147652/225115964-3c8279d6-2f51-4285-b8d2-7100afe51a07.png)

### Evolved - 500 generations, 10 population
![image](https://user-images.githubusercontent.com/103147652/225115625-1951c30c-97a7-45ec-b067-0a9744f31d85.png)
![image](https://user-images.githubusercontent.com/103147652/225115650-42fbff1e-d27e-45ea-8d41-11772e4050ff.png)
![image](https://user-images.githubusercontent.com/103147652/225115678-9ad13860-f005-4d31-ab1f-82ded2906fbf.png)
![image](https://user-images.githubusercontent.com/103147652/225115713-e48b4667-8d6e-473a-850e-cf9bfeed3b58.png)
![image](https://user-images.githubusercontent.com/103147652/225115753-9eb55d03-102e-4c02-bf77-4a440ab08265.png)
![image](https://user-images.githubusercontent.com/103147652/225115767-036ae3f3-87b8-4b8d-9baf-d5666c43f14a.png)

### Visualization of Results
### 10 seeds x 500 generations x 10 population = 50,000 simulations
![Figure_1](https://user-images.githubusercontent.com/103147652/224849475-b6fa0add-d7cc-466d-b8d6-61e913f30c9a.png)

After evolving for 500 generations, we can see that evolution occurs much more rapidly in earlier generations, and eventually plateaus in later generations. It can also be seen that evolution typically stopped or plateaued if there was an extreme improvement in fitness, which makes sense as we essentially "skip" the earlier levels of fitness by having one big jump. 

If we do not set a limit to the number of links we generate, we may be able to see even better fitness values, although the program may become computationally taxing, depending on the number of generations. 

Ultimately, most of the robots saw a significant improvement in their movement, going from moving extremely slowly or not at all to moving significantly faster. Even within the evolved robots, some robots were faster than others, which is evident by the fitness diagram above. It would be interesting to see how much better these robots can get if we increase the generations and populations and set no limits to growth. 

## Code/Files to Look At:

viewfinal.py - Runs simulations of the best robots saved from each seed from the 500 generations of 10 population for 10 seeds.

search.py - Runs the parallel hill climber using multiple seeds (randomization that can be replicated) and graphs the fitness results of the robot.

parallelHillClimber.py - Generates the list of parents and children to mutate/evolve, actually evolves them, and shows the best result.

solution.py - The actual "robots" and where they are generated. - AddNewLinkAndJoint() adds new links and joints to add to the link and joint lists, and BuildBody() goes through these lists and actually creates the links and joints. The Mutate() function is where mutations occur such as extending the robot's body or removing a link from the body.

## Steps to run the program: 
Open Command Prompt/Git Bash and move to a local directory where you want to add the git repo using the cd command. cd (insert directory name here)

Clone the repository using the following command: git clone https://github.com/SofianR2/mybots.git

Select the repository using the following command: cd https://github.com/SofianR2/mybots.git

Check your current branch using the following command: git branch

If the branch highlighted is not Final, input the following commands to change to this branch: git fetch origin Final

git checkout Final

Make sure to run the command git pull to ensure that the code is the latest available.

Take all of the best*.txt files from the "Final" branch in the git repo and copy them into your working directory. 

Now type the command python viewfinal.py to run the simulation.*

**If this doesn’t work, try running python3 viewfinal.py instead.*

If you would like to run the simulation of 500 generations of 10 population for 10 seeds, run search.py instead of viewfinal.py.

***WARNING: FULLY RUNNING search.py TAKES A FEW HOURS AND DEPENDS ON THE SPECS OF THE MACHINE IT'S BEING RUN ON***

## Credits:
Explosion Effect - https://www.youtube.com/watch?v=Q7KmAe8_jZE

Video Music - https://www.youtube.com/watch?v=6eWIffP2M3Y

Inspiration from Karl Sims and Ludobots
