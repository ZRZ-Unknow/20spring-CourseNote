# Week1

+ KR 是一个surrogate（替代，代理），不用作用在原事物上而是在这个surrogate上进行推理

+ semantics 语义, 连接了surrogate与real object

+ Web of data 四项原则:

  >+ Give all things a name
  >+ Build relationships between the objects
  >+ Things are named uniquely on the Web
  >+ Explicit, Formal Semantics

+ Since the conception of the Semantic Web, people use

  - knowledge base
  - ontolody (本体，知识图谱): often denoted as knowledge graph

+ OWL (网络本体语言) is one language for writing ontologies

+ the role KR plays

  >+ A KR is a surrogate:
  >
  >  > + 推理本身是内部的一个过程，而推理的内容是外部世界的，推理/思考本身是外部世界行动的surrogate
  >  > + surrogate和real thing是有误差/区别的，surrogate经常会忽略掉一些东西/属性，包含简化的假设/人为添加的东西， 完美的surrogate只能是real thing本身
  >  > + 因此不正确的inferences（推理/推论）是不可避免的
  >
  >+ A KR is a set of ontological commitments(过滤眼镜)
  >
  >  >+ 从不同角度对同一事物的KR是不一样的，（盲人摸象）
  >  >

# Week2

+ **Knowledge Acquisition（获得）**

  >+ 从source of knowledge中搬到sink、知识库中

+ Source

  - Domain Experts
  - know a lot about the domain
  - highly reliable about the domain
  - know how to articulate domain knowledge
  - have good metaknowledge

+ Immediate Sink

  - A document encoded in natural language or semi-NL

+ Ultimate Sink

  - A document encoded in formal KR language form

+ **Knowledge Base(KB)**:

  >+ 分为TBox与ABox，类似于数据库column与每一行的概念，后者是instance
  >
  >- TBox: 框架性的知识，描述的是一个群体的知识，往往恒定不会变化
  >- ABox: 个体性的知识，描述的是个体的性质，可能随时间变化
  
+ DL：descriptional logics，描述逻辑

+ ![image-20200227231035320](pic\image-20200227231035320.png)

# Week3

### knowledge acquisition 到representation的过程

+ Term extraction:
  + 包含concept names,role names,individuals
  + 是relevant，domain-dependent领域相关的
  + 不同的term颗粒度不同：如animal和cat
+ Grouping:
  + 分组
  + A key slogan: to determine which terms to care about
    + context sensitive:我们要怎样的应用？
    + interest relative：应用需要什么？应用的audience是谁？
+ Normalise Terms:
  + 规范化，如单复数、语法上的form、spelling(名词、形容词)
  + 把concept name的首字母大写，role names的首字母小写，individual全部小写
+ Organise Terms:
  + General和specific，反义词，对应的词
  + definition:用来描述一个term的一个陈述
    + extensional的方式：列举出term中的所有元素
    + intensional的方式：使用genus-differentia pattern，也就是说： giving the next more general term (genus) plus differentiating features for this term and its siblings ,如：恒温动物是一个有机体，维持它身体在一个恒定的温度
+ $\mathcal{EL}$中的concept对应$\mathcal{ALL}$中的class
+ protege的使用：动手实践





# Week4

+ Semantic Web语义网（第3代网页的一个理想代表）：a platform for distributed applications and sharing (linking) data
  
  + Web1.0: 公司发布，data之间存在一定的关联，用户只是可读模式
  + Web 2.0: B2B，B2C，允许用户之间产生交互行为，用户可以“创造”出联系，可读可写
+ Web 3.0：知识和信息不再以自然语言形式存储，而是以实体形式，将结构化的知识上传到网络来，构成一个广泛意义上的巨大的网络
  
  + RDF：resource description framework 资源描述框架，由三元组主语（个体）、谓语、宾语（个体）组成，描述个体与个体的联系，可以理解成ABOX，provides uniform syntactic structure for data 
  + OWL：基于DL描述逻辑，和RDF的区别：知识图谱一般用RDF表示，而OWL里有TBOX (整体性的知识，与个体无关系，ABOX反之)，provides machine readable schemas (ontologies) 
  + SPARQL:一种搜索语言，关系型数据库一般用SQL进行查询，RDF的数据都是以图形式存储的，它的查询语言使用的是SPARQL。
     一条SPARQL查询，其核心是对于一组变量及其之间关系的描述，构成了一种带有变量的图模式，与SQL类似，SPARQL查询可以返回一条或多条结果，每条结果包含的是对上述每个变量的一个绑定-指明了该变量与一个RDF术语之间的对应关系。
