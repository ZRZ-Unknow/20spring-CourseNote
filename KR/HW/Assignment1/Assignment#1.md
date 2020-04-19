# Assignment1

*181220076 周韧哲*



### Q1

We can inter that Tibbs‘s Types is Cat. We know that "hasPet only Cat or Dog" means that  under the circumstance that Fred hasPet, Fred must have a Cat or a Dog. And Tibbs is not Dog, so Tibbs is a Cat.

### Q2

We do not know whether Fido is a Dog. Because Fred hasPet Fido, PetOwner hasPet some Cat and hasPet some Dog, "exist" means Fido could be a Cat or Dog, according to the open world assumption, we don't know whether Fido is a Dog

### Q3

No. Because a thing owning a Cat only means that the thing is a Person that hasPet some Cat. But PetOwner is the SubClassof Person that hasPet some Cat, so it is possible that the thing is not PetOwner: PetOwner is not equivalent to Person that hasPet some Cat.

### Q4

a petOwner can have >=1 Cats. Because "exist" and "forall" means petOwner must have a Pet Cat and Pet must be Cat(hasPet some Cat and hasPet only Cat).

### Q5

In the dictionary we know that the meaning of "surrogate" is  "something that replaces or is used instead of something else". And "KR is surrogate" also means that we use KR to replace something instead of using something directly. Here "something" refers to object in the external world. The most significant and profound reason is :

+ **reasoning is a process that goes on internally, while most things it wishes to reason about exist only externally.**

Therefore, there is a conseptual map between KR and object in the real world. But such a surrogate is not precisely: **the completely precise representation of an object is the object itself.** So any representation expect itself inevitably contains simplification and artificial additions. Therefore, imperfect surrogates result in inevitably incorrect inferences. This means that the results of our reasoning can not avoid containing errors or faluts. What we can need to do is to minimize error and reduce it in the specific task we care about.



### Q6

Because my sushi ontology is just a sushi ingredients hierarchy, to make it useful in restaurant ordering, there are following coordinations I will add:

+ Add the specific food and its content. For example, avocado maki is made of avocado,mayo,nori and rice, then we create a role name "has", add a class "AvocadoMaki" which is the SubClassOf "has some avocado and mayo and nori and rice".
+ Add how spicy the food is and is the food vegan or vegetarian. For example, Dynamite "hasType some mild", Yasai "hasType some Vegan".
+ Add is the food new product. Because customers may be more willing to try new products.





### Q8

To develop my sushi ontology, the first thing to do is to capture: browse the sushi menu roughly and start to look up foreign words (there are so many) in the dictionary. Then we will have a general and overall impression of this menu. Then I follow the slides to start the formal process.

+ **Term Extraction**:

  Term extraction is obviously necessary: **we have to extract the domain-related words we need from the long segments.** For example,  when we read about such a paragraph:

  + Tuna mayo: Poached yellowfin tuna with cucumber, red onion & garlic mayo, rolled in chives. A classic dish with a YO! twist! 127 kcal.                                                                                                     YO!roll: Our signature roll! Fresh salmon, avocado & mayo, rolled in orange masago. 163 kcal.

  We pull these out: *yellowfin, tuna, cucumber, onion, garlic, mayo, chives, dish, fresh, salmon, avocado, orange, masago.* These are domain-dependent, context sensitive and interest relative, so we have:

  + yellowfin, tuna, cucumber, onion, garlic, mayo, chives, dish, fresh, salmon, avocado, orange, masago

  Therefore, through Term Extraction we can get what we want (sushi ingredients) in a concise and intuitive form. Going this step one by one we get a list of terms extracted from the sushi menu.

+ **Grouping**:

  Grouping is necessary too: **we need to find the correlation between different words to build a hierarchy.**  Because we are going to build a sushi ingredients hierarchy, the ingredients should be separated according to their types. So we group the objects based on their types:

  + (Vegetable) cucumber, onion, garlic, chives
  + (Egg) mayo
  + (Fish) tuna, masago, salmon
  + (Fruit)  avocado
  + (Stuff) yellowfin, dish, fresh, orange

  We have some background knowledge we can use to round out these terms. For examble we know that the things in Stuff is not the things we care about in this task, so we remove them from our terms.

+ **Normalise Terms**:

  Same words may have different spellings in different contexts, and in many cases we will get a list of terms that are non-uniform spelling and grammar. So we need to normalise the terms, for example we normalise "chives" as "chive". And then capitalize the first letter of the words above. Moreover, we have some background knowledge we can use. Here "Masago" is the roe of capelin, so we add "Capelin" into it. After that we can get:

  + (Vegetable) Cucumber, Onion, Garlic, Chive
  + (Egg) Mayo
  + (Fish) Tuna, (Capelin)Masago, Salmon
  + (Fruit)  Avocado

+ **Organise Terms**:

  We also need to organise terms to sort out their logical hierarchy and add some more words needed. Cucumber, Onion, Garlic, Chive are specific, but they belong to a general concept: Vegetable, so they are SubClassOf Vegetable. And Tuna, Masago, Capelin, Salmon is SubClassOf Fish, Mayo is SubClassOf Egg, Avocado is SubClassOf Fruit.

+ **Encode**:

  The final work to do is to encode the terms in Protégé using OWL which means to write the terms in OWL. Once the previous work is done, this step is very easy.

Using these techniques and follow these steps, I successfully finish my sushi ingredients ontology. It contains all of the ingredients that appear in the sushi menu and classifies them into a basic hierarchy.

