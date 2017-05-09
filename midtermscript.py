#Kacper Puczydlowski
#midterm script

import numpy as np

def main():
	#format: vec_from_to, trans_from_to, rot_from_to

	#answer to part A
	vec_cam_b = np.matrix('-3; 6.5; -7; 1')
	vec_cam_c = np.matrix('-2; 3; -7; 1')
	vec_cam_d = np.matrix('3.5; -0.5; 2; 1')

	print("Part A")
	print("P_cam_b:")
	print(vec_cam_b)
	print("P_cam_c:")
	print(vec_cam_b)

	#answer to part B
	trans_d0_cam = np.matrix('1 0 0 -3.5; 0 1 0 0.5; 0 0 1 6; 0 0 0 1')
	vec_d0_b = trans_d0_cam * vec_cam_b

	print("Part B")
	print("P_d0_b:")
	print (vec_d0_b)
	
	#Part C, D, 
	#Waypoints are marked up on the map attached
	#Waypoints reference the camera as (0,0,8)
	#angle is  included, and the rotational transforms are explicit below
	# Waypoints are: [3.5, -0.5, 2, 0] [3.5, -0.5, 10, 0] [5.5, -0.5, 10, 0] [5.5, 4.5, 10, 0] 
	# 				 [5.5, 4.5, 10, 90] [5.5, 4.5, 10, 166.75 ] [-3, 6.5, 10, 166.75] 
	#				 [-3, 6.5, 10, 0] 
	#increase 8 altitude (z)
	trans_0_1 = np.matrix([[1, 0, 0, 0], [0, 1, 0 , 0], [0, 0, 1 , 8], [0, 0, 0, 1]])
	
	#increase x 2
	trans_1_2 = np.matrix([[1, 0, 0, 2], [0, 1, 0 , 0], [0, 0, 1 , 0], [0, 0, 0, 1]])
	
	#rotate 90 CCW
	theta1 = -np.pi/2
	rot_2_3 = np.matrix([[np.cos(theta1), -np.sin(theta1), 0 , 0], [np.sin(theta1), np.cos(theta1), 0 , 0], [0, 0, 1 , 0], [0, 0, 0 , 1]])
	
	#increase x 5
	trans_3_4 = np.matrix([[1, 0, 0, 5], [0, 1, 0 , 0], [0, 0, 1 , 0], [0, 0, 0, 1]]) 

	#rotate 76.75 degs CCW
	theta2 = -np.arctan2(8.5,2.0)
	rot_4_5 = np.matrix([[np.cos(theta2), -np.sin(theta2), 0 , 0], [np.sin(theta2), np.cos(theta2), 0 , 0], [0, 0, 1 , 0], [0, 0, 0 , 1]])
	
	#final translation
	dist_final = np.sqrt((2*2 + 8.5*8.5))
	trans_5_6 =  np.matrix([[1, 0, 0, dist_final], [0, 1, 0 , 0], [0, 0, 1 , 0], [0, 0, 0, 1]])
	
	#get back to original orientation
	rot_2_3i = np.matrix([[np.cos(-theta1), -np.sin(-theta1), 0 , 0], [np.sin(-theta1), np.cos(-theta1), 0 , 0], [0, 0, 1 , 0], [0, 0, 0 , 1]])
	rot_4_5i = np.matrix([[np.cos(-theta2), -np.sin(-theta2), 0 , 0], [np.sin(-theta2), np.cos(-theta2), 0 , 0], [0, 0, 1 , 0], [0, 0, 0 , 1]])

	a = rot_2_3i*rot_4_5i*trans_5_6*rot_4_5*trans_3_4*rot_2_3*trans_1_2*trans_0_1*vec_cam_d
	print("Part C,D,E check. See comments in code")
	print(a)

if __name__ == '__main__':
	main()