#!/usr/bin/env python

from manimlib.imports import *

class isohash(Scene):
	def construct(self):
		
		main_posList = []
		main_posList.append(np.array([-6,0,0]))
		
		main_nodeList = []
		first_node = Dot(radius=0.15).move_to(main_posList[0])
		main_nodeList.append(first_node)
		
		main_edgeList = []
		main_labelList = []
		
		branch_posList = []
		branch_edgeList = []
		branch_labelList = []
		
		root_label = TexMobject("j_0").next_to(first_node,LEFT)
		root_label.set_color(ORANGE).scale(1.3)
		
		zero_label = TexMobject("0").set_color(GRAY)
		one_label = TexMobject("1").set_color(BLUE)
		
		
		for i in range(0,6):
			
			#Fix root position
			root_pos = main_posList[i]
			
			#Alternate main, branch positions
			if i % 2 == 0:
				branch_pos = root_pos.copy() + np.array([2,1,0])
				main_pos = root_pos.copy() + np.array([2,-0.5,0])
			
			else:
				main_pos = root_pos.copy() + np.array([2,0.5,0])
				branch_pos = root_pos.copy() + np.array([2,-1,0])
			
			#Save main, branch positions
			branch_posList.append(branch_pos)
			main_posList.append(main_pos)
			
			#Create, save main node
			main_node = Dot(radius=0.15).move_to(main_pos)
			main_nodeList.append(main_node)
			
			#Create, save main, branch edges
			main_start = root_pos
			main_end = root_pos + 0.9*(main_pos - root_pos)
			
			branch_start = root_pos
			branch_end = root_pos + 0.9*(branch_pos - root_pos)
			
			main_edge = Arrow().put_start_and_end_on(main_start,main_end)
			main_edge.set_color(BLUE)
			branch_edge = Arrow().put_start_and_end_on(branch_start,branch_end)
			branch_edge = DashedVMobject(branch_edge).set_color(GRAY)
			
			main_edgeList.append(main_edge)
			branch_edgeList.append(branch_edge)
			
			if i % 2 == 0:
				main_label = zero_label.copy().next_to(main_edge,DOWN,buff=-0.1)
				branch_label = one_label.copy().next_to(branch_edge,UP,buff=-0.2)
			
			else:
				main_label = one_label.copy().next_to(main_edge,UP,buff=-0.1)
				branch_label = zero_label.copy().next_to(branch_edge,DOWN,buff=-0.2)
			
			main_labelList.append(main_label.set_color(BLUE))
			branch_labelList.append(branch_label.set_color(GRAY))
			
		
		destination_label = TexMobject("j")
		destination_label.next_to(main_posList[-1],RIGHT,buff=0.4)
		destination_label.set_color(ORANGE).scale(1.3)
		destination_label.shift(0.1*UP)
		
		main_nodeList_VG = VGroup(*main_nodeList)
		main_labelList_VG = VGroup(*main_labelList)
		main_edgeList_VG = VGroup(*main_edgeList)
		
		main_VG = VGroup(main_nodeList_VG,main_labelList_VG,main_edgeList_VG)
		
		branch_labelList_VG = VGroup(*branch_labelList)
		branch_edgeList_VG = VGroup(*branch_edgeList)
		
		branch_VG = VGroup(branch_labelList_VG,branch_edgeList_VG)
		
		walk_VG = VGroup(main_VG,branch_VG,root_label,destination_label)
		
		
		self.play(
			FadeIn(first_node),
			Write(root_label)
			)
		self.add_foreground_mobjects(first_node)
		self.wait()
		
		for i in range(0,6):
			
			if i == 5:
				self.play(
					FadeIn(main_nodeList[i+1]),
					ShowCreation(main_edgeList[i]),
					ShowCreation(branch_edgeList[i]),
					Write(destination_label),
					Write(main_labelList[i]),
					Write(branch_labelList[i])
					)
				continue
			
			self.play(
				FadeIn(main_nodeList[i+1]),
				ShowCreation(main_edgeList[i]),
				ShowCreation(branch_edgeList[i]),
				Write(main_labelList[i]),
				Write(branch_labelList[i])
				)
			
			self.add_foreground_mobjects(main_nodeList[i+1])
			self.wait()
			
			
		rectangle = RoundedRectangle(height=3,width=12.5)
		rectangle.set_color(RED)
		rectangle.shift(0.25*DOWN)
		
		rectangle_label = TextMobject("Supersingular 2-isogeny graph")
		rectangle_label.set_color(RED)
		rectangle_label.next_to(rectangle,DOWN)
		
		self.play(
			FadeIn(rectangle)
			)
		self.play(
			FadeInFromDown(rectangle_label)
			)
		self.wait()
		
		self.play(
			FadeOutAndShift(rectangle),
			FadeOutAndShift(rectangle_label)
			)
		self.wait()
		
		hash_label = TexMobject(
						"H(",     #0
						"010101", #1 
						") = ",   #2
						"j"      #3
						)
		hash_label.to_corner(UP).scale(1.4)	
		hash_label[1].set_color(BLUE)
		hash_label[3].set_color(ORANGE)
		
		self.play(
			FadeInFromDown(hash_label[0]),
			FadeInFromDown(hash_label[2])
			)
		self.wait()
		
		self.play(
			ReplacementTransform(main_labelList_VG.copy(),hash_label[1])
			)
		self.play(
			ReplacementTransform(destination_label.copy(),hash_label[3])
			)
		self.wait(2)
		
		self.remove_foreground_mobjects(first_node)
		self.remove_foreground_mobjects(*main_nodeList)
		
		self.play(
			FadeOut(hash_label),
			FadeOut(walk_VG)
			)
		self.wait()
			
				
				

		
		
		
		
		
		
		
		
		
		
		
		
		
		
