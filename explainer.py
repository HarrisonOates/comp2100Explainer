from manim import *

class RedBlackTree(MovingCameraScene):
    def construct(self):
        # Create title
        titlepage = Text("Let's learn about Red-Black Trees")

        self.play(Write(titlepage, run_time = 5))
        self.wait(2)
        self.play(Unwrite(titlepage))

        # Create the initial tree
        pointlist = Tex("[11,7,3,2,5,6,13]")
        self.play(Write(pointlist))
        self.wait()
        newpointlist =  Tex("[2,3,5,6,7,11,13]")
        self.play(ReplacementTransform(pointlist,newpointlist))
        self.wait()
        self.play(Unwrite(newpointlist))
        self.wait()

        # The worst-case tree
        node_2 = Circle(fill_opacity=1, radius=0.3, color=BLUE)
        node_2_label = Text("2", font_size=20).next_to(node_2, DOWN, buff=0.2)

        node_3 = Circle(fill_opacity=1, radius=0.3, color=BLUE).next_to(node_2, RIGHT+DOWN, buff=1)
        node_3_label = Text("3", font_size=20).next_to(node_3, DOWN, buff=0.2)

        node_5 = Circle(fill_opacity=1, radius=0.3, color=BLUE).next_to(node_3, RIGHT+DOWN, buff=1)
        node_5_label = Text("5", font_size=20).next_to(node_5, DOWN, buff=0.2)

        node_6 = Circle(fill_opacity=1, radius=0.3, color=BLUE).next_to(node_5, RIGHT+DOWN, buff=1)
        node_6_label = Text("6", font_size=20).next_to(node_6, DOWN, buff=0.2)

        node_7 = Circle(fill_opacity=1, radius=0.3, color=BLUE).next_to(node_6, RIGHT + DOWN, buff=1)
        node_7_label = Text("7", font_size=20).next_to(node_7, DOWN, buff=0.2)
        # Create left subtree
        
        
        left_arrow1 = Arrow(node_2, node_3, buff=0.1)
        left_arrow2 = Arrow(node_3, node_5, buff=0.1)
        left_arrow3 = Arrow(node_5, node_6, buff=0.1)
        left_arrow4 = Arrow(node_6, node_7, buff=0.1)
        
        # Create right subtree
        node_11 = Circle(fill_opacity=1, radius=0.3, color=BLUE).next_to(node_7, RIGHT+DOWN, buff=1)
        node_11_label = Text("11", font_size=20).next_to(node_11, DOWN, buff=0.2)
        
        node_13 = Circle(fill_opacity=1, radius=0.3, color=BLUE).next_to(node_11, RIGHT+DOWN, buff=1)
        node_13_label = Text("13", font_size=20).next_to(node_13, DOWN, buff=0.2)
        
        right_arrow1 = Arrow(node_7, node_11, buff=0.1)
        right_arrow2 = Arrow(node_11, node_13, buff=0.1)

        self.play(self.camera.frame.animate.scale(1.5).move_to(node_6))
        self.play(
            Create(node_7),
            Create(node_7_label),
            Create(node_3),
            Create(node_3_label),
            Create(node_2),
            Create(node_2_label),
            Create(node_5),
            Create(node_5_label),
            Create(node_6),
            Create(node_6_label),
            Create(left_arrow1),
            Create(left_arrow2),
            Create(left_arrow3),
            Create(left_arrow4),
            Create(node_11),
            Create(node_11_label),
            Create(node_13),
            Create(node_13_label),
            Create(right_arrow1),
            Create(right_arrow2)
        )

        self.wait(4)

        # Highlighting visiting each node
        # Going to go to 13
        caption = Text("Let's see if 13 is in the tree")
        self.play(Write(caption.next_to(node_2, 2*RIGHT)))
        counter = 1
        displayCounter = Text(str(counter))
        travelingCircle1 = Circle(fill_opacity=0, radius = 0.3, color = RED)
        travelingCircle2 = Circle(fill_opacity=0, radius = 0.3, color = RED).next_to(travelingCircle1, RIGHT + DOWN, buff = 1)
        travelingCircle3 = Circle(fill_opacity=0, radius = 0.3, color = RED).next_to(travelingCircle2, RIGHT + DOWN, buff = 1)
        travelingCircle4 = Circle(fill_opacity=0, radius = 0.3, color = RED).next_to(travelingCircle3, RIGHT + DOWN, buff = 1)
        travelingCircle5 = Circle(fill_opacity=0, radius = 0.3, color = RED).next_to(travelingCircle4, RIGHT + DOWN, buff = 1)
        travelingCircle6 = Circle(fill_opacity=0, radius = 0.3, color = RED).next_to(travelingCircle5, RIGHT + DOWN, buff = 1)
        travelingCircle7 = Circle(fill_opacity=0, radius = 0.3, color = RED).next_to(travelingCircle6, RIGHT + DOWN, buff = 1)
        location = RIGHT + DOWN
        self.play(Create(travelingCircle1))
        self.play(ReplacementTransform(travelingCircle1, travelingCircle2))
        self.play(ReplacementTransform(travelingCircle2, travelingCircle3))
        self.play(ReplacementTransform(travelingCircle3, travelingCircle4))
        self.play(ReplacementTransform(travelingCircle4, travelingCircle5))
        self.play(ReplacementTransform(travelingCircle5, travelingCircle6))
        self.play(ReplacementTransform(travelingCircle6, travelingCircle7))
        self.wait()
        self.play(
            FadeOut(node_2),
            FadeOut(node_2_label),
            FadeOut(node_3),
            FadeOut(node_3_label),
            FadeOut(node_5),
            FadeOut(node_5_label),
            FadeOut(node_6),
            FadeOut(node_6_label),
            FadeOut(node_7),
            FadeOut(node_7_label),
            FadeOut(node_11),
            FadeOut(node_11_label),
            FadeOut(node_13),
            FadeOut(node_13_label),
            FadeOut(left_arrow1),
            FadeOut(left_arrow2),
            FadeOut(left_arrow3),
            FadeOut(left_arrow4),
            FadeOut(right_arrow1),
            FadeOut(right_arrow2),
            FadeOut(caption),
            FadeOut(travelingCircle7)
        )



        sectionTitle = Title("But what if we could guarantee worst case performance?")
        self.play(self.camera.frame.animate.scale(1).move_to(sectionTitle))
        self.wait()
        self.play(Write(sectionTitle))

        self.wait(10)




        # The red-black tree initial
        node_3 = Circle(fill_opacity=1, radius=0.3, color=GREY)
        node_3_label = Text("3", font_size=20).next_to(node_3, DOWN, buff=0.2)

        node_2 = Circle(fill_opacity=1, radius=0.3, color=GREY).next_to(node_3, LEFT+DOWN, buff=1)
        node_2_label = Text("2", font_size=20).next_to(node_2, DOWN, buff=0.2)

        node_6 = Circle(fill_opacity=1, radius=0.3, color=RED).next_to(node_3, RIGHT+DOWN, buff=1)
        node_6_label = Text("6", font_size=20).next_to(node_6, DOWN, buff=0.2)

        node_5 = Circle(fill_opacity=1, radius=0.3, color=GREY).next_to(node_6, LEFT+DOWN, buff=1)
        node_5_label = Text("5", font_size=20).next_to(node_5, DOWN, buff=0.2)

        node_11 = Circle(fill_opacity=1, radius=0.3, color=GREY).next_to(node_6, RIGHT+DOWN, buff=1)
        node_11_label = Text("11", font_size=20).next_to(node_11, DOWN, buff=0.2)

        # Create node_7 node
        node_7 = Circle(fill_opacity=1, radius=0.3, color=RED).next_to(node_11, LEFT+DOWN, buff=1)
        node_7_label = Text("7", font_size=20).next_to(node_7, DOWN, buff=0.2)

        node_13 = Circle(fill_opacity=1, radius=0.3, color=RED).next_to(node_11, RIGHT+DOWN, buff=1)
        node_13_label = Text("13", font_size=20).next_to(node_13, DOWN, buff=0.2)
        
        # Arrows
        left_arrow1 = Arrow(node_3, node_2, buff=0.1)
        left_arrow2 = Arrow(node_3, node_6, buff=0.1)
        left_arrow3 = Arrow(node_6, node_5, buff=0.1)
        left_arrow4 = Arrow(node_6, node_11, buff=0.1)
        right_arrow1 = Arrow(node_11, node_7, buff=0.1)
        right_arrow2 = Arrow(node_11, node_13, buff=0.1)

        # Add all nodes and arrows to the scene
        self.play(self.camera.frame.animate.scale(1.5).move_to(node_6))

        redBlackRequirements = Text("Required properties of Red-Black Trees\n1. Every node is either red or black\n2. All null nodes, and the root node, are considered black\n3. A red node does not have a red child\n4. Every path from node to leaf contains the same number of black nodes", font_size = 30)
        self.play(Write(redBlackRequirements.next_to(node_3, RIGHT + RIGHT, buff = 1), run_time = 20))
        self.wait(5)
        self.play(
            Create(node_7),
            Create(node_7_label),
            Create(node_3),
            Create(node_3_label),
            Create(node_2),
            Create(node_2_label),
            Create(node_5),
            Create(node_5_label),
            Create(node_6),
            Create(node_6_label),
            Create(left_arrow1),
            Create(left_arrow2),
            Create(left_arrow3),
            Create(left_arrow4),
            Create(node_11),
            Create(node_11_label),
            Create(node_13),
            Create(node_13_label),
            Create(right_arrow1),
            Create(right_arrow2)
        )

        self.wait(5)
        # Check for 13
        travelingCircle1 = Circle(fill_opacity=0, radius = 0.3, color = GREEN)
        travelingCircle2 = Circle(fill_opacity=0, radius = 0.3, color = GREEN).next_to(travelingCircle1, RIGHT + DOWN, buff = 1)
        travelingCircle3 = Circle(fill_opacity=0, radius = 0.3, color = GREEN).next_to(travelingCircle2, RIGHT + DOWN, buff = 1)
        travelingCircle4 = Circle(fill_opacity=0, radius = 0.3, color = GREEN).next_to(travelingCircle3, RIGHT + DOWN, buff = 1)
        self.play(ReplacementTransform(travelingCircle1, travelingCircle2))
        self.wait()
        self.play(ReplacementTransform(travelingCircle2, travelingCircle3))
        self.wait()
        self.play(ReplacementTransform(travelingCircle3, travelingCircle4))
        self.wait()
        self.play(FadeOut(travelingCircle4))



        self.wait(7)
        # But what if we want to add another node?
        node_1 = Circle(fill_opacity=1, radius=0.3, color=RED).next_to(node_2, LEFT+DOWN, buff=1)
        node_1_label = Text("1", font_size=20).next_to(node_1, DOWN, buff=0.2)
        left_arrow5 = Arrow(node_2, node_1, buff=0.1)

        travelingCircle1 = Circle(fill_opacity=0, radius = 0.3, color = GREEN)
        travelingCircle2 = Circle(fill_opacity=0, radius = 0.3, color = GREEN).next_to(travelingCircle1, LEFT + DOWN, buff = 1)
        travelingCircle3 = Circle(fill_opacity=0, radius = 0.3, color = GREEN).next_to(travelingCircle2, LEFT + DOWN, buff = 1)
        self.play(ReplacementTransform(travelingCircle1, travelingCircle2))
        self.wait()
        self.play(ReplacementTransform(travelingCircle2, travelingCircle3))
        self.wait()
        self.play(ReplacementTransform(travelingCircle3, node_1))
        self.play(Create(node_1_label))
        self.play(Create(left_arrow5))
        self.wait()

        # But what if we insert a node that interrupts the colouring scheme?
        node_12 = Circle(fill_opacity=1, radius=0.3, color=RED).next_to(node_13, LEFT+DOWN, buff=1)
        node_12_label = Text("12", font_size=20).next_to(node_12, DOWN, buff=0.2)
        left_arrow6 = Arrow(node_13, node_12)

        travelingCircle1 = Circle(fill_opacity=0, radius = 0.3, color = GREEN)
        travelingCircle2 = Circle(fill_opacity=0, radius = 0.3, color = GREEN).next_to(travelingCircle1, RIGHT + DOWN, buff = 1)
        travelingCircle3 = Circle(fill_opacity=0, radius = 0.3, color = GREEN).next_to(travelingCircle2, RIGHT + DOWN, buff = 1)
        travelingCircle4 = Circle(fill_opacity=0, radius = 0.3, color = GREEN).next_to(travelingCircle3, RIGHT + DOWN, buff = 1)
        self.play(ReplacementTransform(travelingCircle1, travelingCircle2))
        self.wait()
        self.play(ReplacementTransform(travelingCircle2, travelingCircle3))
        self.wait()
        self.play(ReplacementTransform(travelingCircle3, travelingCircle4))
        self.wait()
        self.play(ReplacementTransform(travelingCircle4, node_12))
        self.play(Create(node_12_label))
        self.play(Create(left_arrow6))
        self.wait(5)
        # We need to recolour the tree.

        self.play(FadeToColor(node_13, color = GREY),
                FadeToColor(node_7, color = GREY),
                FadeToColor(node_11, color = RED),
            )
        self.wait(9)
        # We can't push redness any further up the tree, so we need to rotate.
        
        node_6q = Circle(fill_opacity=1, radius=0.3, color=GREY)
        node_6_labelq = Text("6", font_size=20).next_to(node_3, DOWN, buff=0.2)

        node_3q = Circle(fill_opacity=1, radius=0.3, color=RED).next_to(node_6q, 2*LEFT + DOWN, buff=1)
        node_3_labelq = Text("3", font_size=20).next_to(node_3q, DOWN, buff=0.2)

        node_2q = Circle(fill_opacity=1, radius=0.3, color=GREY).next_to(node_3q, LEFT + DOWN, buff=1)
        node_2_labelq = Text("2", font_size=20).next_to(node_2q, DOWN, buff=0.2)
        
        node_1q = Circle(fill_opacity=1, radius=0.3, color=RED).next_to(node_2q, LEFT+DOWN, buff=1)
        node_1_labelq = Text("1", font_size=20).next_to(node_1q, DOWN, buff=0.2)

        node_5q = Circle(fill_opacity=1, radius=0.3, color=GREY).next_to(node_3q, RIGHT+DOWN, buff=1)
        node_5_labelq = Text("5", font_size=20).next_to(node_5q, DOWN, buff=0.2)

        node_11q = Circle(fill_opacity=1, radius=0.3, color=RED).next_to(node_6q, 2*RIGHT+DOWN, buff=1)
        node_11_labelq = Text("11", font_size=20).next_to(node_11q, DOWN, buff=0.2)

        # Create node_7 node
        node_7q = Circle(fill_opacity=1, radius=0.3, color=GREY).next_to(node_11q, LEFT+DOWN, buff=1)
        node_7_labelq = Text("7", font_size=20).next_to(node_7q, DOWN, buff=0.2)

        node_13q = Circle(fill_opacity=1, radius=0.3, color=GREY).next_to(node_11q, RIGHT+DOWN, buff=1)
        node_13_labelq = Text("13", font_size=20).next_to(node_13q, DOWN, buff=0.2)

        node_12q = Circle(fill_opacity=1, radius=0.3, color=RED).next_to(node_13q, LEFT+DOWN, buff=1)
        node_12_labelq = Text("12", font_size=20).next_to(node_12q, DOWN, buff=0.2)

        left_arrow1q = Arrow(node_3q, node_2q, buff=0.1)
        left_arrow2q = Arrow(node_6q, node_3q, buff=0.1)
        left_arrow3q = Arrow(node_3q, node_5q, buff=0.1)
        left_arrow4q = Arrow(node_6q, node_11q, buff=0.1)
        left_arrow5q = Arrow(node_2q, node_1q, buff=0.1)
        left_arrow6q = Arrow(node_13q, node_12q)
        right_arrow1q = Arrow(node_11q, node_7q, buff=0.1)
        right_arrow2q = Arrow(node_11q, node_13q, buff=0.1)

        self.play(ReplacementTransform(node_6, node_6q),
            ReplacementTransform(node_3, node_3q),
            ReplacementTransform(node_2, node_2q),
            ReplacementTransform(node_1, node_1q),
            ReplacementTransform(node_5, node_5q),
            ReplacementTransform(node_11, node_11q),
            ReplacementTransform(node_7, node_7q),
            ReplacementTransform(node_13,node_13q),
            ReplacementTransform(node_12, node_12q),

            ReplacementTransform(node_6_label, node_6_labelq),
            ReplacementTransform(node_3_label, node_3_labelq),
            ReplacementTransform(node_2_label, node_2_labelq),
            ReplacementTransform(node_1_label, node_1_labelq),
            ReplacementTransform(node_5_label, node_5_labelq),
            ReplacementTransform(node_11_label, node_11_labelq),
            ReplacementTransform(node_7_label, node_7_labelq),
            ReplacementTransform(node_13_label, node_13_labelq),
            ReplacementTransform(node_12_label, node_12_labelq),
            ReplacementTransform(left_arrow1, left_arrow1q),
            ReplacementTransform(left_arrow2, left_arrow2q),
            ReplacementTransform(left_arrow3, left_arrow3q),
            ReplacementTransform(left_arrow4, left_arrow4q),
            ReplacementTransform(left_arrow5, left_arrow5q),
            ReplacementTransform(left_arrow6, left_arrow6q),
            ReplacementTransform(right_arrow1, right_arrow1q),
            ReplacementTransform(right_arrow2, right_arrow2q)
        )
        self.wait(20)
        fadeanims = [
            FadeOut(node_6q),
            FadeOut(node_3q),
            FadeOut(node_1q),
            FadeOut(node_5q),
            FadeOut(node_11q),
            FadeOut(node_7q),
            FadeOut(node_13q),
            FadeOut(node_12q),
            FadeOut(node_2q),
            FadeOut(node_6_labelq),
            FadeOut(node_3_labelq),
            FadeOut(node_1_labelq),
            FadeOut(node_5_labelq),
            FadeOut(node_11_labelq),
            FadeOut(node_7_labelq),
            FadeOut(node_13_labelq),
            FadeOut(node_12_labelq),
            FadeOut(node_2_labelq),
            FadeOut(left_arrow1q),
            FadeOut(left_arrow2q),
            FadeOut(left_arrow3q),
            FadeOut(left_arrow4q),
            FadeOut(left_arrow5q),
            FadeOut(left_arrow6q),
            FadeOut(right_arrow1q),
            FadeOut(right_arrow2q), 
            FadeOut(sectionTitle),
            FadeOut(redBlackRequirements),
        ]

        self.play(AnimationGroup(*fadeanims))
        self.wait()
        self.play(self.camera.frame.animate.scale(1).move_to(ORIGIN))

        sectionTitle = Title("Today we saw how Red-Black trees guarantee {$\mathcal{O} (\log n)$} search")
        acknowledgement = Text("Made by Harrison Oates with the Manim library.")
        source = Text("Source code in the description.").next_to(acknowledgement, DOWN, buff = 1)

        self.play(Create(sectionTitle))
        self.wait()
        self.play(Create(acknowledgement), Create(source))
        self.wait(10)
        self.play(Uncreate(acknowledgement), Uncreate(source))
        self.wait()
