CREATE TABLE Players (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    playerId INTEGER,
    unionId INTEGER
);

CREATE TABLE Unions (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    unionId INTEGER NOT NULL,
    name TEXT NOT NULL,
    initials TEXT,
    rank INTEGER,
    leader TEXT,
    leaderId INTEGER
);

CREATE TABLE Viziers (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    primaryAttributes TEXT,
    grouping TEXT,
    consortId INTEGER
);

CREATE TABLE Consorts (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    vizierId INTEGER
);

CREATE TABLE PlayerViziers (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    playerId INTEGER NOT NULL,
    consortId INTEGER,
    talent INTEGER,
    military INTEGER,
    political INTEGER,
    research INTEGER,
    prestige INTEGER
);

INSERT INTO Unions (id, unionId, name, initials, rank, leader, leaderId) VALUES(1,204190029,"G.O.A.T.","GOAT",2,"Goat",20419003553);
INSERT INTO Unions (id, unionId, name, initials, rank, leader, leaderId) VALUES(2,204190001,"Air Acolytes","AA",1,"Aang",20419000046);
INSERT INTO Unions (id, unionId, name, initials, rank, leader, leaderId) VALUES(3,204190008,"REIGN","REIGN",3,"Lady Kenna",20419000104);
INSERT INTO Unions (id, unionId, name, initials, rank, leader, leaderId) VALUES(4,204190056,"Defiant Bastards","DB",4,"Khan",20419009638);
INSERT INTO Unions (id, unionId, name, initials, rank, leader, leaderId) VALUES(5,204190003,"Fallen Angels","FA",5,"Archangelspawn",20419000023);
INSERT INTO Unions (id, unionId, name, initials, rank, leader, leaderId) VALUES(6,204190063,"Legends","LEG",6,"Corinne",20419000261);
INSERT INTO Unions (id, unionId, name, initials, rank, leader, leaderId) VALUES(7,204190052,"White Gold","WG",7,"Lex Wellan",20419009246);
INSERT INTO Unions (id, unionId, name, initials, rank, leader, leaderId) VALUES(8,204190019,"Valhalla","VAL",8,"Skady",20419008112);
INSERT INTO Unions (id, unionId, name, initials, rank, leader, leaderId) VALUES(9,204190030,"Greenhorns","GH",9,"Emaa77",20419003413);
INSERT INTO Unions (id, unionId, name, initials, rank, leader, leaderId) VALUES(10,204190050,"The Pheonix","PHX",10,"Elva Hopper",20419003822);
INSERT INTO Unions (id, unionId, name, initials, rank, leader, leaderId) VALUES(11,204190002,"The Winners","WIN",11,"Felosial",20419000229);
INSERT INTO Unions (id, unionId, name, initials, rank, leader, leaderId) VALUES(12,204190005,"Dioses","DIO",12,"Yarelli castillo",20419000362);
INSERT INTO Unions (id, unionId, name, initials, rank, leader, leaderId) VALUES(13,204190039,"Brasil Wolf","BW",13,"Issabella Forbes",20419009252);
INSERT INTO Unions (id, unionId, name, initials, rank, leader, leaderId) VALUES(14,204190051,"FREEDOM","FREE",14,"Ada Blankenship",20419007774);
INSERT INTO Unions (id, unionId, name, initials, rank, leader, leaderId) VALUES(15,204190041,"BLM","BLM",15,"Amanda1",20419002026);
INSERT INTO Unions (id, unionId, name, initials, rank, leader, leaderId) VALUES(16,204190049,"Champion_Leads","CL",16,"Rosalind Briar",20419002532);
INSERT INTO Unions (id, unionId, name, initials, rank, leader, leaderId) VALUES(17,204190046,"Overgrowth","OVER",17,"Ivytongue",20419007359);
INSERT INTO Unions (id, unionId, name, initials, rank, leader, leaderId) VALUES(18,204190018,"ohana","OHANA",18,"isabell August",20419006956);
INSERT INTO Unions (id, unionId, name, initials, rank, leader, leaderId) VALUES(19,204190033,"Xout","XOUT",19,"Xout",20419008508);
INSERT INTO Unions (id, unionId, name, initials, rank, leader, leaderId) VALUES(20,204190070,"NoFucksGivn","NFG",20,"Adela",20419009622);
-- INSERT INTO Unions (id, unionId, name, initials, rank, leader, leaderId) VALUES(,,"","",,"",)

