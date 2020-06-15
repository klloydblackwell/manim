from manimlib.imports import *

class pathfinder(Scene):
	def construct(self):

		E_label = TexMobject("E").move_to(np.array([-4,-2,0]))


		Ep_label = TexMobject("E'").move_to(np.array([4,-2,0]))

		self.play(
			Write(E_label),
			Write(Ep_label)
			)
		self.wait()

		unknown_line = DashedLine().put_start_and_end_on(E_label.get_center() + 0.5*RIGHT, Ep_label.get_center() + 0.5*LEFT)
		unknown_line.add_tip().set_color(RED)

		question_mark = TexMobject("\\text{\\textbf{???}}").move_to(unknown_line.get_center()+0.3*UP).set_color(RED)

		self.play(
			FadeIn(unknown_line),
			FadeIn(question_mark)
			)
		self.wait()
		self.play(
			FadeOut(unknown_line),
			FadeOut(question_mark)
			)
		self.wait()

		End_E_label = TexMobject("\\text{End}(E)").move_to(np.array([-4,2,0])).set_color(YELLOW)
		End_Ep_label = TexMobject("\\text{End}(E')").move_to(np.array([4,2,0])).set_color(YELLOW)

		ladder_1 = DashedLine().put_start_and_end_on(E_label.get_center() + 0.5*UP, End_E_label.get_center() + 0.5*DOWN)
		ladder_1.set_color(YELLOW).add_tip()

		ladder_2 = ladder_1.copy().shift(8*RIGHT)

		self.play(
			Write(End_E_label),
			Write(End_Ep_label),
			ShowCreation(ladder_1),
			ShowCreation(ladder_2)
			)
		self.play(
			FadeOut(ladder_1),
			FadeOut(ladder_2)
			)
		self.wait()

		iso_rel_1 = TexMobject("\\simeq \\mathcal{O}").next_to(End_E_label,RIGHT)
		iso_rel_2 = TexMobject("\\simeq \\mathcal{G'}").next_to(End_Ep_label,RIGHT)

		self.play(
			FadeIn(iso_rel_1),
			FadeIn(iso_rel_2)
			)
		self.wait()

		ids = []
		subpaths = []
		for i in range(0,5):
			ids_str = "I_" + str(i+1)
			ids.append(TexMobject(ids_str).move_to(np.array([-3 + i*1.5, (i % 2)*1 + 0.4,0])).set_color(RED))

		for i in range(1,5):
			path = Arrow().put_start_and_end_on(ids[i-1].get_center(),ids[i].get_center()).scale(0.6).set_color(BLUE)
			subpaths.append(path)

		ids_VG = VGroup(*ids)
		subpaths_VG = VGroup(*subpaths)

		subrel_1 = ArcBetweenPoints(End_E_label.get_center()+0.5*DOWN, ids[0].get_center() + 0.3*LEFT).add_tip().set_color(GREEN)
		subrel_2 = ArcBetweenPoints(ids[4].get_center() + 0.3*RIGHT,End_Ep_label.get_center()+0.5*DOWN).add_tip().set_color(GREEN)

		self.play(
			ShowCreation(subrel_1)
			)
		self.play(
			Write(ids[0])
			)
		for i in range(1,5):
			self.play(
				ShowCreation(subpaths[i-1]),
				Write(ids[i])
				)

		self.play(
			ShowCreation(subrel_2)
			)
		self.wait()

		bullet_1_dot = Dot(color=ORANGE, radius=0.1).move_to(np.array([-1.5,-1,0]))
		bullet_1_label = TexMobject("\\text{Norm}(", "I_i", ") = \\ell").next_to(bullet_1_dot,RIGHT)
		bullet_1_label[1].set_color(RED)
		bullet_1 = VGroup(bullet_1_dot,bullet_1_label)

		bullet_2_dot = Dot(color=ORANGE, radius=0.1).move_to(np.array([-1.5,-2,0]))
		bullet_2_label = TexMobject("I_{i+1}", "\\mathcal{G}_i \\subseteq \\mathcal{G}_{i+1}").next_to(bullet_2_dot,RIGHT)
		bullet_2_label[0].set_color(RED)
		bullet_2 = VGroup(bullet_2_dot,bullet_2_label)

		self.play(
			Write(bullet_1)
			)
		self.wait()

		self.play(
			Write(bullet_2)
			)
		self.wait()

		self.play(
			FadeOut(bullet_1),
			FadeOut(bullet_2)
			)
		self.wait()

		ideal_path_VG = VGroup(ids_VG,subpaths_VG)

		isopath = []
		for i in range(0,16):
			start = np.array([-3.5 + i*0.4375, -2 + ((-1)**i)*0.25,0])

			if i == 0:
				start = E_label.get_center()+0.3*RIGHT

			end = np.array([-3.5 + (i+1)*0.4375, -2 + ((-1)**(i+1))*0.25,0])

			if i == 15:
				end = Ep_label.get_center()+0.3*LEFT

			if (i % 2) == 0:
				path = Line().put_start_and_end_on(start,end).set_color(RED)

			else:
				path = Line().put_start_and_end_on(start,end).set_color(BLUE)

			isopath.append(path)

		isopath[15].add_tip()
		isopath_VG = VGroup(*isopath)

		corresp_arrow = DashedLine().put_start_and_end_on(ids[2].get_center()+0.3*DOWN,np.array([0, -1.5,0])).set_color(YELLOW).add_tip()

		self.play(
			ShowCreation(corresp_arrow),
			ReplacementTransform(ideal_path_VG.copy(),isopath_VG)
			)
		self.play(
			FadeOut(corresp_arrow)
			)
		self.wait()

		self.play(
			FadeOut(End_E_label),
			FadeOut(End_Ep_label),
			FadeOut(isopath_VG),
			FadeOut(ids_VG),
			FadeOut(subpaths_VG),
			FadeOut(subrel_1),
			FadeOut(subrel_2),
			FadeOut(iso_rel_1),
			FadeOut(iso_rel_2),
			FadeOut(E_label),
			FadeOut(Ep_label)
			)
		self.wait()










