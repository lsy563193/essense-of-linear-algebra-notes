## 什么是四元数

### 四元数的故事 
what you were looking at right now is something called quaternion multiplication, or rather ,you're looking at a certain representation of a specific motion happening on a four-dimensional sphere being represented in our three-dimensional space, one which he'll understand by the end of this video.

你现在看到的是四元数乘法，或者更确切地说，你正在观察在我们的三维空间中表现的四维球体上发生的特定运动的某种表示。 在本视频结束时你会理解这个概念。

quaternion are an absolutely fascinating and often underappreciated number system from math. just as complex numbers are a two-dimensional extension of the real numbers, quaternions are a four dimensional extension of complex numbers. but they're not just playful mathematical shenanigans, they have a surprisingly pragmatic utility for describing rotation in three dimensions, and even for quantum mechanics.

四元数是一个绝对迷人且经常被低估的数学系统。 正如复数是实数的二维扩展一样，四元数是复数的四维扩展。 但它们不仅仅是有趣的数学诡计，它们具有令人惊讶的实用性，可用于描述三维旋转，甚至是量子力学。

the story of their discovery is also quite famous in math. the Irish mathematician William Rowan Hamilton spent much of his life seeking a three dimensional number system analogous to the complex numbers. and as the story goes, his son would ask him every morning whether or not he had figured out how to divide triples, and he would always say no not yet. but on October 16th 1843, while crossing the Broome bridge in Dublin, he realized what they supposed flash of insight, that what he needed was not to add a single dimension to the complex numbers, but to add two more imaginary dimensions. three imaginary dimensions describing space, and the real numbers sitting perpendicular to that in some kind of fourth dimension. he carved the crucial equation describing these three imaginary units into the bridge, which today bears a plaque in his honor showing that equation. now you have to understand our modern notion of "vectors" with their "dot product" and the "cross product" and things like that didn't really exist in Hamilton's time, at least not in a standardized form. so after his discovery, he pushed hard for quaternion to be the primary language with which we teach students to describe three-dimensional space. even forming an official quaternion society to proselytize his discovery.

他们的发现故事在数学方面也很有名。爱尔兰数学家威廉罗恩汉密尔顿一生中大部分时间都在寻求类似于复数的三维数字系统。正如故事所说，他的儿子每天早上会问他是否已经弄清楚如何划分三倍，并且他总是会说不。但是在1843年10月16日，当他穿过都柏林的布鲁姆桥时，他意识到他们所谓的闪光洞察力，他所需要的不是为复数增加一个维度，而是增加两个想象的维度。描述空间的三个虚构维度，以及与某种第四维度垂直的实数。他把描述这三个想象单位的关键等式刻在桥上，今天有一块牌匾用于表示这个等式。现在你必须了解我们现代的“矢量”概念及其“点积”和“叉积”以及类似的东西,在汉密尔顿的时代并不存在，至少不是标准化的形式。所以在他被发现之后，他努力推动四元数成为我们教导学生描述三维空间的主要语言。甚至形成一个官方的四元数社区来传播他的发现。

now unfortunately, this was balanced with mathematicians on the other side of the fence, who believed that the confusing notion of quaternion multiplication was not necessary for describing three dimensions, resulting in some truly hilarious old-timey trash-talk legitimately calling them evil.

现在不幸的是，这与围栏另一侧的数学家相平衡，他们认为四元数乘法的混淆概念对于描述三个维度是不必要的，导致一些真正热闹的旧时垃圾谈话合法地称他们为邪恶。

it's even believed that the Mad Hatter scene from Alice in Wonderland (whose author ,you may know, was an Oxford mathematician) was written in reference to quaternions, that the chaotic table placement changes were mocking their multiplication, and that certain quotes were referencing their non commutative nature

它甚至认为来自爱丽丝梦游仙境（其作者，你可能知道，是牛津数学家）的Mad Hatter场景是参照四元数写的，混乱的表格位置变化嘲弄它们的乘法，并且某些引用引用了它们 非交换性

fast forward about a century, and the computing industry gave quaternions a resurgence, among programmers who work with graphics and robotics and anything involving orientation in 3d space. and this is because they give an elegant way to describe and compute 3d rotations, which is computationally more efficient than other methods, and which also avoids a lot of the numerical errors, that arise in these other methods. 

快进大约一个世纪，计算机行业让四元数复兴，在使用图形和机器人技术的程序员以及涉及三维空间定位的任何事物中。 这是因为它们提供了一种优雅的方式来描述和计算3d旋转，这在计算上比其他方法更有效，并且还避免了在这些其他方法中出现的许多数值误差。 

the 20th century also brought quaternion some more love, from a completely different direction quantum mechanics. you see the special actions the quaternions described in four dimensions are actually quite relevant to the way the two-state systems, like spin of an electron or the polarization of a photon are described mathematically.

20世纪也带来了四元数更多的爱，来自完全不同的量子力学方向。 你会看到四元数在四维中描述的特殊行为实际上与双态系统的方式非常相关，例如电子自旋或光子极化在数学上的描述。

### 可视化四元数

what I'll show you here is a way to visualize quaternions in their full four-dimensional. it would surprise me if this approach was fully original, but "+i" can say that it's certainly not the standard way to teach quaternions. and that the specific "four-dimensional right-hand-rule-image", that "+i"'d like to build up to, is something that "+i" haven't really seen elsewhere. building up an understanding for this visual will take us (meaningful) time, but once you have it, there is a very natural and satisfying intuition for how to think about quaternion multiplication. 

我将在这里向您展示的是一种在四维空间中可视化四元数的方法。 如果这种方法完全原创，我会感到惊讶，但我可以说它肯定不是教授四元数的标准方法。 并且我想要建立的特定的“四维右手规则图像”是我在其他地方没有真正看到的东西。 建立对这种视觉的理解将花费我们（有意义的）时间，但是一旦你拥有它，对于如何思考四元数乘法有一种非常自然和令人满意的直觉。