INSERT INTO Consorts (id, name, description, vizierId) VALUES (1,"Dilara","Dilara is the daughter of a powerful merchant, She has a deep understanding of fortune, fate and destiny.  Vizier Veli is a friend of her family.",1);
INSERT INTO Consorts (id, name, description, vizierId) VALUES (2,"Iris","Iris is a free spirited soul, who speaks straight from the heart.  This ability to channel her emotion makes her a wonderful musician.  Vizier Hadim is very fond of her music.",2);
INSERT INTO Consorts (id, name, description, vizierId) VALUES (3,"Cecilia","Cecilia is a beauty with a deeply passionate heart and smooth unblemished skin.  Her family was rescued by Vizier Lufti, and they have remained friends ever since.",3);
INSERT INTO Consorts (id, name, description, vizierId) VALUES (4,"Canfeza","Canfeza's beautiful dancing and sweet smile is often on your mind.  Her father is the swordmaster of Vizier Piyale",4);
INSERT INTO Consorts (id, name, description, vizierId) VALUES (5,"Demure","Demure is a senseitive and protective soul.  She is aftraid to open her heart to you, but can't ignore her attractions.",5);
INSERT INTO Consorts (id, name, description, vizierId) VALUES (6,"Ceren","Ceren is a rare beauty, both smart and pretty, talented as a seamstress, and so graceful in her gowns.  It was Vizier Kane that helped import some of her fine silks.",6);
INSERT INTO Consorts (id, name, description, vizierId) VALUES (7,"Indirah","Indirah grew up amongst the common folk, but her beauty marked her for greatness.  It was Vizier Ahmelek who first brought her to your attention.",7);
INSERT INTO Consorts (id, name, description, vizierId) VALUES (8,"Silken","Silken is a gentle and fragile beauty, so shy and unassuming, nervous in your presence but full of passion.  Some of her handcrafts were taught by Vizier Ishak.",8);
INSERT INTO Consorts (id, name, description, vizierId) VALUES (9,"Lydia","Lydia has an irresistable youth, smile, and playfulness, as well as an amazing artistic talent for painting.  Vizier Lala also loves her paintings.",9);
INSERT INTO Consorts (id, name, description, vizierId) VALUES (10,"Heather","Like a wild flower, Heather loves to roam the palace grounds, meet you in hidden places, and whisper secrets.",10);
INSERT INTO Consorts (id, name, description, vizierId) VALUES (11,"Daphne","Following in her father's footsteps, Daphne became a respected teacher in the palace.  Her father was a good friend of Vizier Karaman, so they have always been close to the royal family.",11);
INSERT INTO Consorts (id, name, description, vizierId) VALUES (12,"Halima","Halima has the perfect body to fit into any outfit, and loves to spend her time fawning over clothes and fashion accessories.  One of her best friends is Vizier Eviliya's wife.",12);
INSERT INTO Consorts (id, name, description, vizierId) VALUES (13,"Rana","Rana is a strong and clever woman of great beauty.  Her experience as a nurse and physician make her wordly and charming like no other.  She once tended to Vizier Piri's wounds.",13);
INSERT INTO Consorts (id, name, description, vizierId) VALUES (14,"Felicia","Felicia is an alluring and mysterious beauty, deeply involved in her romance novels, and very passionate.  She often sees Vizier Sinan in the library.",14);
INSERT INTO Consorts (id, name, description, vizierId) VALUES (15,"Elva","Elva is a clever and ambitious woman who speaks very softly and always has a compliment.",15);
INSERT INTO Consorts (id, name, description, vizierId) VALUES (16,"Hope","Hope grew up in Rhodes.  When the Ottoman forces came to conquer the city, it was Vizier Mesih who helped her move safely to Istanbul with her family.  Ever since, their families have been close friends.",16);
INSERT INTO Consorts (id, name, description, vizierId) VALUES (17,"Fiona","Fiona is the niece of Vizier Zaganos, and grew up in the Palace serving as a maid.  She schooled and cared for the Sultan's kids, and her caring ways eventually warmed the Sultan's heart.",17);
INSERT INTO Consorts (id, name, description, vizierId) VALUES (18,"Teri","Teri is a quiet and romantic soul who loves aromatic candles, healing massage, and being at peace.  Some of her techniques were learned from Vizier Ayas' wife.",18);
INSERT INTO Consorts (id, name, description, vizierId) VALUES (19,"Osilda","Osilda is a charming foreign student with a talent for languages and fun-loving personality.  She sometimes studies with Vizier Merzif.",19);
INSERT INTO Consorts (id, name, description, vizierId) VALUES (20,"Clara","Clara is a kindhearted young woman with a special talent for cooking and baking.  She sometimes tests her cuisine with Vizier Davut , who imports foreign spices for her.",20);
INSERT INTO Consorts (id, name, description, vizierId) VALUES (21,"Delorah","Delorah is an exquisite beauty with a whimsical personality and a love for birdwatching.  One of her family;s oldest friends is Vizier Kopru",21);
INSERT INTO Consorts (id, name, description, vizierId) VALUES (23,"Rosa","Rosa is an elegent flower of captivating beauty.  She loves roaming the gardens in the gentle palace breeze.  Her father is an old friend of Vizier Hersek.",23);
INSERT INTO Consorts (id, name, description, vizierId) VALUES (24,"Amber","",24);
INSERT INTO Consorts (id, name, description, vizierId) VALUES (35,"Alessa","Alessa, like her cat, has both a graceful beauty and a curious cuteness that intrigues you.  Sometimes she takes care of Vizier Murat's cat too when he is travelling.",35);
INSERT INTO Consorts (id, name, description, vizierId) VALUES (36,"Elena","",36);
INSERT INTO Consorts (id, name, description, vizierId) VALUES (62,"Maida","Maida, the cousin of Nasuh, also inherited an artistic spirit and skill.  Her medium of art is the mosaic.  She excels in creating colurful images made from thousands of finely chiseled pieces of stone, decorating the palace and delighting the court.",62);
-- INSERT INTO Consorts (id, name, description, vizierId) VALUES (,"","",);
INSERT INTO Viziers (id, name, description, primaryAttributes, grouping, consortId) VALUES (1,"Veli","Veli's martial skills may outpace his intellect, but his effectiveness on the battlefield cannot be denied","military","Military Forces", 1);
INSERT INTO Viziers (id, name, description, primaryAttributes, grouping, consortId) VALUES (2,"Hadim","Ambition and vengeance burn within Hadim's heart -- and in the service of the empire, who can say how much he will acheieve?","military","Military Forces",2);
INSERT INTO Viziers (id, name, description, primaryAttributes, grouping, consortId) VALUES (3,"Lufti","With each campaign, Lufti's mastery of the military arts deepends.  His eyes burn with the need to return to the front and bring glory to the empire.","military,political","Military Forces",3);
INSERT INTO Viziers (id, name, description, primaryAttributes, grouping, consortId) VALUES (4,"Piyale","With over 60 successful sieges to his name, Piyale has a battle-tested strategy for any occasion.  Heed his advice and you will not be disappointed.","","Military Forces",4);
INSERT INTO Viziers (id, name, description, primaryAttributes, grouping, consortId) VALUES (5,"Gedik","The business of war has its share of grim truths, but Gedik knows that an inspired soldier is an effective one.  His pre-battle speeches can lift the spirit of the most cynical warrior.","military,research","Military Forces",5);
INSERT INTO Viziers (id, name, description, primaryAttributes, grouping, consortId) VALUES (6,"Kane","Humble and gracious, Kane has never forgotten how far he has come in his years of service.  If only more at the imperial court followed his example...","prestige","Wise Forces",6);
INSERT INTO Viziers (id, name, description, primaryAttributes, grouping, consortId) VALUES (7,"Ahmelek","Ahmelek views the empire as a machine fueled by commerce and oiled by wise policy.  There are few with the skill to keep the economy running like he can.","political","Wise Forces",7);
INSERT INTO Viziers (id, name, description, primaryAttributes, grouping, consortId) VALUES (8,"Ishak","Under Ishak's guidance, the city of Istanbul has grown into one of the largest cities in the world.  He knows the value of inspiring envy among friends and enemies alike.","research","Wise Forces",8);
INSERT INTO Viziers (id, name, description, primaryAttributes, grouping, consortId) VALUES (9,"Lala","The brightest minds can never go unnoticed.  Lala's insightful writings led him on a path to protecting the Sultan's heir.  Only the truly wise can earn such trust!","prestige","Wise Forces",9);
INSERT INTO Viziers (id, name, description, primaryAttributes, grouping, consortId) VALUES (10,"Sokolluzade","Many Viziers first mastered the art of war through practical experience, but Sokolluzade emerged as a strategic prodigy as a young scholar.  He is known for his deeply held ethics.","political,research","Wise Forces",10);
INSERT INTO Viziers (id, name, description, primaryAttributes, grouping, consortId) VALUES (11,"Karaman","Karaman views the law as a simple thing: a means to separate the worthy from the traitorous.  While his methods might be questionable, his results are not.","research,prestige","Loyal Forces",11);
INSERT INTO Viziers (id, name, description, primaryAttributes, grouping, consortId) VALUES (12,"Evliya","Though the empire is vast, Eviliya has seen the furthest reaches of the world in his travels, and he bears knowledge that other Viziers only dream of.","research","Loyal Forces",12);
INSERT INTO Viziers (id, name, description, primaryAttributes, grouping, consortId) VALUES (13,"Piri","Danger lurks behind every corner -- at least as far as Piri is concerned.  You can sleep safely knowing that cautious Viziers like him are guarding the empire.","political","Loyal Forces",13);
INSERT INTO Viziers (id, name, description, primaryAttributes, grouping, consortId) VALUES (14,"Sinan","In an age where those with passion and imagination can change the world, Sinan's unparalleled architectural designs reflect the soul of the empire and its people.","political","Loyal Forces",14);
INSERT INTO Viziers (id, name, description, primaryAttributes, grouping, consortId) VALUES (15,"Hocas","Some serve the Sultan on the battlefield, others as elder statesmen.  Hocas' imcomparable writing style and wisdom bring honor to the empire even today.","research","Loyal Forces",15);
INSERT INTO Viziers (id, name, description, primaryAttributes, grouping, consortId) VALUES (16,"Mesih","Some enter imperial service for personal glory, while others, like Mesih, seek honor for their families above all.  His loyalty and work ethic are beyond reproach.","military,prestige","Experienced Forces",16);
INSERT INTO Viziers (id, name, description, primaryAttributes, grouping, consortId) VALUES (17,"Zaganos","Those honored with the opportunity to teach a prince have reason to think highly of themselves.  Zaganos bears his professional qualifications with pride.","political,prestige","Experienced Forces",17);
INSERT INTO Viziers (id, name, description, primaryAttributes, grouping, consortId) VALUES (18,"Ayas","The empire faces enemies on many fronts, but none as important as the hearts and minds of the people.  For those that stray from the path of peace and order, Ayas stands ready to deliver justice.","prestige","Experienced Forces",18);
INSERT INTO Viziers (id, name, description, primaryAttributes, grouping, consortId) VALUES (19,"Merzif","Through his years serving the empire, Merzif has faced his share of rivals.  None who question his honor or loyalty ever do so twice.","political,research","Experienced Forces",19);
INSERT INTO Viziers (id, name, description, primaryAttributes, grouping, consortId) VALUES (20,"Davut","A conqueror must be strong, resolute, and fearless -- essentially, like Davut!  He has little time for the niceties of courtly customs.  Show him his next conquest!","military","The Braves",20);
INSERT INTO Viziers (id, name, description, primaryAttributes, grouping, consortId) VALUES (21,"Fazil","Knowledge changes those who learn it.  Fazil has never been one to turn away from the unpleasant truths behind the modern world.  He has heard much that you should know.","military","The Braves",21);
INSERT INTO Viziers (id, name, description, primaryAttributes, grouping, consortId) VALUES (22,"Baltac","Cultivating a favorable peace between the empire and its neighbors has been Baltac's life's work, and he has much left to do.  Imperial dominance is his goal.","political","The Braves",NULL);
INSERT INTO Viziers (id, name, description, primaryAttributes, grouping, consortId) VALUES (23,"Hersek","For every Vizier that brings nuance and intrigue to the Sultan's service, there is one like Hersek: a straightforward soldier without secrets or pretention.","military,prestige","The Braves",23);
INSERT INTO Viziers (id, name, description, primaryAttributes, grouping, consortId) VALUES (24,"Nash","Some of the rich hoard their wealth, but Nash has always used his skills for the good of all.  A capable diplomat, he has helped levy thousands of imperial troops.","research","The Braves",24);
INSERT INTO Viziers (id, name, description, primaryAttributes, grouping, consortId) VALUES (25,"Kocasin","Despite years of loyal and distinguished service, Kocasin has always felt the need to keep proving himself.  Trust his hard-earned experience and wisdom.","military","The Magnificent Five",NULL);
INSERT INTO Viziers (id, name, description, primaryAttributes, grouping, consortId) VALUES (26,"Seydi","Throughout his naval career, Seydi has proven himself every bit the equal of his mentor, Admiral Barbaros Hayrettin.  Count on him for sound naval strategy.","military","The Magnificent Five",NULL);
INSERT INTO Viziers (id, name, description, primaryAttributes, grouping, consortId) VALUES (27,"Kilic","Charismatic and professional, the naval strategist Kilic speaks to the Sultan as an intellectual peer, never mincing his words -- even on matters of advanced military theory.","military","The Magnificent Five",NULL);
INSERT INTO Viziers (id, name, description, primaryAttributes, grouping, consortId) VALUES (28,"Kuyu","Kuyu's success against the rebels in the 100-year campaign brought him great renown as an inventive governor and general.  Few can match his determination.","military","The Magnificent Five",NULL);
INSERT INTO Viziers (id, name, description, primaryAttributes, grouping, consortId) VALUES (29,"Ozdem","One look in Ozdem's eyes will tell you all you need to know -- that standing in his way is the surest path to death.  He has neither mercy nor pity.","military","The Magnificent Five",NULL);
INSERT INTO Viziers (id, name, description, primaryAttributes, grouping, consortId) VALUES (30,"Sinadim","","military,political","The Outstanding Four",NULL);
INSERT INTO Viziers (id, name, description, primaryAttributes, grouping, consortId) VALUES (31,"Semsi","Some Viziers bring a practical approach to war and governance, but Semsi has the soul of a poet and a musician's ear.  To him, we are but characters in an endless opera.","military,political","The Outstanding Four",NULL);
INSERT INTO Viziers (id, name, description, primaryAttributes, grouping, consortId) VALUES (32,"Yavuz","","military,political","The Outstanding Four",NULL);
INSERT INTO Viziers (id, name, description, primaryAttributes, grouping, consortId) VALUES (33,"Karahmet","","military,political","The Outstanding Four",NULL);
INSERT INTO Viziers (id, name, description, primaryAttributes, grouping, consortId) VALUES (34,"Yusuf","Yusuf's loyalty to the empire is founded on a practical understanding of the cost of war and the value of family.  He defends the realm with a father's ferocity.","military","The Gallants",NULL);
INSERT INTO Viziers (id, name, description, primaryAttributes, grouping, consortId) VALUES (35,"Murat","As a tactician, Murat has always prided himself in seeing the hidden factors behind every battle and sword-stroke.  He brought those insights to Sultan's elite guard, making them even deadlier.","","The Gallants",35);
INSERT INTO Viziers (id, name, description, primaryAttributes, grouping, consortId) VALUES (36,"Ibrahim","Wise, intelligent, generous, and courageous, Ibrahim embodies the heroic ideal.  Yet for all his greatness, he remains humble in the Sultan's presence.  A true friend and capable advisor.","military,research","The Gallants",36);
INSERT INTO Viziers (id, name, description, primaryAttributes, grouping, consortId) VALUES (37,"Candar","","research","The Gallants",NULL);
INSERT INTO Viziers (id, name, description, primaryAttributes, grouping, consortId) VALUES (38,"Alamus","Only the empire's finest minds have a chance to serve the Sultan as an heir's tutor.  Alamus is one such mind -- an eccentric, undeniably brillian teacher.","prestige","The Gallants",NULL);
INSERT INTO Viziers (id, name, description, primaryAttributes, grouping, consortId) VALUES (39,"Tahrun","","research","The Gaurds",NULL);
INSERT INTO Viziers (id, name, description, primaryAttributes, grouping, consortId) VALUES (40,"Semi","","political","The Gaurds",NULL);
INSERT INTO Viziers (id, name, description, primaryAttributes, grouping, consortId) VALUES (41,"Alihad","","prestige","The Gaurds",NULL);
INSERT INTO Viziers (id, name, description, primaryAttributes, grouping, consortId) VALUES (42,"Serdar","","military","The Gaurds",NULL);
INSERT INTO Viziers (id, name, description, primaryAttributes, grouping, consortId) VALUES (43,"Mustafa","","prestige","The Valiants",NULL);
INSERT INTO Viziers (id, name, description, primaryAttributes, grouping, consortId) VALUES (44,"Kopru","","political","The Valiants",NULL);
INSERT INTO Viziers (id, name, description, primaryAttributes, grouping, consortId) VALUES (45,"Rustem","","military","The Valiants",NULL);
INSERT INTO Viziers (id, name, description, primaryAttributes, grouping, consortId) VALUES (46,"Joan of Arc","","","Foreign Legends",NULL);
INSERT INTO Viziers (id, name, description, primaryAttributes, grouping, consortId) VALUES (47,"Beryl","","","Foreign Legends",NULL);
INSERT INTO Viziers (id, name, description, primaryAttributes, grouping, consortId) VALUES (48,"Columbus","","","Foreign Legends",NULL);
INSERT INTO Viziers (id, name, description, primaryAttributes, grouping, consortId) VALUES (49,"Tolana","","","Foreign Legends",NULL);
INSERT INTO Viziers (id, name, description, primaryAttributes, grouping, consortId) VALUES (50,"Leonardo Da Vinci","","military,research","Unique Forces",NULL);
INSERT INTO Viziers (id, name, description, primaryAttributes, grouping, consortId) VALUES (51,"Grace O'Malley","","military,prestige","Unique Forces",NULL);
INSERT INTO Viziers (id, name, description, primaryAttributes, grouping, consortId) VALUES (52,"Damat","","","Legendary Team",NULL);
INSERT INTO Viziers (id, name, description, primaryAttributes, grouping, consortId) VALUES (53,"Jonas","","military,political","Legendary Team",NULL);
INSERT INTO Viziers (id, name, description, primaryAttributes, grouping, consortId) VALUES (54,"Nicolaus Copernicus","","","Legendary Team",NULL);
INSERT INTO Viziers (id, name, description, primaryAttributes, grouping, consortId) VALUES (55,"Sormet","","military,prestige","Legendary Team",NULL);
INSERT INTO Viziers (id, name, description, primaryAttributes, grouping, consortId) VALUES (56,"Piri Reis","","","Legendary Team",NULL);
INSERT INTO Viziers (id, name, description, primaryAttributes, grouping, consortId) VALUES (57,"Barbaros","","military","The Specials",NULL);
INSERT INTO Viziers (id, name, description, primaryAttributes, grouping, consortId) VALUES (58,"Dragut","","","Eternal Warriors",NULL);
INSERT INTO Viziers (id, name, description, primaryAttributes, grouping, consortId) VALUES (59,"Asya","","","Imperial Guardian",NULL);
INSERT INTO Viziers (id, name, description, primaryAttributes, grouping, consortId) VALUES (60,"Jasmine","","","Imperial Guardian",NULL);
INSERT INTO Viziers (id, name, description, primaryAttributes, grouping, consortId) VALUES (61,"Teliah","","","Imperial Guardian",NULL);
INSERT INTO Viziers (id, name, description, primaryAttributes, grouping, consortId) VALUES (62,"Nasuh","A gifted Janissary from Bosnia, Nasuh rose through the ranks, as a swordsman, sharpshooter, and later, a mathematician.  But, his biggest talent lies in painting miniatures.  He even created a board game called Matrak.  Nasuh sees the world through the patient eyes of a master illuminator, noticing the slightest detail.","military,research","Imperial Shield",62);
-- INSERT INTO Viziers (name, description, primaryAttributes, grouping, consortId) VALUES (,"","","","",)
