#!/usr/bin/env python

from manimlib.imports import *



class lwe_def(Scene):
	def construct(self):

		exp_eqn_1 = TexMobject(
			"\\mathbf{a}_1",
			"\\leftarrow",
			"\\mathbb{Z}_{q}^{n}",
			"\\hphantom{-},\\hphantom{-}",
			"b_1",
			"= \\langle",
			"\\mathbf{s}",
			",",
			"\\mathbf{a}_1",
			"\\rangle + e_1 \\in \\mathbb{Z}_q"
			).move_to(2.5*UP)

		eqn_blue_list = [0,8]
		eqn_green_list = [6]
		eqn_red_list = [4]

		exp_eqn_a1_list = [0]
		exp_eqn_a2_list = [8]
		exp_eqn_b_list = [4]
		exp_eqn_s_list = [6]
		exp_eqn_e_list = [9]

		


		exp_eqn_2 = TexMobject(
			"\\mathbf{a}_2",
			"\\leftarrow",
			"\\mathbb{Z}_{q}^{n}",
			"\\hphantom{-},\\hphantom{-}",
			"b_2",
			"= \\langle",
			"\\mathbf{s}",
			",",
			"\\mathbf{a}_2",
			"\\rangle + e_2 \\in \\mathbb{Z}_q"
			).move_to(1.75*UP)

		exp_eqn_buffer = TexMobject("\\vdots").next_to(exp_eqn_2[3],DOWN)

		

		for i in eqn_blue_list:
			exp_eqn_1[i].set_color(BLUE)
			exp_eqn_2[i].set_color(BLUE)


		for i in eqn_green_list:
			exp_eqn_1[i].set_color(GREEN)
			exp_eqn_2[i].set_color(GREEN)


		for i in eqn_red_list:
			exp_eqn_1[i].set_color(RED)
			exp_eqn_2[i].set_color(RED)


		exp_eqn_a1_VG = VGroup(exp_eqn_1[0],exp_eqn_2[0])
		exp_eqn_a2_VG = VGroup(exp_eqn_1[8],exp_eqn_2[8])
		exp_eqn_b_VG = VGroup(exp_eqn_1[4],exp_eqn_2[4])
		exp_eqn_s_VG = VGroup(exp_eqn_1[6],exp_eqn_2[6])
		exp_eqn_e_VG = VGroup(exp_eqn_1[9],exp_eqn_2[9])

		self.play(
			Write(exp_eqn_1)
			)
		self.wait()
		self.play(
			Write(exp_eqn_2),
			FadeIn(exp_eqn_buffer)
			)
		self.wait()

		exp_eqn_VG = VGroup(exp_eqn_1,exp_eqn_2,exp_eqn_buffer)

		LWE_comp_eqn = TexMobject(
			"\\Bigg[ \\hphantom{--} \\mathbf{A} \\hphantom{--} \\Bigg]",
			",",
			"\\big[ \\hphantom{--} \\mathbf{b}^{t} \\hphantom{--} \\big]",
			" = ",
			"\\mathbf{s}^{t}",
			"\\mathbf{A}",
			"+ \\mathbf{e}^{t}"
			).shift(1*DOWN)
		LWE_comp_eqn[0].set_color(BLUE)
		LWE_comp_eqn[5].set_color(BLUE)
		LWE_comp_eqn[2].set_color(RED)
		LWE_comp_eqn[4].set_color(GREEN)

		SIS_aux_VG = VGroup(*[LWE_comp_eqn[i] for i in [1,3,6]])

		
		# morph A
		self.play(
			ReplacementTransform(exp_eqn_a1_VG.copy(),LWE_comp_eqn[0])
			)
		self.wait()

		# morph S
		self.play(
			ReplacementTransform(exp_eqn_s_VG.copy(),LWE_comp_eqn[4])
			)
		self.wait()

		# remorph A
		self.play(
			ReplacementTransform(LWE_comp_eqn[0].copy(),LWE_comp_eqn[5])
			)
		self.wait()

		# morph E
		self.play(
			ReplacementTransform(exp_eqn_e_VG.copy(),LWE_comp_eqn[6])
			)
		self.wait()

		# fade aux and morph b
		self.play(
			FadeInFrom(LWE_comp_eqn[3]),
			FadeInFrom(LWE_comp_eqn[1]),
			ReplacementTransform(exp_eqn_b_VG.copy(),LWE_comp_eqn[2])
			)
		self.wait(2)

		self.play(
			FadeOutAndShift(exp_eqn_VG,UP),
			Transform(LWE_comp_eqn,LWE_comp_eqn.copy().to_corner(UP))
			)
		self.wait(2)

		search_label = TexMobject(
			"\\text{Search: }",
			"\\text{Find secret }",
			"\\mathbf{s}",
			"\\in \\mathbb{Z}_q^n",
			"\\text{ given }",
			"(",
			"\\mathbf{A}",
			",",
			"\\mathbf{b}",
			")"
			)
		search_label[0].set_color(BLUE)
		search_label[2].set_color(GREEN)
		search_label[6].set_color(BLUE)
		search_label[8].set_color(RED)

		dist_label = TexMobject(
			"\\text{Decision: }",
			"\\text{Distinguish }",
			"(",
			"\\mathbf{A}",
			",",
			"\\mathbf{b}",
			")",
			"\\text{ from uniform }",
			"(",
			"\\mathbf{A}",
			",",
			"\\mathbf{b}"
			")"
			).shift(2*DOWN)
		dist_label[0].set_color(RED)
		dist_label[5].set_color(RED)
		dist_label[3].set_color(BLUE)
		dist_label[9].set_color(BLUE)
		dist_label[11].set_color(BLUE)

		self.play(
			Write(search_label)
			)
		self.wait(2)

		self.play(
			Write(dist_label)
			)
		self.wait(2)

		
		dialogue_rect_dual = RoundedRectangle(height=2,width=6,fill_opacity=1,color=ORANGE,fill_color=BLACK)
		dialogue_rect_dual.to_corner(DOWN)

		def_label_dual_A = TextMobject("LWE Lattice BDD").set_color(ORANGE)
		def_label_dual_A.move_to(dialogue_rect_dual.get_center() + 0.5*UP)

		def_label_dual_B = TexMobject(
			"\\mathcal{L}",
			"(A)",
			" = \\lbrace \\mathbf{z}^t \\equiv_q \\mathbf{c}^t A  \\rbrace"
			)
		def_label_dual_B.set_color(ORANGE)
		def_label_dual_B.move_to(dialogue_rect_dual.get_center() + 0.5*DOWN)

		dialogue_box_dual = VGroup(dialogue_rect_dual,def_label_dual_A,def_label_dual_B)


		self.play(
			Transform(search_label,search_label.copy().shift(15*LEFT)),
			Transform(dist_label,dist_label.copy().shift(15*RIGHT)),
			FadeInFrom(dialogue_box_dual,DOWN)
			)
		self.add_foreground_mobjects(dialogue_box_dual)
		self.wait(2)

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
			FadeOutAndShift(LWE_comp_eqn,UP),
			FadeInFrom(lattice_dots_VG),
			FadeInFrom(grid)
			)
		self.wait()

		L_radii = []
		for i in range(-8,9):
			for j in range(-5,6):
				loc = i*x_vec + j*y_vec
				L_radii.append(Dot(loc,radius=1.1,color=GRAY).fade(0.75).fade(0.5))
				
		L_radii_VG = VGroup(*L_radii)

		self.play(
			FadeIn(L_radii_VG)
			)
		self.wait(2)

		b_dot = Dot(np.array([-1.5,0.5,0]),color=RED,radius=0.15)

		bu_dot = Dot(np.array([3,0,0]),color=BLUE,radius=0.15)

		bu_label = TexMobject(
			"\\mathbf{b}^t"
			).scale(0.8)
		bu_label.set_color(BLUE)
		bu_label.next_to(bu_dot,RIGHT)

		b_label = TexMobject(
			"\\mathbf{b}^t"
			).scale(0.8)
		b_label.set_color(RED)
		b_label.next_to(b_dot,RIGHT)

		self.play(
			FadeIn(b_dot),
			FadeIn(bu_dot)
			)
		self.add_foreground_mobjects(b_dot)
		self.play(
			Write(b_label),
			Write(bu_label)
			)
		self.add_foreground_mobjects(b_label)
		self.wait(2)

		finder_circ = Dot(b_dot.get_center(),color=YELLOW,radius=1.1)
		finder_circ.fade(0.9)

		dest_circ = Dot(y_vec-x_vec,color=GREEN,radius=0.15)

		dest_label = TexMobject("\\mathbf{s}").set_color(GREEN).scale(0.8).next_to(dest_circ,DOWN+LEFT,buff=0.1)

		
		self.play(
			GrowFromPoint(finder_circ,b_dot.get_center()),
			lag_ratio = 0.3,
			run_time = 3
			)
		self.play(
			FadeIn(dest_circ),
			Write(dest_label)
			)
		self.wait(2)

		grid_markers_VG = VGroup(
			grid,
			finder_circ,
			L_radii_VG,
			lattice_dots_VG,
			b_dot,
			b_label,
			bu_label,
			bu_dot,
			dest_label,
			dest_circ,
			origin_label)
		
		


		dialogue_rect_A = RoundedRectangle(height=1.5,width=6.5,fill_opacity=1,color=BLUE,fill_color=BLACK)
		dialogue_rect_A.to_corner(UL)

		def_label_A = TexMobject(
			"\\text{Search: }",
			"\\text{BDD}(",
			"\\mathbf{b}^t",
			")",
			"\\text{ on }",
			"\\mathcal{L}(A)"
			)
		def_label_A[0].set_color(BLUE)
		def_label_A[2].set_color(RED)
		def_label_A.move_to(dialogue_rect_A.get_center())
		dialogue_box_A = VGroup(dialogue_rect_A,def_label_A)

		dialogue_rect_B = RoundedRectangle(height=1.5,width=5,fill_opacity=1,color=RED,fill_color=BLACK)
		dialogue_rect_B.to_corner(UR)

		def_label_B = TexMobject(
			"\\text{Decision: }",
			"\\mathbf{b}^t",
			"\\text{ vs }",
			"\\mathbf{b}^t"
			)
		def_label_B[0].set_color(RED)
		def_label_B[1].set_color(RED)
		def_label_B[-1].set_color(BLUE)
		def_label_B.move_to(dialogue_rect_B.get_center())
		dialogue_box_B = VGroup(dialogue_rect_B,def_label_B)

		def_labels_VG = VGroup(dialogue_box_A,dialogue_box_B)


		self.play(
			FadeOutAndShift(dialogue_box_dual,DOWN),
			Transform(grid_markers_VG,grid_markers_VG.copy().shift(1.5*DOWN))
			)
		self.play(
			FadeIn(def_labels_VG,UP)
			)
		self.wait(3)

