#!/usr/bin/env python

from manimlib.imports import *

def branchAndPointTo(start,end,edgeColor,dotColor):
		
#	shortEnd = start + 0.9*(end - start)
	edge = Line().put_start_and_end_on(start, end)
	edge.set_color(edgeColor)
	
	dot = Dot(radius=0.3).move_to(end)
	dot.set_color(dotColor)
	
	return [edge,dot,end]
		

def brancher(start,side,legs,edgeColor,dotColor):
	
	# start is np.array of root pt
	# side is 1 means screen left claw, else screen right claw
	# legs is number of legs - 2 or 3
	
	if side == 1:
		xShift = 1.5
	
	else:
		xShift = -1.5
	
	# Create collector for branch edges, dots
	# Starts from uppermost branch to lowest
	branch_edgeList = []
	
	if legs == 3:
		jump = 1
		
	else:
		jump = 2
		
	for i in range(-1,2,jump):
		
		branch_pos = np.array([start[0] + xShift, start[1] - i, 0])
		
		edgeAndDot = branchAndPointTo(start,branch_pos,edgeColor,dotColor)
		
		branch_edgeList.append(edgeAndDot)
			
	
	return branch_edgeList



class claws(Scene):
		
	def construct(self):
		
		rightStart = np.array([6,-2,0])
		rightStart_dot = Dot(color=BLUE,radius=0.3).move_to(rightStart)
		rightStart_label = TexMobject("E_B").set_color(BLUE)
		rightStart_label.next_to(rightStart_dot,RIGHT,buff=0.1)
		
		rightWalker = TexMobject("\\text{\\textbf{B}}").move_to(rightStart)
		rightWalker.set_color(RED)
		
		leftStart = np.array([-6,2,0])
		leftStart_dot = Dot(color=YELLOW,radius=0.3).move_to(leftStart)
		leftStart_label = TexMobject("E_A").set_color(YELLOW)
		leftStart_label.next_to(leftStart_dot,LEFT,buff=0.1)
		
		leftWalker = TexMobject("\\text{\\textbf{A}}").move_to(leftStart)
		leftWalker.set_color(RED)
		
		rTriClaw = brancher(rightStart,0,3,BLUE,BLUE)
		
		lTriClaw = brancher(leftStart,1,3,YELLOW,YELLOW)
		
		self.play(
			FadeIn(rightStart_dot),
			Write(rightStart_label),
			FadeIn(leftStart_dot),
			Write(leftStart_label)
			)
		self.play(
			Write(rightWalker),
			Write(leftWalker)
			)
		self.add_foreground_mobjects(rightWalker,leftWalker)
		self.wait()
		
		
		for i in range(0,3):
			self.play(
				ShowCreation(rTriClaw[i][0]),
				FadeIn(rTriClaw[i][1]),
				ShowCreation(lTriClaw[i][0]),
				FadeIn(lTriClaw[i][1])
				)
				
		self.play(
			Transform(leftWalker,leftWalker.copy().move_to(lTriClaw[2][2])),
			Transform(rightWalker,rightWalker.copy().move_to(rTriClaw[0][2]))
			)
		self.wait()
		
		lBiClaw_1 = brancher(lTriClaw[2][2],1,2,YELLOW,YELLOW)
		
		rBiClaw_1 = brancher(rTriClaw[0][2],0,2,BLUE,BLUE)
		
		for i in range(0,2):
			self.play(
				ShowCreation(rBiClaw_1[i][0]),
				FadeIn(rBiClaw_1[i][1]),
				ShowCreation(lBiClaw_1[i][0]),
				FadeIn(lBiClaw_1[i][1])
				)
				
		self.play(
			Transform(leftWalker,leftWalker.copy().move_to(lBiClaw_1[0][2])),
			Transform(rightWalker,rightWalker.copy().move_to(rBiClaw_1[1][2]))
			)
		self.wait()
		
		lBiClaw_2 = brancher(lBiClaw_1[0][2],1,2,YELLOW,YELLOW)
		
		rBiClaw_2 = brancher(rBiClaw_1[1][2],0,2,BLUE,BLUE)
		
		for i in range(0,2):
			self.play(
				ShowCreation(rBiClaw_2[i][0]),
				FadeIn(rBiClaw_2[i][1]),
				ShowCreation(lBiClaw_2[i][0]),
				FadeIn(lBiClaw_2[i][1])
				)
				
		self.play(
			Transform(leftWalker,leftWalker.copy().move_to(lBiClaw_2[1][2])),
			Transform(rightWalker,rightWalker.copy().move_to(rBiClaw_2[0][2]))
			)
		self.wait()
		
		lBiClaw_3 = brancher(lBiClaw_2[1][2],1,2,YELLOW,YELLOW)
		
		rBiClaw_3 = brancher(rBiClaw_2[0][2],0,2,BLUE,BLUE)
		
		GreenDot = Dot(radius=0.3,color=GREEN_SCREEN).move_to(ORIGIN)
		RedCircle = Circle().scale(0.5)
		
		self.play(
			ShowCreation(rBiClaw_3[1][0]),
			FadeIn(rBiClaw_3[1][1]),
			ShowCreation(lBiClaw_3[0][0]),
			FadeIn(lBiClaw_3[0][1])
			)
		self.play(
			ShowCreation(rBiClaw_3[0][0]),
			ShowCreation(lBiClaw_3[1][0]),
			FadeIn(GreenDot),
			FadeIn(RedCircle),
			FadeOut(leftWalker),
			FadeOut(rightWalker)
			)
		self.wait()
		
		route = VGroup(
			lTriClaw[2][0],
			lTriClaw[2][1],
			lBiClaw_1[0][0],
			lBiClaw_1[0][1],
			lBiClaw_2[1][0],
			lBiClaw_2[1][1],
			lBiClaw_3[1][0],
			rTriClaw[0][0],
			rTriClaw[0][1],
			rBiClaw_1[1][0],
			rBiClaw_1[1][1],
			rBiClaw_2[0][0],
			rBiClaw_2[0][1],
			rBiClaw_3[0][0]
			)
		
		self.add_foreground_mobjects(rightStart_dot,leftStart_dot)
		
		self.play(
			FadeOut(RedCircle),
			Transform(route,route.copy().set_color(GREEN_SCREEN))
			)
		self.wait()
		
		rel_label = TexMobject(
						"\\phi", #0
						":",     #1
						"E_A",   #2
						"\\to",  #3
						"E_B"    #4
						).scale(1.5)
		rel_label[0].set_color(GREEN_SCREEN)
		rel_label[2].set_color(YELLOW)
		rel_label[4].set_color(BLUE)
	
		rel_label.to_corner(DOWN + LEFT)
		
		self.play(
			Write(rel_label[1]),
			Write(rel_label[3])
			)
		self.play(
			ReplacementTransform(rightStart_label.copy(),rel_label[4]),
			ReplacementTransform(leftStart_label.copy(),rel_label[2])
			)
		self.play(
			ReplacementTransform(route.copy(),rel_label[0])
			)
		self.wait()
		
		
	
