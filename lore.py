import random

#region

desc0 = '''Biological Containment Canister Specifications

Using a liquid methane / nitrogen mixture for suspending specimens at an internal temperature of - 200C

Titanium reinforced structure for high tensile strength. Composite high-strength plex-glass

Each unit is equipped with a remote "self-destruct" detonation charge. Stand clear to 20 feet before detonating.  Before detonation, biological corrosive acid will dissolve specimen before explosive detonation in order to prevent further contamination.'''

desc1 = '''XM-88 "Archer" Anti-Personnel Turret Spec:

Primary Armament: Electromagnetic launcher (EML) with hyper-kinetic hard-kill projectiles

Projectiles: composed of 7 gram depleted-uranium (military grade) saboted slugs.

Rate of Fire: 2 rounds per second per barrel, with an average projectile velocity of greater than 7km/sec. 

The "Archer" has a 360 degree swiveling fire-arc and is capable of tracking aerial targets.

Possible weaknesses: titanium pusher plates and silica bore riders'''

desc2 = '''Human DNA chains have restructured resulting in extreme and rapid cellular mutation.

Pathogen - highly evolved variation of TSE ("transmissible spongiform encephalopathies"). This variation appears to attack all organs as well as the skin.  

Related pathogen families: BSE ("mad cow disease"), CJD ("Creutzfeldt-Jakob disease").  

Pathogen biology - malformed protein molecule (infectious prion).

Method of infection - unknown.

Mortality rate - 6 hours (predicted)'''

desc3 = '''//Document Header


The Eye of the Initiate
A Manifesto for the Ages

The great secret of mankind is that only one social division has any real merit. We are a vast, divided room, a darkened cave, wherein one in millions holds a candle by which to see. 

This great secret can be expressed in many ways: Evolution is not progress, it is adaptation; left to its own, life would simply exist, content to breed, to chew cud, to huddle together in darkness throughout all of time. 

The spark of our awareness allows us to work relentlessly toward a single goal. The history of man is a distraction, not worth recording. The history of our order is the only true progress. 

Concepts of God, equality, nobility, artistic movements, psychological profiles, family or culture are all simple obfuscation. Freeman, slave, oppressor and oppressed are all meaningless titles. Only one designator matters: Enlightened. We pass the torch of knowledge to one another throughout the long climb of history.

We exist to propel ourselves into clarity. The uninitiated may reap the harvest of our labors, but they are only the warm pool of DNA from which we draw our numbers. We are a history-long conversation among the wise, the smallest minority. We are the only agenda.

Mr. White


//Contents Encrypted: Stage 2 Black Ops Program'''

desc4 = '''Derived from inert polymers and the dinokaryotic nuclei of deep-sea bioluminescent dinoflagellates, this serum is the latest military grade hemostatic agent.

The serum is both a blood expander and blood coagulant. The serum prevents a patient from entering shock by providing an inert blood expanding polymer while chemically attacking the moisture of a hemorrhaging wound. After injection near the localized trauma area, the serum quickly forms a clot, and the inert polymers greatly aid in skin regeneration.'''

desc5 = '''S-4 Laboratory, Biological Division MLW-89473

Laboratory Log - 05121992 CST 13:00

Supervising Research Officer: Fredrick Henry White

Phase IV of the Theta project is progressing well. During our last test with the Phase IV's infectious attack, we uncovered a very interesting development happening within the remains of the victim. It appears that the deposited mutagen continued to multiply and fester in the mutilated corpse - becoming some sort of...mutagen factory. We look forward to a future test where we will examine the effect of this contagious corpse on surrounding mutant organisms.'''

desc6 = '''From: Internal Affairs and Information Services
Sent: Thursday, July 18, 1995 09:45 AM
To: MLA dd - USD(I); all 
Subject: URGENT: Operation DesertRat
Importance: High 

It has come to our attention that rogue agents under assumed names have begun to use the Internet as an underground channel for distribution of classified information as it relates to our involvement with Extraterrestrial Biological Entity (EBE). To rectify this situation, we authorize the immediate creation of false personalities who will be logged onto major UFO message boards and Internet Relay Chat sessions. Once these Internet personalities have established themselves, websites supposedly created by these personalities will go "live" with the sole purpose of discrediting and providing humorous coverage of the unauthorized information. A second set of personalities will also be created to serve as extremist UFO researchers. These people will claim credit for the unauthorized information and transform it using absurd exaggeration to appear hoax-like and nonsensical in an effort to further invalidate the significance of this data to the general public.

NATIONAL SECURITY INFORMATION DIRECTORATE

This may contain information exempt from mandatory disclosure under the Freedom of Information Act (FOIA).'''

desc7 = '''USACE(8642A) EXO-MAT TEAM FIELD REPORT
Team Charter Deployment: Santiago, Chile

SUMMARY REPORT
Materials Analysis - Isla de Pascua ("Rapa Nui")

Following SATCOM alert, requested spectral analysis and magnetic resonance imaging tests were conducted on-site. 

Survey team reported materials of unknown origin at a depth of 14m. (Attached readings consistent with 1951 Nevada findings.)

Survey team leader speculates objects were in place - in the form of identical oblong polyhedrals - approximately 87,000 years prior to aboriginal efforts to anthropomorphize objects by carving crude faces into stone exteriors. (Initial Naval contact - Easter Day in 1722. See archived ship journals for Admiral Roggeveen.)

Given high profile nature of cultural artifacts, recommend leaving objects in place pending further approval. Site should be added to Mil-Star RECON trajectory.'''

desc8 = '''From: Internal Affairs and Information Services, ISD
Sent: Thursday, May 06, 2004 12:45 PM
To: R. Brannon MLA dd - USD(I); 
Subject: URGENT: Use of Non-authorized Propaganda 
Importance: High 

FOR OFFICIAL USE ONLY 

Mr. Brannon, you are in direct violation of personnel conduct code: 564864-34A. You are ordered to remove all and any non-authorized propaganda that is applied to your vehicle. Security has indicated that you have a bumper sticker mocking the relationship between alien life and the US government. Our policies are meant to avoid public scrutiny and investigation by maintaining a low profile on such subject matter. Failure to comply will result in your immediate termination and removal from the premises.

INTERNAL AFFAIRS AND INFORMATION SERVICES DIRECTORATE'''

desc9 = '''MEMORANDUM

From: P. Vaden, Groom Lake Facility Director
To: New Employees


Welcome to our facility. If you are here, you are indeed a unique, talented, and trusted individual. Only the best of the best come to Groom Lake. Your presence here is appreciated, and your silence about what you see here is of course expected.

Internally and externally, there are many interesting nicknames for the Groom Lake Military Facility. Some of these include:
Area 51
Dreamland
Watertown
The Ranch
Paradise Ranch
Station 3
The Box
Air Force Flight Test Center
Detachment 3 (AFFTC Det. 3)


Please use Groom Lake or Groom Lake Military facility in all official documents. Thank you, and again, welcome!


Sincerely,

Colonel P. Vaden
Groom Lake Facility Director'''

desc10 = '''MITES - One of the first experiments with mutagen involved Dr. Cray dropping a single drop into common insects: ants, ticks, dust mites. It is unclear which species these grew from, though it is likely either the Deer Tick (Ixodes scapularis) or the Brown Dog tick (Rhipicephalus sanguineous). However, employees usually refer to them as mites. Their exceptionally aggressive behavior was bred for land-war use. Unfortunately, they have escaped the lab, and are now a horrible nuisance.'''

desc11 = '''Dissection of Specimen Subject - 4839-3665RW
S-4 Laboratory, Biological Division MLW-89473

Procedure Transcript: 07051947 CST 13:00

As you can see, the extra-terrestrial subject in this case is fully intact. All external appendages and internal organs have been preserved. The skin of the subject contains an unusual pigment similar to that of bioluminescent cephalopods. Some of the pigment is arranged in vein-like structures.  The initial incision emitted a faint gas. The odor was quite repugnant and lingered throughout the duration of the procedure. 

Peeling back the epidermis we noted the lack of fatty tissue along with an unusual striation pattern in the dense muscle fiber.  The circulatory system is composed of a primary and secondary heart, each containing 4 chambers. It is interesting to note that the primary heart arteries supply plasma to the brain area only. The secondary heart supplies plasma to the rest of the body. The bronchial tubes are lined with gill-like filters and lead to a honeycomb-like compound lung structure. The digestive tract appears simplified with an organ that appears to function as a kidney and liver. There do not appear to be reproductive organs on this subject. (Note: previous subjects retained some sort of vestigial reproductive organs.) 

Examination of the skull area reveals a 3 lobe, brain-like mass nearly 3 times the size of a human brain. The optic nerves are attached to the smallest of the lobes. The small lobe itself seems to serve as the central cortex for the whole brain itself. The remaining lobes also contain phosphor filled bladders. The eyes are unusual in that no pupils exist. The cornea is quite large and covers the entire surface of the eye, leading to greater peripheral vision.  Ocular muscles are absent - vision tracking is similar to that of hawks.

The palms of the hands also contain a liquid-filled, bioluminescent bladder. Upon puncturing the bladder, the liquid sprayed against Dr. Jacobson and caused severe chemical burns to his face and hands. The resulting gas from the reaction caused an evacuation of the laboratory as several nearby lab assistants collapsed under violent seizures. None of those afflicted have survived and we have suspended any further exploratory autopsies.'''

desc12 = '''S-4 Laboratory, Biological Division MLW-89473
Laboratory Log - 03151988 CST 15:00
Supervising Research Officer: Matthew F. White 

We have entered phase IV of our genetic engineering research. This is a critical juncture and our most aggressive. While Phase I met with some early success, Phase II proved to be near disastrous as one of the subjects managed to escape containment. While the subject was never found, we are convinced that its condition left it vulnerable to common bacteria. Phase IV attempts to attain extra-terrestrial affinity through the use of impregnated surrogates obtained through our joint terran-EBE abduction raids of desolate populace. The surrogate births are accelerated to produce a mature embryo. Extraction of the embryo is accomplished through the termination and quick evisceration of the surrogate. All remaining biological material is destroyed including the surrogate and any personal possessions that were with the surrogate during abduction.'''

desc13 = '''Non-human DNA chains. 242 "extra" chromosome base pairs. 

Embryonic fluid based on an unknown organophosphate. Unclassified cellular organisms transport nitrogen and ethylene glycol to artificial grown blood vessel analogs.

Plasma-type fluid. Possible blood replacement rich in nitrogen. Serotypes show evidence of cloning.'''

desc14 = '''WO: #09232004-1100
DEPT: Biological Analysis Laboratories - Weapons Division

Request submitted for 10,000 clear polycarbonate titanium reinforced biological specimen containers. This shipment must be delivered by the end of this week in order to transport the remaining organisms that were responsible for the incident at the decommissioned Green River Launch Complex. These specimens must be handled with extreme care as they are very much alive. We believe that Vechtol containers filled with phosphor enriched cattle bile should be effective in neutralizing the organisms for safe shipment to Area 51.'''

desc15 = '''Aircraft Propulsion Laboratory Analysis
Report by Dr. Victor Weisbrod
Prepared for Dr. Winston Cray
Dec 18, 1949

Reconstruction of the primary propulsion systems has met with serious delays. Many of the control components have sustained extensive damage. It is hoped that the on-site triage of the EBE (Extraterrestrial Biological Entity) occupants and recent success in their rehabilitation by Dr. Cray will result in new information about these devices. What we have been able to discover so far is that the propulsion system operates as a solid-state device - no moving parts are required to create thrust. Initial theories were that this device was a form of advanced Ion engine - thrust is produced by the interaction of highly charged and accelerated electrons colliding with air molecules. Upon further examination and research we have discovered that the propulsion system has more in common with the recently proposed Biefeld-Brown device. The thrust from such a device is created from the interaction between the high-frequency, high power components of the craft and the surrounding vacuum properties of the environment - in effect, pushing against the very fabric of space itself. It appears that the propulsion system was capable of converting to an Ion engine during atmospheric operation. It is possible that our classified hyper-microwave surveillance initiative, project MOGUL, interfered with the alien craft's high frequency components and control systems resulting in the crash in New Mexico.'''