+ ontology：A model of (some aspect of) the world 对世界的建模 
  +  Introduces vocabulary relevant to domain 
  +  Specifies meaning (semantics语义学上) of terms 
  +  Formalised using suitable logic 适合的逻辑语言
+ 描述逻辑比一阶逻辑语法更简洁，是可决定的，且低复杂度
+ Web Ontology Language OWL:

  + 一种本体书写语言，有API，开发环境，推理系统等，基于描述逻辑
+ DL Knowledge Base (KB) consists of two parts: –
  + Ontology (aka TBox) axioms define terminology (schema)
  + Ground facts (aka ABox) ，use the terminology (data)
  + <img src="pic\image-20200310144306306.png" alt="image-20200310144306306" style="zoom:67%;" />
  + <img src="pic\image-20200310144501219.png" alt="image-20200310144501219" style="zoom:67%;" />
  + 表示John has-child Mary，Mary是John的孩子
+ interpretation：一个解释函数，见KR随笔
  + ![image-20200328095351304](pic\image-20200328095351304.png)
  + Video-week4-part2
  + ontology O是consisternt的 如果 存在O的一个model 



# Week5

+ 如果要将individual归类为某class，则class一定得有充分必要条件，而仅有必要条件如subclassof则无法判断。

+ OWL与FOL的转换：![image-20200317143232442](pic\image-20200317143232442.png)

  ![image-20200317143331953](pic\image-20200317143331953.png)

+ KR systems assumptinos:

  + Unique name assumption
  + Closed domain assumption

  + Minimal models
  + Closed world assumption: 凡是不能被O导出的都认为是错的
    + What isn’t entailed by O isn’t true
  + Open world assumption: 没说的东西，它就有可能对
    + an axiom can be such that
      + it’s entailed by O or
      + it’s negation is entailed by O or
      + none of the above

+ protege里role的functional指只能跟一个值，如hasSex some Female,只能有1个

+ hasChild only Daughter, 表示要是有孩子则只有女儿;如果再加一个hasChild some Son，此时reasoning会成功，因为daughter和son没说互斥,即protege是open world assumption。

+ An axiom pattern is 
  + a recurring regularity in how axioms are used in an ontology
  + atomic SubClassOf axioms, i.e. A SubClassOfB where A, B are class names

+ Class name用驼峰结构，首字母大写；individual全小写，可以用下划线；property name驼峰结构，首字母小写

+ All classes and individuals hav a label, creator, description annotation property（即注释）



# Week6

### Competency Questions for ontologies

+ What must an ontology be “competent” to do  (answer)? 
  + The ontology should have the axioms sufficient to answer competence questions
  + What vegetarian pizzas are there that don’t have olives? 
  + Implies discriminations of different toppings, vegetable/fish/meat toppings and closure of toppings




### Axiom Pattern

+ An axiom pattern 是一个经常出现的关于axiom如何在ontology中使用的模式

  + 最常见的：A subclassof B

  + ![image-20200328105734015](pic\image-20200328105734015.png)

  + partitions pattern：类似与划分，一个元素有n个子类，但某个a只能属于这些子类中的一个

    ![image-20200328110100074](pic\image-20200328110100074.png)

  + ![image-20200328110146278](pic\image-20200328110146278.png)

  + content pattern: 

    + isComponentOf: 是一种组成部分/元素，如把手是车门的组成部分
      + functional：把把手从车门拿开影响了functional
      + non-homeomeric：把手和门是两种不同的事物
      + separable：是可以把把手从车门中拿走
    + isIngredientOf：一种材料和用这种材料做成的物体，如牛奶isIngredientOf卡布奇诺，面粉isIngredientOf面包
      + non-functional：牛奶在卡布奇诺的任何地方都有
      + non-homeomeric：牛奶和卡布奇诺是两种不同的事物
      + non-separable：不可以把牛奶从卡布奇诺中拿走
    + isPortionOf：对象的部分isPortionOf对象，如买一些猪肉，这些猪肉是猪肉的一部分; 面包片是面包的一部分
      + non-functional：这些猪肉可以存在于猪肉的任何位置
      + homeomeric：都是猪肉
      + separable：能够砍出一部分猪肉
    + isSpatialPartOf：一个地方和他周围区域的关系，如南京isSpatialPartOf中国
      + non-functional
      + homeomeric
      + non-separable
    + isMemberOf：个体和群体的关系：tree-Forest; 
      + non-functional
      + homeomeric
      + non-separable

  + ![image-20200328113543729](pic\image-20200328113543729.png)

  + 





