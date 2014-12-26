#!/usr/bin/env python3
# -*- coding: utf-8-unix -*-

import datetime
import gantt

t1 = gantt.Task(name='tache1', start=datetime.date(2014, 12, 25), duration=4, percent_done=44, ressources=["Alexandre"])
t2 = gantt.Task(name='tache2', start=datetime.date(2014, 12, 28), duration=6)
t7 = gantt.Task(name='tache7', start=datetime.date(2014, 12, 28), duration=5, percent_done=50)
t3 = gantt.Task(name='tache3', start=datetime.date(2014, 12, 25), duration=4, depends_of=[t1, t7, t2])
t4 = gantt.Task(name='tache4', start=datetime.date(2015, 01, 01), duration=4, depends_of=t1)
t5 = gantt.Task(name='tache5', start=datetime.date(2014, 12, 23), duration=3)
t6 = gantt.Task(name='tache6', start=datetime.date(2014, 12, 25), duration=4, depends_of=t7, ressources=["Alexandre"])
t8 = gantt.Task(name='tache8', start=datetime.date(2014, 12, 25), duration=4, depends_of=t7, ressources=["Alexandre", "JLS"])


p1 = gantt.Project(name='Projet 1')
p1.add_task(t1)
p1.add_task(t7)
p1.add_task(t2)
p1.add_task(t3)
p1.add_task(t5)
p1.add_task(t8)



p2 = gantt.Project(name='Projet 2', color='#FFFF40')
p2.add_task(t2)
p2.add_task(t4)

p = gantt.Project(name='Gantt')
p.add_task(p1)
p.add_task(p2)
p.add_task(t6)




##########################$ MAKE DRAW ###############
p.make_svg_for_tasks(filename='test_full.svg', today=datetime.date(2014, 12, 31), start=datetime.date(2014, 12, 22), end=datetime.date(2015, 01, 14))
p.make_svg_for_tasks(filename='test_full2.svg', today=datetime.date(2014, 12, 31))
p.make_svg_for_tasks(filename='test.svg', today=datetime.date(2014, 12, 31), start=datetime.date(2015, 01, 3), end=datetime.date(2015, 01, 06))
p1.make_svg_for_tasks(filename='test_p1.svg', today=datetime.date(2014, 12, 31))
p2.make_svg_for_tasks(filename='test_p2.svg', today=datetime.date(2014, 12, 31))
##########################$ MAKE DRAW ###############
