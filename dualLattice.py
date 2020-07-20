#!/usr/bin/env python

from manimlib.imports import *

grid_shift = np.array([0,0,0])

x_vec = np.array([5,0,0])

y_vec = np.array([3,2,0])

class dualLattice(Scene):
	def construct(self):

		OG_lattice = []
		for i in range(-10,10):
			for j in range(-10,10):
				OG_lattice.append(Dot(i*x_vec + j*y_vec,radius=0.1,color=GRAY))

		OG_lattice_VG = VGroup(*OG_lattice)

		# ORIGIN: label and dot
		origin_dot = Dot(ORIGIN,radius=0.1,color=GRAY).shift(grid_shift)
		origin_label = TexMobject("O").scale(0.6).set_color(GRAY)
		origin_label.next_to(origin_dot,DOWN+LEFT,buff=0.1).shift(0.1*RIGHT)

		origin_VG = VGroup(origin_dot,origin_label)
		origin_faded_VG = VGroup(origin_dot.copy().fade(0.75), origin_label.copy().fade(0.3))

		# First L basis x
		x_arrow = Arrow().put_start_and_end_on(ORIGIN,np.array([4.95,0,0])).shift(grid_shift)
		x_arrow.set_color(BLUE)
		x_label = TexMobject("\\mathbf{x}")
		x_label.next_to(x_vec,DOWN,buff=0.2).scale(0.75).set_color(BLUE).shift(grid_shift)

		# Second L basis y
		y_arrow = Arrow().put_start_and_end_on(ORIGIN,np.array([2.95,1.95,0])).shift(grid_shift)
		y_arrow.set_color(GREEN)
		y_label = TexMobject("\\mathbf{y}")
		y_label.next_to(y_vec,UP+LEFT,buff=0.1).scale(0.75).set_color(GREEN).shift(grid_shift)

		# x over norm squared
		xns_arrow = Arrow().put_start_and_end_on(ORIGIN, 0.3*np.array([4.95,0,0])).shift(grid_shift)
		xns_arrow.set_color(BLUE)
		xns_label = TexMobject("\\frac{\\mathbf{x}}{|| \\mathbf{x} ||^2}")
		xns_label.next_to(0.3*x_vec,DOWN,buff=0.2).scale(0.75).set_color(BLUE).shift(grid_shift)

		# x over norm squared gridder line
		xns_dots = [
			Dot(radius=0.1,color=BLUE).move_to(i*0.3*x_vec) for i in range(-20,20)
			]
		xns_line = Line().put_start_and_end_on(-20*x_vec,20*x_vec).set_color(BLUE)
		xnsGrid_VG = VGroup(*xns_dots,xns_line)

		# x over norm squared paragrid
		xns_pg_core = xns_line.copy().rotate(TAU/4).fade(0.5)
		xns_pg_VG = VGroup(*[xns_pg_core.copy().move_to(i*0.3*x_vec) for i in range(-20,20)])

		# y over norm squared
		yns_arrow = Arrow().put_start_and_end_on(ORIGIN,0.25*np.array([2.95,1.95,0])).shift(grid_shift)
		yns_arrow.set_color(GREEN)
		yns_label = TexMobject("\\frac{\\mathbf{y}}{|| \\mathbf{y} ||^2}")
		yns_label.next_to(0.25*y_vec,UP+LEFT,buff=0.1).scale(0.75).set_color(GREEN).shift(grid_shift)

		# y over norm squared gridder line
		yns_dots = [
			Dot(radius=0.1,color=GREEN).move_to(i*0.25*y_vec) for i in range(-20,20)
			]
		yns_line = Line().put_start_and_end_on(-20*y_vec,20*y_vec).set_color(GREEN)
		ynsGrid_VG = VGroup(*yns_dots,yns_line)

		# y over norm squared paragrid
		yns_pg_core = yns_line.copy().rotate(TAU/4).fade(0.5)
		yns_pg_VG = VGroup(*[yns_pg_core.copy().move_to(i*0.25*y_vec) for i in range(-20,20)])

		#dual lattice dots
		dual_dots_core = VGroup(*[ Dot(color=YELLOW,radius=0.1).move_to(i*0.25*y_vec) for i in range(-20,20,2)])
		dual_dots_VG = VGroup(*[dual_dots_core.copy().shift(i*np.array([0,1.625,0])) for i in range(-20,20)])



		# Fade in ORIGIN VG and put dot in foreground
		self.play(
			FadeIn(origin_VG),
			lag_ratio = 0.6,
			run_time = 2
			)
		self.wait()
		self.add_foreground_mobjects(origin_dot)

		# Draw original basis vectors
		self.play(
			ShowCreation(x_arrow),
			ShowCreation(y_arrow),
			lag_ratio = 0.3,
			run_time = 3
			)
		self.play(
			Write(x_label),
			Write(y_label)
			)
		self.wait(1)

		self.play(
			FadeIn(OG_lattice_VG)
			)
		self.wait(2)

		# Switch to norm squared vectors
		self.play(
			FadeOutAndShift(x_label),
			FadeOutAndShift(y_label),
			lag_ratio=0.6,
			run_time=2
			)
		self.play(
			FadeOut(OG_lattice_VG)
			)
		self.play(
			ReplacementTransform(x_arrow,xns_arrow),
			ReplacementTransform(y_arrow,yns_arrow),
			lag_ratio=0.6,
			run_time=2
			)
		self.play(
			Write(xns_label),
			Write(yns_label)
			)
		self.wait(2)

		# Switch to gridders
		self.play(
			FadeOut(xns_label),
			FadeOut(yns_label),
			FadeIn(xnsGrid_VG),
			FadeIn(ynsGrid_VG),
			lag_ratio = 0.3,
			run_time = 2
			)
		self.wait(2)
		self.play(
			FadeOut(xns_arrow),
			FadeOut(yns_arrow)
			)
		self.wait()

		# Create paragrids
		self.play(
			FadeIn(xns_pg_VG)
			)
		self.wait()
		self.play(
			FadeIn(yns_pg_VG)
			)
		self.wait(2)

		# Remove gridders
		self.play(
			FadeOut(xnsGrid_VG),
			FadeOut(ynsGrid_VG)
			)
		self.wait(2)
		self.remove_foreground_mobjects(origin_dot)

		self.play(
			FadeIn(dual_dots_VG)
			)
		self.wait(2)

		dialogue_rect = RoundedRectangle(height=1.6,width=8.5,fill_opacity=1,fill_color=BLACK)
		dialogue_rect.to_corner(DOWN)

		def_label_A = TextMobject("Dual Lattice")
		def_label_A.set_color(YELLOW)
		def_label_A.move_to(dialogue_rect.get_center() + 0.4*UP)

		def_label_B = TexMobject("\\mathcal{L}^{\\bot} = \\lbrace \\mathbf{v} \\in \\mathcal{V}: \\exists \\mathbf{x} \\in \\mathcal{L} \\ni \\langle \\mathbf{x},\\mathbf{v} \\rangle \\in \\mathbb{Z} \\rbrace ")
		def_label_B.set_color(YELLOW)
		def_label_B.move_to(dialogue_rect.get_center() + 0.4*DOWN)

		dialogue_box = VGroup(dialogue_rect,def_label_A,def_label_B)

		self.play(
			FadeInFromDown(dialogue_box)
			)
		self.wait(4)

		self.play(
			FadeOut(def_label_B),
			Transform(def_label_A,def_label_A.copy().move_to(dialogue_rect.get_center())),
			FadeOut(xns_pg_VG),
			FadeOut(yns_pg_VG)
			)
		self.wait(1)

		OG_lattice_label = TextMobject("Original Lattice").set_color(GRAY).move_to(dialogue_rect.get_center())

		def_label_A_copy = def_label_A.copy()
		dual_dots_VG_copy = dual_dots_VG.copy()

		self.play(
			Transform(def_label_A,OG_lattice_label),
			Transform(dual_dots_VG,OG_lattice_VG)
			)
		self.wait(3)

		self.play(
			Transform(def_label_A,def_label_A_copy),
			Transform(dual_dots_VG,dual_dots_VG_copy)
			)
		self.wait(3)







