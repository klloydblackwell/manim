#!/usr/bin/env python

from manimlib.imports import *

class volcano(Scene):
	def construct(self):

		c30 = TexMobject("\\mathbb{Z}[\\pi] \\simeq \\mathbb{Z} + 30 \\mathcal{O}_K")
		c30.to_corner(DOWN)

		c6 = TexMobject("\\mathbb{Z} + 6 \\mathcal{O}_K")
		c6.shift(1*DOWN + 4*LEFT)
		c10 = TexMobject("\\mathbb{Z} + 10 \\mathcal{O}_K")
		c10.shift(1*DOWN)
		c15 = TexMobject("\\mathbb{Z} + 15 \\mathcal{O}_K")
		c15.shift(1*DOWN + 4*RIGHT)
		orders_layer1 = VGroup(c6,c10,c15)

		L_30_10 = Line().put_start_and_end_on(np.array([0,-2.7,0]),np.array([0,-1.5,0]))
		L_30_6  = Line().put_start_and_end_on(np.array([-1,-2.7,0]),np.array([-3.5,-1.5,0]))
		L_30_15  = Line().put_start_and_end_on(np.array([1,-2.7,0]),np.array([3.5,-1.5,0]))
		Lines_layer1 = VGroup(L_30_10,L_30_6,L_30_15)

		c2 = TexMobject("\\mathbb{Z} + 2 \\mathcal{O}_K")
		c2.shift(1*UP + 4*LEFT)
		c3 = TexMobject("\\mathbb{Z} + 3 \\mathcal{O}_K")
		c3.shift(1*UP)
		c5 = TexMobject("\\mathbb{Z} + 5 \\mathcal{O}_K")
		c5.shift(1*UP + 4*RIGHT)
		orders_layer2 = VGroup(c2,c3,c5)

		L_6_2 = Line().put_start_and_end_on(np.array([-4,-0.5,0]),np.array([-4,0.5,0]))
		L_10_2 = Line().put_start_and_end_on(np.array([-1,-0.5,0]),np.array([-3.5,0.5,0]))
		L_6_3 = Line().put_start_and_end_on(np.array([-3.5,-0.5,0]),np.array([-1,0.5,0]))
		L_10_5 = Line().put_start_and_end_on(np.array([1,-0.5,0]),np.array([3.5,0.5,0]))
		L_15_3 = Line().put_start_and_end_on(np.array([3.5,-0.5,0]),np.array([1,0.5,0]))
		L_15_5 = Line().put_start_and_end_on(np.array([4,-0.5,0]),np.array([4,0.5,0]))
		Lines_layer2 = VGroup(L_6_2,L_10_2,L_6_3,L_10_5,L_15_3,L_15_5)

		L_2_0 = Line().put_start_and_end_on(np.array([-3.5,1.5,0]),np.array([-0.4,2.7,0]))
		L_3_0 = Line().put_start_and_end_on(np.array([0,1.5,0]),np.array([0,2.7,0]))
		L_5_0 = Line().put_start_and_end_on(np.array([3.5,1.5,0]),np.array([0.4,2.7,0]))
		Lines_layer3 = VGroup(L_2_0,L_3_0,L_5_0)

		c0 = TexMobject("\\mathcal{O}_K")
		c0.to_corner(UP)

		self.play(
			Write(c30),
			Write(c0)
			)
		self.wait()

		self.play(
			Write(orders_layer1),
			)
		self.wait()

		self.play(
			ShowCreation(Lines_layer1)
			)
		self.wait()

		self.play(
			Write(orders_layer2)
			)
		self.wait()

		self.play(
			ShowCreation(Lines_layer2)
			)
		self.wait()

		self.play(
			ShowCreation(Lines_layer3)
			)
		self.wait(3)

		L_30_0 = DashedLine().put_start_and_end_on(np.array([0,-2.7,0]),np.array([0,-2.1,0]))
		L_30_0.set_color(YELLOW)


		self.play(
			FadeOutAndShift(orders_layer1),
			FadeOutAndShift(Lines_layer1),
			FadeOutAndShift(orders_layer2),
			FadeOutAndShift(Lines_layer2),
			FadeOutAndShift(Lines_layer3),
			Transform(c0, c0.copy().shift(5*DOWN)),
			ShowCreation(L_30_0)
			)
		self.wait()


		bubble = ThoughtBubble()
		bubble.pin_to(c0)
		cloud = bubble[-1]
		cloud.shift(1.7*RIGHT).scale(1.2)
		bubble[0].shift(0.25*UL)
		bubble[1].scale(0.7)
		bubble[2].scale(0.7).shift(0.4*DOWN)

		self.play(
			ShowCreation(bubble)
			)
		self.wait()

		e1 = Dot(color=ORANGE,radius=0.1)
		e2 = e1.copy()
		e3 = e1.copy()
		e4 = e1.copy()

		e1.move_to(np.array([0,1,0]))
		e2.move_to(np.array([1,0,0]))
		e3.move_to(np.array([0,-1,0]))
		e4.move_to(np.array([-1,0,0]))

		e1_label = TexMobject("E_1").next_to(e1,UP).scale(0.75)
		e2_label = TexMobject("E_2").next_to(e2,RIGHT).scale(0.75)
		e3_label = TexMobject("E_3").next_to(e3,DOWN).scale(0.75)
		e4_label = TexMobject("E_4").next_to(e4,LEFT).scale(0.75)

		cycle = VGroup(e1,e1_label,e2,e2_label,e3,e3_label,e4,e4_label)

		self.play(
			FadeIn(cycle.move_to(cloud.get_center()))
			)
		self.wait()

		arc1 = ArcBetweenPoints(e2.get_center(),e1.get_center(),angle=TAU/(3.2)).set_color(ORANGE)
		arc2 = ArcBetweenPoints(e3.get_center(),e2.get_center(),angle=TAU/(3.2)).set_color(ORANGE)
		arc3 = ArcBetweenPoints(e4.get_center(),e3.get_center(),angle=TAU/(3.2)).set_color(ORANGE)
		arc4 = ArcBetweenPoints(e1.get_center(),e4.get_center(),angle=TAU/(3.2)).set_color(ORANGE)

		arcs = VGroup(arc1, arc2, arc3, arc4)

		self.play(
			ShowCreation(arcs)
			)
		self.wait()

		self.play(
			FadeOut(arcs),
			FadeOut(cycle),
			FadeOut(bubble)
			)
		self.wait()

		o_L1 = TexMobject("\\mathcal{O}_{L1}").shift(4*LEFT)
		o_L2 = TexMobject("\\mathcal{O}_{L2}")
		o_L3 = TexMobject("\\mathcal{O}_{L3}").shift(4*RIGHT)
		m_orders_1 = VGroup(o_L1,o_L2,o_L3)

		o_P1 = TexMobject("\\mathcal{O}_{P1}").move_to(o_L1.get_center())
		o_P1.shift(2*UP + 1*LEFT)
		o_P2 = TexMobject("\\mathcal{O}_{P2}").move_to(o_L1.get_center())
		o_P2.shift(2*UP + 1*RIGHT)

		o_Q1 = TexMobject("\\mathcal{O}_{Q1}").move_to(o_L2.get_center())
		o_Q1.shift(2*UP + 1*LEFT)
		o_Q2 = TexMobject("\\mathcal{O}_{Q2}").move_to(o_L2.get_center())
		o_Q2.shift(2*UP + 1*RIGHT)

		o_R1 = TexMobject("\\mathcal{O}_{R1}").move_to(o_L3.get_center())
		o_R1.shift(2*UP + 1*LEFT)
		o_R2 = TexMobject("\\mathcal{O}_{R2}").move_to(o_L3.get_center())
		o_R2.shift(2*UP + 1*RIGHT)

		m_orders_2 = VGroup(o_P1,o_P2,o_Q1,o_Q2,o_R1,o_R2)

		L_K_L1 = Line().put_start_and_end_on(np.array([-0.4,-1.3,0]),np.array([-3.5,-0.4,0]))
		L_K_L2 = Line().put_start_and_end_on(np.array([0,-1.3,0]),np.array([0,-0.4,0]))
		L_K_L3 = Line().put_start_and_end_on(np.array([0.4,-1.3,0]),np.array([3.5,-0.4,0]))
		m_orders_lines_1 = VGroup(L_K_L1,L_K_L2,L_K_L3)

		self.play(
			Write(m_orders_1)
			)
		self.wait()

		self.play(
			ShowCreation(m_orders_lines_1)
			)
		self.wait()


		self.play(
			Write(m_orders_2)
			)
		self.wait()

		L_L1_P1 = Line().put_start_and_end_on(np.array([-4.3,0.4,0]),np.array([-5,1.6,0]))
		L_L1_P2 = Line().put_start_and_end_on(np.array([-3.7,0.4,0]),np.array([-3,1.6,0]))
		final_lines_1 = VGroup(L_L1_P1,L_L1_P2)
		final_lines_2 = final_lines_1.copy().shift(4*RIGHT)
		final_lines_3 = final_lines_1.copy().shift(8*RIGHT)
		final_lines = VGroup(final_lines_1,final_lines_2,final_lines_3)

		self.play(
			ShowCreation(final_lines)
			)
		self.wait()

		rectangle = RoundedRectangle(height=1,width=12).set_color(RED).shift(2*UP)

		self.play(
			FadeIn(rectangle)
			)
		self.wait()

		max_label = TextMobject("Maximal Orders").set_color(RED).shift(3*UP)

		self.play(
			DrawBorderThenFill(max_label)
			)
		self.wait()

		self.play(
			FadeOutAndShift(c30),
			FadeOutAndShift(L_30_0),
			FadeOutAndShift(c0),
			FadeOutAndShift(m_orders_1),
			FadeOutAndShift(m_orders_lines_1),
			FadeOutAndShift(final_lines)
			)
		self.wait()

		self.play(
			FadeOut(max_label),
			FadeOut(rectangle),
			FadeOut(m_orders_2)
			)
		self.wait()







