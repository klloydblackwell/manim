#!/usr/bin/env python

from manimlib.imports import *

grid_shift = 5*LEFT + 1*DOWN

b1h = np.array([2,0,0])

b2h = np.array([1.5,1.125,0])

class ajtai(ThreeDScene):
	def construct(self):

		L_dots  = []
		Lexp_dots = []
		#L_radii = []
		#L_radii_r = []
		for i in range(-10,10):
			for j in range(-10,10):
				loc = i*b1h + j*b2h
				loc2 = i*2*b1h + j*2*b2h
				L_dots.append(Dot(loc,radius=0.1,color=BLUE).fade(0.4))
				Lexp_dots.append(Dot(loc2,radius=0.1,color=BLUE).fade(0.4))
				#L_radii.append(Dot(loc,radius=1.2,color=GRAY).fade(0.75))
				#L_radii_r.append(DashedLine(loc,loc+np.array([-0.5,1.06,0])).set_color(RED))


		#radii_core = Dot(ORIGIN,radius=1.2,color=GRAY).fade(0.75)
		#radii_r_core = DashedLine(ORIGIN,ORIGIN+np.array([-0.5,1.06,0])).set_color(RED)


		L_dots_VG = VGroup(*L_dots).shift(grid_shift)
		Lexp_dots_VG = VGroup(*Lexp_dots).shift(grid_shift)
		#L_radii_VG = VGroup(*L_radii).shift(grid_shift)
		#L_radii_r_VG = VGroup(*L_radii_r).shift(grid_shift)

		origin_dot = Dot(ORIGIN,radius=0.1,color=BLUE).shift(grid_shift)
		origin_label = TexMobject("O").scale(0.75).set_color(BLUE)
		origin_label.next_to(origin_dot,DOWN,buff=0.1)

		#radii_label = TexMobject("r").set_color(RED).next_to(radii_r_core,RIGHT,buff=0)
		#radii_template_VG = VGroup(radii_core.copy(),radii_r_core.copy(),Dot(ORIGIN,radius=0.1,color=BLUE),radii_label)
		

		b1h_arrow = Arrow().put_start_and_end_on(ORIGIN,np.array([1.95,0,0])).shift(grid_shift)
		b1h_arrow.set_color(BLUE)
		b1h_label = TexMobject("b_1")
		b1h_label.next_to(b1h,DOWN,buff=0.2).scale(0.75).set_color(BLUE).shift(grid_shift)

		b2h_arrow = Arrow().put_start_and_end_on(ORIGIN,np.array([1.45,1.075,0])).shift(grid_shift)
		b2h_arrow.set_color(BLUE)
		b2h_label = TexMobject("b_2")
		b2h_label.next_to(b2h,UP+LEFT,buff=0.1).scale(0.75).set_color(BLUE).shift(grid_shift)

		c1h_arrow = Arrow().put_start_and_end_on(ORIGIN,0.99*(3*b1h + b2h)).shift(grid_shift)
		c1h_arrow.set_color(ORANGE)
		c1h_label = TexMobject("s_1")
		c1h_label.next_to(3*b1h + b2h,DOWN,buff=0.2).scale(0.75).set_color(ORANGE).shift(grid_shift)

		c2h_arrow = Arrow().put_start_and_end_on(ORIGIN,0.99*(2*b1h + 1*b2h)).shift(grid_shift)
		c2h_arrow.set_color(ORANGE)
		c2h_label = TexMobject("s_2")
		c2h_label.next_to(2*b1h + 1*b2h,UP,buff=0.3).scale(0.75).set_color(ORANGE).shift(grid_shift)


		self.play(
			FadeIn(origin_dot),
			Write(origin_label)
			)
		self.add_foreground_mobjects(origin_dot)
		self.play(
			ShowCreation(b1h_arrow),
			Write(b1h_label),
			ShowCreation(b2h_arrow),
			Write(b2h_label),
			lag_ratio = 0.5,
			run_time = 2
			)
		self.wait(1)

		b_VG = VGroup(b1h_arrow,b1h_label,b2h_label,b2h_arrow)

		self.play(
			FadeIn(L_dots_VG)
			)
		
		self.wait(1)

		self.play(
			ShowCreation(c1h_arrow),
			Write(c1h_label),
			ShowCreation(c2h_arrow),
			Write(c2h_label),
			lag_ratio = 0.5,
			run_time = 2
			)
		self.wait(2)

		s_VG = VGroup(c1h_label,c1h_arrow,c2h_label,c2h_arrow)

		self.play(
			FadeOutAndShift(b_VG),
			FadeOutAndShift(s_VG),
			FadeOutAndShift(origin_label),
			FadeOut(origin_dot),
			ReplacementTransform(L_dots_VG,Lexp_dots_VG)
			)
		self.wait(2)

		input_vec_dot = Dot(2*b2h,radius=0.2,color=ORANGE)
		input_vec_cir = Circle(arc_center = 2*b2h).scale(0.5).set_color(ORANGE)
		input_vec_mark = VGroup(input_vec_dot,input_vec_cir).shift(grid_shift)

		self.play(
			GrowFromPoint(input_vec_mark,2*b2h + grid_shift),
			lag_ratio=0.7,
			run_time=1.5
			)
		self.wait(1)


		input_vec_label = TexMobject("\\mathbf{v} \\in \\mathcal{L}").set_color(ORANGE).scale(0.8)
		input_vec_label.next_to(2*b2h + grid_shift,UP,buff=0.75)

		self.play(
			Write(input_vec_label)
			)
		self.wait(1)

		input_vec_VG = VGroup(input_vec_mark,input_vec_label)

		err_dest = 2*b1h + b2h

		err_dot = Dot(err_dest,radius=0.2,color=RED).shift(grid_shift)
		err_dot_label = TexMobject("\\mathbf{t}").set_color(RED).next_to(err_dot,DOWN,buff=0.2)
		err_arrow = Arrow().put_start_and_end_on(2*b2h,err_dest).set_color(YELLOW).scale(0.8).shift(grid_shift)
		err_label = TexMobject("\\mathbf{e}").scale(0.8).set_color(YELLOW).next_to(err_arrow,UP,buff=-0.2)

		self.play(
			ShowCreation(err_arrow),
			FadeIn(err_dot)
			)
		self.play(
			Write(err_dot_label),
			Write(err_label)
			)
		self.wait(1)

		err_VG = VGroup(err_arrow,err_label)

		err_zone = Dot(err_dest+grid_shift,radius=3,color=RED).fade(0.8)

		radius_VG = VGroup(
			DashedLine().put_start_and_end_on(err_dest+grid_shift,err_dest+grid_shift+3*RIGHT).set_color(YELLOW),
			TexMobject("\\mathbf{e}").set_color(YELLOW).scale(0.8).next_to(err_dest+grid_shift+1.5*RIGHT,DOWN)
			)

		candidates = VGroup(
			Dot(2*b1h+grid_shift,radius=0.2,color=ORANGE),
			Dot(4*b1h+grid_shift,radius=0.2,color=ORANGE),
			Dot(2*b2h+grid_shift,radius=0.2,color=ORANGE),
			Dot(2*b1h+2*b2h+grid_shift,radius=0.2,color=ORANGE)
			)

		self.play(
			FadeOut(input_vec_VG),
			FadeOut(err_VG)
			)
		self.play(
			GrowFromPoint(err_zone,err_dest+grid_shift),
			lag_ratio=0.5,
			run_time=2
			)
		self.play(
			ShowCreation(radius_VG),
			FadeIn(candidates)
			)
		self.wait(1)

		disc_VG = VGroup(err_dot,err_dot_label,err_zone)

		dialogue_rect = RoundedRectangle(height=1,width=6,fill_opacity=1,fill_color=BLACK)
		dialogue_rect.to_corner(UP+LEFT)

		def_label_A = TexMobject("\\text{Discrete Gaussian } D_{\\mathcal{L},t}").set_color(RED)
		def_label_A.move_to(dialogue_rect.get_center())

		dialogue_VG = VGroup(dialogue_rect,def_label_A)

		

		self.play(
			FadeOut(radius_VG)
			)
		self.play(
			FadeOutAndShift(Lexp_dots_VG),
			FadeOutAndShift(candidates),
			FadeOutAndShift(disc_VG),
			FadeInFrom(dialogue_VG,UP)
			)
		self.wait()

		
		self.add_fixed_in_frame_mobjects(dialogue_VG)
		

		
		s = ParametricSurface(
			self.func,
			u_min=-2,
			u_max=2,
			v_min=-2,
			v_max=2,
			fill_color = RED_D, 
        	fill_opacity = 0.8,
			checkerboard_colors = [RED_D, RED_E],
			stroke_color = RED_E,
			stroke_width = 0.5
			)

		axes = ThreeDAxes(
			number_line_config={"color": LIGHT_GREY,"include_tip": False,"exclude_zero_from_default_numbers": True,}     	
        	)

		#conf = {"fill_color": BLUE_D, 
        #		"fill_opacity": 1.0,
		#		"checkerboard_colors": [BLUE_D, BLUE_E],
		#		"stroke_color": BLUE_E,
		#		"stroke_width": 0.5,}

		surface = VGroup(axes, s)
		surface.scale(2)

		self.move_camera(0.8 * np.pi / 2, -0.45 * np.pi)
		self.play(
			ShowCreation(axes)
			)
		self.play(Write(s))
		self.wait()

		self.begin_ambient_camera_rotation()
		self.wait(5)

	def func(self, u, v):
		return np.array([u,v,np.exp(-(u**2 + v**2))])