# Week7

+ java的OWLAPI相关



# Week8

### Reasoning in ALC

+ 判定satisfiable的 Tableau Methods：

  + transform a given concept into Negation Normal Form (NNF)：将所有的not放在concept前面

    ![image-20200407144304884](pic\image-20200407144304884.png)

  + apply completion rules in arbitrary order as long as possible：

  + the concept is satisfiable if, and only if, a clash-free tableau can be derived to which no completion rule（扩展规则） is applicable：当且仅当 没有矛盾的rule饱和的tableau被推导出

  ![image-20200407145040324](pic\image-20200407145040324.png)

+ To show that the tableau does what it is supposed to do one has to show

  + Soundness: If the concept is satisfiable, then there is a branch without clash such that no rule is applicable;
  + Termination: The tableau terminates after finitely many steps for any input concept in NNF;
  + Completeness: If there is a branch without clash such that no rule is applicable, then the concept is satisfiable





# Week9: Catch up lecture

+ TBox、ABox类似与传统数据库DB的框架和每一行的数据



# Week10:Tableau,DLReasoning

+ 见slides



# Week11:DL Lite

+ TODO



# Week12:RDF&OWL

+ RDF: Resource Description Framework
  + 三元组：主谓宾   Simple triple based datamodel Subject, Predicate, Object



# Week14:OBDA

+ Ontology Based Data Access：

  + An ontology provides meta-information about the data and the vocabulary used to query the data. It can impose constraints on the data.
  + Actual data can be incomplete w.r.t. such meta-information and constraints. So data should be stored using open world semantics rather than closed world semantics: use ABoxes instead of relational database instances.
  + During query answering, the system has to take into account the ontology
  + 相当于一个database with ontology

+ <img src="pic\image-20200519142204442.png" alt="image-20200519142204442" style="zoom: 67%;" />

  







# review

### part1

+ relationship between AI and KR

  + KR acts as a surrogate,  standing in for things that exist in the world (reasonging is an internal process, while the things we wish to reason about are external), reasoning operates on the surrogate rather than the things itself.

  + The correspondence between the representation and the things it is intended to represent is **semantics(语义)**。（**why is formal semantics importannt for KR**：to reasoning on KR, we have KR act as a surrogate standing in for things, formal semantics link the things and KR, so the reasonging in meaningful,或者课件上的 we need to specify the relationship between statements in the logic and the existential phenomena they describe.

  + OWL is one language for writing ontologies, which is web ontology language, based on description logic, and DL is a fragments of first order logic designed for KR

  + A knowledge representation (KR) is most fundamentally a `surrogate`, a substitute for the thing itself, used to enable an entity to determine consequences by thinking rather than acting, i.e., by reasoning about the world rather than taking action in it.

    It is a `set of ontological commitments`, i.e., an answer to the question: In what terms should I think about the world?

    It is a `fragmentary theory of intelligent reasoning`, expressed in terms of three components: (i) the representation's fundamental conception of intelligent reasoning; (ii) the set of inferences the representation `sanctions`; and (iii) the set of inferences it `recommends`.

    It is a `medium for pragmatically efficient computation`, i.e., the computational environment in which thinking is accomplished. One contribution to this pragmatic efficiency is supplied by the guidance a representation provides for organizing information so as to facilitate making the recommended inferences.

    It is a `medium of human expression`, i.e., a language in which we say things about the world.

  + **什么是Ontology？**An ontology is a specification of a conceptualization, a model of (some aspect of ) the world. Consists of two parts

    + Set of axioms describing structure of the model
    + Set of facts describing some particular concrete situation

    Introduces vocabulary relevant to domain and  Specifies intended meaning of vocabulary
    
    ontology在week12中的定义：
    
    + a knowledge model which defines a set of concepts and the relationship between those concepts within a specific domain
    + Supports automated reasoning and inference of data using logical rules
    + Provides Knowledge sharing and reuse among people or software agents

### part2

+ patterns(closure、)

+ KA is the transfer of declarative statements from source to sink。

  + 操作性定义operational definition：given a source of knoledge and a sink, KA is the transfer of declarative statements from source to sink。

  K refinement : 将已经在sink中的提炼出来 modification of the statements in our sink

  ultimate sink: 用formal KR language表示的，比如一个ontology

  在这里 KA=KE（knowledge elicitation）

  knowledge engineer(KE): 做的是encoding的任务

