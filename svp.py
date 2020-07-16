#!/usr/bin/env python

from manimlib.imports import *

grid_shift = 4*LEFT + 2*DOWN

b1h = np.array([4,0,0])

b2h = np.array([3,1.3,0])

class svp(Scene):
	def construct(self):

		Z2_dots  = []
		for i in range(-8,9):
			for j in range(-5,6):
				Z2_dots.append(Dot(i*b1h + j*b2h,radius=0.08).fade(0.4))

		Z2_dots_VG = VGroup(*Z2_dots).shift(grid_shift)

		origin_dot = Dot(ORIGIN,radius=0.1,color=BLUE).shift(grid_shift)
		origin_label = TexMobject("O").scale(0.75).set_color(BLUE)
		origin_label.next_to(origin_dot,DOWN,buff=0.1)

		

		b1h_arrow = Arrow().put_start_and_end_on(ORIGIN,np.array([3.95,0,0])).shift(grid_shift)
		b1h_arrow.set_color(BLUE)
		b1h_label = TexMobject("b_1")
		b1h_label.next_to(b1h,DOWN,buff=0.2).scale(0.75).set_color(BLUE).shift(grid_shift)

		b2h_arrow = Arrow().put_start_and_end_on(ORIGIN,np.array([2.95,1.25,0])).shift(grid_shift)
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
			ShowCreation(Z2_dots_VG),
			lag_ratio = 0.5,
			run_time = 2
			)
		self.wait(1)

		short_vec = Arrow().put_start_and_end_on(ORIGIN,b2h - b1h)
		short_vec.set_color(YELLOW).shift(grid_shift)

		short_vec_label = TexMobject("\\boldsymbol{\\gamma}").set_color(YELLOW)
		short_vec_label.next_to(b2h-b1h,UP,buff=0.2).shift(grid_shift).scale(1.2)

		self.play(
			ShowCreation(short_vec),
			lag_ratio = 0.5,
			run_time = 2
			)
		self.play(
			Write(short_vec_label)
			)
		self.wait(1)

		dialogue_rect = RoundedRectangle(height=2.5,width=6,fill_opacity=1,fill_color=BLACK)
		dialogue_rect.to_corner(UP)

		def_label_A = TextMobject("Shortest Vector").set_color(YELLOW)
		def_label_A.move_to(dialogue_rect.get_center() + 0.5*UP)

		def_label_B = TexMobject("\\boldsymbol{\\gamma}",  "= \\min \\lbrace \\; || x ||  \\; : \\; x \\in \\mathcal{L} \\; \\rbrace")
		def_label_B[0].set_color(YELLOW)
		def_label_B.move_to(dialogue_rect.get_center() + 0.5*DOWN)

		dialogue_box = VGroup(dialogue_rect,def_label_A,def_label_B)

		self.play(
			FadeInFrom(dialogue_box,UP),
			lag_ratio=0.5,
			run_time=2
			)
		self.wait(3)
		self.play(
			FadeOutAndShift(dialogue_box,UP),
			)
		self.play(
			FadeOut(short_vec),
			FadeOut(short_vec_label)
			)
		self.wait(1)

		x_vec = Arrow().put_start_and_end_on(ORIGIN,2*b1h).shift(grid_shift)
		x_vec.set_color(ORANGE)
		x_vec_label = TexMobject("x")
		x_vec_label.next_to(2*b1h,DOWN,buff=0.3).set_color(ORANGE).shift(grid_shift)

		y_vec = Arrow().put_start_and_end_on(ORIGIN,b1h+b2h).shift(grid_shift)
		y_vec.set_color(ORANGE)
		y_vec_label = TexMobject("y")
		y_vec_label.next_to(b1h+b2h,UP,buff=0.3).set_color(ORANGE).shift(grid_shift)

		dist = DashedLine(width=2).put_start_and_end_on(2*b1h,b1h+b2h).set_color(RED).shift(grid_shift)
		dist_label = TexMobject("\\lambda").set_color(RED).scale(1.2)
		dist_label.next_to(dist,RIGHT,buff=0)

		self.play(
			ShowCreation(x_vec),
			ShowCreation(y_vec),
			lag_ratio=0.5,
			run_time=2
			)
		self.play(
			Write(x_vec_label),
			Write(y_vec_label)
			)
		self.wait(1)

		self.play(
			ShowCreation(dist),
			lag_ratio=0.5,
			run_time=2
			)
		self.play(Write(dist_label))
		self.wait(1)	

		dialogue_rect = RoundedRectangle(height=2.5,width=8,fill_opacity=1,fill_color=BLACK)
		dialogue_rect.to_corner(UP)

		def_label_A = TextMobject("Minimum Distance").set_color(RED)
		def_label_A.move_to(dialogue_rect.get_center() + 0.5*UP)

		def_label_B = TexMobject("\\lambda}",  "= \\min \\lbrace \\; ||x - y||  \\; : \\; x,y \\in \\mathcal{L} \\; \\rbrace")
		def_label_B[0].set_color(RED)
		def_label_B.move_to(dialogue_rect.get_center() + 0.5*DOWN)

		dialogue_box = VGroup(dialogue_rect,def_label_A,def_label_B)

		self.play(
			FadeInFrom(dialogue_box,UP),
			lag_ratio=0.5,
			run_time=2
			)
		self.wait(3)
		self.play(
			FadeOutAndShift(dialogue_box,UP),
			)
		self.play(
			FadeOut(x_vec),
			FadeOut(x_vec_label),
			FadeOut(y_vec_label),
			FadeOut(y_vec),
			FadeOut(dist),
			FadeOut(dist_label)
			)
		self.wait(1)



