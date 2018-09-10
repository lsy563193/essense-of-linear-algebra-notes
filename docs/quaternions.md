你现在正在看的东西叫做四元数乘法，或者更确切地说你正在观察在我们的三维空间中表现出的四维球体上发生的特定运动的某种表现形式，他将会理解这一点。这段视频的结尾。

四元数是一个绝对迷人且经常被低估的数学系统，就像复数是实数的二维扩展一样，四元数是复数的四维扩展。但它们不仅仅是有趣的数学诡计，它们具有令人惊讶的实用性，可用于描述三维旋转甚至是量子力学。

他们的发现故事在数学方面也很有名。爱尔兰数学家威廉·罗恩·汉密尔顿一生都在寻求一个类似于复数的三维数字系统，正如故事所述，他的儿子每天早上会问他是否已经弄清楚如何划分三元组，他总是会说不，还没有。但是在1843年10月16日，当他穿过都柏林的布鲁姆桥时，他意识到他们认为他需要的东西不是为复杂的数字增加一个维度而是为了增加两个想象的维度。在描述空间的三个虚构维度和与某个第四维度垂直的实数坐标时，他刻画了将这三个虚构单元描述成桥梁的关键方程式，今天有一块牌匾用于表示这个方程式。

现在你必须了解我们现代的矢量与他们的点积和交叉积的概念，这样的事情在汉密尔顿的时代并不存在，至少不是标准化的形式。所以在他被发现之后，他努力推动四元数成为我们教导学生描述三维空间的主要语言，甚至形成一个官方的四元数社会来传播他的发现。现在不幸的是，这与围栏另一侧的数学家相平衡，他们认为四元数乘法的混淆概念对于描述三个维度是不必要的，导致一些真正热闹的旧时垃圾谈话合法地称他们为邪恶。

 it's even believed that the Mad Hatter scene from Alice in Wonderland, whose author you may know was an Oxford mathematician was written in reference to quaternions that the chaotic table placement changes were mocking their multiplication, and that certain quotes were referencing their non commutative nature.

 它甚至认为来自爱丽丝梦游仙境的Mad Hatter场景，你可能知道的作者是牛津数学家，是关于四元数的写法，其中混乱的表格位置变化嘲弄它们的乘法，并且某些引用引用了它们的非交换性质。

fast forward about a century, and the computing industry gave quaternions a resurgence among programmers who work with graphics and robotics and anything involving orientation in 3d space, and this is because they give an elegant way to describe and compute 3d rotations, which is computationally more efficient than other methods, and which also avoids a lot of the numerical errors, that arise in these other methods, the 20th century also brought quaternion some more love from a completely different direction quantum mechanics.

快进大约一个世纪，计算机行业使四元数在使用图形和机器人以及任何涉及三维空间定位的程序员中复活，这是因为它们提供了一种优雅的方式来描述和计算三维旋转，这在计算上更多与其他方法一样有效，并且也避免了在这些其他方法中出现的许多数值误差，20世纪也给四元数带来了更多来自完全不同方向的量子力学的爱。


you see the special actions the quaternions described in four dimensions are actually quite relevant to the way the two-state systems like spin of an electron or the polarization of a photon are described mathematically.

你会看到四元数在四维中描述的特殊行为实际上与数学描述双态系统如电子自旋或光子极化的方式非常相关。

what I'll show you here is a way to visualize quaternions in their full four-dimensional , it would surprise me if this approach was fully original, but I can say that it's certainly not the standard way to teach quaternions. and that the specific four-dimensional right-hand-rule image that I'd like to build up to is something that I haven't really seen elsewhere building up an understanding for this visual will take us meaningful time. but once you have it there is a very natural and satisfying intuition for how to think about quaternion multiplication. 

我将在这里向您展示的是一种在四维空间中可视化四元数的方法，如果这种方法完全是原创的话，我会感到惊讶，但我可以说它当然不是教授四元数的标准方法。我想要建立的特定的四维右手规则图像是我在其他地方没有真正看到的东西，建立对这种视觉的理解将带给我们有意义的时间。但是一旦你拥有了它，就会有一种非常自然而令人满意的直觉来思考如何考虑四元数乘法。

it won't be until the next video that I show you how exactly quaternions describe orientation in three dimensions which is for some people the whole reason we care about it, but once we're able to go at it armed with the image of what they're doing to a 4d hyper sphere, there's a pleasing understanding to be had for the otherwise opaque formulas characterizing this relationship. the structure here will be to start by imagining teaching complex numbers to someone who only understands one dimension, then describing 3d rotations to someone who only understands two dimensions, and ultimately to represent what quaternions are doing up in four dimensions within the constraints of our 3 dimensions space .

直到下一个视频，我才会告诉你四元数究竟是如何描述三维方向的，这对某些人来说是我们关心它的全部原因，但是一旦我们能够用它的形象武装起来 他们正在做一个4d超级球体，对于表征这种关系的其他不透明的公式有一个令人愉快的理解。 这里的结构将首先想象教导复杂的数字给那些只理解一个维度的人，然后将3d旋转描述给只理解两个维度的人，并最终代表四元数在3d的约束下在四个维度上做什么。 空间 。

---
our first character is Linus, the line Lander, whose mind can only grasp the one dimensional geometry of lines in the algebra of real numbers.

