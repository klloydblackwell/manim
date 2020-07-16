#!/usr/bin/env python

from manimlib.imports import *

grid_shift = 5*LEFT
label_scale = 0.8


class gramSchmidt(Scene):
	def construct(self):

		grid = NumberPlane(faded_line_ratio=0,
						x_min = -20,
						x_max = 20,
						y_min = -20,
						y_max =20
						)
		grid.shift(grid_shift)
		grid.set_color(GREEN).fade(0.75)
		grid.get_axes().set_width(1)

		self.play(
			ShowCreation(grid),
			lag_ratio = 0.5,
			run_time = 2
			)
		self.wait()

		b1 = Arrow().put_start_and_end_on(ORIGIN,np.array([3,2,0])).set_color(BLUE)
		b1.shift(grid_shift)

		b1_label = TexMobject("b_1").set_color(BLUE).scale(label_scale)
		b1_label.move_to(1.1*np.array([3,2,0])).shift(grid_shift)

		b2 = Arrow().put_start_and_end_on(ORIGIN,np.array([4,-2,0])).set_color(BLUE)
		b2.shift(grid_shift)

		b2_label = TexMobject("b_2").set_color(BLUE).scale(label_scale)
		b2_label.move_to(1.1*np.array([4,-2,0])).shift(grid_shift)

		self.play(
			ShowCreation(b1),
			ShowCreation(b2),
			lag_ratio = 0.5,
			run_time = 2
			)
		self.play(
			Write(b1_label),
			Write(b2_label)
			)
		self.wait()

		b1_fix = TexMobject("= \\overline{b_1}").set_color(RED).scale(label_scale)
		b1_fix.next_to(b1_label)

		b1_bar = TexMobject("\\overline{b_1}").set_color(RED).scale(label_scale)
		b1_bar.move_to(b1_label.get_center())

		self.play(
			FadeInFromDown(b1_fix),
			lag_ratio = 0.5,
			run_time = 2
			)
		self.wait()

		b1_label_VG = VGroup(b1_label,b1_fix)

		self.play(
			Transform(b1_label_VG,b1_bar),
			Transform(b1,b1.copy().set_color(RED))
			)
		self.wait()

		b1_bar_VG = VGroup(b1,b1_label_VG)

		proj = Arrow().put_start_and_end_on(ORIGIN,(8/13)*np.array([3,2,0]))
		proj.set_color(YELLOW)
		proj.shift(grid_shift)

		proj_label = TexMobject("\\text{Proj}_{\\overline{b_1}}(b_2)").scale(label_scale)
		proj_label.set_color(YELLOW)
		proj_label.next_to(proj,RIGHT,buff=0)

		proj_VG = VGroup(proj,proj_label)

		self.play(
			ReplacementTransform(b2.copy(),proj)
			)
		self.play(
			FadeInFromDown(proj_label),
			lag_ratio = 0.5,
			run_time = 2
			)
		self.wait()

		dialogue_rect = RoundedRectangle(height=2.5,width=6,fill_opacity=1,fill_color=BLACK)
		dialogue_rect.to_corner(RIGHT)

		def_label = TexMobject("\\text{Proj}_{b_i}(b_j) = \\frac{b_i \\cdot b_j}{b_i \\cdot b_i}b_i")
		def_label.set_color(YELLOW)
		def_label.move_to(dialogue_rect.get_center())

		self.play(
			FadeInFrom(dialogue_rect,direction=RIGHT),
			lag_ratio=0.5,
			run_time = 2
			)
		self.wait()
		self.play(
			ReplacementTransform(proj_label.copy(),def_label),
			lag_ratio=0.5,
			run_time = 2
			)
		self.wait(2)

		dialogue_VG = VGroup(dialogue_rect,def_label)

		self.play(
			FadeOutAndShift(dialogue_VG,direction=RIGHT)
			)
		self.wait()

		negProj = Arrow().put_start_and_end_on(ORIGIN,(-8/13)*np.array([3,2,0]))
		negProj.set_color(YELLOW)
		negProj.shift(grid_shift).shift(np.array([4,-2,0]))

		negProj_label = TexMobject("-\\text{Proj}_{\\overline{b_1}}(b_2)").scale(label_scale)
		negProj_label.set_color(YELLOW)
		negProj_label.next_to(negProj,RIGHT+0.7*DOWN,buff=-0.5)

		negProj_VG = VGroup(negProj,negProj_label)

		self.play(
			ReplacementTransform(proj_VG.copy(),negProj_VG)
			)
		self.play(
			Transform(proj_VG,proj_VG.copy().fade(0.6))
			)
		self.wait()

		b2b_vec = np.array([4,-2,0]) + (-8/13)*np.array([3,2,0])
		b2_bar = Arrow().put_start_and_end_on(ORIGIN,b2b_vec).set_color(RED)
		b2_bar.shift(grid_shift)

		b2_bar_label = TexMobject("\\overline{b_2}").set_color(RED).scale(label_scale)
		b2_bar_label.move_to(1.1*b2b_vec).shift(grid_shift).shift(0.4*LEFT)

		b2_bar_VG = VGroup(b2_bar,b2_bar_label)

		self.play(
			ShowCreation(b2_bar),
			lag_ratio = 0.5,
			run_time = 2
			)
		self.play(
			Write(b2_bar_label),
			Transform(negProj_VG,negProj_VG.copy().fade(0.6))
			)
		self.wait()

		dialogue_rect = RoundedRectangle(height=4.5,width=6,fill_opacity=1,fill_color=BLACK)
		dialogue_rect.to_corner(RIGHT)

		def_label = TexMobject("\\overline{b_j}", " =", " b_j", " -", " \\sum_{i=1}^{j-1} \\frac{b_i \\cdot b_j}{b_i \\cdot b_i}b_i")
		def_label[0].set_color(RED)
		def_label[2].set_color(BLUE)
		def_label[-1].set_color(YELLOW)
		def_label.move_to(dialogue_rect.get_center() + UP)

		def_label_alt = TexMobject("\\overline{b_i}", "\\cdot", "\\overline{b_j}", "=0 \\quad \\forall \\; i \\ne j")
		def_label_alt[0].set_color(RED)
		def_label_alt[2].set_color(RED)
		def_label_alt.move_to(dialogue_rect.get_center()+DOWN)

		self.play(
			FadeInFrom(dialogue_rect,direction=RIGHT),
			lag_ratio=0.5,
			run_time = 2
			)
		self.wait()
		self.play(
			ReplacementTransform(b2_bar_label.copy(),def_label),
			lag_ratio=0.5,
			run_time = 2
			)
		self.wait(3)
		self.play(
			FadeInFrom(def_label_alt,direction=UP)
			)
		self.wait(3)

		dialogue_VG = VGroup(dialogue_rect,def_label_alt,def_label)

		self.play(
			FadeOutAndShift(dialogue_VG,direction=RIGHT),
			FadeOut(proj_VG),
			FadeOut(negProj_VG),
			FadeOut(b2),
			FadeOut(b2_label),
			FadeOut(grid),
			FadeOut(b1_bar_VG),
			FadeOut(b2_bar_VG),
			lag_ratio = 0.75,
			run_time = 2
			)
		self.wait(2)