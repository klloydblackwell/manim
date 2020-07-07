#!/usr/bin/env python

from manimlib.imports import *

class veluLG(Scene):
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
							"x^2 + ",
							"B",
							"x + ",
							"C"
							)
		E1_label[0].set_color(GREEN)
		E1_label[2].set_color(GREEN)
		E1_label[4].set_color(GREEN)
		E1_label[6].set_color(GREEN)
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

		generator_dot = [Dot(E1_axes.coords_to_point(-1.325,0), color=RED,radius=0.1),
						Dot(E1_axes.coords_to_point(-0.577,1.177), color=RED,radius=0.1),
						Dot(E1_axes.coords_to_point(-0.577,-1.177), color=RED,radius=0.1),
						Dot(E1_axes.coords_to_point(0,1), color=RED,radius=0.1),
						Dot(E1_axes.coords_to_point(0,-1), color=RED,radius=0.1),
						Dot(E1_axes.coords_to_point(1.3,1.377), color=RED,radius=0.1),
						Dot(E1_axes.coords_to_point(1.3,-1.377), color=RED,radius=0.1)
						]

		generator_VG = VGroup(*generator_dot)

		self.play(
					FadeIn(generator_VG)
					)
		self.wait()

		subgp_label = TexMobject(
						"G",
						"\\subset",
						"E",
						"(\\overline{k})"
						)
		subgp_label[0].set_color(RED)
		subgp_label[2].set_color(GREEN)
		subgp_label.move_to(np.array([-2,-2,0]))

		self.play(
			ReplacementTransform(generator_VG.copy(),subgp_label)
			)
		self.wait()

		E1_graph_VG = VGroup(E1_axes,E1_label,E1,generator_VG,subgp_label)

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
							"x^2 + ",
							"B'",
							"x + ",
							"C'"
							)
		E2_label[0].set_color(BLUE)
		E2_label[2].set_color(BLUE)
		E2_label[4].set_color(BLUE)
		E2_label[6].set_color(BLUE)
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
							"\\mathcal{J}(",   #sk - 0      
							"x",               #co - 1
							",",               #sk - 2
							"y",               #co - 3
							") = \\bigg(",     #sk - 4
							"x",               #co - 5          
							"+",               #sk - 6
							"\\sum_{Q \\in G}",#ke - 7
							"{.",            #sk - 8
							"f'",              #cu - 9
							"(",               #cu - 10
							"Q",               #ke - 11
							")",               #cu - 12
							"\\over",          #sk - 13
							"x",               #co - 14
							"-",               #co - 15
							"x",               #co - 16
							"(",               #co - 17
							"Q",               #ke - 18
							")",               #co - 19
							".}",               #sk - 20
							"+",               #sk - 21
							"{.",               #sk - 22
							"2",               #cu - 23
							"f",               #cu - 24
							"(",               #cu - 25
							"Q",               #ke - 26
							")",               #cu - 27
							"\\over",          #sk - 28
							"(",               #op - 29
							"x",               #co - 30
							"-",               #co - 31
							"x",               #co - 32
							"(",               #co - 33
							"Q",               #ke - 34
							")",               #co - 35
							")^2",             #op - 36
							".}",               #sk - 37
							",",               #sk - 38
							"y",               #co - 39
							"+",               #sk - 40
							"\\sum_{Q \\in G}",#ke - 41
							"{.",               #sk - 42
							"-y",              #co - 43
							"f'",              #cu - 44
							"(",               #cu - 45
							"Q",               #ke - 46
							")",               #cu - 47
							"\\over",          #sk - 48
							"(",               #op - 49
							"x",               #co - 50
							"-",               #co - 51
							"x",               #co - 52
							"(",               #co - 53
							"Q",               #ke - 54
							")",               #co - 55
							")^2",             #op - 56
							".}",               #sk - 57
							"-",               #sk - 58
							"{.",               #sk - 59
							"4",               #co - 60
							"y",               #co - 61
							"f'",              #cu - 62
							"(",               #cu - 63
							"Q",               #ke - 64
							")",               #cu - 65
							"\\over",          #sk - 66
							"(",               #op - 67
							"x",               #co - 68
							"-",               #co - 69
							"x",               #co - 70
							"(",               #co - 71
							"Q",               #ke - 72
							")",               #co - 73
							")^3",             #op - 74
							".}",               #sk - 75
							"\\bigg)"          #sk - 76
							)
		velu_eqn.scale(0.75)

		sk_index = [0,2,4,6,8,13,20,21,22,28,37,38,40,42,48,57,58,59,66,75,76]
		op_index = [29,36,49,56,67,74]

		co1_index = [1,3]
		co2_index = [5,14,15,16,17,19,30,31,32,33,35,39,43,50,51,52,53,55,60,61,68,69,70,71,73]

		cu_index = [9,10,12,23,24,25,27,44,45,47,62,63,65]

		ke_index = [7,11,18,26,34,41,46,54,64,72]

		for i in [8,20,22,37,42,57,59,75]:
			velu_eqn[i].set_color(BLACK)


		sk_VG = VGroup(*[velu_eqn[i] for i in sk_index])
		op_VG = VGroup(*[velu_eqn[i] for i in op_index])

		co1_VG = VGroup(*[velu_eqn[i].set_color(YELLOW) for i in co1_index])
		co2_VG = VGroup(*[velu_eqn[i].set_color(YELLOW) for i in co2_index])

		cu_VG = VGroup(*[velu_eqn[i].set_color(GREEN) for i in cu_index])

		ke_VG = VGroup(*[velu_eqn[i].set_color(RED) for i in ke_index])

		velu_eqn_VG = VGroup(sk_VG,op_VG,co1_VG,co2_VG,cu_VG,ke_VG)

		velu_eqn.to_edge(DOWN)

		preimage_pos = E1_axes.coords_to_point(0.577,0.784)
		preimage_dot = Dot(preimage_pos,color=YELLOW,radius=0.13)
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
				Write(sk_VG)
				)
		self.wait()

		self.play(
			ReplacementTransform(preimage_coords_VG.copy(),co1_VG)
			)
		self.play(
			ReplacementTransform(co1_VG.copy(),co2_VG)
			)
		self.wait(1)
		self.play(
			ReplacementTransform(E1_label.copy(),cu_VG)
			)
		self.wait(1)
		self.play(
			ReplacementTransform(generator_VG.copy(),ke_VG)
			)
		self.wait(1)
		self.play(
			FadeIn(op_VG)
			)
		self.wait(1)



		image_pos = E2_axes.coords_to_point(-1.45,-0.645)
		image_dot = Dot(image_pos,color=YELLOW,radius=0.15)
		image_label = TexMobject(
							"\\mathcal{J}(",   #sk - 0      
							"x",               #co - 1
							",",               #sk - 2
							"y",               #co - 3
							")"                #sk - 4)
							)
		image_label[1].set_color(YELLOW)
		image_label[3].set_color(YELLOW)
		image_label.scale(0.8)
		image_label.next_to(image_dot,DOWN+LEFT,buff=0)

		self.play(
			FadeIn(image_dot)
			)
		self.wait(1)
		self.play(
			ReplacementTransform(velu_eqn_VG.copy(),image_label)
			)
		self.wait(2)