我们的第一个角色是Linus，即Lander线，它的思维只能掌握实数代数中线条的一维几何。

 we're gonna try to describe complex members to Linus, and it's really important for you to empathize with him as much as you can during this ,because in a few minutes you're gonna be in his shoes. on the one hand you could define complex numbers purely algebraically. you say each one is expressed as some real number plus some other real number times "i",  where "i" is a newly invented constant whose defining property is that "i * i = -1". then you say to Linus to multiply two complex numbers, you just use the distributive property, what many people learn in school is ""FOIL". and you apply this rule that "i * i = -1" to simplify things down further, and that's fine, that totally works in the standard textbook way to introduce quaternions is analogous to this, showing the algebraic rules and calling it done. but I think something is missing if we don't at least try to show Linus the geometry of complex numbers then what complex multiplication looks like. since the problems in math and physics we're ,complex numbers are shockingly useful, often leverage this spatial intuition. 

我们要试着向Linus描述一些复杂的成员，在这期间尽可能多地同情他是非常重要的，因为在几分钟之内你就会陷入困境。一方面，你可以纯粹代数地定义复数。你说每一个都表示为一些实数加上一些其他实数乘以“i”，其中“i”是一个新发明的常数，其定义属性是“i * i = -1”。然后你说Linus要增加两个复数，你只需要使用分配属性，很多人在学校里学到的就是“”FOIL“。你应用这个规则”i * i = -1“来进一步简化事情，这很好，完全按照标准教科书的方式引入四元数类似于此，显示代数规则并称之为完成。但我认为如果我们至少不试图向Linus展示复杂的几何形状，那么就会缺少某些东西然后是复数乘法的数字。因为数学和物理学中存在的问题，复杂的数字非常有用，通常会利用这种空间直觉。

you and I who understand two dimensions might think of it like this, when you multiply two complex numbers, Z times W, you can think of Z as a sort of function acting on W rotating and stretching it in some way, I like to think of this by broadening the view and asking what does he do to the entire plane. and you can think of that bird's-eye view action, by imagining using one hand to fix the number 0 in place and using v another hand to drag the point at 1 up to Z. since anything times 0 is 0, and anything times 1 is itself, and in two dimensions there is one and only one stretching rotating action on the plane that'll do this. this is also how I'll have you thinking about quaternion multiplication later on. where the number on the Left acts as a kind of function to the one on the right, and we'll understand this function by seeing how it acts by transforming space although instead of rotating 2d space. it does a sort of double rotation in 4d space. 
理解两个维度的你和我可能会想到这样，当你将两个复数乘以Z乘以W时，你可以将Z视为一种作用于W旋转并以某种方式拉伸它的函数，我喜欢思考通过扩大视野并询问他对整个飞机做了什么。并且你可以想象那个鸟瞰视图动作，想象用一只手将数字0固定到位并用另一只手将点拖动到1到Z.因为任何时候0都是0，任何时候都是1就其本身而言，在二维中，在平面上只有一个拉伸旋转动作，这样做。这也是我稍后会考虑四元数乘法的方法。左边的数字作为右边一个函数的一种函数，我们通过转换空间来看它是如何起作用的，而不是旋转2d空间，我们将理解这个函数。它在4d空间中进行一种双重旋转。


by the way, if you want to review thinking about complex numbers as a kind of action, a good warm-up for this video might be the one I did on "e to the PI" I explained with introductory goop theory. now line is the line Lander is pretty comfortable with the idea of stretching， that's what multiplication by real numbers looks like maybe it's a little weird for him to think about stretching in multiple dimensions. but it's not fundamentally different. the difficult thing to communicate to Linus is rotation, specifically focus on the unit circle of the complex plane. all the numbers a distance one from zero, since multiplication by these numbers corresponds to pure rotation .
.
顺便说一句，如果你想回顾一下复杂数字作为一种动作的看法，对于这个视频的一个很好的热身可能是我在“e到PI”上做的那个我用介绍性的goop理论解释的。现在行是Lander对拉伸的想法非常舒服，这就是实数乘以看起来似乎对他来说考虑多维拉伸有点奇怪。但它并没有根本不同。与Linus沟通的难点是旋转，特别是关注复平面的单位圆。所有数字与零的距离为1，因为乘以这些数字对应于纯旋转。
。

how would you explain to Linus the look and the feel of multiplying by these numbers . at first, that might seem impossible. I mean rotation is just such an intrinsically two-dimensional idea. but on the other hand, rotation involves only one degree of freedom , a single number the angle specifies a given rotation uniquely. so in principle, it should be possible to associate the set of all rotations to the one dimensional continuum, that is  Linus's world. and there are many ways you could do this, but the one I'm going to show you is what's called a stereographic projection. it's a special way to map a circle onto a line, or a sphere into a plane, or even a 4d hyper sphere into 3d space.
你如何向Linus解释乘以这些数字的外观和感觉。起初，这似乎是不可能的。我的意思是轮换就是这样一个本质上是二维的想法。但另一方面，旋转仅涉及一个自由度，角度唯一指定给定旋转的单个数字。原则上，应该可以将所有旋转的集合与一维连续体相关联，即Linus的世界。你可以用很多方法做到这一点，但我要向你展示的是所谓的立体投影。这是一种将圆圈映射到一条线上，或将一个球体映射到一个平面中，或者甚至将一个4d超球体映射到3d空间中的特殊方法。