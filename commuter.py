from manimlib.imports import *

class commuter(Scene):
	def construct(self):


		E_label = TexMobject("E").move_to(np.array([-3,2,0]))

		E_mod_u_label = TexMobject(
							"E / \\langle", #0
							"U",            #1
							"\\rangle"      #2 
							)
		E_mod_u_label.move_to(np.array([3,2,0]))
		E_mod_u_label[1].set_color(RED)


		E_mod_v_label = TexMobject(
							"E / \\langle", #0
							"V",            #1
							"\\rangle"      #2
							)
		E_mod_v_label.move_to(np.array([-3,-2,0]))
		E_mod_v_label[1].set_color(BLUE)

		E_mod_uv_label = TexMobject(
							"E / \\langle", #0
							"U",            #1
							",",            #2
							"V",            #3
							"\\rangle"      #4
							)
		E_mod_uv_label.move_to(np.array([3,-2,0]))
		E_mod_uv_label[1].set_color(RED)
		E_mod_uv_label[3].set_color(BLUE)

		phi_label = TexMobject("\\phi").set_color(GREEN).move_to(np.array([0,2.3,0]))
		phi_start = np.array([-2,2,0])
		phi_end = np.array([2,2,0])
		phi_arc = Arrow().put_start_and_end_on(phi_start,phi_end).set_color(GREEN)

		gamma_label = TexMobject("\\gamma").set_color(ORANGE).move_to(np.array([-3.3,0,0]))
		gamma_start = np.array([-3,1.5,0])
		gamma_end = np.array([-3,-1.5,0])
		gamma_arc = Arrow().put_start_and_end_on(gamma_start,gamma_end).set_color(ORANGE)

		self.play(
			Write(E_label)
			)
		self.wait()

		self.play(
			ShowCreation(phi_arc),
			FadeIn(phi_label),
			Write(E_mod_u_label)
			)
		self.wait()

		self.play(
			ShowCreation(gamma_arc),
			FadeIn(gamma_label),
			Write(E_mod_v_label)
			)
		self.wait()

		self.play(
			Write(E_mod_uv_label)
			)
		self.wait()

		phi_p_label = TexMobject("\\phi'").set_color(GREEN).move_to(np.array([0,-2.3,0]))
		phi_p_start = np.array([-2,-2,0])
		phi_p_end = np.array([2,-2,0])
		phi_p_arc = Arrow().put_start_and_end_on(phi_p_start,phi_p_end).set_color(GREEN)

		gamma_p_label = TexMobject("\\gamma'").set_color(ORANGE).move_to(np.array([3.3,0,0]))
		gamma_p_start = np.array([3,1.5,0])
		gamma_p_end = np.array([3,-1.5,0])
		gamma_p_arc = Arrow().put_start_and_end_on(gamma_p_start,gamma_p_end).set_color(ORANGE)

		self.play(
			ShowCreation(phi_p_arc),
			FadeIn(phi_p_label)
			)
		self.wait()

		self.play(
			ShowCreation(gamma_p_arc),
			FadeIn(gamma_p_label)
			)
		self.wait()

		diagram_VG = VGroup(
							E_label,
							E_mod_v_label,
							E_mod_u_label,
							E_mod_uv_label,
							phi_label,
							phi_arc,
							phi_p_label,
							phi_p_arc,
							gamma_arc,
							gamma_p_arc,
							gamma_label,
							gamma_p_label
							)

		diagram_VG_tgt = diagram_VG.copy().shift(4*LEFT).scale(0.75)
		
		self.play(
			Transform(diagram_VG,diagram_VG_tgt)
			)
		self.wait()

		num_u_label = TexMobject(
								"\\#",  #0
								"U",    #1
								"=",    #2
								"N_1"   #3
								)
		num_u_label.move_to(np.array([2,2,0]))
		num_u_label[1].set_color(RED)
		num_u_label[3].set_color(RED)

		num_v_label = TexMobject(
								"\\#",   #0
								"V",    #1
								"=",    #2
								"N_2"   #3
								)
		num_v_label.move_to(np.array([2,1,0]))
		num_v_label[1].set_color(BLUE)
		num_v_label[3].set_color(BLUE)

		coprime_label = TexMobject(
								"\\text{gcd} (",   #0
								"N_1",             #1
								",",               #2
								"N_2",             #3
								") =",             #4
								"1"                #5
								)
		coprime_label.move_to(np.array([2,0,0]))
		coprime_label[1].set_color(RED)
		coprime_label[3].set_color(BLUE)              

		num_ker_label = TexMobject(
								"\\# \\langle",    #0
								"U",               #1
								",",               #2
								"V",               #3
								"\\rangle = ",     #4
								"N_1",             #5
								"\\cdot",          #6
								"N_2"              #7
								)
		num_ker_label.move_to(np.array([2,-1,0]))
		num_ker_label[1].set_color(RED)
		num_ker_label[3].set_color(BLUE)
		num_ker_label[5].set_color(RED)
		num_ker_label[7].set_color(BLUE)

		self.play(
			Write(num_u_label),
			Write(num_v_label)
			)
		self.wait()

		self.play(
			Write(coprime_label[0:6:2])
			)
		self.wait()

		self.play(
			ReplacementTransform(num_u_label[3].copy(),coprime_label[1]),
			ReplacementTransform(num_v_label[3].copy(),coprime_label[3]),
			Write(coprime_label[5])
			)
		self.wait()

		self.play(
			Write(num_ker_label[0:6:2])
			)
		self.wait()

		self.play(
			ReplacementTransform(num_u_label[1].copy(),num_ker_label[1]),
			ReplacementTransform(num_v_label[1].copy(),num_ker_label[3])
			)
		self.wait()

		self.play(
			ReplacementTransform(coprime_label[1].copy(),num_ker_label[5]),
			ReplacementTransform(coprime_label[3].copy(),num_ker_label[7]),
			FadeIn(num_ker_label[6])
			)
		self.wait()

		self.play(
			FadeOut(coprime_label)
			)

		num_u_target = num_u_label.copy().move_to(np.array([-2,3.5,0])).scale(0.8)
		num_v_target = num_v_label.copy().next_to(num_u_target,RIGHT,buff=0.4).scale(0.8)
		num_ker_target = num_ker_label.copy().next_to(num_v_target,RIGHT,buff=0.4).scale(0.8)

		self.play(
			Transform(num_u_label,num_u_target),
			Transform(num_v_label,num_v_target),
			Transform(num_ker_label,num_ker_target)
			)
		self.wait()

		bullet_1_dot = Dot(radius=0.1).move_to(np.array([0.3,2,0]))
		bullet_1_label = TexMobject("\\text{deg } \\phi = \\text{deg } \\phi' = ").scale(0.8)
		bullet_1_label.next_to(bullet_1_dot,RIGHT)
		bullet_1_VG = VGroup(bullet_1_dot,bullet_1_label)

		self.play(
			Write(bullet_1_VG)
			)
		self.wait()

		num_u_target = num_u_label.copy().next_to(bullet_1_VG,RIGHT,buff=0.2)

		self.play(
			Transform(num_u_label,num_u_target)
			)
		self.wait()

		bullet_2_dot = Dot(radius=0.1).move_to(np.array([0.3,1,0]))
		bullet_2_label = TexMobject("\\text{deg } \\gamma = \\text{deg } \\gamma' = ").scale(0.8)
		bullet_2_label.next_to(bullet_2_dot,RIGHT)
		bullet_2_VG = VGroup(bullet_2_dot,bullet_2_label)

		self.play(
			Write(bullet_2_VG)
			)
		self.wait()

		num_v_target = num_v_label.copy().next_to(bullet_2_VG,RIGHT,buff=0.2)

		self.play(
			Transform(num_v_label,num_v_target)
			)
		self.wait()

		bullet_3_dot = Dot(radius=0.1).move_to(np.array([0.3,0,0]))
		bullet_3_label = TexMobject(
									"\\text{deg } \\gamma' \\circ \\phi", #0
									"=",                                  #1
									" \\text{deg } \\phi' \\circ \\gamma" #2
									).scale(0.8)
		bullet_3_label.next_to(bullet_3_dot,RIGHT)

		bullet_3_label_sub_A = TexMobject("=",
										"\\# \\langle",    #1
										"U",               #2
										",",               #3
										"V",               #4
										"\\rangle"      #5
										)
		bullet_3_label_sub_A.scale(0.8).next_to(bullet_3_label[1],DOWN,buff=0.5)
		bullet_3_label_sub_A.shift(0.65*RIGHT)
		bullet_3_label_sub_A[2].set_color(RED)
		bullet_3_label_sub_A[4].set_color(BLUE)

		bullet_3_label_sub_B = TexMobject("=",
										"N_1",             #1
										"\\cdot",          #2
										"N_2"              #3
										)
		bullet_3_label_sub_B.scale(0.8).next_to(bullet_3_label_sub_A,DOWN,buff=0.5)
		bullet_3_label_sub_B[1].set_color(RED)
		bullet_3_label_sub_B[3].set_color(BLUE)
		
		bullet_3_VG = VGroup(bullet_3_dot,bullet_3_label)
		bullet_3_sub_VG = VGroup(bullet_3_label_sub_A,bullet_3_label_sub_B)

		self.play(
			Write(bullet_3_VG)
		)
		self.wait()

		self.play(
			Transform(num_ker_label,bullet_3_sub_VG),
			)
		self.wait()

		self.play(
			FadeOut(diagram_VG),
			FadeOut(bullet_1_VG),
			FadeOut(num_u_label),
			FadeOut(bullet_2_VG),
			FadeOut(num_v_label),
			FadeOut(bullet_3_VG),
			FadeOut(num_ker_label)
			)
		self.wait()