it won't be until the next video that "+i" show you how exactly quaternions describe orientation in three dimensions. which is for some people the whole reason we care about it. but once we're able to go at it armed with the image (of what they're doing to a 4d hyper sphere), there's a pleasing understanding to be had for the otherwise opaque formulas characterizing this relationship. the structure here will be to start (by imagining) teaching complex numbers to someone who only understands one dimension, then describing 3d rotations to someone who only understands two dimensions, and ultimately to represent what quaternions are doing up in four dimensions (within the constraints of our 3 dimensions space).

直到下一个视频，我才会向您展示四元数如何在三个维度中描述方向。 这对某些人来说是我们关心它的全部原因。 但是，一旦我们能够使用图像（他们正在对4d超球体所做的事情）进行操作，对于表征这种关系的其他不透明的公式，我们会有一种令人愉快的理解。 这里的结构将开始（通过想象）将复数教给那些只理解一个维度的人，然后将3d旋转描述给只理解两个维度的人，并最终表示四元数在三维空间的约束内在四维中的作用。

### Linus the lineLander
our first character is "Linus the lineLander" whose mind can only grasp the one dimensional geometry of lines in the algebra of real numbers.

我们的第一个角色是Linus，即Lander线，它的思维只能掌握实数代数中线条的一维几何。

 we're gonna try to describe complex members to Linus, and it's reallyimportant for you to empathize with him as much as you can during this ,because in a few minutes you're gonna be in his shoes. on the one hand you could define complex numbers purely algebraically. you say each one is expressed as some real number plus some other real number times "i",  where "i" is a newly invented constant whose defining property is that "i x i = -1". then you say to Linus to multiply two complex numbers, you just use the distributive property, what many people learn in school is ""FOIL". and you apply this rule that "i x i = -1" to simplify things down further, and that's fine, that totally works in the standard textbook way to introduce quaternions is analogous to this, showing the algebraic rules and calling it done. but "+i" think something is missing if we don't at least try to show Linus the geometry of complex numbers then what complex multiplication looks like. since the problems in math and physics we're ,complex numbers are shockingly useful, often leverage this spatial intuition. 

我们要试着向Linus描述一些复杂的成员，在这期间尽可能多地同情他是非常重要的，因为在几分钟之内你就会陷入困境。一方面，你可以纯粹代数地定义复数。你说每一个都表示为一些实数加上一些其他实数乘以“i”，其中“i”是一个新发明的常数，其定义属性是“ixi = -1”。然后你说Linus要增加两个复数，你只需要使用分配属性，很多人在学校里学到的就是“”FOIL“。你应用这个规则”i x i = -1“来进一步简化事情，这很好，完全按照标准教科书的方式引入四元数类似于此，显示代数规则并称之为完成。但我认为如果我们至少不试图向Linus展示复杂的几何形状，那么就会缺少某些东西然后是复数乘法的数字。因为数学和物理学中存在的问题，复数非常有用，通常会利用这种空间直觉。

you and I who understand two dimensions might think of it like this, when you multiply two complex numbers, Z times W, you can think of Z as a sort of function acting on W rotating and stretching it in some way, "+i" like to think of this by broadening the view and asking what does he do to the entire plane. and you can think of that bird's-"+i" view action, by imagining using one hand to fix the number 0 in place and using v another hand to drag the point at 1 up to Z. since anything times 0 is 0, and anything times 1 is itself, and in two dimensions there is one and only one stretching rotating action on the plane that'll do this. this is also how "+i"'ll have you thinking about quaternion multiplication later on. where the number on the Left acts as a kind of function to the one on the right, and we'll understand this function by seeing how it and so far it's probably not clear how exactly quaternion do describe 3d rotation. "+i" mean if you consider one of these actions on the unit sphere passing through "+i" J and K, it doesn't leave that sphere in place it morphs it out of position. so the way that this works is slightly more complicated than a single quaternion product. it involves a process called conjugation. and "+i"'ll make a full follow-on video all about it, so that we have the time to go through some examples in the meantime. for more information on the story of quaternions and their relation to orientation.

理解二维的你和我可能会想到这样，当你将两个复数相乘，"ZxW"，你可以将Z视为一种作用于W旋转并以某种方式拉伸它的函数，我喜欢思考通过扩大视野并询问他对整个平面做了什么。并且你可以想象那个鸟瞰视图动作，想象用一只手将数字0固定到位,并用另一只手将点拖动到1到Z.因为"v x 0 = 0，v x 1 = v"，在二维中，在平面上只有一个拉伸旋转动作，这样做。这也是我稍后会考虑四元数乘法的方法。左边的数字作为右边一个函数的一种函数，我们通过转换空间来看它是如何起作用的，而不是旋转2d空间，我们将理解这个函数。它在4d空间中进行一种双重旋转。

by the way, if you want to review thinking about complex numbers as a kind of action, a good warm-up for this video might be the one "+i" did on "e to the P"+i"" "+i" explained with introductory goop theory. now line is the line Lander is pretty comfortable with the idea of stretching， that's what multiplication by real numbers looks like maybe it's a little weird for him to think about stretching in multiple dimensions. but it's not fundamentally different. the difficult thing to communicate to Linus is rotation, specifically focus on the unit circle of the complex plane. all the numbers a distance one from zero, since multiplication by these numbers corresponds to pure rotation.

顺便说一句，如果你想回顾一下复数作为一种动作的看法，对于这个视频的一个很好的热身可能是我在“e to Pi and i"”上做的那个我用介绍性的goop理论解释的。 现在行是Lander对拉伸的想法非常舒服，这就是实数乘以看起来似乎对他来说考虑多维拉伸有点奇怪。 但它并没有根本不同。 与Linus沟通的难点是旋转，特别是关注复平面的单位圆。 所有数字与零的距离为1，因为乘以这些数字对应于纯旋转。

how would you explain to Linus the look and the feel of multiplying by these numbers . at first, that might seem impossible. "+i" mean rotation is just such an intrinsically two-dimensional idea. but on the other hand, rotation involves only one degree of freedom , a single number the angle specifies a given rotation uniquely. so in principle, it should be possible to associate the set of all rotations to the one dimensional continuum, that is  Linus's world. and there are many ways you could do this, but the one "+i"'m going to show you is what's called a stereographic projection. it's a special way to map a circle onto a line, or a sphere into a plane, or even a 4d hyper sphere into 3d space.

你如何向Linus解释乘以这些数字的外观和感觉。起初，这似乎是不可能的。我的意思是轮换就是这样一个本质上是二维的想法。但另一方面，旋转仅涉及一个自由度，角度唯一指定给定旋转的单个数字。原则上，应该可以将所有旋转的集合与一维连续体相关联，即Linus的世界。你可以用很多方法做到这一点，但我要向你展示的是所谓的立体投影。这是一种将圆圈映射到一条线上，或将一个球体映射到一个平面中，或者甚至将一个4d超球体映射到3d空间中的特殊方法。


#### 起点-1,区间[0,+1]投影直线内,[0,-1]投影直线外
for every point on the unit circle, draw a line from "-1" through that point, and wherever it intersects the vertical line through the circle Center ,that's where the point of the circle gets projected. so for example the point of one gets projected into the center of the line, the point "i" actually stays fixed in place, as does  "-i". all of the points on that 90-degree arc between "1" and "i" will get projected somewhere, in the interval between where "1" landed and where "i" landed, as you continue farther around the circle, on the arc between "i" and "-1" the projected points end up farther and farther away at an increasing rate. similarly if you come around the other way towards"-1", the projected points end up farther and farther on the other end of the line.

对于单位圆上的每个点，从“-1”到该点绘制一条直线，并且无论它与垂直直线相交的是圆心，也就是投影圆点的位置。 因此，例如，一个点被投射到线的中心，点“i”实际上保持固定，就像“-i”一样。 在“1”和“i”之间的90度弧上的所有点将被投射到某处，在“1”着陆和“i”着陆之间的间隔中，当你继续在圆周上，在弧上 在“i”和“-1”之间，投射点以越来越快的速度越来越远。 类似地，如果你绕过“-1”，则投影点在线的另一端越走越远。

#### 特殊点分析得出公式
this line of projected points is what we show to Linus labeling a few key points like "1" and "i" and "-1". all for reference technically the point at "-1" has no projection under this map, since the tangent line to the circle at that point never crosses the vertical line, but what we say is that "-1" ends up at the point at infinity. this is a special point you imagine adding to the line, where you would approach it if you walk infinitely far along the line in either direction.

这一系列的投射点是我们向Linus展示的几个关键点，如“1”，“i”和“-1”。所有参考技术上，“-1”处的点在此地图下没有投影，因为该点处圆圈的切线从未穿过垂直线，但我们所说的是“-1”最终在该点处结束无穷。这是一个特殊的点，你想象添加到线上，如果你沿任一方向的线无限远地走，你会接近它。

now it's important to remember and to remind Linus that what he's seeing is only the complex numbers that are a distance 1 from the origin. the unit circle Linus doesn't see most numbers like "0 or 1 plus "+i" or negative 2 minus i", but that's okay, because right now we just want to describe complex numbers Z. we're multiplying by Z has the effect of a pure rotation, so he only needs to understand the unit circle. for example, when we take the number "i" and multiply it by any other complex number "W", the effect is to rotate by 90 degrees counterclockwise, and when we apply this action to the circle, being projected down to the line for Linus, what does he see, well, it's a bit of a strange morphing action on the line, one which "+i" want you to become familiar with for something we'll see you later on. it's easiest to understand by following a few key reference points:

1.  "i x 1 = i" so that means the number 1 should move up to i. 

2.  "i x i  = -1" so the point at "i" slides off to infinity, 

3. "i x -1 = -i", so that point at infinity kind of comes back around from the bottom to the position one unit below the center and 

4. i x-i =1 so that point at "-1" slides up to "1", 

even though this is kind of a weird motion it lets us communicate some important ideas to Linus.

#### 非单元不可见
现在重要的是要记住并提醒Linus他所看到的只是与原点距离1的复数。单位圈Linus没有看到大多数数字如`0`或`1+i`或`-2-i`.
但这没关系，因为现在，我们只想描述复数Z，我们乘以Z有纯旋转的效果，所以他只需要了解单位圈。例如，当我们取数字“i”并将其乘以任何其他复数“W”时，效果是逆时针旋转90度，当我们将此动作应用于圆时，向下投射到线Linus，他看到了什么，好吧，这是一个奇怪的变形动作，我想让你熟悉我们稍后会见到的东西。遵循几个关键参考点最容易理解

1. “i x 1 = i”这意味着数字1应该向上移动到i。

2. “i x i = -1”因此“i”处的点滑向无穷大，

3. “i x -1 = -i”，因此无限远处的点从底部返回到中心下方一个单位的位置

4. i x -i = 1使得“-1”处的点滑动到“1”，
 
即使这是一种奇怪的动作，它让我们可以向Linus传达一些重要的想法。

for example, multiplying by "i" 4 times, which corresponds to rotating by 90 degrees four times in a row gets us back to where we started. " ixixixixi=1" here to get more of a feel for things. let me just show the circle rotated. at various different angles, on both the left and the right, half of the screen here, and putting a hand on the point that started at the "1" to help us and to help Linus keep track of the overall motion．

例如，乘以“i”4次，相当于连续四次旋转90度，让我们回到我们开始的地方。 “i x i x i x i x i = 1”在这里可以获得更多的感觉。 让我只显示旋转的圆圈。 在不同的角度，在左侧和右侧，屏幕的一半，并将手放在从“1”开始的点上，以帮助我们并帮助Linus跟踪整体运动。

### Felix the flatlander

next let's introduce "Felix the flatlander", who only understands two-dimensional geometry imagine trying to explain rotations of a sphere to
接下来让我们介绍一下这个平板的菲利克斯，他只了解二维几何, 想象试图向费利克斯解释一个球体的旋转.

in the spirit of transitioning from complex numbers to quaternions. let's extend the complex numbers with its horizontal axis of real numbers and its vertical axis of imaginary numbers, with a third axis defined by some newly invented constant J sitting. one unit away from zero perpendicular to the complex plane, instead of having this new axis in the z direction, like you might expect for a better analogy with how well visualize quaternions. we'll want to orient things, so that the "+i" and the J axes sit in the X and the y directions, with the real number line aligned along the z direction, so every point in 3d space is described as "1.25+1.5i+-1.0j". as it happens, it's not possible to define a notion of multiplication for a 3d number system like this, that would satisfy the usual algebraic properties that make multiplication a useful construct. perhaps all outline why this is the case in a follow-on video, but staying focused on our current goal, think about describing 3d rotations in this coordinate system to Felix. the flatlander the unit sphere consists of all those numbers, which are a distance one from zero at the origin, meaning the sum of the squares of their coordinates is one. 

本着从复数转换到四元数的精神。让我们用它的实数水平轴和虚数的垂直轴来扩展复数，第三个轴由一些新发明的常数J坐标定义。
一个单位远离零垂直于复平面，而不是在z方向上有这个新轴，就像你可能期望更好地类比四边形的可视化程度。 我们想要定位东西，使"+i"轴和J轴位于X和y方向，实数线沿z方向对齐，因此3d空间中的每个点都被描述为“1.25 + 1.5i +-1.0j”。 事实上，不可能为这样的3d数字系统定义乘法概念，这将满足通常的代数属性，使乘法成为一个有用的结构。 或许所有人都会在后续视频中概述为什么会出现这种情况，但仍然专注于我们目前的目标，考虑在这个坐标系中向Felix描述三维旋转。 flatlander单位球体由所有这些数字组成，这些数字在原点距离为零，这意味着它们坐标的平方和为1。 

we can't show all of 3d space to Felix. but what we can do is project this 2d surface to him, and give him a feel for what reorientation of the sphere looked like, under, that projection analogous to what we did before, stereographic projection will associate almost every point on the unit sphere with a unique point on the horizontal plane, defined by the "+i" in the J axes for each point on the sphere. 

draw a line from "-1" at the South Pole through that point and see where it intersects the plane. so the point one at the North Pole ends up at the center of the plane, all of the points of the Northern Hemisphere get mapped somewhere inside the unit circle of the "+i"J plane, and that unit circle (which passes through "+i"J negative "+i" and "-j" ) actually stays fixed in place and that's an important point to make note of. even though most points and lines and patches (that Felix the flatlander sees )are going to be Warped projections of the real sphere. this unit circle is the one thing that he has, which is an honest part of our unit sphere unaltered by projection.

我们无法向Felix展示所有的3D空间。但是我们能做的就是将这个2d表面投射到他身上，让他感觉到球体的重新定向是什么样的，在那个类似于我们之前所做的投影的情况下，立体投影几乎将单位球体上的每个点与水平面上的唯一点，由球体上每个点的J轴中的"+i"定义。


#### 起点-1,区间[0,+1]投影单位圆内,[0,-1]投影单位圆外
从南极的负1处画一条线，然后看到它与平面相交的位置。因此，北极点的一点最终位于平面的中心，北半球的所有点都被映射到"+i"J平面的单位圆内的某个位置，并且该单位圆（通过"+i"J负"+i"和负） J）实际上保持固定，这是一个值得注意的重点。即使大多数点，线和补丁（平板运动员菲利克斯看到的）都是真实球体的扭曲投影。这个单位圆是他所拥有的一件事，这是我们单位范围内未经投影改变的诚实部分。

all of the points in the southern hemisphere get projected outside that unit circle. each getting farther and farther away as you approach negative one at the South Pole. and again -1 has no projection under this mapping, but what we say is that it ends up at some point at infinity. that point at infinity is something such that no matter which direction, you walk on the plane as you go infinitely far out, you'll be approaching that point. it's analogous to how if you walk any direction away from the North Pole, you're approaching the South Pole. 

南半球的所有点都被投射到该单位圆外。 当你在南极接近负面时，每一个都越走越远。 并且-1在此映射下没有投影，但我们所说的是它最终在无限远处的某个点。 无限远处的那个点是这样的，无论你走向哪个方向，当你走得无限远时，你都会在飞机上行走，你将接近那一点。 它类似于如果你走向任何方向远离北极，你正在接近南极。

now let me just pull up a view of what Felix sees in two dimensions. as "+i" rotate the sphere in various ways, the lines of latitude and longitude drawn on that sphere get projected into various circles and lines in Felix's space, and the way "+i"'ve done things up here the checkerboard pattern on the surface of the sphere is accurately reflected in the projected view that you see with Felix. 

#### 非单元不可见
现在让我简单介绍一下Felix在二维看到的内容。当我以各种方式旋转球体时，在球体上绘制的纬度和经度线被投射到Felix空间中的各种圆和线中，并且我在这里做的事情是球体表面上的棋盘图案是准确地反映在您与Felix看到的投影视图中。

and the pink dot represents where the point that started at the North Pole ends up after the rotation, and that yellow circle represents where the Equator ended up after the projection. the more you put yourself in Felix's shoes right now, the easier quaternions will be in a moment. and as with Linus, it helps to focus on a few key reference objects, rather than trying to see the whole sphere.

粉红点表示旋转后从北极开始的点结束的位置，黄色圆圈表示在投影后赤道结束的位置。你现在越多地把自己放在菲利克斯的鞋子里，更容易的四元数将在片刻。和Linus一样，它有助于专注于几个关键的参考对象，而不是试图看到整个球体。


this circle passing through "1" "+i" "-1" and "-i" gets mapped onto a line which Felix sees as the horizontal axis. it's important to remind Felix that what he sees is not the same thing as the i axis. remember we're only projecting the numbers that have a distance 1 from the origin, so most points on the actual "+i" axis like "0 & 2 "+i" and 3i" etcetera are completely invisible to Felix. similarly, the circle that passes through 1j "-1" and "-j" gets projected onto what he sees as a vertical line. and in general any line that Felix sees comes from some circle on the sphere ,that passes through "-1". in some sense, a line is just a circle that passes through the point at infinity. 

#### 旋转时投影看到什么
这个圆圈通过“1”“+ i”“-1”和“-i”被映射到Felix看作水平轴的一条线上。 重要的是要提醒菲利克斯他所看到的与i轴不同。 记住我们只是投射与原点距离为1的数字，因此实际"+i"轴上的大多数点如`0`,`2+i`和`3i`等对Felix完全不可见。 类似地，通过1j“-1”和“-j”的圆被投射到他所看到的垂直线上。 一般来说，菲利克斯看到的任何一条线来自球体上的某个圆圈，它通过“-1”。 从某种意义上说，一条线只是一个穿过无限远点的圆。


now think about what Felix sees, as we rotate the sphere a 90 degree, rotation about the J axis brings "1" to "+i", "+i" to "-1", "-1" to  "-i", and "-i" to 1 .so what Felix the flatlander sees is an extension of the rotation, that line is the line lander was seeing. notice also that this action rotates the "+i" J unit circle to the position where the 1 J unit circle used to be. so what Felix sees is his yellow unit circle ,getting transformed into a vertical line, while that red vertical line gets transformed into the unit circle. of course, from our perspective, we know this is all just rigid motion no actual stretching or more thing is taking place. all of that is just an artifact of the projection. similarly, a rotation about the "+i" axis involves moving 1 to j, j to "-1", "-1" to "-j", and "-j" to 1. this rotation turns the "+i" J unit circle into the 1i unit circle, which to Felix looks like the unit circle getting transformed into a horizontal line. a rotation about the real axis is actually quite easy for Felix to understand. since the whole projection simply gets rotated about the origin, where the only point staying fixed in place are one at the origin, and negative one off at infinity. 

#### 特殊点分析得出公式
现在想想费利克斯看到的是什么，当我们将球体旋转90度时，围绕J轴的旋转将“1”变为“+ i”，“+ i”变为“-1”，“ - 1”变为“-i”并且“ - i”到1。所以平板运动员菲利克斯看到的是旋转的延伸，该线是着陆器看到的线。另请注意，此操作将“+ i”J单位圆圈旋转到1 J单位圆圈所在的位置。所以菲利克斯看到的是他的黄色单位圆，变成了一条垂直线，而那条红色的垂直线变成了单位圆。当然，从我们的角度来看，我们知道这只是刚性的动作，没有真正的伸展或更多的事情正在发生。所有这些只是投影的一件神器。类似地，围绕“+ i”轴的旋转涉及将1移动到j，j移动到“-1”，“ - 1”移动到“-j”，并且将“-j”移动到1.此旋转变为“+ i” J单位圈成1i单位圆，这对于Felix看起来像单位圆变成水平线。围绕实轴的旋转实际上很容易被Felix理解。因为整个投影只是围绕原点旋转，其中唯一保持固定位置的点是原点处的一个点，而在无穷点处是负点。

### You, the 3d Lander

in the same way, that the complex numbers included the real numbers with a single extra quote-unquote imaginary dimension, represented by the unit "+i". and that the "not-actually-a-number-system", thing we had in three dimensions included a second imaginary direction J, the quaternions include the real numbers together with three separate imaginary dimensions, represented by the unit's "+i" J and K. each of these three imaginary dimensions is perpendicular to the real number line. and they're all perpendicular to each other somehow. so in the same way, that complex numbers are represented as a pair of real numbers. each quaternion can be written using four real numbers, and it lives in four-dimensional space. you often think of this as being broken up into a real or "scalar part", and then a 3d "imaginary part". and Hamilton used a special word for quaternions that had no real part, and just ijk components a word, which was previously somewhat foreign in the lingo of math and physics, "vector". 

以同样的方式，复数包括实数和一个虚拟维度由单元`i`表示。 而在所谓“非实际数字系统”,有三个维度,包括第二个想象方向J， 四元数包括实数和三个独立的虚数维度，由单位的"i" "j"和"k"表示。 这三个假想维度中的每一个都垂直于实数行。并且他们都以某种方式彼此垂直。所以以同样的方式，复数表示为一对实数。每个四元数可以使用四个实数来编写，它存在于四维空间中。你经常把它想象成一个真实的或“标量部分”，然后是一个3d“想象的部分”。 汉密尔顿使用了一个特殊的单词来表示非实数部分的四元数，只是由"ijk"组成的一个单词“矢量”，这在以前在数学和物理学的术语中有点陌生。

#### 点积和叉积
on the one hand, you could just define quaternion multiplication by giving the rules for how "+i" J and K multiplied together, and saying that everything must distribute nicely. this is analogous to defining complex multiplication, by saying that "i x i = -1", and then distributing and simplifying products. and indeed, this is how you would tell a computer to perform quaternion multiplication. and the relative compactness of this operation ,compared to say matrix multiplication, is what's made quaternion so useful for graphics programming and many other things.

一方面，您可以通过给出I J和K如何相乘的规则来定义四元数乘法，并说一切都必须很好地分配。这类似于定义复数乘法，通过说“i x i = -1”，然后分配和简化点积。事实上，这就是你告诉计算机执行四元数乘法的方法。与矩阵乘法相比，这种操作的相对紧凑性使得四元数对图形编程和许多其他东西非常有用。

there's also a rather elegant form of this multiplication rule written in terms of the "dot product" and the "cross product". and in some sense, quaternion multiplication subsumes both of these notions. at least as they appear in three dimensions. but just as a deeper understanding for complex multiplication comes from understanding its geometry, that multiplying by a complex number involves a combination of scaling and rotating, you and I are here for the four dimensional geometry of quaternion multiplication. and just as the magnitude of a complex number its distance from zero is the square root of the sum of the squares of its component, that same operation gives you the magnitude of a quaternion. 

根据“点积”和“交叉积”，这个乘法规则也有一种相当优雅的形式。从某种意义上说，四元数乘法包含了这两个概念。至少它们出现在三维空间中。但正如对复杂乘法的更深入理解来自于理解它的几何，乘以复数涉及缩放和旋转的组合，你和我在这里用于四元数乘法的四维几何。正如一个复数的大小，它与零的距离是其分量的平方和的平方根，同样的操作给出了四元数的大小。

and multiplying quaternion q1 by another q2 has the effect of scaling q2 by the magnitude of q1. followed by a very special type of rotation in four dimensions and those special 4d rotations. the heart of what we need to understand correspond to the hyper sphere of quaternions, a distance 1 from the origin, both in the sense, that the quaternions whose multiplying action is a pure rotation live on that hyper sphere. and in the sense, that we can understand this weird 4d action just by following points on the hyper sphere, rather than trying to look at all of the points in the inconceivable stretch, as a four dimensional space analogous to what we did for Linus and Felix, we stereographically project this hyper sphere into 3d space

并且将四元数q1乘以另一个q2具有将q2按q1的大小缩放的效果。 接着是四维非常特殊的旋转类型和特殊的4d旋转。 我们需要理解的内容对应于四元数的超球面，距离原点的距离为1，在这个意义上，其乘法动作为纯旋转的四元数存在于超球面上。 从某种意义上说，我们可以通过跟随超球面上的点来理解这种奇怪的4d动作，而不是试图看到不可思议的延伸中的所有点，作为一个四维空间，类似于我们为Linus和 菲利克斯，我们立体地将这个超球体投射到三维空间中

#### 四元数的投影
this label in the upper right is going to show a given unit quaternion. and this little pink dot will show where that particular quaternion gets projected in our 3d space. just as before we're projecting from the number "-1" which sits on the real number line, that is somehow perpendicular to all of our 3d space. and beyond our perception just as before, the "1" ends up projected straight into the center of our space. and in the same way, that "+i" and "-i" were fixed in place for Linus, and that the "+i"J unit circle was fixed in place for Felix, we get a whole sphere passing through "+i" J and K on that unit hyper sphere, which stays in place under the projection. so what we see is a unit sphere in our 3d space, represents the only unaltered part of the hyper sphere of quaternions getting projected down on to us. it's something analogous to the equator of a 3d sphere .and it represents all of the unit quaternions whose real part is zero, of what Hamilton would have described as "unit vectors". the unit quaternions with positive real parts between 0 & 1 end up somewhere inside this unit sphere, closer to the number 1 in our 3d space, which should feel analogous to how the Northern Hemisphere got mapped inside the unit circle for Felix.

#### 起点 -1,区间[0, +1],[0,-1]
右上角的这个标签将显示给定的单位四元数。这个小粉红点将显示特定四元数在我们的3d空间中投影的位置。就像之前我们从位于实数线上的数字“-1”投射一样，它在某种程度上垂直于我们所有的3d空间。
具有0和1之间的正实部的单位四元数最终在该单位球内的某处，更接近我们的3d空间中的数字1，这应该感觉类似于北半球如何映射到Felix的单位圆内。
就像以前一样，“1”最终直接投射到我们空间的中心。并且以同样的方式，“+ i”和“-i”被固定在Linus的位置，并且"+i"J单位圆固定在Felix的位置，我们得到一个整个球体通过"+i"J和K在该单位超球体，在投影下保持原位。所以我们看到的是我们的三维空间中的单位球体，代表四元数超球体中唯一未经改变的部分被投射到我们身上。它类似于3d球体的赤道。它代表所有单位四元数，其实部为零，汉密尔顿将其描述为“单位向量”。

on the other hand, all the unit quaternions with negative real part end up somewhere outside. that unit sphere the number "-1" is sitting off at the pointed infinity, which you can easily find by walking in any direction. keep in mind, even though we see the projection of some of these quaternions as being closer or farther from the origin of our 3d space, everything you're looking at represents a unit quaternion. so everything you're looking at really has the same magnitude the same distance from the "0". and that "0" itself is nowhere to be found in this picture. like all other non unit quaternions it's invisible to us in the same way, that for Felix, the circle passing through "1" "i" "-1" and "-i" got projected into a line through the origin when we see this line through the origin passing "+i" and "-i", we should understand that it really represents a circle. likewise upon, the hyper sphere invisible to us there is a unit sphere passing through "1" "+i" "-j" "-1" "-i" and "-j" and that whole sphere gets projected into the plane that we see passing through "1", "+i", "-i" "j" "- j" and "-1", off at infinity, what you and i might call the XY plane. in general, any plane that you see here really represents the projection of a sphere somewhere up on the hyper sphere which passes through "-1"  .

另一方面，具有负实部的所有单位四元数最终都在外面的某个地方。单位球体数字“-1”位于指向无限远处，您可以通过任何方向行走轻松找到它。

#### 非单元不可见
请记住，即使我们看到其中一些四元数的投影距离我们的3d空间的原点更近或更远，您所看到的所有内容都代表一个单位四元数。所以你所看到的一切都与“0”的距离相同。并且在这张照片中找不到“0”本身。像所有其他非单位四元数一样，它以同样的方式对我们是不可见的.

#### 所见皆投影
对于Felix来说，当我们看到这个时，通过“1”“i”“-1”和“-i”的圆被投射到原点的一条线上通过原点到达“+ i”和“-i”，我们应该明白它确实代表了一个圆圈。同样地，超球对我们来说是不可见的，有一个单位球体通过`1`,`+i`,`-j`,`-1`,`-i`和`-j`，整个球体投射到平面中我们看到通过`1`，`+i`，`-i`,`j`,`-j`和`-1`，`无限远处`，你和我可以称之为XY平面。一般来说，你在这里看到的任何一个平面都代表一个球体在超球面上的投影，它通过“-1”。


now the action of taking a unit quaternion and multiplying it by any other quaternion from the left can be thought of in terms of two separate 2d rotations, happening perpendicular to and in sync with each other in a way that could only ever be possible in four dimensions.

as a first example, let's look at multiplication by "i", we already know what this does to the circle, that passes through "1" and "+i", which we see as a line. "1" goes to "+i" "+i" goes to "-1", off at infinity, -1 comes back around to "-i" and "-i" goes to 1. remember just like what "line" saw, all of this is the stereographic projection of a 90 degree rotation. now look at the circle passing through J and K, which is in a sense perpendicular to the circle passing through "1" and "+i". now it might feel weird to talk about two circles being perpendicular to each other. especially when they have the same center the same radius and they don't touch each other at all. but nothing could be more natural in four dimensions. you can think of the action of "+i" on this perpendicular circle as obeying a certain right hand rule, if you'll excute the intrusion of my (ghostly green screen )hand into our otherwise pristine platonic mathematical stage. you let that thumb of your right hand point from the "1" to "+i". and you curl your fingers, the JK circle will rotate in the direction of that curl. how much, well, by the same amount as the "1" ,"i" circle rotates which is 90 degrees in this case. this is what "+i" meant, by two rotations perpendicular to and in sync with each other. so J goes to K, K goes to "-J", "-J" goes to "-K" and "-K" goes to J. this gives us a little table for what the number "+i" does to the other quaternions. but I want this not to be something that you memorize, but something that you could close your eyes and you could really see

现在采用单位四元数并将其乘以左边的任何其他四元数的动作可以被认为是两个独立的2d旋转，这些旋转垂直于彼此并且以一种只能在四维中可能的方式彼此同步发生

作为第一个例子，让我们看看乘以“i”，我们已经知道它对圆圈的作用，它通过“1”和“+ i”，我们将其看作一条线。 “1”变为“+ i”“+ i”变为“-1”，在无穷远处关闭，-1返回到“-i”并且“-i”变为1.记住就像“行”一样看到，所有这些都是90度旋转的立体投影。现在看看穿过J和K的圆圈，它在某种意义上垂直于通过“1”和“+ i”的圆圈。现在谈论两个圆相互垂直可能会感觉很奇怪。特别是当它们具有相同半径的相同中心并且它们根本不相互接触时。但在四个方面没有什么比这更自然了。你可以把这个垂直圆圈上的“+ i”的动作想象成服从某个右手的规则，如果你将我的（幽灵般的绿色屏幕）手侵入我们原本柏拉图式的数学阶段。你让你的右手拇指从“1”指向“+ i”。当你弯曲你的手指时，JK圆圈会沿着那个卷曲的方向旋转。多少，与“1”相同的量，“i”圈在这种情况下旋转90度。这就是“+ i”的意思，通过两个垂直于彼此并且彼此同步的旋转。所以J转到K，K转到“-J”，“ - J”转到“-K”，“ - K”转到J.这给了我们一个小表，表示数字“+ i”对于其他四元数。但是我希望这不是你记忆中的东西，而是你可以闭上眼睛看到的东西


if you know what a quaternion does to the numbers 1 "+i"J and K, you know what it does to any arbitrary quaternion. since multiplication distributes nicely in the language of linear algebra. 1 "+i" J and K form a basis of our four dimensional space, so knowing what our transformation does to them gives us the full information about what it does to all of space geometrically. a four dimensional creature would be able to look at those two perpendicular rotations that "+i" just described, and understand that they lock you into one and only one rigid motion for the hyper sphere.

如果你知道四元数对数字1 "+i"J和K的作用，你知道它对任意四元数的作用。因为乘法在线性代数的语言中很好地分配。 1 "+i" J和K构成了我们四维空间的基础，因此知道我们的变换对它们的作用给了我们关于它对几何空间所做的全部信息。一个四维生物将能够看到我刚才描述的那两个垂直旋转，并且理解它们会将你锁定为超球的唯一刚性运动。

we might lack the intuitions of such a hypothetical creature, but we can maybe try to get close. here's what the action of repeatedly multiplying by "i" looks like. on our stereographic projection of the ijk sphere, it gets rotated into what we see as a plane, then gets rotated further back to where it used to be, though the orientation is all reversed. now then it gets rotated again into what we see. as a plane and after the fourth iteration it ends up right back where it started. as another example, think of a quaternion like "q equals negative square root of 2 over 2 plus square root of 2 over 2 times i", which if we pull up a picture of a complex plane is a 135 degree rotation away from 1, in the direction of "+i". under our projection, we see this along the line from 1 to "+i". somewhere outside the unit sphere, if that sounds weird just remember how linus would have seen the same number the action of multiplying this Q by all other quaternions will look to us like dragging the point at 1 all the way to this projected version of Q while the JK circle gets rotated 135 degrees according to our right-hand rule. 

##### 例子 i
我们可能缺乏这种假想生物的直觉，但我们也许可以尝试接近。这是反复乘以“i”的动作。在我们对ijk球体的立体投影中，它会旋转到我们所看到的平面，然后进一步旋转回到原来的位置，尽管方向都是相反的。现在它再次旋转到我们所看到的。作为一个平面，在第四次迭代之后，它最终会在它开始的地方回来。

##### 例子 2的负2的平方根加2的2的平方根
作为另一个例子，想象一个四元数，如“q等于2的负2的平方根加2的2的平方根”，如果我们拉出一个复平面的图像是从1开始135度旋转，在“+ i”的方向。根据我们的预测，我们在1到“+ i”的线上看到了这一点。在单位范围之外的某个地方，如果这听起来很奇怪，只记得linus如何看到相同的数字，将这个Q乘以所有其他四元数的动作对我们来说就像将点一直拖到Q的预测版本一样根据我们的右手规则，JK圆圈旋转135度。

multiplication by any other quaternion is completely similar. for example, let's see what it looks like, for "J" to act on other quaternions, by multiplication from the left, the circle through 1 + J, which we see projected， as a line through the origin, gets rotated 90 degrees dragging 1 up to J, so "J x 1 = 1", "+ J x J = -1", the circle perpendicular to that 1 passing through "+"+i"" and "K" gets rotated 90 degrees according to this right-hand rule, where you point your thumb from 1 to J, so "J x "+i" =  -K" and "J x K = "+i"". 

##### 例子 J
乘以任何其他四元数是完全相似的。 例如，让我们看看它看起来是什么样的，“J”作用于其他四元数，通过左边的乘法，圆圈通过1 + J，我们看到投影，作为穿过原点的直线，旋转90度拖动 1到J，所以“J x 1 = 1”，“+ J x J = -1”，垂直于那个穿过“+ "+i"”和“K”的圆圈根据这个右手旋转90度 规则，你将拇指从1指向J，所以“J x "+i" = -K”和“J x K = "+i"”。

in general, for any other unit quaternion, you see somewhere in space start by drawing the unit circle passing through 1 Q and "-1" ,which we see in our projection as a line through the origin. then draw the circle perpendicular to that one ,on what we see as the unit sphere. you rotate the first circle so that one ends up where Q was and rotate the perpendicular circle by the same amount, according to the right hand rule.


##### 一般情况
一般来说，对于任何其他单位四元数，你会看到空间中的某个地方开始绘制通过1 Q和负1的单位圆，我们在投影中看到它是穿过原点的直线。 然后在我们所看到的单位球体上绘制垂直于那个圆的圆。 根据右手规则，旋转第一个圆圈，使其最终在Q所在的位置，并将垂直圆圈旋转相同的量。

one thing worth noticing here is that order of multiplication matters it's not as mathematicians would say commutative. for example, "i x j is k" which you might think of in terms of "+i" acting on the quaternion "J" rotating it up to K. but if you think of J is acting on +i, " J times +i", it rotates "+i" to "-K". in fact, commutativity this ability to swap the order of multiplication is a way more special property than a lot of people realize. and most groups of actions on some space don't have it. it's like how in solving a rubik's cube order matters a lot,  or how rotating a cube about the z axis and then about the x axis gives a different final state from rotating it about the x axis then about the z axis. 

这里值得注意的一点是，乘法的顺序并不像数学家所说的那样是可交换的。例如，“"+i" times J is K”，你可能会想到“+ i”代表四元数“J”将它旋转到K.但如果你认为J代表+ i，“J次+ i“，它将我旋转为”-K“。事实上，交换这种交换顺序的能力是一种比许多人意识到的更特殊的属性。某些空间上的大多数行动都没有。这就像解决rubik的立方体顺序很重要，或者如何围绕z轴旋转立方体然后围绕x轴旋转它会产生不同的最终状态，使其围绕x轴旋转，然后围绕z轴旋转。

and last, as one final but rather important point so far, i've shown you how to think about quaternions, as acting by left multiplication, where when you read an expression like "+i x j", you think of "+i" as a kind of function morphing all of space ,and "j" is just one of the points that it's acting on. but you can also think of them as a different sort of action, by multiplying from the right, where in this expression j would be acting on "+i". in that case the rule for multiplication is very similar. it's still the case that 1 goes to "j" and "j" goes to "-1" etc. but instead of applying the right-hand rule to the circle perpendicular to the 1j circle, you would use your left hand. so either way "i" times "j" is equal to k. but you can either think about this with your right hand curling the number "j" to the "number k" as your thumb points from "1" to "i". or as your left hand curling ""+i"" to "K" ,as it's thumb points from 1 to J. understanding this left hand rule for multiplication from the other side will be extremely useful for understanding how unit quaternions describe rotation in three dimensions.

最后，作为目前为止最后但又相当重要的一点，我已经向你展示了如何思考四元数，作为左乘法的表现，当你读到像“+ i x j”这样的表达式时，你会想到“+ i “作为一种变形所有空间的函数，”j“只是它所作用的一个点。但你也可以把它们视为一种不同的动作，从右边开始，这个表达式中j将作用于“+ i”。在这种情况下，乘法规则非常相似。它仍然是1变为“j”而“j”变为“-1”等的情况，但不是将右手规则应用于垂直于1j圆的圆，你可以使用你的左手。所以“i”次“j”等于k。但是当你的拇指从“1”到“i”时，你可以用右手将数字“j”卷曲到“数字k”来考虑这一点。或者你的左手将“"+i"”卷曲成“K”，因为它的拇指点从1到J.理解这个从另一侧乘法的左手规则对于理解单位四元数如何描述三维旋转非常有用。

and so far it's probably not clear how exactly quaternion do describe 3d rotation. "+i" mean if you consider one of these actions on the unit sphere passing through "+i" J and K, it doesn't leave that sphere in place it morphs it out of position. so the way that this works is slightly more complicated than a single quaternion product. it involves a process called conjugation. and "+i"'ll make a full follow-on video all about it, so that we have the time to go through some examples in the meantime. for more information on the story of quaternions and their relation to orientation.

到目前为止，可能还不清楚四元数究竟是如何描述3d旋转的。我的意思是如果你考虑通过"+i" J和K的单位球体上的这些动作之一，它不会将该球体留在原位，它会使它变形到位置之外。所以它的工作方式比单个四元数产品稍微复杂一些。它涉及一个叫做共轭的过程。我将制作一个关于它的完整后续视频，以便我们有时间在此期间通过一些例子。有关四元数的故事及其与方向的关系的更多信息。

in 3d space quanta a mathematical publication. "+i"'m sure a lot of you are familiar with just put out a post, in a kind of loose conjunction with this video link in the description .if you enjoyed this, consider sharing it with some friends, and if you felt like the narrative structure here was actually helpful for understanding maybe reassure those friends who would be turned off by a large timestamp that good math is actually worth the time and many thanks to the patrons among you. "+i" actually spent way longer than "+i" care to admit on this project, so your patience and support is especially appreciated this time around you.

在3d空间量子中的数学出版物。我确定你们很多人都熟悉只是发布一个帖子，与描述中的这个视频链接有一种松散的联系。如果你喜欢这个，考虑与一些朋友分享，如果你觉得这样的叙述这里的结构实际上对理解有帮助可能会让那些被大量时间戳关闭的朋友放心，好的数学实际上值得花时间，非常感谢你们中的顾客。实际上，我花费的时间远远超过了我对这个项目的承认，所以这次你的耐心和支持特别受到赞赏。
