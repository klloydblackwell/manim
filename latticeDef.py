#!/usr/bin/env python

from manimlib.imports import *


def segPath(d1, d2, b1, b2, b1_label, b2_label,baseColor):

	destination_dot = Dot(d1*b1 + d2*b2,radius=0.1)

	coeff_x, coeff_y = d1, d2

	if d1 < 0:
		b1 = -1*b1
		coeff_x = "({0})".format(d1)

	if d2 < 0:
		b2 = -1*b2
		coeff_y = "({0})".format(str(d2))

	

	destination_label = TexMobject("{0}{1} + {2}{3}".format(coeff_x,b1_label,coeff_y,b2_label)).scale(0.6)

	if d2 >= 0:
		destination_label.next_to(destination_dot,UP,buff=0.1)
	else:
		destination_label.next_to(destination_dot,DOWN,buff=0.1)

	b1_veclist = [Arrow().put_start_and_end_on(ORIGIN + h*b1,ORIGIN + (h+0.95)*b1).set_color(baseColor)
					for h in range(0,np.abs(d1))]

	b1_veclist_label = TexMobject("{0}{1}".format(d1,b1_label))

	b2_veclist = [Arrow().put_start_and_end_on(np.abs(d1)*b1 + h*b2,np.abs(d1)*b1 + (h+0.95)*b2).set_color(baseColor)
					for h in range(0,np.abs(d2))]

	b2_veclist_label = TexMobject("{0}{1}".format(d2,b2_label))

	return [VGroup(*b1_veclist,*b2_veclist),b1_veclist_label,b2_veclist_label,destination_dot, destination_label]




