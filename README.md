<p align="left">
	<img src="https://github.com/buenos-dan/cheetah_sim/blob/master/assets/pictures/cheetah.jpg" alt="Cheetah_model"  width="600" height="370"/>
</p>

# cheetah_sim
quadrupedal robot simulation by ROS and Gazebo  

## Architecture of this project.    
#### ./ros_package 

|**folder**                        |**Description**                     |   
|----------------------------------|------------------------------------|   
|[cheetah_description](https://github.com/buenos-dan/cheetah_sim/tree/master/ros_package/cheetah_description)              |contains STL files and URDF file    |   
|[cheetah_gazebo](https://github.com/buenos-dan/cheetah_sim/tree/master/ros_package/cheetah_gazebo)                    |contains a launch file for using gazebo and spawn the model|    
|[cheetah_control](https://github.com/buenos-dan/cheetah_sim/tree/master/ros_package/cheetah_control)                   |contains a launch file for load joint's plugins   |    
|[cheetah_core](https://github.com/buenos-dan/cheetah_sim/tree/master/ros_package/cheetah_core)                   |contains many code snippets such as inverseKinematics,Jacobi,Force control..   |    


#### ./assets

|**folder**                        |**Description**                     |   
|----------------------------------|------------------------------------|   
|[pictures](https://github.com/buenos-dan/cheetah_sim/tree/master/assets/picture)              |contains a few of pictures of model and simulation |   
|[docs](https://github.com/buenos-dan/cheetah_sim/tree/master/assets/docs)                    |contains some documents for tutorials|    
