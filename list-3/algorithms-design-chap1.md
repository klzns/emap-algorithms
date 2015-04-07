## Exercise 1
> Decide whether you think the following statement is true or false. If it is true, give a short explanation. If it is false, give a counterexample.

> True or false? In every instance of the Stable Matching Problem, there is a stable matching containing a pair (m, w) such that m is ranked first on the preference list of w and w is ranked first on the preference list of m.

Falso, tomemos como contra-exemplo um grupo m com a lista de preferências:

m|1º|2º
---|---|---
m'| w'| w"
m"| w"| w'

E um grupo w com a lista de preferências:

w|1º|2º
---|---|---
w'| m"| m'
w"| m'| m"

O algoritmo de Gale-Shapley iria formar os pares: (m',w') e (m",w"). Com isso, não teríamos nenhum par no qual os dois indíviduos possuem a pessoa predileta de sua lista de preferências.



## Exercise 3
> There are many other settings in which we can ask questions related to some type of “stability” principle. Here’s one, involving competition between two enterprises.

> Suppose we have two television networks, whom we’ll call A and B. There are n prime-time programming slots, and each network has n TV shows. Each network wants to devise a schedule—an assignment of each show to a distinct slot—so as to attract as much market share as possible.

> Here is the way we determine how well the two networks perform relative to each other, given their schedules. Each show has a fixed rating, which is based on the number of people who watched it last year; we’ll assume that no two shows have exactly the same rating. A network wins a given time slot if the show that it schedules for the time slot has a larger rating than the show the other network schedules for that time slot. The goal of each network is to win as many time slots as possible.

> Suppose in the opening week of the fall season, Network A reveals a schedule S and Network B reveals a schedule T. On the basis of this pair of schedules, each network wins certain time slots, according to the rule above. We’ll say that the pair of schedules (S, T) is stable if neither network can unilaterally change its own schedule and win more time slots. That is, there is no schedule S' such that Network A wins more slots with the pair (S', T) than it did with the pair (S, T); and symmetrically, there is no schedule T' such that Network B wins more slots with the pair (S, T') than it did with the pair (S, T).

> The analogue of Gale and Shapley’s question for this kind of stability is the following: For every set of TV shows and ratings, is there always a stable pair of schedules? Resolve this question by doing one of the following two things:

> (a) give an algorithm that, for any set of TV shows and associated ratings, produces a stable pair of schedules; or

> (b) give an example of a set of TV shows and associated ratings for which there is no stable pair of schedules.


Resolvendo pelo item (b).

Dado que a Network A possui duas agendas, S e S', e a Network B possui duas agendas, T e T'. Cada agenda tem sua ordem de prefência de agenda para competir por pontos de audiência, ou seja, a agenda S tem como preferência T, pois ganha mais audiência do que ela, e T tem como preferência S', pois ganha mais audiência do que ela.

Network A

Agenda|Ganha|Perde
---|---|---
S | T | T'
S'| T' | T

Network B

Agenda| Ganha | Perde
---|---|---
T | S'| S
T'| S | S'

Ao formar o par de agendas (S, T), temos que existe uma agenda T' no qual a Network B ganhará mais audiência que T, sendo assim instável.



## Exercise 4

> Gale and Shapley published their paper on the Stable Matching Problem in 1962; but a version of their algorithm had already been in use for ten years by the National Resident Matching Program, for the problem of assigning medical residents to hospitals.

> Basically, the situation was the following. There were m hospitals, each with a certain number of available positions for hiring residents. There were n medical students graduating in a given year, each interested in joining one of the hospitals. Each hospital had a ranking of the students in order of preference, and each student had a ranking of the hospitals in order of preference. We will assume that there were more students graduating than there were slots available in the m hospitals.

> The interest, naturally, was in finding a way of assigning each student to at most one hospital, in such a way that all available positions in all hospitals were filled. (Since we are assuming a surplus of students, there would be some students who do not get assigned to any hospital.)

> We say that an assignment of students to hospitals is stable if neither of the following situations arises.

> First type of instability: There are students s and s', and a hospital h, so that:
- s is assigned to h, and
- s' is assigned to no hospital, and
- h prefers s' to s.

> Second type of instability: There are students s and s', and hospitals h and h', so that:
- s is assigned to h, and
– s' is assigned to h', and
- h prefers s' to s, and
- s' prefers h to h'.

> So we basically have the Stable Matching Problem, except that (i) hospitals generally want more than one resident, and (ii) there is a surplus of medical students.

> Show that there is always a stable assignment of students to hospitals, and give an algorithm to find one.