class latticeDef(Scene):
	def construct(self):

		origin_dot = Dot(ORIGIN,radius=0.1,color=GREEN)

		b1 = np.array([1,0,0])

		b2 = np.array([0,1,0])

		b1_arrow = Arrow().put_start_and_end_on(ORIGIN,np.array([0.95,0,0]))
		b1_arrow.set_color(GREEN)
		b1_label = TexMobject("b_1").set_color(GREEN)
		b1_label.next_to(b1_arrow,DOWN,buff=0).scale(0.75)

		b2_arrow = Arrow().put_start_and_end_on(ORIGIN,np.array([0,0.95,0]))
		b2_arrow.set_color(GREEN)
		b2_label = TexMobject("b_2").set_color(GREEN)
		b2_label.next_to(b2_arrow,LEFT,buff=0).scale(0.75)


		self.play(
			FadeIn(origin_dot)
			)
		self.play(
			ShowCreation(b1_arrow),
			Write(b1_label)
			)
		self.play(
			ShowCreation(b2_arrow),
			Write(b2_label)
			)
		self.wait(1)

		self.play(
			Transform(b1_arrow,b1_arrow.copy().fade(0.75)),
			Transform(b1_label,b1_label.copy().fade(0.3)),
			Transform(b2_arrow, b2_arrow.copy().fade(0.75)),
			Transform(b2_label, b2_label.copy().fade(0.3)),
			Transform(origin_dot,origin_dot.copy().fade(0.75))
			)
		self.wait(1)

		B1_3_2 = segPath(3, 2, b1, b2, "b_1", "b_2",GREEN)

		self.play(
			ShowCreation(B1_3_2[0]),
			lag_ratio = 0.2,
			run_time = 2
			)
		self.play(
			FadeIn(B1_3_2[-2]),
			Write(B1_3_2[-1])
			)
		self.wait()

		self.play(
			FadeOut(B1_3_2[0])
			)
		self.wait()

		B1_n1_3 = segPath(-1, 3, b1, b2, "b_1", "b_2",GREEN)

		self.play(
			ShowCreation(B1_n1_3[0]),
			lag_ratio = 0.2,
			run_time = 2
			)
		self.play(
			FadeIn(B1_n1_3[-2]),
			Write(B1_n1_3[-1])
			)
		self.wait()

		self.play(
			FadeOut(B1_n1_3[0])
			)
		self.wait()

		B1_n5_n1 = segPath(-5, -1, b1, b2, "b_1", "b_2",GREEN)

		self.play(
			ShowCreation(B1_n5_n1[0]),
			lag_ratio = 0.2,
			run_time = 2
			)
		self.play(
			FadeIn(B1_n5_n1[-2]),
			Write(B1_n5_n1[-1])
			)
		self.wait()

		self.play(
			FadeOut(B1_n5_n1[0])
			)
		self.wait()

		B1_4_n2 = segPath(4, -2, b1, b2, "b_1", "b_2",GREEN)

		self.play(
			ShowCreation(B1_4_n2[0]),
			lag_ratio = 0.2,
			run_time = 2
			)
		self.play(
			FadeIn(B1_4_n2[-2]),
			Write(B1_4_n2[-1])
			)
		self.wait()

		self.play(
			FadeOut(B1_4_n2[0])
			)
		self.wait()

		grid = NumberPlane(faded_line_ratio=0,
						x_min = -20,
						x_max = 20,
						y_min = -20,
						y_max =20
						)
		grid.set_color(GREEN).fade(0.75)
		grid.get_axes().set_width(1).fade(0.9)

		Z2_dots  = []
		for i in range(-8,9):
			for j in range(-5,6):
				Z2_dots.append(Dot(np.array([i,j,0]),radius=0.05).fade(0.5))

		Z2_dots_VG = VGroup(*Z2_dots)
		
		self.play(
			FadeOut(B1_3_2[-2]),
			FadeOut(B1_3_2[-1]),
			FadeOut(B1_n1_3[-2]),
			FadeOut(B1_n1_3[-1]),
			FadeOut(B1_n5_n1[-2]),
			FadeOut(B1_n5_n1[-1]),
			FadeOut(B1_4_n2[-2]),
			FadeOut(B1_4_n2[-1]),
			Write(grid),
			lag_ratio=0.4,
			run_time=3
			)
		self.play(
			FadeIn(Z2_dots_VG)
			)
		self.wait()

		dialogue_rect = Rectangle(height=2,width=6,fill_opacity=1,fill_color=BLACK)
		dialogue_rect.to_corner(DOWN+LEFT)

		def_label = TexMobject("\\mathcal{L} = \\sum_{i=1}^m (\\mathbb{Z} \\cdot", "b_i", ")")
		def_label[-2].set_color(GREEN)
		def_label.move_to(dialogue_rect.get_center())

		dialogue_box = VGroup(dialogue_rect,def_label)

		self.play(
			FadeInFromDown(dialogue_box)
			)
		self.wait(2)

		self.play(
			FadeOutAndShift(dialogue_box)
			)
		self.wait()

		b1h = np.array([2,1,0])

		b2h = np.array([1,1,0])

		b1h_arrow = Arrow().put_start_and_end_on(ORIGIN,np.array([1.95,0.95,0]))
		b1h_arrow.set_color(ORANGE)
		b1h_label = TexMobject("\\hat{b_1}")
		b1h_label.next_to(np.array([2,1,0]),RIGHT,buff=0).scale(0.75).set_color(ORANGE)

		b2h_arrow = Arrow().put_start_and_end_on(ORIGIN,np.array([0.95,0.95,0]))
		b2h_arrow.set_color(ORANGE)
		b2h_label = TexMobject("\\hat{b_2}")
		b2h_label.next_to(np.array([1,1,0]),UP,buff=0).scale(0.75).set_color(ORANGE)


		
		self.play(
			ShowCreation(b1h_arrow),
			Write(b1h_label)
			)
		self.play(
			ShowCreation(b2h_arrow),
			Write(b2h_label)
			)
		self.wait(1)

		self.play(
			Transform(b1h_arrow,b1h_arrow.copy().fade(0.75)),
			Transform(b1h_label,b1h_label.copy().fade(0.3)),
			Transform(b2h_arrow, b2h_arrow.copy().fade(0.75)),
			Transform(b2h_label, b2h_label.copy().fade(0.3)),
			Transform(origin_dot,origin_dot.copy().fade(0.75))
			)
		self.wait(1)

		B1h_1_2 = segPath(1, 2, b1h, b2h, "\\hat{b_1}", "\\hat{b_2}",ORANGE)

		self.play(
			ShowCreation(B1h_1_2[0]),
			lag_ratio = 0.2,
			run_time = 2
			)
		self.play(
			FadeIn(B1h_1_2[-2]),
			Write(B1h_1_2[-1])
			)
		self.wait()

		self.play(
			FadeOut(B1h_1_2[0])
			)
		self.wait()

		B1h_n2_n1 = segPath(-2, -1, b1h, b2h, "\\hat{b_1}", "\\hat{b_2}",ORANGE)

		self.play(
			ShowCreation(B1h_n2_n1[0]),
			lag_ratio = 0.2,
			run_time = 2
			)
		self.play(
			FadeIn(B1h_n2_n1[-2]),
			Write(B1h_n2_n1[-1])
			)
		self.wait()

		self.play(
			FadeOut(B1h_n2_n1[0])
			)
		self.wait()

		B1h_3_n6 = segPath(3, -6, b1h, b2h, "\\hat{b_1}", "\\hat{b_2}",ORANGE)

		self.play(
			ShowCreation(B1h_3_n6[0]),
			lag_ratio = 0.2,
			run_time = 2
			)
		self.play(
			FadeIn(B1h_3_n6[-2]),
			Write(B1h_3_n6[-1])
			)
		self.wait()

		self.play(
			FadeOut(B1h_3_n6[0])
			)
		self.wait()


		B1h_n3_5 = segPath(-3, 5, b1h, b2h, "\\hat{b_1}", "\\hat{b_2}",ORANGE)

		self.play(
			ShowCreation(B1h_n3_5[0]),
			lag_ratio = 0.2,
			run_time = 2
			)
		self.play(
			FadeIn(B1h_n3_5[-2]),
			Write(B1h_n3_5[-1])
			)
		self.wait()

		self.play(
			FadeOut(B1h_n3_5[0])
			)
		self.wait()


		grid2 = NumberPlane(faded_line_ratio=0,
						x_min = -20,
						x_max = 20,
						y_min = -20,
						y_max =20
						)
		grid2.set_color(ORANGE).fade(0.75)
		grid2.get_axes().set_width(1).fade(0.9)

		grid2.prepare_for_nonlinear_transform()
		grid2.apply_function(lambda p: p[0]*np.array([2,1,0]) + p[1]*np.array([1,1,0]))


		self.play(
			FadeOut(B1h_1_2[-2]),
			FadeOut(B1h_1_2[-1]),
			FadeOut(B1h_n2_n1[-2]),
			FadeOut(B1h_n2_n1[-1]),
			FadeOut(B1h_3_n6[-2]),
			FadeOut(B1h_3_n6[-1]),
			FadeOut(B1h_n3_5[-2]),
			FadeOut(B1h_n3_5[-1]),
			Write(grid2),
			lag_ratio=0.4,
			run_time=3
			)
		self.wait()

		dialogue_rect = Rectangle(height=2,width=8,fill_opacity=1,fill_color=BLACK)
		dialogue_rect.to_corner(DOWN+LEFT)

		def_label = TexMobject("\\mathcal{L} = \\sum_{i=1}^m (\\mathbb{Z} \\cdot", "b_i", ") = \\sum_{i=1}^m (\\mathbb{Z} \\cdot", "\\hat{b_i}", ")")
		def_label[1].set_color(GREEN)
		def_label[-2].set_color(ORANGE)
		def_label.move_to(dialogue_rect.get_center())

		dialogue_box = VGroup(dialogue_rect,def_label)

		self.play(
			FadeInFromDown(dialogue_box)
			)
		self.wait(2)

		self.play(
			FadeOutAndShift(dialogue_box)
			)
		self.wait()



