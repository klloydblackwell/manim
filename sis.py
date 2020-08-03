#!/usr/bin/env python

from manimlib.imports import *



class sis_def(Scene):
	def construct(self):

		# Label random draw of vectors

		dialogue_rect_vec = RoundedRectangle(height=2,width=4,fill_opacity=1,color=RED,fill_color=BLACK)
		dialogue_rect_vec.to_corner(UP+LEFT)

		def_label_vec_A = TexMobject("\\Bigg[ \\mathbf{a}_k \\Bigg]", 
			"\\overset{R}{\\longleftarrow}",
			"\\mathbb{Z}_{q}^{n}"
			)
		def_label_vec_A.set_color(RED)

		def_label_vec_A.move_to(dialogue_rect_vec.get_center())

		dialogue_box_vec = VGroup(dialogue_rect_vec,def_label_vec_A)

		self.play(
			FadeInFrom(dialogue_box_vec,LEFT),
			lag_ratio=0.5,
			run_time=2
			)
		self.wait(1)

		#Expanded SIS Equation
		SIS_eqn_exp = TexMobject(
			"z_1",                             #0 BLUE
			"\\cdot",
			"\\Bigg[ \\mathbf{a}_1 \\Bigg]",   #2 RED
			"+",
			"z_2",                             #4 BLUE
			"\\cdot",
			"\\Bigg[ \\mathbf{a}_2 \\Bigg]",   #6 RED
			"+",
			"\\cdots",
			"+",
			"z_m",                             #10 BLUE
			"\\cdot",
			"\\Bigg[ \\mathbf{a}_m \\Bigg]",   #12 RED
			"=",
			"\\mathbf{0}"
			).shift(2*DOWN)

		SIS_eqn_exp_auxVG = VGroup(*[SIS_eqn_exp[i] for i in [1,3,5,7,9,11,13,14]]) 

		SIS_eqn_vec_VG = VGroup(*[SIS_eqn_exp[i] for i in [2,6,12]])
		for i in [2,6,12]:
			SIS_eqn_exp[i].set_color(RED)
			self.play(
				ReplacementTransform(def_label_vec_A[0].copy(),SIS_eqn_exp[i])
				)
		self.play(FadeInFrom(SIS_eqn_exp[8]))
		self.wait(1)

		

		# Label tertiary coordinates

		dialogue_rect_coo = RoundedRectangle(height=2,width=4,fill_opacity=1,color=BLUE,fill_color=BLACK)
		dialogue_rect_coo.to_corner(UP+RIGHT)

		def_label_coo_A = TexMobject(
			"z_k", 
			"\\in \\lbrace -1, 0, 1 \\rbrace"
			)
		def_label_coo_A.set_color(BLUE)

		def_label_coo_A.move_to(dialogue_rect_coo.get_center())

		dialogue_box_coo = VGroup(dialogue_rect_coo,def_label_coo_A)

		self.play(
			FadeInFrom(dialogue_box_coo,RIGHT),
			lag_ratio=0.5,
			run_time=2
			)
		self.wait(1)

		SIS_eqn_coo_VG = VGroup(*[SIS_eqn_exp[i] for i in [0,4,10]])
		for i in [0,4,10]:
			SIS_eqn_exp[i].set_color(BLUE)
			self.play(
				ReplacementTransform(def_label_coo_A[0].copy(),SIS_eqn_exp[i])
				)
		self.play(FadeInFrom(SIS_eqn_exp_auxVG))
		self.wait(2)


		# compact SIS eqn
		SIS_comp_eqn = TexMobject(
			"\\Bigg[ \\hphantom{--} \\mathbf{A}^{n \\times m} \\hphantom{--} \\Bigg]",
			"\\Bigg[ \\mathbf{z} \\Bigg]",
			"= \\mathbf{0}"
			)
		SIS_comp_eqn[0].set_color(RED)
		SIS_comp_eqn[1].set_color(BLUE)

		self.play(
			ReplacementTransform(SIS_eqn_vec_VG.copy(),SIS_comp_eqn[0])
			)
		self.wait(1)
		self.play(
			ReplacementTransform(SIS_eqn_coo_VG.copy(),SIS_comp_eqn[1])
			)
		self.wait(1)
		self.play(
			ReplacementTransform(SIS_eqn_exp_auxVG.copy(),SIS_comp_eqn[2])
			)
		self.wait(1)
		
		self.play(
			FadeOutAndShift(SIS_eqn_exp,DOWN),
			FadeOutAndShift(dialogue_box_coo,RIGHT),
			FadeOutAndShift(dialogue_box_vec,LEFT)
			)
		self.wait(2)

		dialogue_rect_dual = RoundedRectangle(height=2,width=8,fill_opacity=1,color=ORANGE,fill_color=BLACK)
		dialogue_rect_dual.to_corner(DOWN)

		def_label_dual_A = TexMobject("q\\text{-ary Lattice}").set_color(ORANGE)
		def_label_dual_A.move_to(dialogue_rect_dual.get_center() + 0.5*UP)

		def_label_dual_B = TexMobject(
			"\\mathcal{L}^{\\bot}",
			"(A)",
			" = \\lbrace \\mathbf{x} \\in \\mathbb{Z}_{q}^{n}: \\hphantom{.} A\\mathbf{x}=\\mathbf{0} \\rbrace"
			)
		def_label_dual_B.set_color(ORANGE)
		def_label_dual_B.move_to(dialogue_rect_dual.get_center() + 0.5*DOWN)

		dialogue_box_dual = VGroup(dialogue_rect_dual,def_label_dual_A,def_label_dual_B)

		self.play(
			Transform(SIS_comp_eqn,SIS_comp_eqn.copy().shift(1*UP)),
			FadeInFrom(dialogue_box_dual,DOWN)
			)
		self.add_foreground_mobjects(dialogue_box_dual)
		self.wait()


		x_vec = np.array([3,2,0])

		y_vec = np.array([1,3,0])

		lattice_dots = []
		for i in range(-10,10):
			for j in range(-10,10):
				lattice_dots.append(Dot(i*x_vec + j*y_vec,radius=0.1,color=ORANGE))

		origin_label = TexMobject("\\mathbf{O}").set_color(ORANGE).scale(0.8).next_to(ORIGIN,DOWN+RIGHT,buff=0.15)
		lattice_dots_VG = VGroup(*lattice_dots,origin_label)
		
		grid = NumberPlane(faded_line_ratio=0,
						x_min = -20,
						x_max = 20,
						y_min = -20,
						y_max =20
						)
		grid.set_color(ORANGE).fade(0.75)
		grid.get_axes().set_width(1).fade(0.9)

		grid.prepare_for_nonlinear_transform()
		grid.apply_function(lambda p: p[0]*x_vec + p[1]*y_vec)

		self.play(
			FadeOutAndShift(SIS_comp_eqn,UP),
			FadeInFrom(lattice_dots_VG),
			FadeInFrom(grid)
			)
		self.wait(2)

		self.play(
			FadeOutAndShift(dialogue_box_dual,LEFT)
			)
		self.wait()

		short_circ = Dot(ORIGIN,color=BLUE,radius=2.4).fade(0.75)

		soln_marker_1 = Dot(x_vec - y_vec, color=YELLOW, radius=0.15)
		soln_marker_2 = Dot(y_vec - x_vec, color=YELLOW, radius=0.15)

		soln_marks_VG = VGroup(soln_marker_1,soln_marker_2)

		self.play(
			GrowFromPoint(short_circ,ORIGIN),
			lag_ratio = 0.2,
			run_time = 3
			)
		self.play(
			FadeIn(soln_marks_VG)
			)
		self.wait()

		short_solns_grid_VG = VGroup(short_circ,lattice_dots_VG,grid,soln_marks_VG)


		dialogue_rect_short = RoundedRectangle(height=1.5,width=6,fill_opacity=1,color=YELLOW,fill_color=BLACK)
		dialogue_rect_short.to_corner(UP)

		def_label_short_A = TextMobject("Short solutions lie in").set_color(YELLOW).scale(0.8)
		def_label_short_A.move_to(dialogue_rect_short.get_center() + 0.5*LEFT)

		def_label_short_B = Dot(ORIGIN,color=BLUE,radius= 0.6).fade(0.75)
		def_label_short_B.move_to(dialogue_rect_short.get_center() + 2*RIGHT)

		dialogue_box_short = VGroup(dialogue_rect_short,def_label_short_A,def_label_short_B)

		self.play(
			Transform(short_solns_grid_VG, short_solns_grid_VG.copy().shift(1.3*DOWN)),
			FadeInFrom(dialogue_box_short,UP)
			)
		self.wait(2)


