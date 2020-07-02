#!/usr/bin/env python

from manimlib.imports import *

class velu(Scene):
	def construct(self):
		
		
		E1_axes = Axes(
							y_min=-2,
							y_max=2,
							x_min=-2,
							x_max=2
							)
		
		E1_axes.scale(1.3)

		E1_upper = E1_axes.get_graph(lambda x : np.sqrt(x**3 - x + 1),
											color = GREEN,
											x_min = -1.32471795, 
											x_max = 1.65
											)

		E1_lower = E1_axes.get_graph(lambda x : -np.sqrt(x**3 - x + 1),  
											color = GREEN,
											x_min = -1.32471795, 
											x_max = 1.65
											)
		E1 = VGroup(E1_upper,E1_lower)

		E1_label = TexMobject(
							"E",
							": y^2 = x^3 +",
							"A", 
							"x + ",
							"B"
							)
		E1_label[0].set_color(GREEN)
		E1_label[2].set_color(GREEN)
		E1_label[4].set_color(GREEN)
		E1_label.next_to(E1_axes,UP)

		self.play(
					ShowCreation(E1_axes)
					)
		self.wait()
		self.play(
					Write(E1),
					Write(E1_label)
					)
		self.wait()

		generator_dot = Dot(E1_axes.coords_to_point(-1.325,0), color=RED,radius=0.15)
		generator_label = TexMobject(
									"(",
									"x_0",
									",0)"
									)
		generator_label[1].set_color(RED)
		generator_label.next_to(generator_dot,DOWN+LEFT)

		generator_VG = VGroup(generator_dot,generator_label)

		self.play(
					FadeIn(generator_dot)
					)
		self.play(
					FadeInFromDown(generator_label)
					)
		self.wait()

		E1_graph_VG = VGroup(E1_axes,E1_label,E1,generator_VG)

		self.play(
					Transform(E1_graph_VG, E1_graph_VG.copy().scale(1/1.3).move_to(np.array([-3.5,1,0])))
					)
		self.wait()


		E2_axes = Axes(
							y_min=-2,
							y_max=2,
							x_min=-2,
							x_max=2
							)
		

		
		E2_upper = E2_axes.get_graph(lambda x : np.sqrt(x**3 - 1.7*x + 1),
											color = BLUE,
											x_min = -1.533635, 
											x_max = 1.65
											)

		E2_lower = E2_axes.get_graph(lambda x : -np.sqrt(x**3 - 1.7*x + 1),  
											color = BLUE,
											x_min = -1.533635, 
											x_max = 1.65
											)

		E2 = VGroup(E2_upper,E2_lower)

		E2_label = TexMobject(
							"E'",
							": y^2 = x^3 +",
							"A'", 
							"x + ",
							"B'"
							)
		E2_label[0].set_color(BLUE)
		E2_label[2].set_color(BLUE)
		E2_label[4].set_color(BLUE)
		E2_label.next_to(E2_axes,UP).scale(1/1.3)


		E2_graph_VG = VGroup(E2_axes,E2,E2_label)
		E2_graph_VG.move_to(np.array([3.5,1,0]))
		self.play(
					ShowCreation(E2_graph_VG),
					lag_ratio=0.2,
					run_time=5
					)

		self.wait()

		velu_eqn = TexMobject(
							"\\phi(",          #0
							"x",      
							",",
							"y",
							") = \\bigg(",
							"{x^2",            #5 
							"-",       
							"x_0",     
							"x",       
							"+ t",     
							"\\over",          #10
							"x",       
							"-",
							"x_0}",
							",",
							"{(",              #15
							"x",
							"-",
							"x_0",
							")^2",
							"- t",             #20
							"\\over",
							"(",
							"x",
							"-",
							"x_0",             #25
							")^2}",
							"y",
							"\\bigg)"       
							)

		x0_copies = [7,13,18,25]
		xy_copies = [3,1,5,8,11,16,23,27]
		xy_ops = [6,9,12,15,17,19,20,22,24,26]

		x0_copies_VG = VGroup(*[velu_eqn[i] for i in x0_copies])
		xy_copies_VG = VGroup(*[velu_eqn[i] for i in xy_copies])
		xy_ops_VG = VGroup(*[velu_eqn[i] for i in xy_ops])

		velu_else_copies = [i for i in range(0,29) if ((i not in x0_copies) and (i not in xy_copies) and (i not in xy_ops))]

		velu_else_copies_list = [velu_eqn[i] for i in velu_else_copies]
		velu_else_copies_VG = VGroup(*velu_else_copies_list)



		for i in x0_copies:
			velu_eqn[i].set_color(RED)

		for i in xy_copies:
			velu_eqn[i].set_color(YELLOW)

		velu_eqn.to_edge(DOWN)





		

		


		preimage_pos = E1_axes.coords_to_point(0.577,0.784)
		preimage_dot = Dot(preimage_pos,color=YELLOW,radius=0.15)
		preimage_label = TexMobject("(","x",",","y",")")
		preimage_label[1].set_color(YELLOW)
		preimage_label[3].set_color(YELLOW)
		preimage_label.scale(0.9)
		preimage_label.next_to(preimage_dot,DOWN+RIGHT,buff=0)

		preimage_coords_VG = VGroup(preimage_label[1],preimage_label[3])

		self.play(
				FadeIn(preimage_dot),
				Write(preimage_label)
				)
		self.wait()

		self.play(
				Write(velu_else_copies_VG)
				)
		self.wait()

		self.play(
			ReplacementTransform(preimage_coords_VG.copy(),xy_copies_VG)
			)
		self.wait(1)
		self.play(
			ReplacementTransform(generator_label[1].copy(),x0_copies_VG)
			)
		self.wait(1)
		self.play(
			FadeIn(xy_ops_VG)
			)
		self.wait(1)

		velu_eqn_reduc = TexMobject(
									"=",
									"(p\\big(",
									"x",
									"),",
									"q(",
									"x",
									")",
									"y",
									"\\big)"
									)
		velu_eqn_reduc[2].set_color(YELLOW)
		velu_eqn_reduc[5].set_color(YELLOW)
		velu_eqn_reduc[-2].set_color(YELLOW)

		velu_eqn_target = velu_eqn.copy().shift(1.7*LEFT)
		velu_eqn_reduc.next_to(velu_eqn_target,RIGHT)

		self.play(
			Transform(velu_eqn,velu_eqn_target),
			FadeIn(velu_eqn_reduc)
			)
		self.wait()


		image_pos = E2_axes.coords_to_point(-1.45,-0.645)
		image_dot = Dot(image_pos,color=YELLOW,radius=0.15)
		image_label = velu_eqn_reduc.copy()[1:]
		image_label.scale(0.8)
		image_label.next_to(image_dot,DOWN+LEFT,buff=0)

		self.play(
			FadeIn(image_dot)
			)
		self.play(
			ReplacementTransform(velu_eqn_reduc.copy(),image_label)
			)
		self.wait()