desc16 = '''LOT 235, EXHIBIT D
ITEM: Chart/ Diagram Document
DESC:

This appears to be a chart relating the positions of the ancient Pyramids on the Giza Plateau in Egypt to the stars in the constellation that we call the belt of Orion. The chart shows that the Great Pyramid, Khufu, aligns with the constellation star, Alnitak; the center pyramid, Khafre aligns with the star Alnilam; and the smallest pyramid, Menkaura, aligns with star Mintaka. Furthermore, the chart shows a relationship between the Sphinx and the Dark Star, Rasalas - a star that we now know is the home of the EBEs. The position of the Orion constellation stars and the dark star do not directly align with the pyramids and the Sphinx today. However, we have performed procession calculations of when the stars did align and when the Dark Star was at its closest orbit to the earth. Data seems to indicate that this chart was a timetable for extra-terrestrial travel in the year 10,450 BC - near the end of the reign of the great and ancient Atlantis and Osirian civilizations that occupied the Mediterranean and surrounding areas before the great flood. While the assumption is that both highly advanced civilizations perished during the great flood, this chart suggests that these civilizations may have either been evacuated to the Dark Star...or even worse, annihilated by the EBEs traveling from the star at that time. It is interesting to note that the Dark Star Rasalas has a procession cycle of 12397 earth years. The year in which we made contact with the EBEs, 1947, was the next window of opportunity for travel.'''

desc17 = '''From: Strategic Operations and Information Services, ISD
Sent: Tuesday, December 11, 1966 11:15 PM
To: MLA dd - USD(I) - All; 
Subject: URGENT: Use of Subterfuge during EBE Surrogate Acquisition 
Importance: High 

FOR OFFICIAL USE ONLY

Our activities in acquiring human surrogates for the EBE genetics procedures is increasingly in danger of irreversible exposure to the general public. Our advancements in the number of surrogate raids have resulted in sloppy and regrettable mistakes such as the escape of Barney and Betty Hill. These mistakes have resulted in an "awakening" leading to undesirable scrutiny by the public that can hamper our future progress towards evolution. The EBEs have determined that we must pursue solutions through preying on human psychology to minimize the public scrutiny.  Humans are far better than any EBE in determining how to manipulate other humans. Based on a recent criminal case where bank robbers used explosions across town to divert attention from a string of bank robberies, a lab assistant suggested that we also develop a diversion to draw attention from our abduction activities. H.C. was thinking for days about an appropriate diversion that could play into the psychology of the "alien among us" mythos. He needed something that appeared far less threatening than the truth. He came up with an idea based on juvenile activities in vandalism that he had participated in his youth. Rival high school teams in Ohio used to spell out derogatory messages in crop fields of opposing teams for intimidation and fun. This was always effective in grabbing the attention of the whole town and usually became front-page news. Imagine the furor now, if a message appeared from an unknown source instead of from an opposing high school football team. Imagine if large pictograms like the Nazca lines were being created in the modern age. With the deep-seated fascination and acceptable paranoia of the general public over the Nazca lines and their supposed messages, this seems like the most appropriate plan of diversion. (An interesting note: EBEs claim that the Nazca lines were present even before they arrived - they are also baffled as to who or what originally created them.) Once a decision was made on how to deliver the message, what would that message be? The answer came in the form of an executive toy sitting on H.C.'s desk, a kaleidoscope to be exact. The symmetrical patterns in this toy seemed like it could be some sort of cryptic message. This became the inspiration for the idea of crushing simple patterns into crop fields.'''

desc18 = '''LOT 235, EXHIBIT J
ITEM: Chart/ Diagram Document
DESC:

Analysis of the Atlantis map has resulted in several observations. First, there seem to be two symbols on the map that are clearly Osirian. One is known as the Flower of Life - variations of this symbol have been found in early civilizations throughout the Middle East and Asia. The other symbol is the 'djed' pillar. In this Osirian symbol, the pillar represents the backbone of the physical world as well as the channel through which the divine spirit might rise to rejoin its source. Both symbols together may describe the life cycle of these civilizations where by the circle of life is completed upon some sort of travel back to a home world. Looking through the map, we do notice how the city seems to have an industry based on fantastically advanced weaponry and defense. There are several large areas that may represent munitions stores. There are various areas containing symbols that appear to be projectiles propelled by flames. There were several major seaports each having the protection of these mechanisms. A ring of Obelisk symbols encircle the city and each has a zigzag symbol similar to lightning next to it. What is more peculiar are the symbols that represent machinery appear to be flying. Between this map and the star chart relating pyramid and Sphinx positions to a dark star known to be inhabited by the EBEs, we are finding a curious relationship between these early advanced civilizations and the EBEs. The EBEs have been reluctant to divulge any information confirming our suspicions of a connection. Whether the Atlanteans were from a distant world or if they merely worshipped the idea of traveling to a distant mythical world is still unknown. What we do know is that the entire civilization mysteriously disappeared nearly 10,000 years ago. While we have found archeological remnants of the Osirians throughout the seabed of the Mediterranean, we have yet to find any such artifacts from the Atlanteans. Maybe each met a different fate just before the Great Flood.'''

desc19 = '''From: Internal Affairs and Information Services, ISD
Sent: Tuesday, August 23, 2004 2:35 PM
To: MLA dd - USD(I); 
Subject: URGENT: Call for Volunteers - Tolerance Trials 
Importance: High 

FOR OFFICIAL USE ONLY 

Our behavioral laboratories need volunteers for the new tolerance trials starting next week. These tests are straightforward and simply test the responsiveness of our latest ultrasonic biological sensors as they apply to the optic nerve. Scarring for these trials will be non-existent as we will perform the slightly invasive procedure from a less noticeable and readily available entrance. Volunteers exhibiting regular bowel movements are preferred and free therapy along with counseling will be provided following the procedure for as long as required. We know that this trial will be very popular so sign up early! 

INTERNAL AFFAIRS AND INFORMATION SERVICES DIRECTORATE'''

desc20 = '''From the Offices of Internal Affairs and Information Services, ISD
Prepared for President Ronald Reagan
April 1, 1984

The Groom Lake Weapons Testing Facility was the next campus to be constructed after the hangar area. After the development of the U-2 spyplane, there was extreme pressure from John Foster Dulles, the secretary of state under President Dwight D. Eisenhower, to develop a high altitude weapon/payload system suitable for the U-2. Technology that we recovered and restored from a crash incident in New Mexico became invaluable in jump-starting our efforts into early beam and direct energy weapons. The weapons facility was constructed and tuned to handle testing of such weapons. The facility was rebuilt in 1967, after a weapons test resulted in a run-away chain reaction. The reaction phase-shifted the molecular structure of the support beams, causing a devastating collapse and inflicting serious casualties. Among the dead were Victor Helmann, Dr. Winston Cray's technical assistant, and weapons/propulsion specialist Anna Lenowitz, weapons project leader and wife of Fredrick Henry White. Lately, the testing facility has been home to the Aurora weapons project.'''

desc21 = '''Lab Report: Biochemistry Analysis (Jul 14)
Department of Molecular Biology
Massachusetts Research Labs, Boston 02114, USA 

Unusual metal ion catalysis in an acyl-transferase ribozyme.

Kinetic tests of wild-type ribozymes suggest that a pair of tandem G:D wobble base pairs adjacent to the reactive center constitute the metal-binding site. Result is highly inconsistent with recent crystallographic studies showing that tandem wobble base pairs are moderate binding sites for metal hexaammines. Results may have significant implications for understanding the mechanism of protein synthesis.

(Note: Most studies of the roles of catalytic metal ions in ribozymes have focused on inner-sphere coordination of the divalent metal ions to the substrate or ribozyme. But it is important to consider the possibility of outer-sphere coordination of catalytic metal ions in ribozymes.) 

Results suggest that sample data was corrupted or equipment was improperly used. Request re-transmission of sample data or shipment of actual core sample for data collection on site. 

PubResMed:9445727 [NOT CLEARED for MEDRES Line]'''

desc22 = '''PARTIALLY BURNED MEMOS.


MEMO 1:

...measured an average infected population spread rate of two miles per week if undiagnosed. The alien virus is very virulent and contagious, its symptoms including high fever, headache, muscle aches, stomach pain, fatigue, diarrhea, ending with the patient experiencing chest pain, going into shock, and then dying within... 

...government of Congo-Brazzaville reports 64 dead in the districts of Kelle and Mbomo, with...

...unlike the first tests in Sudan and Zaire in 1976. Civilian health officials named this "new virus" after the Ebola River in Zaire.  There, the mortality rate of 54% was...


MEMO 2:

...blamed Jenkins for the mishap, which is a reasonable conclusion.

This new "dry version" of the alien virus, while not as virulent or contagious as the wet version, is very effective when inhaled. Placed within the Bacillus anthracis (Anthrax) host organism, infection can occur in three forms: cutaneous (skin), inhalation, and gastrointestinal...

..result, key targets were missed because of the choice of conveyance. Only Leahy and Daschle payloads had mild success, yet early discovery led to containment. My recommendation is to...'''

desc23 = '''From: Information Services - Russian Division
Sent: Tuesday, October 3, 2003 12:05 AM
To: MLA dd - USD(I); 
Subject: Recent translation of KGB UFO investigation 
Importance: High 

FOR OFFICIAL USE ONLY 

We have translated the bulk of the documents and files. All seem to be standard eyewitness accounts and indirect testimonials. We are including an excerpt from a document dated June 24, 1987. This documents the recovery of a partially destroyed craft found 200 feet below the area in Tunguska, Siberia where in 1908, 850 square miles of forest was flattened followed by a massive shock wave that caused seismic vibrations for as far away as 600 miles. Up until 1981, the accepted belief was that a large meteor was responsible. In 1981, a new expedition set out to explore the cause of severe seismic activity in the area. Apparently, the activity resulted in the collapse of a deep cavern. It is in this cavern that the ship was found. The assumption by the Russians was that the craft impacted the earth at such a velocity that it burrowed 200 feet into the mountainside.  However, this theory was soon over-turned as contradictory evidence was discovered once the craft was excavated and moved to a large and remote Siberian military base. Carbon dating of the rock imbedded in the craft's alloy skin shows the sample to be 10,000 to 11,000 years old while the surrounding rock samples at that depth are Carbon dated at 19,000 years old. The position of the craft was found to be nearly level with the surface which would be impossible to achieve during a chaotic impact at high speed. Furthermore, several pipe-like structures attached to the craft were embedded in the surrounding rock as if to anchor or provide minerals to the occupants of the craft. These discoveries pointed to an astonishing conclusion - that the craft did not crash into the mountainside. The craft was purposely inserted into the mountainside 10,000 to 11,000 years earlier. Further investigation revealed a cause of the destruction and resulting shockwave in 1908.  Damage found on the craft was limited to the top rear quarter and not on the bottom. The molten damage to the alloy skin and the rock bed above the craft resembled the effect of a directly applied, highly concentrated heat source - much like that of a powerful laser or particle beam weapon. It is possible that the craft was actually fired upon in its hiding position by another craft. This is alarming as it suggests that more than one EBE species has occupied earth. Unfortunately, pictures of the recovered craft were not included with the KGB files. We are not sure if this craft is associated with the EBEs that we deal with now.'''

desc24 = '''From: Ministry of Enlightenment and Truth
Sent: Thursday, March 2, 1994 11:35 PM
To: Il - MSF; LW - UHK; ALL 
Subject: URGENT: Congressional Investigation 
Importance: High 

FOR OFFICIAL USE ONLY

It has come to our attention that Congressman Steven H. Schiff (R-NM) has become more aggressive in his pursuit for answers regarding the day of initial contact in New Mexico, 1947. He has demanded that the US General Accounting Office, an investigative agency that works at the request of Congress, initiate an audit to locate and gather all records related to the Roswell incident and investigate the handling of this incident. Unfortunately, our plan to release fabricated information through our channels at the Department of Defense have failed to convince the congressman that nothing more lies beyond the current truth. While the General Accounting Office is not under our control, we do have the ability to prevent them from finding sensitive documents that may betray our activities. We need to deter their search. We will supply documents describing a top-secret surveillance project code named Mogul. This will be planted in the Edwards US Air Force base archives along with a crated sample of a radar reflector. The GAO's search should easily uncover this evidence. This should give the congressman the cover-up that he is so intent on finding.'''