+ Elicitation Technique Requirements：

  + minimise DE(domain expert)'s time
  + minimise DE's KE training and effort
  + support multiple sources
  + KEs must understand enough
  + Always assume DE not invested

+ elicitation techniques, two major families:

  + pre-representation: experts interact with a KE, focused on protocols(协议)
  + post-representation：后期可能有需要改的地方，就是 testing and generating

+ modelling techniques:

  + sorting techniques
  + hierarchy-generation techniques
  + matrix-based techniques
  + roleplay

+ cart sorting: write down each concept on a card, organise them into piles ...

+ formalisation:

  + term extraction, grouping, normalise terms, organise terms

+ semantic web: “a platform for distributed applications and sharing (linking) data。web2.0把网页和网页连接起来，叫做超链接，允许进行自媒体传播，3.0多了语义，内容之间有语义联系。

+ 关于ontology的解释、model、entailment等等：

  + I satisfies an ontology O if I satisfies every axiom α in O • If I satisfies O, we call I a model of O
  + ![image-20200802000109726](pic\image-20200802000109726.png)
  + translate from OWL to FOL
    + ![image-20200802005226149](pic\image-20200802005226149.png)
    + ![image-20200802005251007](pic\image-20200802005251007.png)

+ An axiom pattern is • a recurring regularity in how axioms are used in an ontology

  + 1st logical pattern: property closure pattern

    ![image-20200802005732770](pic\image-20200802005732770.png)

  + 2nd Logical Pattern: the Covering Pattern

    ![image-20200802005825798](pic\image-20200802005825798.png)

  + part-whole relations: Describing a whole by means of its parts

    + propertiy:

      + functional
      + homeomerous
      + invariant

    + relations:

      + isComponentOf:  handle iscomponentOf CarDoor
      + isIngredientOf: Milk isIngredientOf Capuccino
      + isPortionOf: SomeChocolate isPortionOf Chocolate
      + isSpatialPartOf: holds between a place and its surrounding area

    + 作用： 帮助在model ontology的过程中更加准确

    + modelling these in ontology:

      + transitivity: X is part of Y, Y is part of Z, thus X is part of Z

        Careful, this is only true for some/with the same kind of composition，比如isPartof 可以是transitive的，但isdirectPartOf不是

+ Competency Questions:

  What must an ontology be “competent” to do (answer)? The ontology should have the axioms sufficient to answer competence questions

  cq Obvious relationship to testing • My ontology must be competent to do this question

### part3

+ ontology 是最终的一个产品，一个知识库，它需要一个撰写的语言，OWL直接用来写ontology，而OWL是base在一个DL语言上。Ontology 是那 个概念世界，是最终的产品。OWL 是用于写 ontology 的语言，类似于 ontology 是一个 Java 程序，而 OWL 是 Java 语言。而 OWL 是基于 description logics 开发出来的。大家可以把 OWL 当成 description logics + 一个 wrapper（一个外包装）。从 logic 角度，它叫 description logic，从 KR 角度，叫 OWL。

+ 一个语言越接近自然语言，表达力越强，计算复杂度越高，推理的难度越大。我们选择的底线是表达力能够表示 domain knowledge 的最低标准，这样可以最大程度的保证后续推理的复杂度不会太高。

+ 给出一个interpretation，首先要有domain，然后有解释函数。 

+ web3.0的优势？web2.0把网页和网页连接起来，叫做超链接，允许进行自媒体传播，3.0多了语义，内容之间有语义联系。

+ 一个ontology consistency 是至少能找到一个解释使得它是这个ontology的一个model。一个axiom是否被ontology 语义蕴含，如果所有ontology的model都是这个axiom的model.一个class的satisfiability，是说有一个解释使得这个class不为空。一个individual是不是属于一个class，就叫做instance的relationship

+ only 和exist 二选一：选择exist，因为exist保证了r关系的存在，而for all不可以（如果存在，则...），

+ 可决定性：

  + 关于可决定性是必要条件的讨论 ：One can argue that decidability of basic reasoning tasks is a necessary condition for an ontology language to be useful in practice. If basic query answering (e.g., deciding T |= C v D) is undecidable, then it is impossible to implement an algorithm that gives a correct answer to every possible query. Thus, it is not possible to implement software for which it is guaranteed that a user will always get a correct answer to a query.
  + 可决定性无法保证复杂度，For most applications, a problem can be regarded as tractable if there exists an algorithm that solves the problem in polynomial time:

