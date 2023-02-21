Fitness Function: The fitness function simply has the robot move in the x direction. 

Morphospace: This body creates shapes by extending in either the x, y, or z direction, allowing for many possible shapes and sizes. While the fitness function mostly allows for slow shimmying, it sometimes bounces when the figure seems to have pointed "legs". 

With regards to brains, the links start at one end and are connected to the next like a chain, and the sensors attatched to a link affect that link. 

The bodies are generated based on the direction the last body was generated, as it affects how the next joints need to be lined up. For instance, if moving in the same direction, the next joint will be offset by the full length of the body in that direction, while when changing directions, the next joint will be offset by the dimensions of the new link in the old direction plus the dimensions of the new link in the new direction (ex. offset x by x/2 when coming from the x direction and y by y/2 when going to the y direction). This will be more clearly shown in the diagram. 

Sensors are generated/assigned by keeping track of which links need sensors, in an list of 0s and 1s, with 1s representing sensors. Additionally, the index of this list coorelates to the name of the sensor in question.

Steps to run the program: 
Open Command Prompt/Git Bash and move to a local directory where you want to add the git repo using the cd command. 
cd (insert directory name here)


Clone the repository using the following command:
git clone https://github.com/SofianR2/mybots.git


Select the repository using the following command:
cd https://github.com/SofianR2/mybots.git


Check your current branch using the following command:
git branch


If the branch highlighted is not finalProject, input the following commands to change to this branch:
git fetch origin random3d


git checkout random3d


Make sure to run the command git pull to ensure that the code is the latest available.


Now type the command python search.py to run the simulation.*
*If this doesn’t work, try running python3 search.py instead