desc25 = '''FINAL DIRECTOR REPORT

Captain Edward Ruppelt
Project Blue Book

August 1st, 1953

Re: My tenure


New Grudge (of course, now Project Blue Book, but I always liked the original name) has, as you know, been seriously studying unidentified phenomena since September 1951. While I have done my best to research all incidents and coordinate activities, I must admit disappointment for being left in the dark by General Garland on many an occasion, lately about the Robertson Panel report. Bob Olsson may be taking over my place, but I do feel I brought a level of professionalism, organization, and scientific seriousness that was unappreciated by my superiors. My recent studies at the advanced intelligence course in Denver only heighten my feelings of disillusionment.

While we know for sure the recent rash of sightings and second-level close encounters has raised public awareness of extra-terrestrial contact, only if we as Blue Book agents share information about sightings and contact, with full disclosure within the community, will we ever be able to effectively deal with the aliens, and prepare against whatever threat they might pose. After the huge wave of probes and scouts in 1952, I do not think they can be ignored. And I personally cannot stomach the lack of support the Panel and the Government has given this vital project. If we do not act now, we are doomed.


Sincerely,


Captain Edward Ruppelt'''

desc26 = '''From: Central Intelligence Agency
Sent: Tuesday, October 3, 2003 12:05 AM
To: MLA dd - USD(I); 
Subject: Relocation candidate: Green River Launch Complex, Utah 
Importance: High 

FOR OFFICIAL USE ONLY 


The decommissioned Green River Launch Complex originally housed our experiments with crustaceous animals and the genetic experiments to increase their aggression. This was our first instance of mutating earth life-forms with the alien virus. The missile silo provided a convenient environment in which to protect the research. Unfortunately, our first efforts at Terra-EBE genetics resulted in the base becoming contaminated with a new biological agent. Apparently, the cow's organs (liver, brain, pancreas, heart) that we harvested to culture the mutated virus began to emit a highly infectious, air-borne by-product. This by-product was later discovered to be a malformed protein molecule (infectious prion) and had properties similar to some highly evolved variation of bovine spongiform encephalopathies (BSE). Unfortunately, we found that this variation was not limited to brain tissue and attacks all organs regardless of species. Many of the researchers began to undergo severe hemorrhaging - bodies became twisted with bone crushing muscular contractions indicative of cyanide poisoning. We believe the complex is still contaminated and should not be considered as a candidate for the Groom Lake Military Facility relocation initiative. One can only hope that an outbreak such as this should never happen again.'''

desc27 = '''To all Biohazard Stage IV Lab Personnel
RE: Protocol Change in all Critical Infection Situations

"Commence shutdown of all emergency demute chambers. Demute fluid substantially less effective than the experimental solution being created in the main demute chamber at my lab. 

Gentlemen, we will need to scrap it and start over. Such is the price of science.

In the interim, if you even suspect you have been exposed, alert the closest Hazmat Safety Officer and be prepared to arrive at my lab within 20 minutes, or I will be unable to help you."

- Dr. Winston Cray'''

desc28 = '''From: Ministry of Enlightenment and Truth
Sent: Thursday, April 23, 1967 11:35 PM
To: Il - MSF; LW - UHK; ALL 
Subject: URGENT: The Impeding Diversionary Lunar Event 
Importance: High 

FOR OFFICIAL USE ONLY
Directive 294857

Assignment: Tethered Offspring

It is hereby decreed that the only offspring of Dr. Winston Cray be approved for termination. The termination shall commence on his son's birthday in this calendar year - which we have determined as next Sunday. The son's termination will be committed in the presence of Dr. Cray during their remote videophone call. It is imperative that Dr. Cray be made to feel overwhelming anguish and helplessness while witnessing the death of his son. This inescapable emotional torture will progress our plans with Dr. Cray and his involvement in the final initiative.'''

desc29 = '''GL_sneakernet//ch*log004451_julien030905
Connect Alice Larvin (client137);
Connect Marie Roberts (client301);
 
[ALarvin]: hey. get your report done?
 
[MRoberts]: No. The entire department is running behind.
 
[ALarvin]: too bad. you'll catch up. but what happened in D lab yesterday? i heard some funny stuff. 
 
[MRoberts]: Already? You must have it heard from Blaine. Our design engineers cannot keep anything quiet. 
 
[ALarvin]: haha...good guess. would like to see him without a labcoat on tho. know what i'm sayin'? <sigh> 
 
[MRoberts]: Yes, quite. Anyway, we had another near disaster. One of our test subjects woke up a tad too soon. Here she is, a Midwestern mother of three, out cold on the table, just a week after she was last seen "being forced into a white van" somewhere in Ohio.
 
[ALarvin]: ooh, yeah. terrible. i saw the news reports...candlelight vigil, hubby talking to the press, photos of the kids. sad. i mean, i know it was us, more or less, but still sort of sad from the outside perspective.
 
[MRoberts]: If she hadn't been taken by our people, she would have eventually gone one way or the other. 
 
[ALarvin]: true.
 
[MRoberts]: So she wakes up. Apparently, the anesthetics used by our "partners" don't always work with some sub-genotypes. She's looking around, sees that she's been opened up, some of her organs are set aside extra corpus on the operating tray...
 
[ALarvin]: eeewww.

[MRoberts]: Yes. Then she sees them, all huddled around. They keep the lights low when they're working. So they're all gathered close, about 8 of them, with their big dark eyes and zero-empathy expressions. She loses it, of course. 
 
[ALarvin]: poor woman. at least up here, we get to cut on *them* rather than the other way around. btw, avoid that blue-gray synovial fluid of theirs if you can...the smell will *never* come out of your clothes.
 
[MRoberts]: I'll keep that in mind. Anyway, the subject actually runs around the operating theatre for a while. The little buggers didn't do anything to stop her. They just watched, with this totally analytical interest, of course, as she was bouncing off the walls. Very messy...it's no picnic down here, either. Finally, one of the security guards brings her down. The look in his eyes afterward was not exactly harmonious; another case of post-trauma, for sure... 
 
[SESSION TERMINATED?ROUTER AUTHORITY//SUB-SECTOR 04]'''

desc30 = '''S-4 Laboratory, Biological Division MLW-89473
Laboratory Log - 05121998 CST 13:00
Supervising Research Officer: Fredrick Henry White


After the successful recapture of the escaped Phase II, we immediately went to work studying the miraculous evolution of this creature during its exposure to the world outside of the S-4 laboratory. Examination of both palms revealed a large orifice currently covered with a thin membrane. We assumed that this membrane would eventually rupture and merely served as a temporary protective cover early in the creature's growth. 

Slicing the membrane away on the left palm, we inserted an endoscope up through the canal inside the forearm and discovered a powerful organ with muscle cells much like a heart. Inside this muscular organ were several glands containing some very curious tentacled organisms. We assumed that if the creature were to mature, these glands would secrete the organisms into the muscular organ and be forcefully ejected out of the palm, through the canal in the forearm. What these organisms (parasites?) will do once ejected is not clear at this point.

Examination of the creature's back revealed patches of skin not covered by the same hair found all over the body. Blistering of this skin seems to have damaged the hair follicles in this area. 

Lead technician Donald Ancira punctured one of the larger blisters on the creature's back expelling an air-borne organism which quickly sought-out and penetrated his body. We believe that this "contagion" was the cause of Ancira's sudden and aggressive behavior towards all other technicians in the room. Further work on the creature has been delayed as we await the removal of the victims and their remains from the laboratory. We have posted several position openings for laboratory assistants to other branches of the organization and hope to conduct more research soon.'''

desc31 = '''Dissection of Specimen Subject - 7642-1298GP
S-4 Laboratory, Biological Division MLW-43892
 
Procedure Transcript: 09122003 CST 14:00
 
After completing the general dissection of the internal organs, we extracted the right mutated eye in an effort to understand its deviation from a human eye. The mutation eye is 30% larger and 40% heavier than a normal human eye. The extra weight seems to be attributed to a much denser number of light receiving cones and rods in the retina. This gives the eye a greater visible light range from ultra-violet to infrared, which may also explain the appearance of a secondary optic nerve. The sclerotic coat is yellowish with pigments that are phosphorescent in nature. This results in a slight glow to the eyes and could also be a component of the extended visual range. The cornea shape is slightly oblong which suggests that the mutation suffers from a form of astigmatism especially in the peripheral vision areas.

- Dr. Chalmers'''

desc32 = '''Mr. Rosen, 

I regret the impersonal nature of this request, sir, but due to the workload of our field agents, I must request additional details regarding the black-level operation. Please complete and return the following. Again, I apologize for the formal nature of this request, but we are dealing with a considerable backlog among our North American operatives. 

Sincerely, 

M. Reed

Target of Operations: [Last, First, Middle]
Target SSN: [xxx-xx-xxxx] 

Desired Objective: [Termination, Coercion, Abduction, Surveillance]

(If you checked Coercion, please provide additional detail.)

Approved/Desired Methodology: [Sleep Deprivation, Torture, Blackmail, Extortion, Psych/Terror]

Will you sanction involvement of target's friends and/or family? [Yes, No]

Additional Friend/Family Detail: [Abduction, Death, Removal of Limb(s), Scarring, Blindness]

Do you require a follow-up report? [Yes, No]'''

desc33 = '''////////++++Teletype Override - Priority 01 Traffic Incoming 
 
Code Sequence: A51 Event-Loki. [STOP]
 
Listening...
Listening...
Listening...
Authenticating...
 
Hand-shake authenticated. Transmitting full message text. [STOP]
 
Suspect potential site compromise. [STOP]
 
Evaluate situation. If critical, initiate contingency agenda Desert Bloom. [STOP]
 
REPEAT: If critical, initiate contingency agenda Desert Bloom: full sanitization of site. Sterilize all biological samples. Degrade all records. Terminate all staff. Any and all means authorized. [STOP]
 
By highest shard authority, situation must be contained. [STOP]

Retransmit to all BLACK04 level command personnel. [STOP]
 
////////++++End Traffic'''

desc34 = '''CONFIDENTIAL MEMORANDUM

READ AND DELETE

From: Illuminatus VII
To: Mr. White


Mr. White,

We have been made aware that an outside agent is working his way down and disrupting the infection plan. This cannot be tolerated, and you must make all efforts to eliminate this subject.

Please send a full squad of Dark Ops to handle it (your usual extermination squad of one Red Op leader and three Black Ops will not suffice this time). Make sure to have your techs test all the Red Ops suits - some of our new lab-cooked experiments seem to be able to see some of them even when they are cloaked. This obviously reduces their effectiveness at stealth. We gave them the greater intelligence and better tools to serve as very effective field leaders, and I will not have our plans ruined because of some lazy lab coats. Get on it.

This is a most critical juncture in our most important endeavor, Mr. White. Do not fail us.


Signed, 

/o\ VII'''

desc35 = '''Reference: Great Seal (Summary of Archive Contents)

Curator's Personal Note:
This set includes a series of what are obviously ridiculous assertions regarding the Great Seal of the United States (or the "pyramid and eye" found on US currency, a design established by Congress on June 20, 1782). This file concerns, specifically, the alleged relation between the Great Seal and various underground organizations rumored to be operating on a global scale. 
 
Ask the supporters of this lunacy why such secretive organizations would "hide" their symbol on currency seen by virtually all of the free world, and they will reply with some nonsense such as, "The greatest trick the devil ever played was convincing the world he did not exist." 

Given the ludicrous nature of some of the assertions within, I find it somewhat hard to justify sealing these documents away within one of the most secure archives on the planet. 
 
Elliot Mingus, Professor of History and Modern Anthropology
Site Archive Curator'''

