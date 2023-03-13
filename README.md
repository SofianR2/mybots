# 3D Parallel Hill Climbing Evolutionary Robot
Fitness Function: The fitness function simply has the robot move in the x direction.

Morphospace: This body creates shapes by extending in either the x, y, or z direction from any previous links, allowing for many possible shapes and sizes. While the fitness function mostly allows for slow shimmying, it sometimes bounces when the figure is generated with legs/arms. 

The bodies mutates based on the direction the last body was generated, as it affects how the next joints need to be lined up. For instance, if moving in the same direction, the next joint will be offset by the full length of the body in that direction, while when changing directions, the next joint will be offset by the dimensions of the new link in the old direction plus the dimensions of the new link in the new direction (ex. offset x by x/2 when coming from the x direction and y by y/2 when going to the y direction). This will be more clearly shown in the diagram here:

## Body Generation

As detailed below, links and joints are stored in lists. Send_Cube() which adds links to the simulation is run over each link in the list, and Send_Joint() which adds joints to the simulation is run over each joint in the list, ultimately making a robot. This is repeated for each generation, taking into account any mutations to the robot. 

![image](https://user-images.githubusercontent.com/103147652/224840520-6b693645-5cdf-4bc9-a0c1-1c8b9d2ad5e9.png)


## Body Mutation

The diagram below shows how mutation works.
The robot starts with two links and extends in the x, y, or z direction from any of the existing links. Each link keeps track of which direction it grew from so it can generate a new link from itself properly (with regards to dimensions/coordinates). Each link also keeps track of its occupied faces to prevent links growing from the same face twice or links growing back into their parent. The body has a capacity of 12 links, and when this capacity is reached, the robot stops growing and instead mutates by deleting the last added link and joint and generating a new link randomly somewhere else. 

![image](https://user-images.githubusercontent.com/103147652/224819166-bd374676-e55e-452c-8142-0d8a8848ae80.png)

## Sensor Assignment

![image](https://user-images.githubusercontent.com/103147652/224837539-681611e4-14e2-43c3-9a78-5ba3e92da195.png)

Sensors are generated/assigned by keeping track of which links need sensors, in a list of 0s and 1s, with 1s representing sensors. Additionally, the index of this list coorelates to the name of the sensor in question.

Evolution: This robot evolves by extending its initial link in the X direction continuously. This is done in the mutation function within solution.py, which increments a constant called dx stored in the constants file. This variable is then added on to the initial link in create_body() every time the list of links is generated in a for loop, which ultimately increases the length of the first link as more generations pass. 

## Steps to run the program: 
Open Command Prompt/Git Bash and move to a local directory where you want to add the git repo using the cd command. cd (insert directory name here)

Clone the repository using the following command: git clone https://github.com/SofianR2/mybots.git

Select the repository using the following command: cd https://github.com/SofianR2/mybots.git

Check your current branch using the following command: git branch

If the branch highlighted is not finalProject, input the following commands to change to this branch: git fetch origin Final

git checkout Final

Make sure to run the command git pull to ensure that the code is the latest available.

Now type the command python search.py to run the simulation.* *If this doesn’t work, try running python3 search.py instead

Graph showing improvement of fitness between 5 different seeds with 5 population and 100 generations: 
![image](https://user-images.githubusercontent.com/103147652/222050028-536e50b9-aa0d-4561-b08b-b44091729eed.png)

[Inspiration from Karl Sims and Ludobots]
