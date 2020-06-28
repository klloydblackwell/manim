#!/usr/bin/env python

from manimlib.imports import *


def brancher(curves_pos,start_index,path_intervals,path_thetas,path_colors):
	
	# curve_pos: list of np.arrays of nodes
	# start_index: index of node we're starting on
	# path_intervals: personalized list of jump intervals
	# path_thetas: personalized list of jump angles
	# path_colors: personalized list of arc colors
	
	branches = []
	root = start_index
	
	for i in range(0,4):
		branch = ArcBetweenPoints(curves_pos[root], 
			curves_pos[(root + path_intervals[i]) % 12],
			angle = path_thetas[i],
			stroke_width = 8
			)
		branch.set_color(path_colors[i])
			
		branches.append(branch)
		
		root = (root + path_intervals[i]) % 12
		
	return branches
	



class csidhKey(Scene):
	def construct(self):
		
		
		curves_pos = [np.array([
						2.5 * np.cos(2*np.pi*k / 12),
						2.5 * np.sin(2*np.pi*k / 12),
						0
						]) 
						for k in range(0,12)]
		
		curve_dots = [VGroup(Dot(radius=0.3,color=GRAY).move_to(curves_pos[k]),
							Dot(radius=0.25,color=BLACK).move_to(curves_pos[k])
							)
						for k in range(0,12)]
						
		E0_label = TexMobject("E_0")
		E0_label.next_to(curves_pos[0],RIGHT,buff=0.5)
		
		curve_dots_VG = VGroup(*curve_dots)
		
		self.play(
			FadeIn(curve_dots_VG),
			lag_ratio = 0.2,
			run_time = 2
			)
		self.add_foreground_mobjects(curve_dots_VG)
		self.play(
			Write(E0_label),
			lag_ratio = 0.2,
			run_time = 2
			)
		self.wait()

		alice_path_intervals = [1,4,1,-3]
		alice_path_thetas = [TAU/4,TAU/8,TAU/4,TAU/4]
		alice_path_colors = [BLUE,RED,BLUE,GREEN_SCREEN]
		
		alice_arcs_0 = brancher(curves_pos,
						0,
						alice_path_intervals,
						alice_path_thetas,
						alice_path_colors
						)
						
		alice_arcs_0_VG = VGroup(*alice_arcs_0)
		
		alice_walker = TexMobject("\\text{\\textbf{A}}")
		alice_walker.set_color(TEAL).scale(0.8)
		alice_walker.move_to(curves_pos[0])
		
		self.add_foreground_mobjects(alice_walker)
		
		self.play(
			Write(alice_walker)
			)
		self.wait()
		
		for i in range(0,4):
			self.play(
				ShowCreation(alice_arcs_0[i])
				)
			self.play(
				MoveAlongPath(alice_walker,alice_arcs_0[i]),
				lag_ratio = 0.4,
				run_time = 2
				)
			self.wait()
			
		EA_label = TexMobject("E_A").next_to(curves_pos[3],UP,buff=0.5)
		
		self.play(
			Write(EA_label),
			FadeOut(alice_arcs_0_VG)
			)
		self.wait()
		
		
		bob_path_intervals = [4,4,-3,1]
		bob_path_thetas = [TAU/8,TAU/8,TAU/4,TAU/4]
		bob_path_colors = [RED,RED,GREEN_SCREEN,BLUE]
		
		bob_arcs_0 = brancher(curves_pos,
						0,
						bob_path_intervals,
						bob_path_thetas,
						bob_path_colors
						)
						
		bob_Darcs_0 = [DashedVMobject(x) for x in bob_arcs_0]
						
		bob_Darcs_0_VG = VGroup(*bob_Darcs_0)
		
		bob_walker = TexMobject("\\text{\\textbf{B}}")
		bob_walker.set_color(MAROON).scale(0.8)
		bob_walker.move_to(curves_pos[0])
		
		self.add_foreground_mobjects(bob_walker)
		
		self.play(
			Write(bob_walker)
			)
		self.wait()
		
		for i in range(0,4):
			self.play(
				ShowCreation(bob_Darcs_0[i])
				)
			self.play(
				MoveAlongPath(bob_walker,bob_arcs_0[i]),
				lag_ratio = 0.4,
				run_time = 2
				)
			self.wait()
			
				
		
		EB_label = TexMobject("E_B").next_to(curves_pos[6],LEFT,buff=0.5)
		
		self.play(
			Write(EB_label),
			FadeOut(bob_Darcs_0_VG)
			)
		self.wait()
		
		self.play(
			Transform(alice_walker,alice_walker.copy().move_to(curves_pos[6])),
			Transform(bob_walker,bob_walker.copy().move_to(curves_pos[3])),
			lag_ratio = 0.4,
			run_time = 2
			)
		self.wait()
		
		
				
		alice_arcs_1 = brancher(curves_pos,
						6,
						alice_path_intervals,
						alice_path_thetas,
						alice_path_colors
						)
						
		alice_arcs_1_VG = VGroup(*alice_arcs_1)
		
		
		for i in range(0,4):
			self.play(
				ShowCreation(alice_arcs_1[i])
				)
			self.play(
				MoveAlongPath(alice_walker,alice_arcs_1[i]),
				lag_ratio = 0.4,
				run_time = 2
				)
			self.wait()


		equality_label = TexMobject(
								"E_{AB}",
								"=",
								"E_{BA}"
								).set_color(YELLOW)
		equality_label.to_corner(DOWN)
		
		yellow_eye = VGroup(Dot(radius=0.3,color=YELLOW).move_to(curves_pos[9]),
							Dot(radius=0.25,color=BLACK).move_to(curves_pos[9])
							)
		
		self.play(
			FadeOut(alice_arcs_1_VG),
			FadeOut(alice_walker),
			Transform(curve_dots[9],yellow_eye),
			Write(equality_label[0])
			)
		self.wait()
		
		
		bob_arcs_1 = brancher(curves_pos,
						3,
						bob_path_intervals,
						bob_path_thetas,
						bob_path_colors
						)
					
		bob_Darcs_1 = [DashedVMobject(x) for x in bob_arcs_1]
						
		bob_Darcs_1_VG = VGroup(*bob_Darcs_1)
		
		
		for i in range(0,4):
			self.play(
				ShowCreation(bob_Darcs_1[i])
				)
			self.play(
				MoveAlongPath(bob_walker,bob_arcs_1[i]),
				lag_ratio = 0.4,
				run_time = 2
				)
			self.wait()
		
		
		self.play(
			FadeOut(bob_Darcs_1_VG),
			FadeOut(bob_walker),
			Write(equality_label[2]),
			Write(equality_label[1])
			)
		self.wait()
		









