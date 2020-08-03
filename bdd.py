#!/usr/bin/env python

from manimlib.imports import *

grid_shift = 2.75*LEFT + 1.25*DOWN

b1h = np.array([4,0,0])

b2h = np.array([3,2.25,0])

class bdd(Scene):
	def construct(self):

		L_dots  = []
		L_radii = []
		L_radii_r = []
		for i in range(-8,9):
			for j in range(-5,6):
				loc = i*b1h + j*b2h
				L_dots.append(Dot(loc,radius=0.1,color=BLUE).fade(0.4))
				L_radii.append(Dot(loc,radius=1.2,color=GRAY).fade(0.75))
				L_radii_r.append(DashedLine(loc,loc+np.array([-0.5,1.06,0])).set_color(RED))


		radii_core = Dot(ORIGIN,radius=1.2,color=GRAY).fade(0.75)
		radii_r_core = DashedLine(ORIGIN,ORIGIN+np.array([-0.5,1.06,0])).set_color(RED)


		L_dots_VG = VGroup(*L_dots).shift(grid_shift)
		L_radii_VG = VGroup(*L_radii).shift(grid_shift)
		L_radii_r_VG = VGroup(*L_radii_r).shift(grid_shift)

		origin_dot = Dot(ORIGIN,radius=0.1,color=BLUE).shift(grid_shift)
		origin_label = TexMobject("O").scale(0.75).set_color(BLUE)
		origin_label.next_to(origin_dot,DOWN,buff=0.1)

		radii_label = TexMobject("r").set_color(RED).next_to(radii_r_core,RIGHT,buff=0)
		radii_template_VG = VGroup(radii_core.copy(),radii_r_core.copy(),Dot(ORIGIN,radius=0.1,color=BLUE),radii_label)
		

		b1h_arrow = Arrow().put_start_and_end_on(ORIGIN,np.array([3.95,0,0])).shift(grid_shift)
		b1h_arrow.set_color(BLUE)
		b1h_label = TexMobject("b_1")
		b1h_label.next_to(b1h,DOWN,buff=0.2).scale(0.75).set_color(BLUE).shift(grid_shift)

		b2h_arrow = Arrow().put_start_and_end_on(ORIGIN,np.array([2.95,2.20,0])).shift(grid_shift)
		b2h_arrow.set_color(BLUE)
		b2h_label = TexMobject("b_2")
		b2h_label.next_to(b2h,UP+LEFT,buff=0.1).scale(0.75).set_color(BLUE).shift(grid_shift)


		self.play(
			FadeIn(origin_dot),
			Write(origin_label)
			)
		self.play(
			ShowCreation(b1h_arrow),
			Write(b1h_label),
			ShowCreation(b2h_arrow),
			Write(b2h_label),
			lag_ratio = 0.5,
			run_time = 2
			)
		self.wait(1)

		

		grid = NumberPlane(faded_line_ratio=0,
						x_min = -20,
						x_max = 20,
						y_min = -20,
						y_max =20
						)
		grid.set_color(BLUE).fade(0.75)
		grid.get_axes().set_width(1).fade(0.9)

		grid.prepare_for_nonlinear_transform()
		grid.apply_function(lambda p: p[0]*b1h + p[1]*b2h)
		grid.shift(grid_shift)

		self.play(
			Transform(b1h_arrow,b1h_arrow.copy().fade(1)),
			Transform(b1h_label,b1h_label.copy().fade(1)),
			Transform(b2h_arrow, b2h_arrow.copy().fade(1)),
			Transform(b2h_label, b2h_label.copy().fade(1)),
			Transform(origin_dot,origin_dot.copy().fade(0.75)),
			Transform(origin_dot,origin_dot.copy().fade(0.75)),
			Transform(origin_label,origin_label.copy().fade(0.2)),
			FadeIn(grid)
			)
		self.play(
			FadeIn(L_dots_VG)
			)
		
		self.wait(2)

		self.play(
			FadeIn(L_radii_VG)
			)
		self.wait(2)

		self.play(
			FadeIn(L_radii_r_VG)
			)
		self.wait(2)

		dialogue_rect = RoundedRectangle(height=3,width=7,fill_opacity=1,fill_color=BLACK)
		dialogue_rect.to_corner(UP)

		radii_template_VG.move_to(dialogue_rect.get_center() + 1.75*LEFT)

		def_label_A = TexMobject("r < \\lambda_1 (\\mathcal{L}) / 2").set_color(RED)
		def_label_A.move_to(dialogue_rect.get_center()+1.55*RIGHT)

		dialogue_box = VGroup(dialogue_rect,def_label_A,radii_template_VG)

		self.play(
			FadeInFrom(dialogue_box,UP),
			lag_ratio=0.5,
			run_time=2
			)
		self.wait(3)
		self.play(
			FadeOutAndShift(dialogue_box,UP),
			)

		self.add_foreground_mobjects(L_dots_VG)

		self.play(
			FadeOutAndShift(L_radii_r_VG),
			Transform(L_radii_VG,L_radii_VG.copy().fade(0.7))
			)
		self.wait(2)

		corr_dot_1 = Dot(1*b1h + np.array([0.3,-0.7,0]), radius=0.2, color=RED).shift(grid_shift)
		corr_dot_r_1 = radii_core.copy().set_color(YELLOW).move_to(corr_dot_1.get_center())
		corr_dot_1_tgt = Dot(1*b1h, radius=0.15, color=RED).shift(grid_shift)

		self.play(
			FadeIn(corr_dot_1)
			)
		self.play(
			FadeIn(corr_dot_r_1)
			)
#		self.play(
#			Transform(L_radii[104],L_radii[104].copy().set_color(YELLOW))
#			)
		self.wait(2)

		self.play(
			Transform(corr_dot_1,corr_dot_1_tgt)
			)
		self.wait(2)
		self.play(
			FadeOut(corr_dot_r_1)
			)
		self.wait(2)

		corr_dot_2 = Dot(-1*b1h + 1*b2h + np.array([0.3,0.7,0]), radius=0.2, color=RED).shift(grid_shift)
		corr_dot_r_2 = radii_core.copy().set_color(YELLOW).move_to(corr_dot_2.get_center())
		corr_dot_2_tgt = Dot(-1*b1h + 1*b2h, radius=0.15, color=RED).shift(grid_shift)

		self.play(
			FadeIn(corr_dot_2)
			)
		self.play(
			FadeIn(corr_dot_r_2)
			)
#		self.play(
#			Transform(L_radii[83],L_radii[83].copy().set_color(YELLOW))
#			)
		self.wait(2)

		self.play(
			Transform(corr_dot_2,corr_dot_2_tgt)
			)
		self.wait(2)
		self.play(
			FadeOut(corr_dot_r_2)
			)
		self.wait(2)