+ RDF: Resource Description Framework，三元组 subject, p, object

+ ![image-20200802130507820](pic\image-20200802130507820.png)

+ FOPL：query，见week13

  ![image-20200804100036458](pic\image-20200804100036458.png)

+ ABox的tabluea：见week13

+ OBDA: Actual data can be incomplete w.r.t. such meta-information and constraints. So data should be stored using open world semantics rather than closed world semantics: use ABoxes instead of relational database instances.

+ DB vs Ontology:

  Important differences in semantics

  + DB: UNA, CWA and constraints
  + Ontology: OWA and implications

+ decidalility：判断一个句子是否被语义蕴含

+ slides15： signature、PIN、三种diff、S-Module

+ syntactic diff: 语法上的改变，比如代码某一行变了。在ontology中，知识顺序的改变也属于语法改变

  structural diff: 结构上不一样，但语义上一样

  logical diff：

+ P类集合：复杂度为多项式时间的问题

  NP：可以在多项式时间内验证一个解是否正确的集合

  NPC：是NP的一个子集,且其中每一个问题均能由NP中的任何问题在多项式时间内转化成.
  
+ terminological knowledge。这种 knowledge，大家可以理解为框架型知识，比如 Student is a type of Person，College Tutor is a type of Educator。这些 knowledge 与个体没有关 系，是框架型的。而 ABox 表示某个个体的知识，比如 jack is a Student。比如 tom 是 jack 的 爸爸。所以但凡是 individual 进来了，那么就是 ABox 的知识。

+ TopConcept ⊑ ∀hasChild.Student。这句话什么意思？True（表示论域内所有 人）被包含于某个群体，这个群体是“如果有孩子，这孩子一定是 student”。这限定了hasChild的range一定是Student。



### hw

+ Use your own words to describe what it means for knowledge representation (KR) to play a role of surrogate?
  + In the dictionary we know that the meaning of "surrogate" is "something that replaces or is used instead of something else". And "KR is surrogate" also means that we use KR to replace something instead of using something directly. Here "something" refers to object in the external world. The most significant and profound reason is : **reasoning is a process that goes on internally, while most things it wishes to reason about exist only externally.** Therefore, there is a conseptual map between KR and object in the real world. But such a surrogate is not precisely: the completely precise representation of an object is the object itself. So any representation expect itself inevitably contains simplification and artificial additions. Therefore, imperfect surrogates result in inevitably incorrect inferences. This means that the results of our reasoning can not avoid containing errors or faluts. What we can need to do is to minimize error and reduce it in the specific task we care about.
+ What are Competency Questions? How would you use them during the process of ontology development?
  + Competency Questions are some questions that help capture scope, content and a form of evaluation. For example, if we have a pizza ontology, we can ask "Does this pizza contain halal meat?". CQs play an important role in the ontology development, it means what should the ontology be competent to answer, they gives the specification of requirements. if we can answer CQ then the ontology is OK, otherwise, the ontology needs to be adjust according to our requirements.
  + I will use them reasonably to meet the development requirements of my ontology. During the process of ontology development (assuming I'm operating protege), everytime when I complete a phase of work, I would ask whether ontology meets some requirements based on the existing axiom. For example, if I'm developing a sushi ontology, I wll ask "Which sushi is spicy?".
+ Clarify, in your own words, the distinctions between closed world assumption (CWA) and open world assumption (OWA). When do CWA and OWA apply? Illustrate with an example how CWA and OWA lead to a distinction when applying them to a data/knowledge base
  + The most important difference between CWA and OWA is that CWA thinks that things that are not stated must be false and OWA assumps that in this case the answer is ”don’t know”. This means, in CWA, if a thing is not known to us, then it is false; in OWA, it may be true or false which means we don’t know.
  + When we are building a database or knowledge base, if we have detailed information about the system, then CWA should be applied。when we don’t have complete information about the system, OWA should be applied

# Word

terminology 术语

tractable ：易处理的，能在多项式时间内解决

interlude(插入)

mereonomy: 分体学，整体和部分关系的研究

formalism: 一个正式的语言,object oriented formalism,面向对象语言

sound reasoning、unsound reasoning

make explicit 显式显现

fidelity n.精确度，忠诚度

stand-in n.替代

dichotomy n.一分为二，对立

lobby n.大厅，v.游说

shed light on sth 为...提供解释

dispute n.争论

longstanding a.由来已久的，长久存在的

invigorate v.使精力充沛/活跃

ontologic n.本体

assembly v.装配

causality n.因果律