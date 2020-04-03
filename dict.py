opening = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="styles/styles.css">
    <title>Document</title>
    <style>
      .dropbtn {
        background-color: #3498DB;
        width: 900px;
        color: white;
        padding: 16px;
        font-size: 16px;
        border: none;
        cursor: pointer;      }      .dropbtn:hover, .dropbtn:focus {
        background-color: #2980B9;
      }      .dropdown {
        position: relative;
        display: inline-block;
      }      .dropdown-content {
        display: none;
        position: absolute;
        background-color: #f1f1f1;
        min-width: 900px;
        z-index: 1;
      }      .dropdown-content a {
        color: black;
        padding: 12px 16px;
        text-decoration: none;
        display: block;
      }      .dropdown-content a:hover {background-color: #ddd}      .show {display:block;}
    </style>
</head>
<body>
"""
close = """
</body>
</html>
"""
dict_of_camping_returns = {
    "q1": """
<div class="answer">
    <h3>camping alone  </h3>
    <p> woah spooky </p>
</div>""",
    "q2": """
<div class="answer">
    <h3>2-3 people  </h3>
    <p> camping is always better with friends </p>
</div>""",
    "q3": """
<div class="answer">
    <h3>4+ </h3>
    <p> you better bring alot of food so theres that </p>
</div>""",
    "r1": """
<div class="answer">
    <h3>beginner </h3>
    <p> Lorem ipsum dolor sit amet consectetur adipisicing elit. Eius dolore commodi architecto tempore deleniti, laudantium, cum nobis, porro natus recusandae doloremque!
         Architecto hic laboriosam, ad accusantium voluptates ipsam odit magni.</p>
</div>""",
    "r2": """
<div class="answer">
    <h3>Some Experience </h3>
    <p> Lorem ipsum dolor sit amet consectetur adipisicing elit. Fugit nesciunt magnam sunt deleniti rerum nemo ipsam minima maxime aspernatur atque? Enim minus quis
         corrupti deserunt inventore dolores obcaecati officia ducimus.
    </p>
</div>""",
    "r3": """
<div class="answer">
    <h3>I'm practically Bear Grills </h3>
    <p> Lorem ipsum dolor sit amet consectetur adipisicing elit. Hic, modi. Explicabo libero, culpa delectus magni error blanditiis expedita labore quas porro quis numquam tempore dolorem qui natus inventore, sapiente illo.
    Aliquam at, cum fugit dolore quae quis molestiae consequuntur, hic asperiores exercitationem perferendis esse? Tempora mollitia ipsam, aperiam, omnis praesentium cumque obcaecati consectetur sunt, at quibusdam voluptatem ducimus corporis quam.
    Amet tempore tempora voluptatum incidunt id alias et ratione quia ducimus corrupti nesciunt possimus inventore vero quibusdam odio optio iure hic est exercitationem libero, perferendis quos tenetur? Veniam, sed repellat.
    Architecto totam</p>""",
    "s1": """
<div class="answer">
    <h3>Overnight </h3>
    <p> Lorem ipsum dolor sit amet consectetur adipisicing elit. Assumenda fugit eveniet corporis molestiae, dicta eos voluptate, at qui, aut enim necessitatibus expedita labore accusantium? Ratione sed veniam totam modi assumenda.Ipsum quas pariatur quis reprehenderit aspernatur dolores, officia tempora aliquid in aliquam aut aperiam ullam nemo, excepturi natus, iste hic perferendis 
        vero impedit modi eos facilis. Facere officia sit sequi! 
    </p>
</div>""",
    "s2": """
<div class="answer">
    <h3>2-3 days</h3>
    <p> Lorem, ipsum dolor sit amet consectetur adipisicing elit. Ratione illum deserunt placeat? Modi fuga inventore delectus, nihil id, ea consectetur, tenetur quasi ipsa et perspiciatis nobis illo unde! Libero, illo!Pariatur aperiam neque, at praesentium quam iure! Harum laborum velit porro. Esse molestiae, sit eveniet doloremque laboriosam, ipsa ad voluptas 
        cum laudantium delectus explicabo deleniti quae sint hic eius labore.</p>
</div>""",
    "s3": """
<div class="answer">
    <h3>week+ </h3>
    <p> Lorem ipsum dolor sit amet consectetur adipisicing elit. Assumenda fugit eveniet corporis molestiae, dicta eos voluptate, at qui, aut enim necessitatibus expedita labore accusantium? Ratione sed veniam totam modi assumenda.Ipsum quas pariatur quis reprehenderit aspernatur dolores, officia tempora aliquid in aliquam aut aperiam ullam nemo, excepturi natus, iste hic perferendis 
        vero impedit modi eos facilis. Facere officia sit sequi! 
    </p>
</div>""",
}
dict_of_off_roading_returns = {
    "q1": """
<div class="answer">
    <h4>Desired Difficulty</h4>
    <p>Easy</p>
    <p>Experienced</p>
    <p>Advanced</p>
</div>""",
    "q2": """
<div class="answer">
    <h4>Easy</h4>
    <p>Silver Lake</p>
    <p>Midway Trail</p>
    <p>Pony Express</p>
</div>""",
    "q3": """
<div class="answer">
    <h4>Experienced</h4>
    <p>Forst Lake</p>
    <p>Dutchman's Flat</p>
    <p>Pittsburg Lake</p>
</div>""",
    "r1": """
<div class="answer">
    <h4>Advanced</h4>
    <p>Mary Ellens</p>
    <p>Poison Spider</p>
    <p>Hell's Revenge</p>
</div>""",
    "r2": """
<div class="answer">
    <h4>Easy supplies</h4>
    <p>Snacks</p>
    <p>jacket</p>
    <p>camping chair</p>
</div>""",
    "r3": """
<div class="answer">
    <h4>Experienced supplies</h4>
    <p>Snacks</p>
    <p>Jacket</p>
    <p>Camping chair</p>
    <p>Spare Tire</p>
    <p>Jack</p>
    <p>Rachet set</p>
    <p>Sandwhich or light meal</p>
</div>""",
    "s1": "<div>missed mark</div>\n",
    "s2": "<div>missed mark</div>\n",
    "s3": "<h3>test</h3>\n",
    "t1": "<h3>test</h3>\n",
    "t2": "<h3>test</h3>\n",
    "t3": "<h3>test</h3>\n",
}
dict_of_shooting_returns = {
    "q1": """
<div class="answer">
    <h3>Indoor </h3>
    <p>When Shooting indoors you will need ear protection, eye protection and some money in your pocket to purchase ammo if needed </p>
</div>""",
    "q2": """
<div class="answer">
    <h3>Outdoor </h3>
    <p> when Shooting out doors you want to bring extra layer of clothes based on the weather, ear protection, eye protection, 
        some foood all the correct type of ammo you will need</p>
</div>""",
    "r1": """
<div class="answer">
    <h3>beginner </h3>
    <p> as a beginner you need to come with a attitude to learn and have fun</p>
</div>""",
    "r2": """
<div class="answer">
    <h3>intermidate </h3>
    <p> if you see someone being unsafe let them know, so no one will git hurt. </p>
</div>""",
    "r3": """
<div class="answer">
    <h3>expert </h3>
    <p> just because you're an expert does not mean you know everything 
        and always be disaplined with your safety</p>
</div>""",
    "s1": """
<div class="answer">
    <h3>Skeet </h3>
    <p> needs for skeet shooting are a shotgun, skeet targets, shotgun shells,
        something to throw the skeet.
    </p>
</div>""",
    "s2": """
<div class="answer">
    <h3>Rifle </h3>
    <p> needs are ammo for the specfic type of rifle you have, 
        and some kind of target</p>
</div>""",
    "s3": """
<div class="answer">
    <h3>pistol</h3>
    <p> needs are the right type of ammo that your gun takes 
        and all of your PPE  
    </p>
</div>""",
    "s4": """
<div class="answer">
    <h3>Long Range Rifle</h3>
    <p> you know what you need.. ammo your gun and youre ppe  
    </p>
</div>""",
}
dict_of_fishing_returns = {
    "q1": """
<div class="answer">
	<h3>lone fisher</h3>
	<p>Fishing is all about alcohol consumption, if you are alone, know your limits and consume responsibly</p>
</div>""",
    "q2": """
<div class="answer">
	<h3>2-3 people with you</h3>
	<p>Choose your freinds carefully, this is a good party size to rent a boat for a bit, in addition to your fishing equiptment, bring the right amount of booze</p>
</div>""",
    "q3": """
<div class="answer">
	<h3>A party of 4+</h3>
	<p>Not much fishing is going to get done in a group this big, bring a fuckton of booze, and get ready for a good time. hell, fishing equiptment is optional at this point.</p>
</div>""",
    "r1": """
<div class="answer">
	<h3>beginner</h3>
	<p>recomended that you start with lure fishing</p>
</div>""",
    "r2": """
<div class="answer">
	<h3>Some Expierience</h3>
	<p>At this point you may want to get into fly or bait fishing</p>
</div>""",
    "r3": """
<div class="answer">
	<h3>So you are God himself huh?</h3>
	<p>Idk man, you are the god of fishing, do whatever the fuck you want</p>
</div>""",
    "s1": """
<div class="answer">
	<h3>2 hours</h3>
	<p>if you are intent on catching something, try to keep your line in the water as much as possible</p>
</div>""",
    "s2": """
<div class="answer">
	<h3>four hours</h3>
	<p>a nice block of time to fish, keep your line in the water and bring plenty of booze</p>
</div>""",
    "s3": """
<div class="answer">
	<h3>All day fishing is the shit</h3>
	<p>remember the important thing is to have fun</h3>
</div>""",
}
dict_of_LARPing_returns = {
    "q1": """
<div class="answer">
      <h3>Warrior</h3>
      <p>your costume and a questions on how to participate</p>
 </div>""",
    "q2": """
<div class="answer">
        <h3>elf</h3>
        <p>your costume and a understanding on how the campaign will go</p>
    </div>""",
    "q3": """
<div class="answer">
        <h3>Wizard</h3>
        <p>your costume and a way to help others and be a leader amoung the new players</p>
    </div>""",
    "r1": """
<div class="answer">
        <h3>Wasatch Mountain State Park</h3>
        <p>a mountainous adventure fill with lots of places to hide and suprise attack you enemy</p>
    </div>""",
    "r2": """
<div class="answer">
        <h3>Affleck Park</h3>
        <p>a green pasture of openess that will be filled with the blood of your enemy</p>
    </div>""",
    "r3": """
<div class="answer">
        <h3>Apprentice(wizard)</h3>
        <p>A all powerfull being who donesnt let anything cross into his territory</p>
    </div>""",
    "s1": """
<div class="answer">
        <h3>Elven archer</h3>
        <p>A long range shooter who can hit a targets heart from 300yds</p>
    </div>""",
    "s2": """
<div class="answer">
        <h3>Healer</h3>
        <p>Has the ability to save there comrads and heal themselves along with killing the opponent with science</p>
    </div>""",
    "s3": """
<div class="answer">
        <h3>Healer</h3>
        <p>Has the ability to save there comrads and heal themselves along with killing the opponent with science</p>
    </div>""",
}
