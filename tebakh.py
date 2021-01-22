#!/usr/bin/env python

from manimlib.imports import *

class Sum(Scene):
    def construct(self):
        teks = TextMobject("First way to prove it")
        self.play(Write(teks))
        self.wait()

        teks2 = TextMobject("Let")
        teks2.shift(1.5*UP + 2*LEFT)
        pers = TexMobject("A", "=", "1-1+1-1+1...")
        pers2 = TexMobject("B", "=", "1-2+3-4+5...")
        pers3 = TexMobject("C", "=", "1+2+3+4+5...")
        kumpulanpers = VGroup(pers, pers2, pers3).arrange(DOWN)
        self.add(teks2, pers, pers2, pers3)
        self.play(
            LaggedStart(*map(FadeOutAndShiftDown, teks)),
            Write(teks2),
            FadeInFromDown(kumpulanpers)
        )
        self.wait(2.5)

        self.play(
            LaggedStart(*map(FadeOutAndShiftDown, teks2)),
            LaggedStart(*map(FadeOutAndShiftDown, kumpulanpers))
        )
        self.wait()

        persm = TexMobject("A = 1-1+1-1+1...")
        self.play(FadeInFromDown(persm))
        self.wait()
        persm2 = TexMobject("1-A = 1-(1-1+1-1+1...)")
        self.play(ReplacementTransform(persm, persm2))
        self.wait()
        persm3 = TexMobject("1-A = 1-1+1-1+1...")
        self.play(ReplacementTransform(persm2, persm3))
        self.wait()
        persm4 = TexMobject("1-A = A")
        self.play(ReplacementTransform(persm3, persm4))
        self.wait()
        persm5 = TexMobject("1 = 2A")
        self.play(ReplacementTransform(persm4, persm5))
        self.wait()
        persm6 = TexMobject("\\frac{1}{2} = A")
        self.play(ReplacementTransform(persm5, persm6))
        self.wait()

        self.play(LaggedStart(*map(FadeOutAndShiftDown, persm6)))
        self.wait()

        persm_2 = TexMobject("B=1-2+3-4+5...")
        self.play(FadeInFromDown(persm_2))
        self.wait()
        persm_22 = TexMobject("A-B=(1-1+1...)-(1-2+3...)")
        self.play(ReplacementTransform(persm_2, persm_22))
        self.wait()
        persm_23 = TexMobject("A-B=1-2+3-4...")
        self.play(ReplacementTransform(persm_22, persm_23))
        self.wait()
        persm_24 = TexMobject("A-B=B")
        self.play(ReplacementTransform(persm_23, persm_24))
        self.wait()
        persm_25 = TexMobject("\\frac{1}{2}=2B")
        self.play(ReplacementTransform(persm_24, persm_25))
        self.wait()
        persm_26 = TexMobject("\\frac{1}{4}=B")
        self.play(ReplacementTransform(persm_25, persm_26))
        self.wait()

        self.play(LaggedStart(*map(FadeOutAndShiftDown, persm_26)))
        self.wait()

        persm_3 = TexMobject("C = 1+2+3+4+5...")
        self.play(FadeInFromDown(persm_3))
        self.wait()
        persm_32 = TexMobject("B-C = (1-2+3-4...)-(1+2+3+4...)")
        self.play(ReplacementTransform(persm_3, persm_32))
        self.wait()
        persm_33 = TexMobject("B-C = -4-8-12-16...")
        self.play(ReplacementTransform(persm_32, persm_33))
        self.wait()
        persm_34 = TexMobject("B-C = -4(1+2+3...)")
        self.play(ReplacementTransform(persm_33, persm_34))
        self.wait()
        persm_35 = TexMobject("B-C = -4C")
        self.play(ReplacementTransform(persm_34, persm_35))
        self.wait()
        persm_36 = TexMobject("\\frac{1}{4} = -3C")
        self.play(ReplacementTransform(persm_35, persm_36))
        self.wait()
        persm_37 = TexMobject("-\\frac{1}{12}=C")
        self.play(ReplacementTransform(persm_36, persm_37))
        self.wait(2.5)

class Sum2(Scene):
    def construct(self):
        teks = TextMobject("Another way to prove it")
        self.play(Write(teks))
        self.wait()

        teks2 = TextMobject("Let")
        teks2.shift(1.8*UP+1.5*LEFT)
        eq = TexMobject("S = 1+","2+3+4","+5+6+7\\\\","+8+9+10","+11+12+13\\\\","...")
        self.play(
            LaggedStart(*map(FadeOutAndShiftDown, teks)),
            Write(teks2),
            FadeInFromDown(eq)
        )
        self.wait()

        frame1 = SurroundingRectangle(eq[1], buff=.1)
        frame2 = SurroundingRectangle(eq[2], buff=.1)
        frame3 = SurroundingRectangle(eq[3], buff=.1)
        frame4 = SurroundingRectangle(eq[4], buff=.1)
        frame2.set_color(YELLOW_A)
        frame3.set_color(GREEN_B)
        frame4.set_color(MAROON_C)
        self.play(
            ShowCreation(frame1),
            ShowCreation(frame2),
            ShowCreation(frame3),
            ShowCreation(frame4)
        )
        self.wait()

        a = TexMobject('9')
        b = TexMobject('18')
        c = TexMobject('27')
        d = TexMobject('36')
        a.next_to(frame1, UP)
        b.next_to(frame2, UP)
        c.next_to(frame3, DOWN)
        d.next_to(frame4, DOWN)
        self.play(
            FadeInFrom(a, UP),
            FadeInFrom(b, UP),
            FadeInFrom(c, DOWN),
            FadeInFrom(d, DOWN)
        )
        self.wait(2.5)

        self.remove(a, b, c, d)
        self.play(
            Uncreate(frame1),
            Uncreate(frame2),
            Uncreate(frame3),
            Uncreate(frame4)
        )
        self.wait()

        eq2 = TexMobject("S = 1+9+18+27+36+...")
        self.play(LaggedStart(*map(FadeOutAndShiftDown, teks2)), ReplacementTransform(eq, eq2))
        self.wait()
        eq3 = TexMobject("S = 1+9(1+2+3+4...)")
        self.play(ReplacementTransform(eq2, eq3))
        self.wait()
        eq4 = TexMobject("S = 1+9S")
        self.play(ReplacementTransform(eq3, eq4))
        self.wait()
        eq5 = TexMobject("-8S = 1")
        self.play(ReplacementTransform(eq4, eq5))
        self.wait()
        eq6 = TexMobject("S = -\\frac{1}{8}")
        self.play(ReplacementTransform(eq5, eq6))
        self.wait(2.5)
