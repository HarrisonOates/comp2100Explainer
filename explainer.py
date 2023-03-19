from manim import *

class RedBlackTree(MovingCameraScene):
    def construct(self):
        # Create title
        titlepage = Text("Let's learn about Red-Black Trees")

        self.play(Write(titlepage, run_time = 4))
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
        self.clear()
        sectionTitle = Title("But what if we could guarantee worst case performance?")
        self.play(self.camera.frame.animate.scale(1).move_to(sectionTitle))
        self.wait()
        self.play(Write(sectionTitle))

        self.wait()




        # The red-black tree initial
        node_3 = Circle(fill_opacity=1, radius=0.3, color=GREY)
        node_3_label = Text("3", font_size=20).next_to(node_3, DOWN, buff=0.2)

        node_2 = Circle(fill_opacity=1, radius=0.3, color=GREY).next_to(node_3, LEFT+DOWN, buff=1)
        node_2_label = Text("2", font_size=20).next_to(node_2, DOWN, buff=0.2)

        node_6 = Circle(fill_opacity=1, radius=0.3, color=RED).next_to(node_3, RIGHT+DOWN, buff=1)
        node_6_label = Text("6", font_size=20).next_to(node_6, DOWN, buff=0.2)

        node_5 = Circle(fill_opacity=1, radius=0.3, color=GREY).next_to(node_6, LEFT+DOWN, buff=1)
        left_node3_label = Text("5", font_size=20).next_to(node_5, DOWN, buff=0.2)

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

        redBlackRequirements = Text("Required properties of Red-Black Trees\n1. Every node is either red or black\n2. All null nodes are considered black\n3. The root node is always black\n4. A red node does not have a red child\n5. The count of black nodes to leaves should be equal", font_size = 30)
        self.play(Write(redBlackRequirements.next_to(node_3, RIGHT + RIGHT, buff = 1), run_time = 15))
        self.wait()
        self.play(
            Create(node_7),
            Create(node_7_label),
            Create(node_3),
            Create(node_3_label),
            Create(node_2),
            Create(node_2_label),
            Create(node_5),
            Create(left_node3_label),
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