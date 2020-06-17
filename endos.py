from manimlib.imports import *

class endos(Scene):
	def construct(self):

		
		
		E0_pos = np.array([-2,-2,0])
		E0_label = TexMobject("E_0").next_to(E0_pos,DOWN+LEFT)
		E0_dot = Dot(radius=0.2).move_to(E0_pos).set_color(BLUE)

		E1_pos = np.array([2,2,0])
		E1_label = TexMobject("E_1").next_to(E1_pos,UP+RIGHT)
		E1_dot = Dot(radius=0.2).move_to(E1_pos).set_color(BLUE)


		self.play(
			FadeIn(E0_dot),
			Write(E0_label),
			FadeIn(E1_dot),
			Write(E1_label)
			)
		self.wait()

		E0_to_E1_arc = ArcBetweenPoints(E0_pos, E1_pos + 0.5*DOWN ,angle=TAU/(4)).set_color(BLUE).add_tip()
		E0_to_E1_label = TexMobject("\\phi").set_color(BLUE).move_to(np.array([1,-1.5,0]))

		E1_to_E0_arc = ArcBetweenPoints(E1_pos, E0_pos + 0.5*UP ,angle=TAU/(4)).set_color(BLUE).add_tip()
		E1_to_E0_label = TexMobject("\\hat{\\phi}").set_color(BLUE).move_to(np.array([-1,1.5,0]))

		self.play(
			ShowCreation(E0_to_E1_arc),
#			ShowCreation(E1_to_E0_arc)
			)
		self.wait()

		self.play(
			Write(E0_to_E1_label),
#			Write(E1_to_E0_label)
			)
		self.wait()

		automorphism = ArcBetweenPoints(E1_label.get_center() + 0.25*UP + 0.25*LEFT, E1_label.get_center() + 0.25*LEFT, angle=TAU/(1.3))
		automorphism.set_color(GREEN).add_tip()
		automorphism.get_tip().scale(0.85)

		alpha_1 = automorphism.copy().next_to(E1_label,UP+LEFT,buff=-0.1).rotate(-1*TAU/12)
		alpha_1_label = TexMobject("\\alpha_1").move_to(alpha_1.get_center() + 0.05*UP).set_color(GREEN)
		alpha_2 = automorphism.copy().next_to(E1_label,UP+RIGHT,buff=-0.1).rotate(-1*TAU/3)
		alpha_2_label = TexMobject("\\alpha_2").move_to(alpha_2.get_center() + 0.1*RIGHT).set_color(GREEN)
		alpha_3 = automorphism.copy().next_to(E1_label,DOWN+RIGHT,buff=-0.1).rotate(1.2*TAU/3)
		alpha_3_label = TexMobject("\\alpha_3").move_to(alpha_3.get_center()+0.05*DOWN).set_color(GREEN)
		
		self.play(
			ShowCreation(alpha_1),
			ShowCreation(alpha_2),
			ShowCreation(alpha_3)
			)
		self.wait()

		self.play(
			Write(alpha_1_label),
			Write(alpha_2_label),
			Write(alpha_3_label)
			)
		self.wait()

		self.play(
			ShowCreation(E1_to_E0_arc)
			)
		self.wait()

		self.play(
			Write(E1_to_E0_label)
			)
		self.wait(2)

		graph = VGroup(E0_label,E0_dot,E1_label,E1_dot,E0_to_E1_arc,E0_to_E1_label,E1_to_E0_label,E1_to_E0_arc,alpha_1,alpha_2,alpha_3,alpha_1_label,alpha_2_label,alpha_3_label)

		self.play(
			Transform(graph,graph.copy().shift(3*LEFT))
			)
		self.wait()

		bullet_1 = Dot(color=RED,radius=0.1).move_to(np.array([1,1,0]))

		bullet_2 = bullet_1.copy().move_to(np.array([1,0,0]))

		bullet_3 = bullet_1.copy().move_to(np.array([1,-1,0]))

		rel_1 = TexMobject("\\text{End}(E_0) \\simeq \\mathcal{O}").next_to(bullet_1,RIGHT)

		rel_2 = TexMobject("\\hat{\\phi} \\circ \\alpha_i \\circ \\phi \\in \\text{End}(E_0)").next_to(bullet_2,RIGHT)

		rel_3 = TexMobject("\\phi \\circ \\hat{\\phi} = \\left[ \\text{deg}(\\phi)^2 \\right]").next_to(bullet_3,RIGHT)

		stat_1 = VGroup(bullet_1,rel_1)
		stat_2 = VGroup(bullet_2,rel_2)
		stat_3 = VGroup(bullet_3,rel_3)

		self.play(
			Write(stat_1)
			)
		self.wait()

		self.play(
			Write(stat_2)
			)
		self.wait()

		self.play(
			Write(stat_3)
			)
		self.wait(2)

		self.play(
			FadeOut(graph),
			FadeOut(stat_1),
			FadeOut(stat_2),
			FadeOut(stat_3)
			)
		self.wait()