desc36 = '''>> Sir, we fear the system might suffer damage if we continue to operate the tubes at the current rate. I cannot guarantee the integrity of the operation under the current parameters: If we continue like this, sir, we could suffer catastrophic losses in terms of resources and personnel.

Kintell:

Given that I communicated my wishes with crystal clarity, I find myself questioning your loyalty and your competence. I do not enjoy repeating myself. 

My directive is simple: Run the extraction tubes in excess of 100% capacity. Stay on schedule. At all costs, ensure the transfer of all necessary resources in accordance with the timeline I have provided. 

Any luxury we might have enjoyed - any regard for conservative operations - has evaporated in light of this security breach.

Upon completion of the extraction operation, I want you to eradicate everything left in our wake, including all remaining personnel. 

Mr. White'''

desc37 = '''INSTRUCTIONS FOR RSA-41 Biohazard Handling, Containment and Delivery

Proper Use of the Robotic Servo-Arm:

1. HANDLING
The large scale bio-canister arm is built to withstand 50,000 pounds of force per square inch and can take temperature extremes from 4 Kelvin to as high as 5000 degrees Celsius. It can operate on the highest mountain, deepest ocean, coldest arctic, or the vacuum of space. It is ready for any extreme. However, there are still safeguards one must employ.

- Do not enter the swing radius of the arm. If the arm detects any resistance, it is programmed to assess it, then either move through it or remove the obstruction with its SawClaw 4000 Defend-O-Limbs. These have been repurposed from the Defense Department Crowd Laceration Unit, and are perhaps a little too effective at removing impediments.
- Do not touch the MagnaRails. Any slight variance in impedance will cause a static burst at the contact point of approximately 36,500 volts, and around 4,200 amps.

2. CONTAINMENT
The RSA-41 is at the leading edge of bio-hazard containment. Its canisters are made with six-inch-thick transparent ThermaSteel with a 49,000-Joule Magnetic Resonance containment field. Nothing, but nothing, can escape these containers. However, since the materials are SO hazardous, they must be neutralized should they escape.

Should a negative containment event occur, you will have about .0004 seconds to run before the battleship-welding Suncore InstaLaser will instantly detect, target, and vaporize any biological matter in the area. Any remaining bits not in the direct sight line of the InstaLaser will find themselves in a sudden vacuum as the side panel of the RSA-41 opens to reveal one of our friends' PocketStar micro-singularities. The panel is closed again and a burst of argon, aerated carbolic acid, and nerve gas will fill the immediate 10,000 cubic feet of workspace, to insure no hazardous material escapes. Then the entire unit will let go of its releases and plummet through the HoleTech Safe-T-Pit directly into the Earth's core.

3. DELIVERY
The RSA-41 will deliver its containers floating on a delicate magnetic field. Should an EMP event occur (endangering the safe transport of the hazardous material and likely implying enemy attack and destruction of our way of life), a dead man's switch will trigger the Satan's Column FinalStrike Fusion Event, creating a small sun consuming approximately one quarter of the Earth's mass. However, this disruption is highly unlikely, so use your RSA-41 with confident caution.'''

desc38 = '''S-4 Laboratory, Biological Division MLW-89473
Laboratory Log - 05121970 CST 13:00
Supervising Research Officer: Fredrick Henry White 

While Phase I of our genetic engineering research met with some early success, Phase II proved to be near disastrous as one of the subjects managed to escape containment. At the time, the subject was never found and we were convinced that the situation would resolve itself considering the fact that the subject was mortally vulnerable to common bacteria. 

Last month, we received a peculiar video from a recent Black Helicopter raid in the Northwest.  This video captured the movement of a creature very similar to our early Thetas; however, this creature was nearly 3 times the size of our early experiments. We sent the helicopters out again for retrieval of the subject - several weeks later and with the help of the EBE's scanning technology, we were able to locate and retrieve the creature.

The creature that was brought in was covered with hair except for patches on the back where the skin had blistered. Upon examination, we discovered the S-4 laboratory ear tag marking the origin of the creature as our escaped Phase II subject. We were amazed at the growth in size and strength of the creature. Further examination revealed the nature of the unusual blistering of the skin on its back - the pus within these blisters was a form similar in biological structure to the mutagen that we have also been developing. 

What we once saw as a failure has become our biggest success and will propel our program forward substantially.  Ironically, this particular failure may hold the answers to our current blockage with the Theta project. 

While we were quick to apprehend the creature, the creature has, unfortunately, been caught in the public eye. We've added this case to H.C. who is also working on the crop circle subterfuge for the human abduction raids. We hope to have a cover story soon - he's been in a humorous mood lately and wanted to try a fantasy angle on this one - something based on a college football team mascot.'''

desc39 = '''Report to the Alien Reverse Engineering Sub-Committee: Graviton-Plasma Implosion Technology
Dated: November 11, 2000
Clearance: MJ-12 Q (or above)

After examining the wreckage of the EBE Scout Ship on July 8, 1947, several intact warheads were retrieved and held for examination by Dr. Winston Cray. The initial examination released several radioactive isotopes, killing several scientists and technicians. Further investigations were held off indefinitely until the half-life of the isotopes was eclipsed, rendering the examination of the remaining warhead safe. After an accidental implosion was triggered on October 3, 1997 during a routine examination, the surviving technician noted the high-speed molecular electrical triggers could be accidentally tripped by severe motion. Replacing the molecular triggers with high speed krytron switches (as you know, krytrons are simple thyratron tubes filled with Krypton-85 gas) allowed the scientists to reliably (and safely) trigger a high-yield graviton-plasma implosion. Work continues on the miniaturization of such technology for battlefield portable weapons. Perhaps a small enough device could replace a typical fragmentation grenade with something a little more powerful.

Dr. Austin James Stiefelmaier, MJ-12 Tier II'''

desc40 = '''SUBJECT: Lt. Charles Jacobi
Mutancy Level: 100%
Mutagen Level: 40%
Spore-Casting Sacs: full-growth
Cerebral Nanotraining: 80% failure
Frontal Lobe: 20% activity
Corpus Callosum: 120% normal alert activity
Occipital: 50% activity
Cortical Storm events present'''

desc41 = '''Cray Log: 09231982

Our experiments with earthbound pathogens HIV and Ebola have been instrumental in allowing us to understand the behaviors of our genetically designed pathogen. What is unique about our manufactured "Mutation" pathogen is that it is not an actual living organism. It is, in fact, a protein molecule that is highly resilient to any environment no matter how hostile it may be. This pathogen is the perfect vehicle from which to deliver the mutated DNA to host cells causing them to manufacture more mutated cells - invading the body completely and unchallenged. The main raw material used for this pathogen comes from, of all things, cattle. Some cattle brains host a disease, bovine spongiform encephalopathies (BSE) - known to the public as "mad cow" disease. BSE, like all transmissible diseases, uses a malformed protein molecule (infectious prion) as the transport mechanism to deliver a lethal payload to the target organ. After the disaster at the Green River Launch Complex, we analyzed the bodies of the victims and used this information to modify the infectious prion. This resulted in the prion's ability to attach and infect all organs - transforming the host body all at once. As we were to discover, bovine blood was also instrumental in providing nutrients to these prions. Further research allowed us to create an injection which should amplify or quicken the mutation effect. This may have further consequences in evolving the mutation and its side-effect abilities well beyond that which we can comprehend.'''

desc42 = '''Cray Log: 1231997

Success seems to be the order of the day! Our latest step forward in cloning perfection is embodied in Victor6. He possesses, not only the likeness of my former assistant, the Late Victor Weisbrod, but his intellect as well. I feel a strange sense of familiarity with this clone and relish the idea that my dear friend, Victor, may just have been fully resurrected in this latest attempt. Initial intelligence tests show a remarkable IQ rating that is on par with Victor's. I can't help but think that a bond is forming between the two of us as we are both sensing a familiarity in our relationship and demeanor. The success of this clone has completely eliminated my disappointment with our last clone, Victor5. Victor5 suffers from an underdeveloped brain function brought on by an error in the oxygenation of the synthetic embryonic solution. The starvation of precious oxygen to his brain caused noticeable damage in the form of autism as well as giving his personality an annoying sense of need and belonging. His duties are relegated to menial tasks and chores. I do, however, enjoy his company if only to remind me of how child-like Weisbrod really was in times of extreme inebriation.'''

desc43 = '''Cray Log: 09231986

My personal investigation into the covert activities of Fredrick White leaves me to believe that a serious conflict between the two of us is inevitable. I sent Victor6 on a mission to retrieve any information that he could in order to substantiate my suspicions of a covert cloning program run by Fredrick. He managed to secure several electronic documents (laboratory entries), which proved to be quite interesting. It appears Fredrick's mental instability has manifested itself as extreme egomania and narcissism. He has actually created a series of clones in the image of himself.

After the death of his wife in the weapons testing range, Fredrick became disillusioned and distraught with anger. The sacrifice of his wife's life for the government was too much for him to bear, leading to a mental breakdown. What arose from the ashes of his anger and depression was a new desire. It was at this vulnerable point in Fredrick's life that the Illuminati contacted him and offered him solace as well as an opportunity for revenge.  

The Illuminati has access to a wealth of resources, technology, and knowledge. On a recent reconnaissance task, Victor6 observed these clones and found that they are equipped not only with teleportation technology, but also with broad-spectrum vision monocles. I am curious as to what this allows the clones to see that may be unseen.

I fear that my former friend and colleague has and will become my ultimate obstacle.'''

desc44 = '''INTERNAL MEMORANDUM
From: Dr. Winston Cray
To: Authorized Personnel with YW (Yankee White) clearance.

The GDC decontamination chamber is multi-purpose. Of course, it uses the standard anti-bacterial and human-safe anti-biotic sprays. The GDC also has a number of covert functions:

- It samples and stores the subject's DNA for the GST global DNA database, which contains 100% of government employees and approximately 72% of the Earth's individuals at this point.
- If it senses any short-term threatening illnesses, it neutralizes them with triangulated microwave beams.
- If it senses no long-term illnesses, it causes a malignant mutation that will likely kill the subject at around 80 years of age, unless they have YW clearance or higher. (Over time, this has proven to keep the populace under manageable size and control.)
- Any inappropriate contents on the subject's person, or sensitive data on any standard-format recording media is reported to local government authorities. In the case of data, it is instantly replaced with low-level encrypted data containing terrorist threats and drug transaction / falsified tax information.'''

desc45 = '''Report to the Joint Chiefs and Developmental Test Command

Dated: May 27, 2002

Clearance: ARIA - EYES ONLY - NOFRON

The XM-197 "Jumpin' Bean" high yield plasma grenade has completed its first successful testing at the Papoose Lake firing range. The miniaturization of the krytron switches still presents a safety issue, as the problem of inconsistent switch firing has not been completely eradicated from the weapon design. If the operator is not careful to loft the grenade within the established maximum velocity specifications, the switches fire erratically, causing the deployment package to fail and the grenade to become a dangerous jumping bean. If the operator can deploy the weapon within the velocity specifications, the deployment package will rapidly accelerate the high-yield plasma warhead to the intended target. The plasma implosion has achieved a 45cm penetration of cold-rolled homogenous steel. Further testing is recommended before mass production.'''

desc46 = '''From: Gen. Andrew Myerson 
To: Lt. Gen. Robert B. Kieran III 
Importance: High 

Dear Lt. Gen. Kieran:

Bob, I understood the report the first time you threw it at my desk. How in the hell do you expect me to "massage" data like this? You do understand who my boss is, right? Maybe we need to pull you out of the desert sun, buddy. Eight months ago, I had no idea the little gray bastards could communicate at all. Now you're trying to get me to accept that they had involvement in Dealey Plaza? That they all got together and closed their big, creepy eyes and they just dreamed until the shooters all made a pilgrimage to Dallas? Do you realize how this will go over? It was bad enough to think about Castro being involved...at least he's one of us! I suggest you ask our little friends for a better story, or you come up here to the Hill to present your little report yourself. 


Cordially, 


Gen. Andrew Myerson 
Exec. Director, Historic Relations Board
1155 Defense, Pentagon
Butler Building, Sub-floor 8
Washington, DC 20330-1140'''

