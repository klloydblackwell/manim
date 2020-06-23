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

		L_30_0 = DashedLine().put_start_and_end_on(np.array([0,-2.7,0]),np.array([0,-2.3,0]))
		L_30_0.set_color(YELLOW)
		
		L_30_M = L_30_0.copy().shift(1.2*UP)
		
		cM = TexMobject("\\mathcal{O}")
		cM.move_to(c0.get_center()).shift(5.2*DOWN)


		self.play(
			FadeOutAndShift(orders_layer1),
			FadeOutAndShift(Lines_layer1),
			FadeOutAndShift(orders_layer2),
			FadeOutAndShift(Lines_layer2),
			FadeOutAndShift(Lines_layer3),
			Transform(c0, c0.copy().shift(4*DOWN)),
			ShowCreation(L_30_0),
			ShowCreation(L_30_M),
			FadeIn(cM)
			)
		self.wait()


		bubble = ThoughtBubble()
		bubble.pin_to(cM)
		cloud = bubble[-1]
		cloud.set_width(5.5,stretch=True)
		cloud.shift(1.6*RIGHT).scale(1.25)
		bubble[0].next_to(cM,LEFT)
		bubble[1].scale(0.7).shift(0.4*DOWN + 0.7*LEFT)
		bubble[2].scale(0.7).shift(0.6*DOWN+0.5*LEFT)

		self.play(
			ShowCreation(bubble)
			)
		self.wait()

		cycle_nodelist = []
		cycle_node_poslist = []
		cycle_node_labellist = []
		for i in range(0,8):
			
			if i == 6:
				continue
			
			#Generate node dot
			cycle_node = Dot(color=ORANGE,radius=0.1)
			
			#Locate node dot
			pos = np.array([1.5*np.cos((2*np.pi*i)/8),1.5*np.sin((2*np.pi*i)/8),0])
			cycle_node.move_to(pos)
			
			#Save node dot position
			cycle_node_poslist.append(pos)

			#Save node dot
			cycle_nodelist.append(cycle_node)
			
			#Create, locate, save node label
			label = "E_" + str(i+1)
			
			if i == 7:
				label = "E_h"
			
			cycle_node_label = TexMobject(label).scale(0.7)
			cycle_node_label.move_to(1.25*pos)
			cycle_node_labellist.append(cycle_node_label)
			
		cycle = VGroup(*cycle_nodelist,*cycle_node_labellist)
		
		
		cycle_edgelist = []
		for i in range(0,7):
			start = cycle_node_poslist[i % 7]
			end = cycle_node_poslist[(i+1) % 7]
			arc = 2*np.pi/8
			
			if i == 5:
				arc = 2*np.pi/4
			
			cycle_edge = ArcBetweenPoints(start,end,arc)
			
			if i == 5:
				cycle_edge = DashedVMobject(cycle_edge)
			
			cycle_edge.set_color(ORANGE)
			cycle_edgelist.append(cycle_edge)
			
		arcs = VGroup(*cycle_edgelist)
		
		bubble_ctr = bubble.get_center() + 0.6*UP
		self.play(
			FadeIn(cycle_nodelist[0].shift(bubble_ctr)),
			Write(cycle_node_labellist[0].shift(bubble_ctr))
			)
		self.wait()
		
		
		for i in range(1,7):
			self.play(
				ShowCreation(cycle_edgelist[i-1].shift(bubble_ctr)),
				FadeIn(cycle_nodelist[i].shift(bubble_ctr)),
				Write(cycle_node_labellist[i].shift(bubble_ctr))
				)

		self.play(ShowCreation(cycle_edgelist[6].shift(bubble_ctr)))
		self.wait()
		
		cycle_info_1_dot = Dot(radius=0.1).move_to(np.array([2,2,0]))
		cycle_info_1 = TexMobject("\\text{End}\\left(E_i\\right) \\simeq \\mathcal{O}")
		cycle_info_1.next_to(cycle_info_1_dot,RIGHT)
		
		cycle_info_2_dot = Dot(radius=0.1).move_to(np.array([2,1,0]))
		cycle_info_2 = TexMobject("h = \\# \\text{Cl}(\\mathcal{O})")
		cycle_info_2.next_to(cycle_info_2_dot,RIGHT)
		
		self.play(
			FadeIn(cycle_info_1_dot),
			Write(cycle_info_1)
			)
		self.wait()
		
		self.play(
			FadeIn(cycle_info_2_dot),
			Write(cycle_info_2)
			)
		self.wait()

		self.play(
			FadeOut(arcs),
			FadeOut(cycle),
			FadeOut(bubble),
			FadeOut(cycle_info_1_dot),
			FadeOut(cycle_info_1),
			FadeOut(cycle_info_2_dot),
			FadeOut(cycle_info_2),
			FadeOut(cM),
			FadeOut(L_30_M),
			Transform(c0,c0.copy().shift(1.2*DOWN))
			)
		self.wait()
		
		c0_J = TexMobject("\\mathcal{O}_{J}")
		c0_J.move_to(c0.get_center()+4*RIGHT)
		
		c0_H = TexMobject("\\mathcal{O}_{H}")
		c0_H.move_to(c0.get_center()+4*LEFT)
		
		self.play(
			Write(c0_J),
			Write(c0_H)
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

		L_K_L1 = Line().put_start_and_end_on(np.array([-4,-1.4,0]),np.array([-4,-0.4,0]))
		L_K_L2 = Line().put_start_and_end_on(np.array([0,-1.4,0]),np.array([0,-0.4,0]))
		L_K_L3 = Line().put_start_and_end_on(np.array([4,-1.4,0]),np.array([4,-0.4,0]))
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
			Write(max_label)
			)
		self.wait()
		
		zoomed_off_VG = VGroup(
							max_label,
							rectangle,
							o_P1,
							o_P2,
							o_Q2,
							o_R1,
							o_R2
							)


		self.play(
			FadeOutAndShift(c30),
			FadeOutAndShift(L_30_0),
			FadeOutAndShift(c0),
			FadeOutAndShift(m_orders_1),
			FadeOutAndShift(m_orders_lines_1),
			FadeOutAndShift(final_lines),
			FadeOutAndShift(c0_H),
			FadeOutAndShift(c0_J)
			)
		self.wait()
		
		self.play(
			Transform(zoomed_off_VG,zoomed_off_VG.copy().scale(100)),
			Transform(o_Q1,o_Q1.copy().move_to(ORIGIN + 3*UP).scale(2))
			)
		self.wait()
		
		dom_curve_dot = Dot(color=ORANGE,radius=0.15)
		dom_curve_dot.move_to(np.array([2,0,0]))
		dom_curve_label = TexMobject("E").next_to(dom_curve_dot,RIGHT)
		
		ran_curve_dot = dom_curve_dot.copy()
		ran_curve_dot.move_to(np.array([-2,0,0]))
		ran_curve_label = TexMobject("E'").next_to(ran_curve_dot,LEFT)
		
		frobenius_arc = ArcBetweenPoints(np.array([2,0,0]),
									np.array([2*np.cos(0.95*np.pi),2*np.sin(0.95*np.pi),0]),
									0.8*np.pi
									).add_tip().set_color(ORANGE)
		frobenius_arc_label = TexMobject("\\pi")
		frobenius_arc_label.set_color(ORANGE)
		frobenius_arc_label.move_to(np.array([0,1.4,0]))

		frobenius_inv_arc = ArcBetweenPoints(np.array([-2,0,0]),
									np.array([2*np.cos(1.95*np.pi),2*np.sin(1.95*np.pi),0]),
									0.8*np.pi
									).add_tip().set_color(ORANGE)
		frobenius_inv_arc_label = TexMobject("\\pi^{-1}")
		frobenius_inv_arc_label.set_color(ORANGE)
		frobenius_inv_arc_label.move_to(np.array([0,-1.4,0]))
		
		self.play(
			FadeIn(dom_curve_dot),
			Write(dom_curve_label)
			)
		self.wait()
		
		self.play(
			ShowCreation(frobenius_arc),
			Write(frobenius_arc_label),
			FadeIn(ran_curve_dot),
			Write(ran_curve_label)
			)
		self.wait()
		
		self.play(
			ShowCreation(frobenius_inv_arc),
			Write(frobenius_inv_arc_label)
			)
		self.wait()
		
		frobenius_def = TexMobject("\\pi : (x,y) \\mapsto (x^p, y^p)")
		frobenius_def.to_corner(DOWN)
		
		self.play(Write(frobenius_def))
		self.wait(2)
		
		self.play(
			FadeOut(dom_curve_dot),
			FadeOut(dom_curve_label),
			FadeOut(ran_curve_dot),
			FadeOut(ran_curve_label),
			FadeOut(frobenius_arc),
			FadeOut(frobenius_arc_label),
			FadeOut(frobenius_inv_arc),
			FadeOut(frobenius_inv_arc_label),
			FadeOut(o_Q1),
			FadeOut(frobenius_def)
			)
		self.wait()
"""
		self.play(
			FadeOut(max_label),
			FadeOut(rectangle),
			FadeOut(m_orders_2)
			)
		self.wait()


"""




