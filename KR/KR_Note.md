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







# Word

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