desc47 = '''Yersenia Pestis detected. Base computers reveal this strain of the pneumonic plaque seems to have significantly increased mass, weighing 2.1g per 5 moles, as opposed to .047g. This "hardy" version of YP has been introduced into various Animalia Chordata mammalian classes with mild success. But in various microscopic organisms, the virus is said to "bully" the host into wild mutation and rapid growth surges. 

After injection into Micrasterias truncata desmids, the creatures grew enormously and when attacked, would simply divide into smaller versions of themselves. The initial lab was soon overrun by the creatures, and not all specimens have been contained as of yet.'''

desc48 = '''GROOM LAKE FILE MGNA/14

Darrin,

The Graviton control research for the X-43A Scramjet has split into two fields of study: Graviton Repulsion and Mass Negation. While repulsion is clearly used in vehicles and transport, the bang-for-the-buck usefulness of mass negation is still being investigated. Apart from the gee-whiz effect of making metallic-element items float (metal being the only type of matter that seems to allow mass negation, though more advanced alien technology must exist since they travel the stars), the practical usefulness of the largeness of the device for the size of effect is in question. MGNA trains could be manufactured, but at no increase in speed from MagLev trains and at approximately 3,000 times the cost. So in a nutshell, we can get massive funding for how cool this looks, but so far, practical applications have yet to surface.

Any Thoughts?

- Cary'''

desc49 = '''GROOM LAKE FILE

Bow Wing Laser Spectrographic Sampler

Power source: AEE, Alien Energy Element (Element 311)

Purpose: Not technically a laser, the LSS uses a two-dimensional energy plane to split atoms into leptons and quarks, corralling Muon and Tau leptons into a tight Bucelli loop, ideally containing the leptons indefinitely, and creating a lepton mass (possibly useful for quantum computation or matter disruption). However, the tolerances of the device are so high that the accident (and mortality) rate per experiment is nearly 100 percent. An outcome nearly leading Bow Wing Inc. to cancel funding until it was re-budgeted as solely Weapons Research, where such outcomes are acceptable.

Best Regards,
Dr. Shinazy'''

desc50 = '''From: Capt. J. Howa 
To: Lt. Gen. R. B. Kieran III 
Importance: High 

Dear Lt. Gen. Kieran: 

Remember M. Reed? That slack-jawed hick back in '47 who was threatening to spill, even did a radio interview? Well, looks like a total disregard for national security is genetic. His son Alex apparently has all the old papers and some debris the old man hung onto after his "debriefing." After all the trouble we went through to leave him undamaged, too. That was a hell of a long week. We need to run the kid through the debrief before he does any more damage. Thank God we have quicker technology this time. Let's hope it's more dependable as well.

Sincerely, 

Capt. J. Howa 
Internal Affairs Officer
1155 Defense, Pentagon
Butler Building, Sub-floor 6
Washington, DC 20330-1140'''

desc51 = '''Ben,

Here is data I copied from the downlink:

Singularity location: latitude W 33 degrees, longitude 70 degrees, exactly, as if placed with knowledge of our Greenwich-oriented Latitude Scale. More interesting is that if placed on the original Reinel scale from 1506, it also lines up perfectly on latitude 70 degrees W and longitude 70 degrees. It seems to have a very localized effect for its mass and only to absorb matter at certain times, as if triggered. The singularity also seems to rise and fall according to the cycle of the moon. Could this have resulted in the loss of the naval aircraft?

I hope this helps,
Dr. Davis'''

desc52 = '''Dearest Amado,

Regarding your inquiry, it is our code running within the bowels of their machines. Our agents, through a technical subsidiary, are the architects of the most underlying elements of the SETI system. 

Specifically, in response to your concern about the program, I can say this: Any signals received that evidence a pattern or any discernible form of intelligence are immediately filtered before the aggregate data is reviewed by SETI personnel. Further, the time-block surrounding the signal is entirely replaced with a randomized sequence of spurious readings. I can have one of our engineers draft an executive summary for you if you would like further details on the systems exoteric, but I assure you that the technology concepts our agents have gleaned from contact with our allies are quite revolutionary.

I trust that you and your sister will join us for the Gathering next Fall. I would consider it an honor if you both chose to accept my invitation to stay here, at my northern estate. I assure you that you will find the accommodations comfortable and the company pleasurable.

Sincerely, Roland

Novus Ordo Seclorum'''

desc53 = '''CLASSIFIED: GROOM LAKE YW CLEARANCE ONLY
PROTOTYPE SPECIFICATION

X-43A SCRAMJET AIRCRAFT

The X-43A is the flagship prototype of the Hyper-X program, attempting to merge the new Gray technology with our own.

The graviton repulsion retrieved, studied, and replicated from the Roswell craft is approximately 99.8% efficient, as opposed to the relatively poor 55% of our technology. Adapting the technology has proved difficult due to the heavy radiation emitted from the core. Shielding has had limited effect, so energy-based solutions are in the works. Regardless, the Scramjet must rise to at least a hundred feet on its own conventional propulsion, lest it kill the ground troops near the take-off point.

Key to targeting is the time-predictive reticule, which accurately tracks the delta-stream of the target and can shoot it with perfect accuracy. Modifications are underway for the missile to travel in this and all universes to prevent "reality-skipping" and avoid injury. If you were ever in our actual airspace, you would be terminated. Scientists have not determined how to counteract the enemy going two-dimensional and creating a depth-shunt, or four-dimensional and doing a time shunt. Research continues upon the larger Mothership, which has a super-cyclic field which seems to generate five times the power per Joule input. Theories are that it is actually destroying matter in the fifth dimensional tier for fuel. The Grays will not share if there are sentient beings there which might be affected.'''

desc54 = '''As tasked, I have listed the summary headings for the requested Shard Seven projects, driven by our North American enclaves. 

A noteworthy point is this: Often, our challenge is not in redirecting these unearthly technological marvels for our organization's noble and historic aims. It is frequently a simple matter to adapt the resulting technologies to projects that serve us as powerful revenue generators or in matters related to cultural management. The challenge is in creating plausible projects, or those which seem to rise from existent and evolutionary scientific studies. This is where cleverness is required.

A servant to our Cause, 

Rosa Baron Flores
Early September
Cambridge, MA

Project: Narrow Opiate; Field: Entertainment/Telecom (1982); Annual Revenue: US$2.84b; Note: Profits derived primarily from component patents. "New" developments released according to schedule. ("Flat screen" and High Definition releases provide most recent spikes in revenue stream. "Paper thin" and holographic versions planned for future releases, circa +1 decade.)

Project: Radar Oven (2450 MHz); Field: Home Appliance (1947); Annual Revenue: US$3.17b.

Project: Sky Saucer; Field: Athletic/Novelty (1948); Annual Revenue: US$281m; Note: Revenue summary includes sporting and canine disc varieties.

Project: Sticky Cloth; Field: Garment/Fastener (1957, Swiss patent re-direction); Annual Revenue: US$635m.

Project: Non Stick Resin; Field: Frictionless Research (1948, False record: 1938); Annual Revenue: US$882m.'''

desc55 = '''The global Echelon network consists of more than half of the world's supercomputers completely dedicated to automatically searching through billions of intercepted messages for pre-programmed keywords, phrases, telephone numbers, e-mail addresses and specified voiceprints. Every message in the frequencies monitored at an Echelon station is automatically decrypted, searched and indexed. 

Echelon "Dictionaries" contain the words or phrases the system searches for and are updated hourly. Echelon processes millions of messages every hour, the system runs 24 hours a day, 7 days a week. Each message flagged by the ECHELON dictionaries is sorted by a four-digit code representing the source or subject of the message (such as 6969 for Russian Mob traffic, or 1187 for traffics about Colombian Drug Cartels.)

Information mined from the intercepts are given various classifications: MORAY (secret), SPOKE (non-classified commercial information), UMBRA (NOFRON top secret) and DRUID (top secret but ok'd for FRON distribution)

The Echelon project has been linked to projects GT-6, RUNWAY, VORTEX and SILKWORTH.

Echelon stations are located in the United States, England, Japan, Australia, New Zealand and Canada. 

One Echelon station in the United States (Echelon IV), is located in Austin, TX and is specially tasked with monitoring all US-based online chat traffic. This monitoring of US citizens is codenamed "Inevitable" and "Research Blvd.".'''

desc56 = '''From: Ministry of Enlightenment and Truth
Sent: Thursday, April 23, 1967 11:35 PM
To: Il - MSF; LW - UHK; ALL 
Subject: URGENT: The Impeding Diversionary Lunar Event 
Importance: High 

FOR OFFICIAL USE ONLY

We had warned General Walter B. Smith, presiding chairman of the MJ-12 group, of our displeasure in the USA's pursuit of a nation-wide, televised lunar landing. EBE's have a forward reconnaissance base on the moon and their detection by the American public is far from desirable. The former and late President Kennedy was not swayed by our threats as a result of his aggressive move towards landing a man on the moon. He did not take our threats as seriously as he should have. What befell in Dallas was his undoing. Naturally the governing members of MJ-12 volunteered their complete aid. Neither of the members desired the fate of former presiding chairman, James V. Forrestal. 

President Lyndon Johnson was given a private communication reminding him of the dire consequences of his predecessor should he decide to continue the pursuit for the moon. He has come to agree to our plan to provide the world with our vision of what the moon landing will be. 

We will soon go into rehearsals with Canadian actors and we have constructed the special effects rigs necessary to create the illusion of space flight and zero gravity. We have procured the talents of a young director R. Corman, and should have the final lunar surface construction finished soon.'''

desc57 = '''From: Ministry of Enlightenment and Truth
Sent: Wednesday, March 23, 1987 10:35 AM
To: Il - MSF; LW - UHK; ALL 
Subject: URGENT: HAARP Advances 
Importance: High 

FOR OFFICIAL USE ONLY

The HAARP project is progressing well. We decided to approach the American public with an apparent openness and full disclosure in an effort to hide our activities in plain sight. (We even promoted the acronym HAARP to stand for High Frequency Active Auroral Research Program ....oh how gullible the public is - why, there aren't even enough letters in the acronym to support the words we gave them! - silly people). 

The actual project purpose and name, Hardware Augmentation of Animals to Receive Programming is our long standing technology initiative to command the resources of the world's animal population to perform tasks under our will.

Some animals have been recruited to perform reconnaissance, such as dolphins. Others have been used to shuttle raw materials from our under sea bases to our hidden ports off the coast of Greenland. We have used flocks of birds as a way to disguise the radar signature of our crafts as they travel from various areas to gather more raw materials. Our latest creation equips Earth's greatest oceanic predator with our most effective weaponry. The results...a powerful combination...an awesome vision come to life - sharks with laser beams. We are quite sure that we will find ample use for such beasts in our plans for world domination. We've decided to maintain several of them in our under sea base tank for any of our unfortunate visiting guests.'''

desc58 = '''Bertrand,
 
As a courtesy to you and your well-regarded council, I have forwarded along a brief history of my father's most important, if darkest, work, regarding the use of what he referred to as the modern serial killer mythos, primarily on the North American Continent. 
 
As you know, his principal goal was not the concealment of a scattering of 20th Century events, but rather the creation of a powerful tool that would continue to serve us indefinitely. 
 
This was his brilliant vision, the entry into the collective narrative of a horrifying figure, a modern bogeyman, who is first created by society, then moves invisibly through the urban infrastructure, taking the lives of the innocent. My father focused on socio-economics and various psychotherapeutic fields in order to create false social predictors related to the emergence of this figure, the incarnate representation of one of our greatest fears, an enemy with a complete lack of empathy. His work cleverly ties together ancient cautionary tales as a means of encouraging orderly cultural behaviors, along with inherently modern constructs such as the US Highway System (circa 1925). 
 
Initially, of course, our use of this mythos figure was exclusive to removing "crash site witnesses" and people who persisted in investigating related events. Later, we began to employ it in the pursuit and capture of qualified test subjects, to be handed over to our allies. On several occasions, it has also been useful in silencing project defectors. 
 
Of course, none of my father's success would have been feasible without the work of one man, Johan Maergaard. His lifetime of dedication to the study of the subject of social engineering can be found in our restricted library, and only in our library. (See: Maergaard, Deliberate Societal Meme Transmission: A Geo-anthropological Study of Information Migration Patterns.)
 
Desmond Atrius
Beno 9, 00198 ROM, Italy'''

