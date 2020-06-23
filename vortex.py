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
		self.add_foreground_mobjects(vortex_pts_VG)

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
		for k in range(1,11):
			deg2_arcs.append(ArcBetweenPoints(vortex_pos[k], vortex_pos[(k+1) % 12],angle=TAU/(3.6)).set_color(BLUE))

		deg2_arcs_VG = VGroup(*deg2_arcs).shift(2*LEFT)
		

		fwd_2_arc = ArcBetweenPoints(vortex_pos[0], vortex_pos[1],angle=TAU/(3.6)).set_color(BLUE).shift(2*LEFT)
		fwd_2_label = TexMobject("\\mathfrak{p}").set_color(BLUE)
		fwd_2_label.next_to(fwd_2_arc,LEFT,buff=-0.1)
		
		inv_2_arc = ArcBetweenPoints(vortex_pos[0],vortex_pos[11], angle=-TAU/(3.6)).set_color(BLUE).shift(2*LEFT)
		inv_2_label = TexMobject("\\overline{\\mathfrak{p}}").set_color(BLUE)
		inv_2_label.next_to(inv_2_arc,LEFT,buff=-0.1)
		
		norm_2_label = TexMobject("\\text{N}(\\mathfrak{p}) = 2")
		norm_2_label.move_to(vortex_pts_VG.get_center())
		
		
		self.play(
			ShowCreation(fwd_2_arc)
			)
		self.play(
			Write(fwd_2_label)
			)
		self.play(
			Write(norm_2_label)
			)
		self.wait()
		
		self.play(
			ShowCreation(inv_2_arc)
			)
		self.play(
			Write(inv_2_label)
			)
		self.wait()
		
		self.play(
			ShowCreation(deg2_arcs_VG),
			FadeOut(fwd_2_label),
			FadeOut(inv_2_label),
			FadeOut(norm_2_label)
			)
		self.wait()
		
		deg2_arcs_VG = VGroup(deg2_arcs_VG,fwd_2_arc,inv_2_arc)
		
		


		self.play(
			Write(deg3_label)
			)
		self.wait()

		deg3_arcs = []
		for k in range(1,12):
			if k == 8:
				continue
			
			deg3_arcs.append(ArcBetweenPoints(vortex_pos[k], vortex_pos[(k+4) % 12],angle=TAU/(6)).set_color(RED))

		deg3_arcs_VG = VGroup(*deg3_arcs).shift(2*LEFT)


		fwd_3_arc = ArcBetweenPoints(vortex_pos[0], vortex_pos[4],angle=TAU/(6)).set_color(RED).shift(2*LEFT)
		fwd_3_label = TexMobject("\\mathfrak{p}").set_color(RED)
		fwd_3_label.next_to(fwd_3_arc,LEFT,buff=-2).shift(0.2*UP + 0.2*RIGHT)
		
		inv_3_arc = ArcBetweenPoints(vortex_pos[0],vortex_pos[8], angle=-TAU/(6)).set_color(RED).shift(2*LEFT)
		inv_3_label = TexMobject("\\overline{\\mathfrak{p}}").set_color(RED)
		inv_3_label.next_to(inv_3_arc,LEFT,buff=-2).shift(0.2*DOWN + 0.2*RIGHT)
		
		norm_3_label = TexMobject("\\text{N}(\\mathfrak{p}) = 3")
		norm_3_label.move_to(vortex_pts_VG.get_center())
		
		
		self.play(
			ShowCreation(fwd_3_arc)
			)
		self.play(
			Write(fwd_3_label)
			)
		self.play(
			Write(norm_3_label)
			)
		self.wait()
		
		self.play(
			ShowCreation(inv_3_arc)
			)
		self.play(
			Write(inv_3_label)
			)
		self.wait()
		
		self.play(
			ShowCreation(deg3_arcs_VG),
			FadeOut(fwd_3_label),
			FadeOut(inv_3_label),
			FadeOut(norm_3_label)
			)
		self.wait()
		
		deg3_arcs_VG = VGroup(deg3_arcs_VG,fwd_3_arc,inv_3_arc)







		self.play(
			Write(deg5_label)
			)
		self.wait()

		deg5_arcs = []
		for k in range(0,12):
			if k == 11 or k == 8:
				continue
			
			deg5_arcs.append(ArcBetweenPoints(vortex_pos[11-k], vortex_pos[(11-k-3) % 12],angle=TAU/(4)).set_color(GREEN))

		deg5_arcs_VG = VGroup(*deg5_arcs).shift(2*LEFT)


		fwd_5_arc = ArcBetweenPoints(vortex_pos[0], vortex_pos[3],angle= -TAU/(4)).set_color(GREEN).shift(2*LEFT)
		fwd_5_label = TexMobject("\\mathfrak{p}").set_color(GREEN)
		fwd_5_label.next_to(fwd_5_arc,LEFT,buff=-0.1)
		
		inv_5_arc = ArcBetweenPoints(vortex_pos[0],vortex_pos[9], angle=TAU/(4)).set_color(GREEN).shift(2*LEFT)
		inv_5_label = TexMobject("\\overline{\\mathfrak{p}}").set_color(GREEN)
		inv_5_label.next_to(inv_5_arc,LEFT,buff=-0.1)
		
		norm_5_label = TexMobject("\\text{N}(\\mathfrak{p}) = 5")
		norm_5_label.move_to(vortex_pts_VG.get_center())
		
		self.play(
			ShowCreation(fwd_5_arc)
			)
		self.play(
			Write(fwd_5_label)
			)
		self.play(
			Write(norm_5_label)
			)
		self.wait()
		
		self.play(
			ShowCreation(inv_5_arc)
			)
		self.play(
			Write(inv_5_label)
			)
		self.wait()
		
		self.play(
			ShowCreation(deg5_arcs_VG),
			FadeOut(fwd_5_label),
			FadeOut(inv_5_label),
			FadeOut(norm_5_label)
			)
		self.wait()
		
		deg5_arcs_VG = VGroup(deg5_arcs_VG,fwd_5_arc,inv_5_arc)

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




