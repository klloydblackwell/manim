#!/usr/bin/env python

from manimlib.imports import *

class vortexSurfer(Scene):
	def construct(self):

		vortex_pts = []
		vortex_pos = []
		vortex_labels = []

		for k in range(0,12):
			dot_pos = np.array([3*np.cos(k*(np.pi/6)),3*np.sin(k*(np.pi/6)),0])
			dot = Dot(radius=0.1).move_to(dot_pos)
			label_str = "E_{" + str(k+1) + "}"
			dot_label = TexMobject(label_str).move_to(1.15*dot_pos).scale(0.8)
			vortex_pts.append(dot)
			vortex_pos.append(dot_pos)
			vortex_labels.append(dot_label)

		vortex_pts_VG = VGroup(*vortex_pts).shift(2*LEFT)
		vortex_labels_VG = VGroup(*vortex_labels).shift(2*LEFT)
		self.play(
			ShowCreation(vortex_pts_VG),
			Write(vortex_labels_VG)
			)
		self.wait()

		deg2_line = Line().put_start_and_end_on(np.array([0,0,0]),np.array([1,0,0])).set_color(BLUE)
		deg2_text = TextMobject("degree 2").set_color(BLUE).move_to(deg2_line.get_center()+1.5*RIGHT)
		deg2_label = VGroup(deg2_line,deg2_text).shift(2.5*RIGHT + 1*UP)

		deg3_line = Line().put_start_and_end_on(np.array([0,0,0]),np.array([1,0,0])).set_color(RED)
		deg3_text = TextMobject("degree 3").set_color(RED).move_to(deg3_line.get_center()+1.5*RIGHT)
		deg3_label = VGroup(deg3_line,deg3_text).shift(2.5*RIGHT)

		deg5_line = Line().put_start_and_end_on(np.array([0,0,0]),np.array([1,0,0])).set_color(GREEN)
		deg5_text = TextMobject("degree 5").set_color(GREEN).move_to(deg5_line.get_center()+1.5*RIGHT)
		deg5_label = VGroup(deg5_line,deg5_text).shift(2.5*RIGHT + 1*DOWN)

		self.play(
			Write(deg2_label)
			)
		self.wait()


		deg2_arcs = []
		for k in range(0,12):
			deg2_arcs.append(ArcBetweenPoints(vortex_pos[k], vortex_pos[(k+1) % 12],angle=TAU/(3.6)).set_color(BLUE))

		deg2_arcs_VG = VGroup(*deg2_arcs).shift(2*LEFT)
		self.bring_to_back(deg2_arcs_VG)

		self.play(
			ShowCreation(deg2_arcs_VG)
			)
		self.wait()

		self.play(
			Write(deg3_label)
			)
		self.wait()

		deg3_arcs = []
		for k in range(0,12):
			deg3_arcs.append(ArcBetweenPoints(vortex_pos[k], vortex_pos[(k+4) % 12],angle=TAU/(6)).set_color(RED))

		deg3_arcs_VG = VGroup(*deg3_arcs).shift(2*LEFT)
		self.bring_to_back(deg3_arcs_VG)

		self.play(
			ShowCreation(deg3_arcs_VG)
			)
		self.wait()

		self.play(
			Write(deg5_label)
			)
		self.wait()

		deg5_arcs = []
		for k in range(0,12):
			deg5_arcs.append(ArcBetweenPoints(vortex_pos[11-k], vortex_pos[(11-k-3) % 12],angle=TAU/(4)).set_color(GREEN))

		deg5_arcs_VG = VGroup(*deg5_arcs).shift(2*LEFT)
		self.bring_to_back(deg5_arcs_VG)

		self.play(
			ShowCreation(deg5_arcs_VG)
			)
		self.wait(2)

		self.play(
			FadeOut(deg2_arcs_VG),
			FadeOut(deg3_arcs_VG),
			FadeOut(deg5_arcs_VG),
			FadeOut(vortex_labels_VG),
			FadeOut(vortex_pts_VG),
			FadeOut(deg2_label),
			FadeOut(deg3_label),
			FadeOut(deg5_label)
			)
		self.wait()