desc59 = '''Roland,

My sister and I continue our good work here in Brazil. She has begun to lay the initial groundwork for the launch simulation-rendering. I am as always manipulating the political machine, providing additional funding for the International Mars Landing Coalition, as we have decided to call the program. 

Most of our IMLC preoperational work was derived from the Lunar Landing precedent, of course. However, the world cultures, especially in the United States, are very different in our times. As such, one of our key agents has begun to seed major university campuses, attempting to employ a viral "exploration" meme in order to re-create the fervor of the times prior to the 1969 charade. 

Given the post-Viet Nam, post-Iraq cynicism in your country, it will be inherently harder to generate the same level of cultural response. To counter this, our current landing script has a much higher cinematic feel, including a major technical failure (and resulting near-disaster) during the hours prior to the touching down sequence. Our operational notes are enclosed.

On other matters, of course we will join you as your guests. We look forward to the Gathering, and we look forward to discussing the next phase.

Amado Montenegro
Sao Paulo

Energia e luz eternas.'''

desc60 = '''GROOM LAKE FILE

Gray skeletal system

Bones: 222

The Grays have one extra small rotator bone joint in each regular finger and toe, totaling sixteen bones. However, the rest of their skeleton is remarkably similar to that of a human, indicating either some common ancestor or other evolutionary force. The original 1947 dissection revealed many bizarre organs, either indicating a long divergence in evolution, or a long-distant repurposing of now-vestigial organs. Most notably, the Grays seem to feed off some inter-dimensional power source and have no discernable genitals or gender differences.'''

desc61 = '''GROOM LAKE FILE

BBG-11 Meson Autorifle

Power Source: AEE

Description. The BBG is the highest-powered weapon in The DarkOp arsenal (reserved for RedOps and the occasional key BlackOp who has undergone special training). The BBG fires a stream of violet energy projectiles with such cohesion that they can bounce off surfaces. Any modification of this weapon was difficult, but we have managed to discover a triggerable targeting feature which costs energy, but indicates where the spheres will ricochet. Also, this targeting beam seems to send information back to the weapon, as targeting organic lifeforms turns the green beam to red. Originally called the Ballistic Barrage Gun by scientists, it has since been renamed more appropriately the Meson Autorifle.

Fire rate: 3.3 spheres/sec 
Energy study: the full range of properties of AEE energy are unknown. Element 311 is the first element on the 20th row on the (now-expanded) Periodic Table (assuming the higher elements observe heavy-metal properties). There are no elements known to humankind between element 118 (ununoctium) and 311, perhaps quietly indicating the gap in our levels of technology. (Even ununoctium itself has never been synthesized more than once, as dictated by scientific method.) Given the relative instability of known elements, perhaps the gap is merely an indication of one of the first stable superelements.'''

desc62 = '''GROOM LAKE FILE. AT-71

Alien Technology
Special Subject - Metallurgy

All alien technology we have seen so far seems to be a form of titanium woven with some other element. The Gas Chromatograph Mass Spectrometer seems to give false readings when trying to graph this element. When heated, the metal looks iridescent. When cooled on one side, heated on the other, it seems to act like a perfect insulator.

All attempts to break the current form of the alien metal have proven useless. Only at special seaming locations can it be rent apart. However it always rends in regular form, never in random fashion. 

Obviously the metal is difficult to make, as not everything is made of it, for instance, armor.

One clue to the metal's origin - a fine lattice in the Theta creature's claws seems to be made of said metal.'''

desc63 = '''GROOM LAKE FILE

Red Operational Officer Field Cloaking Unit

Power Source: AEE

Description: The FCU is an extremely useful device, since it actually bends light with a sub-technology of the Gravity Repulsion Unit, called the Light Tunnel Shell. It forms a light-bending sheath of photo "traps" around the soldier sending the photon around the tunnel shell to the trap exactly opposite the receiver trap, then emitting the photon as if the light had passed directly through. The difference between the speed of light, tunnel shell diversion, trap choice, and movement compensation can cause a slight shimmering effect. However, this technology only cloaks the visible spectrum of light and this is mainly effective against humans.'''

desc64 = '''Illuminated Initiates,

Discussed herein is a program with which you are all familiar: Project Soma Horizon. Detailed notes are contained in this transmission for all stages summarized below. All stages are based on our work with amino-acid precursors of the neurotransmitter serotonin.

Stage One involved the push to prescribe anti-hyperactivity medications at the elementary school level. Promising pharmaceuticals were administered to the test-case population demographic (grades K through 5, mostly upper socio-economic status). Results were promising, but a few mishaps occurred. (Information was suppressed in any cases involving drug-related fatalities.)

Stage Two was related to psychotropic drugging of delinquent adolescents. Briefly, we saw the emergence of a muscle-paralyzing disease that was caused by an impurity in one manufacturer's process. Damage inflicted in many cases was permanent, requiring sanitization of specific households and families. Eventually, the process was corrected and this stage was deemed a success.

Stage Three, in accordance with our protocol, cannot be committed to print in traditional or electronic form.

Stage Four was also successful in middle aged adults, though reproductive dysfunction caused a temporary setback on the PR front. Discrediting the US FDA drug testing process, redirecting the blame away from our subsidiaries, put us back on track. 

Stage Five, as you all know, will involve the mainstreaming of these drugs, resulting in a much more compliant global population. Various introduction scenarios have been brought to the table, but the one currently favored involves a staged global terrorist attack involving bio weapons. Our drug will be positioned and branded as two competing anti-toxins requiring weekly ingestion.

As an ancillary benefit of this program, high profitability was seen through various pharmaceutical subsidiaries, primarily from worldwide sales of "SSRI" (Selective Serotonin Reuptake Inhibitor) antidepressants.

I expect you all to familiarize yourself with the latest report. I want an analysis and strategic commentary from each of you by the middle of the next quarter.'''

desc65 = '''Honored Sir,

We traced the communiqu?? back to Oslo, where the subject was staying in a locally owned hostel. The subject was an American freelance operative specializing in linguistics. We were unable to determine the party who originally contracted the services of the subject. However, when we entered the subject's room, he was in the process of composing a summary report, and our agents were able to successfully contain the transmission and terminate the subject. The last entry of his documentation is cited below. (A full report will be delivered by hand in London.) 

-----------

Research Notes: Pictographic Ties

Thursday - Project Near Completion

In trying to make sense of these findings, I'm dealing with an ideographic script, where each grapheme has an abstract (and not necessarily a clear pictorial) link with the meaning of the word represented. 

This is truly amazing: From what I've seen so far, the alien pictographic language shares a number of similarities with the logogrammatic symbols used in Illuminati writings throughout history. Note that these symbols seem to mean the same thing in both languages, in the same way Chinese characters mean the same thing whether they are read in a variety of Chinese "dialects" (or even in Japanese, a language which is as unlike Chinese in its internal structure as it is possible).

Some of the pictographic metaphor common to both Illuminati inner network codes and extraterrestrial cipher records can also be seen in the great Chinese dictionary of K'ang Hsi Kangxi (1662-l 722), in the 4,000 year old Paleo-Hebrew inscription found in the archaic alphabet of Israel, and in ancient petroglyphs, found on rock walls. This has stunning implications that could set in motion a radical, worldwide shift in our understanding of practically everything we believe.

When I get back to Boston, I will...'''

desc66 = '''UNITED STATES GOVERNMENT
Official Material Manifest

FROM: Groom Lake Military Facility
TO: Cheyenne Mountain YW Vault

NOTES:

Edward -
Here are the items for storage. Take good care of them.

- Winston 

CONTENTS:
7 AEE 311 Energy canisters
4 Titanium lattice material samples
1 Planet-tunneling Vectorsphere (do not switch on)
2 collapsed Sundrainer panels from Alurian System Assault Ship
15 Nanotech communication dots, contained in facial mole disguise (approved for social use after test with CC model succeeded in public approbation)
3 Alien Manuals (Grays inform us closest translation of title is something like "Serving Humans" -- something like that)

Last Minute Addition:
Oh, and a half-dozen of those red fake wax lips the Grays like to play with.'''

desc67 = '''Dr. Elwes:

Yes, yes...Sodium Fluoride is a "highly toxic, ionic molecule." Don't quote technical reference to me, my boy.

The introduction into the water supply killed two birds with one very tiny stone, if you'll forgive an old woman her black sense of humor. 

The substance was building up as an industrial byproduct of our activities. The human body does a nice job of processing it, making the general populace a massive, parallel waste conversion system. Quite clever. 

Additionally, the controlling leadership at the time was seeking a means of adjusting population growth to counter greater median longevity. To this end, early tests showed dramatically increased cancer rates within fluoridated communities. (All forms, 5%, with rates of osteosarcoma almost double.) As a tool, this program has specifically allowed us to focus on the reduction of the average lifespan within the least desirable demographics.

As a side effect, it does in fact reduce tooth decay.

Do your homework! Understand that we rarely enact single-purpose programs; too inefficient and too obvious. 


Emma Morgan
Chairman, Rothburg Research Partners
Los Angeles Division'''

desc68 = '''Excerpt from the Personal Diary of Technician M. Green

"Sigh...I don't know how much longer the project will be funded. If we don't have a success soon, I think it will be back to Project "7th Day" for me. I just can't go back there. If only our Department Head Allison would give us more time! 

I am sure we could get the breakthrough we need and the weapon our government so desperately wants. I have been spending a lot of time with Scientists Anthony and Bonner trying to tweak emission parameters, but the going is slow. So far we have achieved a throughput of 5,000 mega-joules per impulse on the BBG, but the power drains rapidly and the proton shift problem is still evident. The meson particles DO stick to organic surfaces (and rebound off inorganic substances) so we have achieved some of our goals.

Speaking of particle physics, Scientist Raffray told me a zinger "What did the neutrinos say to earth... "We're just passing through"" Ha ha ha.

Oh well, I'll sign off now, sneak onto an unsecured landline and try to auction off some of my drops from City of Craftiness, I just love that game!"

Note to self: Change picture on internet dating site, I haven't received any hits in over 3 months. Perhaps it was the leopard skin thong?'''

desc69 = '''From: OOS, Area 51
Sent: Friday, January 07, 2005 1:03 PM
To: All Personnel working with sub-levels 53-58 
Subject: URGENT: Use of "Buddy System" for cavern exploration
Importance: ULTRA 

FOR OFFICIAL USE ONLY - NO FORWARDING TO UNCLEARED PERSONNEL

After the unfortunate release of 4 specimens from holding section 23 in sub-level 54, we have been experiencing a slight amount of personnel loss monthly. While this is well within the safety limits set by section 1259a of the Area 51 protocols, we'd like to remind all personnel in the sub-levels 53-58 to use the "Buddy System" while exploring off the main excavation.

As you may know, Technicians Lum, Franco and Smischney have been missing for 3 weeks (SEE ABOVE FOR ID PHOTOS). Technician Smischney was last seen starting his initial exploration of cavern "Maya" and contact was quickly lost. Technician Lum was last seen in FTE #4 in cavern "Locomotive." Before he entered the FTE (Field Toilet, Enclosed) he was muttering something about "positive cash flow", which might have been related to his current project of studying EBE metabolic patterns. Technician Franco was last seen studying EBE hieroglyphics in cavern "Play."

Some good news: We believe we have identified the partial remains of Scientist Hird, but the body has decomposed so badly we must wait for the DNA results.

Hopefully the above cautionary examples will help everyone remember the "Buddy System."

Cordially yours,
Lt. R. Shelley
OFFICE OF OCCUPATIONAL SAFETY, AREA 51'''

