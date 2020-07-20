#!/usr/bin/env python

from manimlib.imports import *

grid_shift = 2.75*LEFT + 1.25*DOWN

b1h = np.array([4,0,0])

b2h = np.array([3,2.25,0])

class mink(Scene):
	def construct(self):

		L_dots  = []
#		L_radii = []
#		L_radii_r = []
		for i in range(-2,4):
			for j in range(-1,5):
				loc = i*b1h + j*b2h
				L_dots.append(Dot(loc,radius=0.1,color=BLUE).fade(0.4))
#				L_radii.append(Dot(loc,radius=1.2,color=GRAY).fade(0.75))
#				L_radii_r.append(DashedLine(loc,loc+np.array([-0.5,1.06,0])).set_color(RED))


#		radii_core = Dot(ORIGIN,radius=1.2,color=GRAY).fade(0.75)
#		radii_r_core = DashedLine(ORIGIN,ORIGIN+np.array([-0.5,1.06,0])).set_color(RED)


		L_dots_VG = VGroup(*L_dots).shift(grid_shift)
#		L_radii_VG = VGroup(*L_radii).shift(grid_shift)
#		L_radii_r_VG = VGroup(*L_radii_r).shift(grid_shift)

		origin_dot = Dot(ORIGIN,radius=0.1,color=BLUE).shift(grid_shift)
		origin_label = TexMobject("O").scale(0.75).set_color(BLUE)
		origin_label.next_to(origin_dot,DOWN,buff=0.1)

#		radii_label = TexMobject("r").set_color(RED).next_to(radii_r_core,RIGHT,buff=0)
#		radii_template_VG = VGroup(radii_core.copy(),radii_r_core.copy(),Dot(ORIGIN,radius=0.1,color=BLUE),radii_label)
		

		b1h_arrow = Arrow().put_start_and_end_on(ORIGIN,np.array([3.95,0,0])).shift(grid_shift)
		b1h_arrow.set_color(BLUE)
		b1h_label = TexMobject("b_1")
		b1h_label.next_to(b1h,DOWN,buff=0.2).scale(0.75).set_color(BLUE).shift(grid_shift)

		b2h_arrow = Arrow().put_start_and_end_on(ORIGIN,np.array([2.95,2.20,0])).shift(grid_shift)
		b2h_arrow.set_color(BLUE)
		b2h_label = TexMobject("b_2")
		b2h_label.next_to(b2h,UP+LEFT,buff=0.1).scale(0.75).set_color(BLUE).shift(grid_shift)

		self.play(
			FadeIn(origin_dot),
			Write(origin_label)
			)
		self.play(
			ShowCreation(b1h_arrow),
			Write(b1h_label),
			ShowCreation(b2h_arrow),
			Write(b2h_label),
			lag_ratio = 0.5,
			run_time = 2
			)
		self.wait(1)

		

		grid = NumberPlane(faded_line_ratio=0,
						x_min = -20,
						x_max = 20,
						y_min = -20,
						y_max =20
						)
		grid.set_color(BLUE).fade(0.75)
		grid.get_axes().set_width(1).fade(0.9)

		grid.prepare_for_nonlinear_transform()
		grid.apply_function(lambda p: p[0]*b1h + p[1]*b2h)
		grid.shift(grid_shift)

		self.play(
			Transform(b1h_arrow,b1h_arrow.copy().fade(1)),
			Transform(b1h_label,b1h_label.copy().fade(1)),
			Transform(b2h_arrow, b2h_arrow.copy().fade(1)),
			Transform(b2h_label, b2h_label.copy().fade(1)),
			Transform(origin_dot,origin_dot.copy().fade(0.75)),
			Transform(origin_dot,origin_dot.copy().fade(0.75)),
			Transform(origin_label,origin_label.copy().fade(0.2)),
			FadeIn(grid)
			)
		self.play(
			FadeIn(L_dots_VG)
			)
		
		self.wait(2)

		# TODO: Fadeout grid

		locList = [
			np.array([-2,-1,0]),
			np.array([6,3.5,0]),
			np.array([4,-1,0]),
			np.array([-2,3,0])
			]

		destList = [
			np.array([0,-1,0]),
			np.array([0,2,0]),
			np.array([1,0,0]),
			np.array([-1,1,0])
			]

		normList = [
			np.linalg.norm(locList[i] - (destList[i][0]*b1h + destList[i][1]*b2h)) for i in range(0,4)
			]

		diskList = [
			Dot(locList[i] + grid_shift,radius=normList[i],color=ORANGE).fade(0.75) for i in range(0,4)
			]

		vdotList = [Dot(i + grid_shift,radius=0.15,color=YELLOW) for i in locList]

		destdotList = [Dot( destList[i][0]*b1h + destList[i][1]*b2h + grid_shift, radius = 0.15, color=RED ) for i in range(0,4)]

		for i in range(0,4):
			self.play(
				FadeIn(vdotList[i])
				)
			self.wait(1)
			self.play(
				GrowFromPoint(diskList[i],vdotList[i].get_center()),
				lag_ratio=0.3,
				run_time=3
				)
			self.play(
				FadeIn(destdotList[i])
				)
			self.wait(2)