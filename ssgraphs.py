#!/usr/bin/env python

from manimlib.imports import *

class superSingularGraphs(Scene):
	def construct(self):

		title = TextMobject("Supersingular Graphs").set_color(BLUE).to_corner(UP)

		self.play(
			Write(title)
			)
		self.wait()

		text_1 = TexMobject("\\text{Quaternion algebras have}", "\\text{ \\textbf{many maximal orders}.}")
		bullet_1 = Dot(color=BLUE,radius=0.1).to_corner(LEFT).shift(2*UP)
		text_1.scale(0.6).next_to(bullet_1,RIGHT)
		text_1[1].set_color(BLUE)

		self.play(
			FadeIn(bullet_1),
			Write(text_1)
			)
		self.wait()

		bullet_2 = Dot(color=BLUE,radius=0.1).to_corner(LEFT).shift(1.4*UP)
		text_2A = TexMobject("\\text{For every }", "\\text{\\textbf{maximal order type} }", "\\text{of } B_{p,\\infty} \\text{ there are}")
		text_2A[1].set_color(BLUE)
		text_2B = TexMobject("\\text{\\textbf{1 or 2 curves over} }", "\\mathbb{F}_{p^2} ", "\\text{ having endomorphism ring}")
		text_2B[0].set_color(BLUE)
		text_2B[1].set_color(BLUE)
		text_2C = TexMobject("\\text{isomorphic to it.}")

		text_2A.scale(0.6).next_to(bullet_2,RIGHT)
		text_2B.scale(0.6).next_to(bullet_2,RIGHT).shift(0.3*DOWN)
		text_2C.scale(0.6).next_to(bullet_2,RIGHT).shift(0.6*DOWN)

		text_2 = VGroup(text_2A,text_2B,text_2C)

		self.play(
			FadeIn(bullet_2),
			Write(text_2)
			)
		self.wait()

		bullet_3 = Dot(color=BLUE,radius=0.1).to_corner(LEFT).shift(0.2*UP)
		text_3A = TexMobject("\\text{There is a }", "\\text{\\textbf{unique isogeny class} }", "\\text{of supersingular}")
		text_3A[1].set_color(BLUE)
		text_3B = TexMobject("\\text{curves over }", "\\overline{\\mathbb{F}}_p \\text{ of size }","\\approx p/12", ".")
		text_3B[-2].set_color(BLUE)

		text_3A.scale(0.6).next_to(bullet_3,RIGHT)
		text_3B.scale(0.6).next_to(bullet_3,RIGHT).shift(0.3*DOWN)
		text_3 = VGroup(text_3A,text_3B)

		self.play(
			FadeIn(bullet_3),
			Write(text_3)
			)
		self.wait()

		bullet_4 = Dot(color=BLUE,radius=0.1).to_corner(LEFT).shift(0.7*DOWN)
		text_4A = TextMobject("Left ideals act on the set of maximal orders like")
		text_4B = TextMobject("isogenies.")
		text_4A.scale(0.6).next_to(bullet_4,RIGHT)
		text_4B.scale(0.6).next_to(bullet_4,RIGHT).shift(0.3*DOWN)
		text_4 = VGroup(text_4A,text_4B)

		self.play(
			FadeIn(bullet_4),
			Write(text_4)
			)
		self.wait()

		bullet_5 = Dot(color=BLUE,radius=0.1).to_corner(LEFT).shift(1.6*DOWN)
		text_5 = TexMobject("\\text{The graph of }", "\\ell", "\\text{-isogenies is }", "(\\ell + 1)", "\\text{-regular.}")
		text_5[1].set_color(BLUE)
		text_5[-2].set_color(BLUE)
		text_5.scale(0.6).next_to(bullet_5,RIGHT)

		self.play(
			FadeIn(bullet_5),
			Write(text_5)
			)
		self.wait()

		graph_outer_pts = []
		graph_outer_pos = []

		for k in range(0,6):
			dot_pos = np.array([2*np.cos(k*(np.pi/3) + np.pi/6),2*np.sin(k*(np.pi/3)+np.pi/6),0])
			dot = Dot(radius=0.1).move_to(dot_pos)
			graph_outer_pts.append(dot)
			graph_outer_pos.append(dot_pos)

		graph_outer_pos.append(np.array([-0.8,0,0]))
		graph_outer_pos.append(np.array([0.8,0,0]))
		graph_outer_pts.append(Dot(radius=0.1).move_to(np.array([-0.8,0,0])))
		graph_outer_pts.append(Dot(radius=0.1).move_to(np.array([0.8,0,0])))
		graph_outer_pts_VG = VGroup(*graph_outer_pts).shift(4*RIGHT)
		self.play(
			ShowCreation(graph_outer_pts_VG)
			)
		self.wait()

		graph_arcs = []
		for k in range(0,6):
			graph_arcs.append(ArcBetweenPoints(graph_outer_pos[k],graph_outer_pos[(k+1) % 6],angle=0).set_color(RED))

		graph_arcs.append(ArcBetweenPoints(graph_outer_pos[0],graph_outer_pos[2],angle=0).set_color(RED))
		graph_arcs.append(ArcBetweenPoints(graph_outer_pos[2],graph_outer_pos[4],angle=0).set_color(RED))
		graph_arcs.append(ArcBetweenPoints(graph_outer_pos[4],graph_outer_pos[0],angle=0).set_color(RED))
		graph_arcs.append(ArcBetweenPoints(graph_outer_pos[1],graph_outer_pos[6],angle=0).set_color(RED))
		graph_arcs.append(ArcBetweenPoints(graph_outer_pos[1],graph_outer_pos[7],angle=0).set_color(RED))
		graph_arcs.append(ArcBetweenPoints(graph_outer_pos[3],graph_outer_pos[6],angle=0).set_color(RED))
		graph_arcs.append(ArcBetweenPoints(graph_outer_pos[3],graph_outer_pos[5],angle=0).set_color(RED))
		graph_arcs.append(ArcBetweenPoints(graph_outer_pos[5],graph_outer_pos[7],angle=0).set_color(RED))
		graph_arcs.append(ArcBetweenPoints(graph_outer_pos[6],graph_outer_pos[7],angle=np.pi/8).set_color(RED))
		graph_arcs.append(ArcBetweenPoints(graph_outer_pos[7],graph_outer_pos[6],angle=np.pi/8).set_color(RED))
		graph_arcs_VG = VGroup(*graph_arcs).shift(4*RIGHT)
		self.bring_to_back(graph_arcs_VG)

		self.play(
			ShowCreation(graph_arcs_VG)
			)
		self.wait()

		graph_label = TexMobject("\\text{3-isogeny graph on } \\mathbb{F}_{97^2}").next_to(graph_outer_pts[4],DOWN).scale(0.6)
		self.play(
			Write(graph_label)
			)
		self.wait(3)

		self.play(
			FadeOut(bullet_1),
			FadeOut(bullet_2),
			FadeOut(bullet_3),
			FadeOut(bullet_4),
			FadeOut(bullet_5),
			FadeOut(text_1),
			FadeOut(text_2),
			FadeOut(text_3),
			FadeOut(text_4),
			FadeOut(text_5),
			FadeOut(title),
			FadeOut(graph_outer_pts_VG),
			FadeOut(graph_arcs_VG),
			FadeOut(graph_label)
			)
		self.wait()