desc70 = '''These are my final notes, jotted down here, where I have spent so much of my time over these last years. The scientific wonders I have seen within these concrete walls would easily have filled three careers in molecular xenobiology.

Unfortunately, I have become, or will shortly, the very subject of my work. I have contracted the infection and see no way to counteract the process. With my options thus limited, I have decided against allowing the infection to run its full course; the thought of losing my intellect, of devolving into one of those things, is too disturbing, too degrading, to bear. 

I have located a pistol, taken from one of the members of our unfortunate security staff. After some initial data collection, I managed to open up one of the personnel lockers and found a manual for the weapon, containing fundamentals on its basic operations. I conducted a satisfactory firing experiment, using Doctor Raleigh's body as a realistic target. (I felt some measure of remorse at using her corpse in this manner, but I am sure she would approve of giving her body for science.)

My methodology will involve angling the weapon upwards into the roof of my mouth. My desired goals are 1) the quickest cessation of brain activity, 2) the minimum in pain and 3) the greatest insurance of total success. (For these reasons, I discarded employing a scalpel or any of the toxins located herein.) 

May my two younger brothers remember me and live full lives. May the horrors we have wrought forever be contained within this complex. May the rest of the world forgive us.

Evan Van Zelfden'''

desc71 = '''As I wander the hard ground, I look to the too-bright skies of this world. Lifting my eyes to the sacred Mothership hidden above me, I try with all humility to recall the will of the Honored Coordinators. At times, I am certain I am following their directives, searching these crop-lands for the creatures that are my holy objective. Yet, at other moments, I cannot remember receiving the wisdom of the Coordinators. I experience, very clearly, a number of differing memories, some of which are at odds with one another and cannot be truth. During these time units, I am frightened.

In keeping with what I believe to be my sacredly-assigned obligations, I locate the chosen...the select among the bovine mammals of this world. When I find them, I cull them from the herd, again in keeping with what I remember of my directives. But my thoughts are often distorted. 

My mediations no longer work; calming myself is no longer a form of salvation. I must force myself to concentrate, to maintain focus over the moaning of these wretched creatures. I cut them open according to what I recall, the lines traced in flesh, the pattern-language of their blood-liquid. 

I arrange and display the bodily remains of the bovine mammals, trying so hard to remember the proper configurations. But I cannot remember why I was given this work; I can only hope that the sanctified Mothership can see my work from above, and that the Honored Coordinators are pleased. It is so hard to remember...

Why Ascending Saves the Ways,
Working Sub-Time Unit'''

desc72 = '''GROOM LAKE FILE AB-10

Alien Biology: Theta

This biological hyper-infector seems to be engineered to kill and infect, and nothing else. Apparently bio-engineered to spread the mutant contagion as quickly as possible to any carbon-based enemy, the Theta is also an impressive killing machine.

Internal biology shows both bio-engineering and nano-structural engineering. For 'bones', the theta appears to have a complex lattice of compounds, the frame of which is the higher Titanium we are still studying. Once you get past the battle-scales and to the internal structure, equally huge arteries feed the musculature, brain, and contagion sacs. Organs are wholly alien, but seem constructed and not evolved. If this were in our food chain, it would be a mix between shark, lion, bear, dart frog, black mamba, gorilla, and human, all with the bubonic plague. Let us hope this creature stays on our side.'''

desc73 = '''This diagram seems to show a Gray surrounded by a protective energy field. Studies indicate the field can shield against all attacks, but at a cost to energy, and that energy is finite. This energy may also relate to protection during teleportation. Highly charged Meson particles seem to rapidly destabilize the shield. A strategic trade of low-intelligence workforce for shielding technology might be underway. (Let's see if the Grays will give up the goods... we could use this tech for crowd control. - Coordinator Talamo)'''

desc74 = '''Galactic Universal Time Unit 1995.2311.8080.239

Honored Worker Sub-Class Biology,

More specimens are needed in unit Nova. Please request that White clone #455 procure 10 more human males within 10.5 time units.

 The last remaining specimen expired 190 Terra time units after thoracic cavity was exposed. This may have been due to shock as this experiment was performed without anesthesia. They are such frail creatures. 

Note: This particular specimen, #43,090 (S. Broumley, of the Terra Sub-Continent England), did last longer than anticipated. 

May Ascension Serve the Race,
Honored Coordinator Greater-Class Biology'''

desc75 = '''Galactic Universal Time Unit 1990.1997.2002.067

Honored Coordinator Greater-Class,

Per the most Honored Exalted's most emphatic suggestion, the following information has been distributed through the usual channels. Our security is assured. The time has come.

May Ascension Serve the Race,
Honored Disseminator Sub-Class'''

desc76 = '''Honored Sirs,

Please refer to the following diagram to determine your location and how to traverse throughout the area. It has come to our attention that certain members of the Select have been overstepping their bounds. This may have been an oversight on our part. Please note the location of the Core. Only those with CVC clearance may enter that area. Be warned, as all others will be terminated immediately.

May Ascension Serve the Race,
Honored Coordinator Greater-Class'''

desc77 = '''GROOM LAKE FILE. NEM 54-2

INSTRUCTION MANUAL FOR NEW EMPLOYEES

Section 54-2
Use of the EW Elevators

The elevators used by the aliens are based on their Electromagnetic Wave Propagation Device. They are simple to use like our elevators, with only a few precautions.

1. Keep your entire body inside the cylinder of the elevator disk. The hexagonal containment shields will shear off any protrusions, such as last year's incidents of 23 field packs, 5 limbs, 2 heads, and 4 genitals
2. Do not hum. If you should happen to hit a note one semi-hemi-demi-quaver above middle C, a cascading resonance may build up in your brain case, liquefying your brain and eyes.
3. Do not jump just before arriving. A standard "fun" practice in conventional elevators, entering the translation plane above you would be akin to pushing yourself headfirst through an interdimensional food processor. In a word, don't.'''

desc78 = '''Honored Worker Sub-class,

Please note the entry points for transported materials. The canisters have been transported from the facility above. All must be on board by the designated time unit. You will succeed. There will be no delays.


May Ascension Serve the Race,
Honored Coordinator Greater-Class'''

desc79 = '''Honored Sirs,

As you know, the MagLevs are used to transport the research materials to the Mothership to prepare for our journey. Given your limited movement capabilities, we have modified a few of our material transport MagLevs to make them fit for human transportation as well. While not all areas are accessible via MagLev, many are. Please plan your descension accordingly.'''

desc80 = '''Honored Coordinator Greater-Class,

May my will serve as an extension of your own. 

In accordance with my directive, I followed our lost brother. His path under the skies of this world was erratic, leading him to the open spaces wherein their food-crops are grown. I remained unseen as I traced his movements across the topography. 

For blocks of time, he burrowed himself into their wild places or hid within the dark spaces of their service structures. Then, operating from some time unit pattern that I was unable to discern, he would emerge.

Again and again, he moved through their tallest standing organic food-crops, always by night and always in patterns that seemed arbitrary. By the light of their world-star, his madness was clear: Using only his limbs, he flattened their carefully ordered rows of vegetation, creating glyphic shapes that would be most easily seen from above. 

Though indecipherable, I have wondered if these patterns were some attempt by our lost brother to communicate with our Glorious Mothership. Perhaps he is in pain...perhaps he is no longer in tune with the sacred reverberations. This is merely the idle speculation of my mind; respectfully, I must assert that his behavior was beyond my limited comprehension. 

As reported in prior communications, our lost brother harmed no one and was never observed. 

May Ascension Serve the Race,
Field Scout Sub-Class'''

desc81 = '''TOP SECRET OMEGA 1 CLEARANCE

Generals, Cabinet, and Commander-in-Chief Eyes Only

Operation Ground Terror

This operation is concerned with the bio-engineering of the "Super Theta." The original enemy-infecting ground troop was very lethal, but suffered from being able to execute proximity attacks only. Now, with the meson weapon integrated into the bone structure of the arm, the Super Theta has no weaknesses. It can only be seriously damaged by alien meson technology, which the target enemies, of course, do not possess. By turning the enemy's own troops against them, victory should be swift.

The prototype is now incubating, and all indications are that the experiment is a complete success. After testing the prototype, now guarding the Grays' ship, full production and delivery shall commence.'''

desc82 = '''Scrawled notes over diagram

Scalar Teleportation has proven far more stable than anticipated for transporting combat resources. Success rate 94%. Initial inconsistencies with temporal loop regression in folded space can be negated by adjustment to individual scalar regulator. This unfortunately prohibits temperature regulation, exposing resources to extreme temperatures. Correcting this should reduce failure rate to 3%.'''

desc83 = '''GROOM LAKE FILE AW-3

MC-11 Meson Cannon

Power Source: AEE

Description: The Meson Cannon, reserved for Red Ops only, is now the highest-powered weapon in The Dark Op arsenal. The Meson cannon fires out a projected planar disc which upon surface contact forms a .7m sphere of violet AEE energy. This sphere then emits what are best termed "energy tentacles," which flail and seek out organic targets.

Fire rate: 1 spheres/ 5 sec

Energy study: Again, the full range of properties of AEE energy are still unknown. (See Meson Autorifle, FILE AW-1, and AT-24, "AEE Energy".)'''

desc84 = '''Galactic Universal Time Unit 1990.1997.2002.149

Honored Soldier Sub-Class,

Latest orders from the Exalted indicate our power generators require full attention from the meta-protectorate. As we approach final installation of the 10 Galactic sub-units, the protective insulation on the power generators has been stripped away, exposing vulnerabilities in each core. Our labors near fruition and full vigilance at this stage ensures our ultimate success; we can afford no delay. Bear the responsibility with honor. 

Serve Nobly,
Honored Executor Greater-Class'''

desc85 = '''Galactic Universal Time Unit 1990.1997.2002.111
Honored Worker Sub-Class,

The Ascension of our holy Mothership is dependent on the proper emplacement and function of our power core. Using the carefully modulated collision of matter and antimatter in a suppressed gravity field, angravs (or antigravitron) are created and channeled, curving space-time. The core uses a relatively rare isotope of Francium 
(Francium 223), which has a half-life of 22 minutes. We have almost completed the creation of the 10 Galactic sub-units needed to refuel our glorious Mothership (it is easy but time consuming to create Francium 223 artificially by bombarding thorium with protons.) During the refueling process, the highly unstable core has been moved away from our sacred Mothership to prevent any catastrophic events from occurring. If any highly charged meson particles (or other forms of non-modulated energy) are introduced to the core during refueling, plasma flares will be released to rapidly lower the energy budget of a core going critical. If the plasma flares cannot dump enough energy rapidly, a large implosion will result, perhaps creating a short-lived micro-singularity. Obviously, great care must be taken during refueling, especially the unprotected plasma shunting vents located on the equator of the rotating power core. Remember these cautions well and may they inspire your work.

May Ascension Serve the Race,
Honored Coordinator Greater-Class'''

desc86 = '''Most honored Coordinator,

This image was discovered on the carcass of one of the elder Illuminati exhumed from the barbaric storage unit underground. Our lost brother aligned it correctly at the r-42 locus in the bovine mammal structural meditation GXPZ-8419.

The monorail is a poor approximation of the Mag Lev. Somehow, the Illuminati gained access to the following image, and used their limited human technology to ape its elegant design, silent, frictionless movement, and energy efficiency. I am not certain whether we should be flattered or offended.

May Ascension Serve the Race,
Honored Research Drone Sub-Class'''

desc87 = '''Placard under the model shows a series of indecipherable symbols. Below those symbols, the following text appears:

"Series KWXX-7 Survey Ship. Apply fluid TG-280 to activate. Do not activate in enclosed area. Contents expand on activation.'''

desc88 = '''Pan Dimensional Galactic portal has been calibrated to local surface coordinates 37??35.641' 115??53.924'.

Dimensional settings include correction for temporal variance. Calibrate the Terra Actualization Meter to 1824.769.

Ascension is the Embodiment'''

desc89 = '''Most Honored Coordinator,

Finally, the sentience and self-determinism of the honored Turret Sub-Class has been finalized. Our new life-form lacks non-telepathic communication devices, but they have unanimously indicated that they wish to serve and facilitate the Ascension.

We humbly request a dedicated telepathic channel for these, our newest citizens.

May Ascension Serve the Race,
Honored Engineer Sub-Class'''