class fundPPed(Scene):
	def construct(self):

		Z2_dots  = []
		for i in range(-8,9):
			for j in range(-5,6):
				Z2_dots.append(Dot(np.array([i,j,0]),radius=0.05).fade(0.5))

		Z2_dots_VG = VGroup(*Z2_dots)

		origin_dot = Dot(ORIGIN,radius=0.1,color=ORANGE)
		origin_label = TexMobject("\\mathcal{O}").scale(0.75).set_color(ORANGE)
		origin_label.next_to(origin_dot,DOWN+LEFT,buff=0)

		b1h = np.array([2,0,0])

		b2h = np.array([1,1,0])

		b1h_arrow = Arrow().put_start_and_end_on(ORIGIN,np.array([1.95,0,0]))
		b1h_arrow.set_color(ORANGE)
		b1h_label = TexMobject("b_1")
		b1h_label.next_to(np.array([2,0,0]),DOWN).scale(0.75).set_color(ORANGE)

		b2h_arrow = Arrow().put_start_and_end_on(ORIGIN,np.array([0.95,0.95,0]))
		b2h_arrow.set_color(ORANGE)
		b2h_label = TexMobject("b_2")
		b2h_label.next_to(np.array([1,1,0]),UP+LEFT,buff=0).scale(0.75).set_color(ORANGE)


		self.play(
			FadeIn(origin_dot),
			Write(origin_label)
			)
		self.play(
			ShowCreation(b1h_arrow),
			Write(b1h_label)
			)
		self.play(
			ShowCreation(b2h_arrow),
			Write(b2h_label)
			)
		self.wait(1)

		self.play(
			Transform(b1h_arrow,b1h_arrow.copy().fade(0.75)),
			Transform(b1h_label,b1h_label.copy().fade(0.3)),
			Transform(b2h_arrow, b2h_arrow.copy().fade(0.75)),
			Transform(b2h_label, b2h_label.copy().fade(0.3)),
			Transform(origin_dot,origin_dot.copy().fade(0.75)),
			Transform(origin_dot,origin_dot.copy().fade(0.75)),
			Transform(origin_label,origin_label.copy().fade(0.3))
			)
		self.wait(1)

		B1h_1_1 = segPath(1, 1, b1h, b2h, "b_1", "b_2",ORANGE)

		self.play(
			ShowCreation(B1h_1_1[0]),
			lag_ratio = 0.2,
			run_time = 2
			)
		self.play(
			FadeIn(B1h_1_1[-2]),
			Write(B1h_1_1[-1])
			)
		self.wait()

		self.play(
			FadeOut(B1h_1_1[0])
			)
		self.wait()

		vertices = [ORIGIN,b1h,b1h+b2h,b2h]
		shaded = Polygon(*vertices,color=YELLOW,fill_color=YELLOW,fill_opacity=1).fade(0.75)

		self.play(
			FadeIn(shaded)
			)
		self.wait()

		dialogue_rect = RoundedRectangle(height=2,width=12,fill_opacity=1,fill_color=BLACK,color=YELLOW)
		dialogue_rect.to_corner(DOWN)
		
		def_label = TexMobject("\\mathcal{P}",
			"(",
			"b_1",
			",\\ldots,",
			"b_n",
			")",
			"= \\bigg\\lbrace \\sum_{i=1}^n x_i",
			"b_i",
			"\\mid x_i \\in \\mathbb{R}, 0 \\leq x_i < 1 \\bigg\\rbrace"
			)
		def_label[0].set_color(YELLOW)
		def_label[1].set_color(YELLOW)
		def_label[5].set_color(YELLOW)
		def_label[2].set_color(ORANGE)
		def_label[4].set_color(ORANGE)
		def_label[-2].set_color(ORANGE)
		def_label.move_to(dialogue_rect.get_center())

		dialogue_box = VGroup(dialogue_rect,def_label)
		

		self.play(
			GrowFromPoint(dialogue_box,shaded.get_center()),
			lag_ratio=0.4,
			run_time=3
			)
		self.wait(2)
		self.add_foreground_mobjects(dialogue_box)

		grid = NumberPlane(faded_line_ratio=0,
						x_min = -20,
						x_max = 20,
						y_min = -20,
						y_max =20
						)
		grid.set_color(ORANGE).fade(0.75)
		grid.get_axes().set_width(1).fade(0.9)

		grid.prepare_for_nonlinear_transform()
		grid.apply_function(lambda p: p[0]*np.array([2,0,0]) + p[1]*np.array([1,1,0]))

		self.play(
			FadeOut(B1h_1_1[-2]),
			FadeOut(B1h_1_1[-1])
			)
		self.play(
			FadeIn(grid)
			)
		self.wait()
