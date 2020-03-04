# lecture1

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

# lecture 2

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

# lecture3

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


# Word

interlude(插入)

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