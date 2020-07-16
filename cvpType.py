#!/usr/bin/env python

from manimlib.imports import *

grid_shift = 4*LEFT + 0.5*DOWN
b1h = np.array([5,0,0])
b2h = np.array([3,1,0])

class cvpType(Scene):
	def construct(self):

		grid = NumberPlane(faded_line_ratio=0,
						x_min = -20,
						x_max = 20,
						y_min = -20,
						y_max =20
						)
		grid.set_color(GREEN).fade(0.75)
		grid.get_axes().set_width(1).fade(0.9)
		grid.shift(grid_shift)


		origin_dot = Dot(ORIGIN,radius=0.1,color=GREEN).shift(grid_shift)
		origin_label = TexMobject("O").scale(0.75).set_color(GREEN)
		origin_label.next_to(origin_dot,DOWN+LEFT,buff=0.1)

		

		b1h_arrow = Arrow().put_start_and_end_on(ORIGIN,np.array([4.95,0,0])).shift(grid_shift)
		b1h_arrow.set_color(YELLOW)
		b1h_label = TexMobject("b_1")
		b1h_label.next_to(b1h,DOWN,buff=0.2).scale(0.75).set_color(YELLOW).shift(grid_shift)

		b2h_arrow = Arrow().put_start_and_end_on(ORIGIN,np.array([2.95,0.95,0])).shift(grid_shift)
		b2h_arrow.set_color(YELLOW)
		b2h_label = TexMobject("b_2")
		b2h_label.next_to(b2h,UP+LEFT,buff=0.1).scale(0.75).set_color(YELLOW).shift(grid_shift)

		L_dots  = []
		for i in range(-8,9):
			for j in range(-5,6):
				L_dots.append(Dot(i*b1h + j*b2h,radius=0.08).fade(0.4).set_color(YELLOW))

		L_dots_VG = VGroup(*L_dots).shift(grid_shift)

		self.play(
			ShowCreation(grid),
			FadeIn(origin_dot),
			Write(origin_label),
			lag_ratio=0.5,
			run_time=2
			)
		self.wait(1)

		self.play(
			ShowCreation(b1h_arrow),
			ShowCreation(b2h_arrow),
			lag_ratio=0.5,
			run_time=2
			)
		self.play(
			Write(b1h_label),
			Write(b2h_label)
			)
		self.wait(1)

		self.play(
			FadeIn(L_dots_VG)
			)
		self.play(
			Transform(b1h_arrow,b1h_arrow.copy().fade(0.85)),
			Transform(b1h_label,b1h_label.copy().fade(0.4)),
			Transform(b2h_arrow, b2h_arrow.copy().fade(0.85)),
			Transform(b2h_label, b2h_label.copy().fade(0.45)),
			Transform(origin_dot,origin_dot.copy().fade(0.45)),
			Transform(origin_label,origin_label.copy().fade(0.45))
			)
		self.wait(1)

		V_pt = Dot((3*b2h) + (-1*b1h) + np.array([-1,0,0]), color = GREEN, radius=0.16 ).shift(grid_shift)

		V_pt_label = TexMobject("\\mathbf{p} \\in \\mathcal{V}").set_color(GREEN).scale(0.8)
		V_pt_label.next_to(V_pt,UP,buff=0.1)
		V_pt_label_B = TexMobject("\\mathbf{p}").set_color(GREEN).scale(0.8)
		V_pt_label_B.next_to(V_pt,DOWN+LEFT,buff=0)

		cvp_pt = Dot((3*b2h) + (-1*b1h), color = RED, radius=0.16 ).shift(grid_shift)

		self.play(
			FadeIn(V_pt)
			)
		self.play(
			Write(V_pt_label)
			)
		self.wait(2)
		self.play(
			FadeOut(V_pt_label)
			)
		self.wait()

		finder_circ = Circle(arc_center = V_pt.get_center()).set_color(RED)

		self.play(
			GrowFromPoint(finder_circ,V_pt.get_center()),
			lag_ratio=0.3,
			run_time=3
			)
		self.play(
			FadeIn(cvp_pt),
			FadeIn(V_pt_label_B)
			)
		self.wait(1)

		pathList = [
					Arrow().put_start_and_end_on(i*b2h, i*b2h + np.array([2.95,0.95,0])).shift(grid_shift).set_color(RED)
					for i in range(0,3)
					]
		pathList.append(
						Arrow().put_start_and_end_on(3*b2h, 3*b2h + np.array([-4.95,0,0])).shift(grid_shift).set_color(RED)
						)

		pathList_VG = VGroup(*pathList)

		dest_label = TexMobject("3 b_1 - b_2","\\in","\\mathcal{L}").scale(1).next_to(cvp_pt,UP+RIGHT,buff=0)
		dest_label[0].set_color(RED)
		dest_label[2].set_color(YELLOW)

		self.play(
			ShowCreation(pathList_VG),
			lag_ratio=0.3,
			run_time=3
			)
		self.play(
			FadeOut(finder_circ)
			)
		self.play(
			FadeInFromDown(dest_label),
			lag_ratio=0.5,
			run_time=2
			)
		self.play(
			FadeOut(pathList_VG)
			)
		self.wait(2)

		dialogue_rect = RoundedRectangle(height=2.5,width=12,fill_opacity=1,fill_color=BLACK)
		dialogue_rect.to_corner(DOWN)

		def_label_A = TextMobject("Closest Vector Problem (CVP)").set_color(RED)
		def_label_A.move_to(dialogue_rect.get_center() + 0.5*UP)

		def_label_B = TexMobject(
			"\\text{CVP}_\\mathcal{L}",
			"(",
			"p",
			")",
			"= \\gamma \\in ",
			"\\mathcal{L}, \\quad",
			"||\\gamma|| = \\text{min}\\lbrace ||x - p|| : x \\in \\mathcal{L} \\rbrace "
			)
		def_label_B.move_to(dialogue_rect.get_center() + 0.5*DOWN)

		dialogue_box = VGroup(dialogue_rect,def_label_A,def_label_B)

		self.play(
			FadeInFrom(dialogue_box,DOWN),
			lag_ratio=0.5,
			run_time=2
			)
		self.wait(3)
		self.play(
			FadeOutAndShift(dialogue_box,DOWN),
			)
		self.play(
			FadeOut(cvp_pt),
			FadeOut(dest_label),
			FadeOut(V_pt),
			FadeOut(V_pt_label_B)
			)
		self.wait(1)



		