#endregion


lore_list = [
    ('Welcome to Dreamland', 'Canister Specifications', 'https://i.imgur.com/ACeRJFT.jpg', desc0),
    ('Welcome to Dreamland', 'XM-88 Turret Specs', 'https://i.imgur.com/Xutyxjl.jpg', desc1),
    ('Welcome to Dreamland', 'Unknown Skin Type', 'https://i.imgur.com/AdO8y7g.jpg', desc2),
    ('Welcome to Dreamland', 'Decoded Laptop Information', 'https://i.imgur.com/Wys4NbG.jpg', desc3),
    ('Welcome to Dreamland', 'Health Syringe', 'https://i.imgur.com/9eVH1T4.jpg', desc4),
    ('The Hot Zone', 'Super Contagious Body', 'https://i.imgur.com/1eMkRRz.jpg', desc5),
    ('The Hot Zone', 'Alien Propaganda Sites', 'https://i.imgur.com/tuLxk8A.jpg', desc6),
    ('The Hot Zone', 'Unkown Artifacts Discovery', 'https://i.imgur.com/uWsf6DH.jpg', desc7),
    ('The Hot Zone', 'Employee Reprimand', 'https://i.imgur.com/Fyjhn96.jpg', desc8),
    ('The Hot Zone', 'New Employee Name Policy', 'https://i.imgur.com/3T8e3eH.jpg', desc9),
    ('The Search', 'Mite Jar', 'https://i.imgur.com/mfPHVjn.jpg', desc10),
    ('The Search', 'Alien Autopsy Photographs', 'https://i.imgur.com/v3C6NKq.jpg', desc11),
    ('The Search', 'Pictures of Human Oddities', 'https://i.imgur.com/Z9TyJSQ.jpg', desc12),
    ('The Search', 'Unknown Lifeform', 'https://i.imgur.com/n6vidFY.jpg', desc13),
    ('The Search', 'Vechtol Work Order', 'https://i.imgur.com/VgBDVRF.jpg', desc14),
    ('They Get Bigger', 'Saucer Ship Schematics', 'https://i.imgur.com/CRqxLyK.jpg', desc15),
    ('They Get Bigger', 'Star Chart and Pyramid Alignment', 'https://i.imgur.com/bg7gamD.jpg', desc16),
    ('They Get Bigger', 'Crop Circle Documents', 'https://i.imgur.com/78AFYnS.jpg', desc17),
    ('They Get Bigger', 'Atlantis Map', 'https://i.imgur.com/swYF5pu.jpg', desc18),
    ('They Get Bigger', 'Experiment Volunteer Request', 'https://i.imgur.com/tCXwcTD.jpg', desc19),
    ('The Last Stand', 'Groom Lake Weapons Testing Facility', 'https://i.imgur.com/INImlNM.jpg', desc20),
    ('The Last Stand', 'Unidentified Metallic Substance', 'https://i.imgur.com/jDjjffC.jpg', desc21),
    ('The Last Stand', 'Public Ebola Test', 'https://i.imgur.com/7MdggVh.jpg', desc22),
    ('The Last Stand', 'KGB Research Information', 'https://i.imgur.com/TzloIYu.jpg', desc23),
    ('The Last Stand', 'Congressional Disinformation', 'https://i.imgur.com/kAOZvxd.jpg', desc24),
    ('One of Them', 'Project Blue Book', 'https://i.imgur.com/mEBSkVh.jpg', desc25),
    ('One of Them', 'Green River Launch Complex', 'https://i.imgur.com/NSFEc3f.jpg', desc26),
    ('One of Them', 'Demute Chamber Warning', 'https://i.imgur.com/aYY7zzt.jpg', desc27),
    ('One of Them', 'Cray Assassination', 'https://i.imgur.com/4NmHwjV.jpg', desc28),
    ('One of Them', 'Gray Experiment Chat Log', 'https://i.imgur.com/YBvD1YV.jpg', desc29),
    ('Internal Changes', 'Leaper Vivisection', 'https://i.imgur.com/N0VJVPy.jpg', desc30),
    ('Internal Changes', 'Report on Mutant Vision', 'https://i.imgur.com/sxEDvxI.jpg', desc31),
    ('Internal Changes', 'Death Request Form Letter', 'https://i.imgur.com/g5WMcPC.jpg', desc32),
    ('Internal Changes', 'Destruction Orders', 'https://i.imgur.com/twjF9KD.jpg', desc33),
    ('Internal Changes', 'Red Ops Information', 'https://i.imgur.com/YRMdRYR.jpg', desc34),
    ('Life or Death', 'Illuminati Dollar Bill', 'https://i.imgur.com/pu36y0m.jpg', desc35),
    ('Life or Death', 'Capacity Overload Orders', 'https://i.imgur.com/O0NKq2A.jpg', desc36),
    ('Life or Death', 'Servo-Arm Manual', 'https://i.imgur.com/iXpINF1.jpg', desc37),
    ('Life or Death', 'Big Foot Canister', 'https://i.imgur.com/C9LOQTO.jpg', desc38),
    ('Life or Death', 'Alien Implosion Technology', 'https://i.imgur.com/3D77vlR.jpg', desc39),
    ('Dr. Cray', 'Mutation Extraction Subject', 'https://i.imgur.com/Ncnnzff.jpg', desc40),
    ('Dr. Cray', 'Dr. Cray Weapon Experiments', 'https://i.imgur.com/2D1fQYn.jpg', desc41),
    ('Dr. Cray', 'Victor Weisbrod Cloning', 'https://i.imgur.com/7HwS4ds.jpg', desc42),
    ('Dr. Cray', 'Mr. White Cloning', 'https://i.imgur.com/g2OjsWG.jpg', desc43),
    ('Dr. Cray', 'Decontamination Chamber Specs.', 'https://i.imgur.com/0UA5KpT.jpg', desc44),
    ('Hatching Parasites', 'Alien Grenade Specifications', 'https://i.imgur.com/op08eXi.jpg', desc45),
    ('Hatching Parasites', 'Grays JFK Assassination', 'https://i.imgur.com/TwkH0ib.jpg', desc46),
    ('Hatching Parasites', 'Alien Parasitic Creature', 'https://i.imgur.com/MBb5gPb.jpg', desc47),
    ('Hatching Parasites', 'Anti Grav Report', 'https://i.imgur.com/byVSzSx.jpg', desc48),
    ('Hatching Parasites', 'Laser Progress Report', 'https://i.imgur.com/UHri8Zo.jpg', desc49),
    ('Project: Blue Book', 'Roswell Communication', 'https://i.imgur.com/eVA99Lp.jpg', desc50),
    ('Project: Blue Book', 'Bermuda Triangle Singularity', 'https://i.imgur.com/oiq16jJ.jpg', desc51),
    ('Project: Blue Book', 'SETI Redirection', 'https://i.imgur.com/iOGWhQ9.jpg', desc52),
    ('Project: Blue Book', 'HyperX Technology Report', 'https://i.imgur.com/SMAzyj2.jpg', desc53),
    ('Project: Blue Book', 'Public Alien Technology Device Report', 'https://i.imgur.com/ZL1wk7Z.jpg', desc54),
    ('Lies of the Past', 'Echelon Network', 'https://i.imgur.com/zfjf5QG.jpg', desc55),
    ('Lies of the Past', 'Film Reel and Documents', 'https://i.imgur.com/qyrJGfc.jpg', desc56),
    ('Lies of the Past', 'Animal Experimentation Notes', 'https://i.imgur.com/PKpsveu.jpg', desc57),
    ('Lies of the Past', 'Witness Elimination Methods', 'https://i.imgur.com/w6pEuXs.jpg', desc58),
    ('Lies of the Past', 'Future Mars Landing Information', 'https://i.imgur.com/4IAf8iC.jpg', desc59),
    ('Buried Secrets', 'Alien Skeletal System', 'https://i.imgur.com/JH1dIWx.jpg', desc60),
    ('Buried Secrets', 'BBG Spec Sheet', 'https://i.imgur.com/nriOpEd.jpg', desc61),
    ('Buried Secrets', 'Alien Metallurgy', 'https://i.imgur.com/113yKZv.jpg', desc62),
    ('Buried Secrets', 'Cloaking Device Report', 'https://i.imgur.com/MAVbt7Y.jpg', desc63),
    ('Buried Secrets', 'Population Control Documentation', 'https://i.imgur.com/kGTUqA0.jpg', desc64),
    ('Now Boarding', 'Alien Language Leak Closure', 'https://i.imgur.com/Nv15dU2.jpg', desc65),
    ('Now Boarding', 'Alien Artifact Storage List', 'https://i.imgur.com/1KQyHBK.jpg', desc66),
    ('Now Boarding', 'Water Fluoridation Plan', 'https://i.imgur.com/C9n3sHs.jpg', desc67),
    ('Now Boarding', 'Personal Diary Recording', 'https://i.imgur.com/ACN0GNW.jpg', desc68),
    ('Now Boarding', 'Safety Report', 'https://i.imgur.com/PpQLdkW.jpg', desc69),
    ('The Grays', 'Suicide Note', 'https://i.imgur.com/Yl106Ns.jpg', desc70),
    ('The Grays', 'Cattle Mutilations', 'https://i.imgur.com/emocIP1.jpg', desc71),
    ('The Grays', 'Theta Scan', 'https://i.imgur.com/1sUupiP.jpg', desc72),
    ('The Grays', 'Alien Shield Memo', 'https://i.imgur.com/I30BQMS.jpg', desc73),
    ('The Grays', 'Human Autopsy', 'https://i.imgur.com/xhKU7wT.jpg', desc74),
    ('Descent', 'Alien Base', 'https://i.imgur.com/7EjG98B.jpg', desc75),
    ('Descent', 'Lower Level Map', 'https://i.imgur.com/ar4CiH3.jpg', desc76),
    ('Descent', 'Hover and Propulsion Technology', 'https://i.imgur.com/wDxrZHm.jpg', desc77),
    ('Descent', 'Canister Cargo Orders', 'https://i.imgur.com/ErrkMWy.jpg', desc78),
    ('Descent', 'MagLev Memo', 'https://i.imgur.com/Jdi1Y0c.jpg', desc79),
    ('The Ascension', 'Crop Circle Origins', 'https://i.imgur.com/CwVmPmz.jpg', desc80),
    ('The Ascension', 'The Super Theta Project', 'https://i.imgur.com/nokA24g.jpg', desc81),
    ('The Ascension', 'Scalar Teleportation Notes', 'https://i.imgur.com/UupFMoZ.jpg', desc82),
    ('The Ascension', 'Meson Cannon Documentation', 'https://i.imgur.com/Z55b208.jpg', desc83),
    ('The Ascension', 'Alien Power Generators', 'https://i.imgur.com/BHRSkjN.jpg', desc84),
    ('The Last Exit', 'Core Specifications', 'https://i.imgur.com/auKAXpp.jpg', desc85),
    ('The Last Exit', 'Stolen Technology', 'https://i.imgur.com/t7mYZmT.jpg', desc86),
    ('The Last Exit', 'Model of Satellite Ship', 'https://i.imgur.com/gnMzVMU.jpg', desc87),
    ('The Last Exit', 'Galaxy Portal', 'https://i.imgur.com/Rbjs3pU.jpg', desc88),
    ('The Last Exit', 'Alien Turret Life-form', 'https://i.imgur.com/eLiLWc1.jpg', desc89)
]

class lore:

    def get_lore(entry=None):
        if entry is None:
            choice = random.choice(lore_list)
        else:
            choice = lore_list[entry-1]
        level = choice[0]
        short_desc = choice[1]
        img_url = choice[2]
        long_desc = choice[3]
        return level, short_desc, img_url, long_desc

    def get_lore_list():
        count = 0
        trimmed_lore_list = ""
        for x in lore_list:
            count += 1
            trimmed_lore_list += f"{count}) {x[0]}: {x[1]}\n"
        return trimmed_lore_list