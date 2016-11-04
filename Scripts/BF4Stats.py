# -*- coding: utf-8 -*-
import obot
import json
import requests
import warnings
from time import sleep
import time

r = obot.login()
warnings.simplefilter("ignore", ResourceWarning)
while True:
	players = requests.get('http://api.bf4stats.com/api/onlinePlayers')
	amount = json.loads(players.text)
	post = r.get_submission('https://www.reddit.com/r/battlefield_4/comments/3xbdaw/we_need_a_stickied_post_for_should_i_get_bf4/')
	pc = amount['pc']['peak24']
	ps4 = amount['ps4']['peak24']
	x360 = amount['xbox']['peak24']
	xone = amount['xone']['peak24']
	ps3 = amount['ps3']['peak24']
	pc = '{0:,}'.format(pc)
	ps4 = '{0:,}'.format(ps4)
	x360 = '{0:,}'.format(x360)
	xone = '{0:,}'.format(xone)
	ps3 = '{0:,}'.format(ps3)
	audate = time.strftime("%d/%m/%Y")
	usdate = time.strftime("%m/%d/%Y")
	post.edit(
'''#**Is the community still active?**

Yes, very. 

 &nbsp;

**24Hr Peaks** %s (%s)):
 &nbsp;




**Check for up to date stats here: http://bf4stats.com/**


 &nbsp;

* **Xbox 360**:

 %s Concurrent Players
 
&nbsp;

* **Playstation 3**:

 %s Concurrent Players

&nbsp;

* **Xbox One**:
 
 %s Concurrent Players
 
&nbsp;
 
*  **Playstation 4**:
 
 %s Concurrent Players
 
 &nbsp;

*  **PC**:
 
 %s Concurrent Players

 &nbsp;


**Check how many players are currently playing in your region**

Once the page loads, you must select your region and click '**Apply Filter**'

**[China Rising Players](http://battlelog.battlefield.com/bf4/servers/pc/?filtered=1&expand=1&settings=&useLocation=1&useAdvanced=1&q=&maps=XP1_002&maps=XP1_004&maps=XP1_003&maps=XP1_001&mapRotation=-1&modeRotation=-1&password=-1&osls=-1&vvsa=-1&vffi=-1&vaba=-1&vkca=-1&v3ca=-1&v3sp=-1&vmsp=-1&vrhe=-1&vhud=-1&vmin=-1&vnta=-1&vbdm-min=1&vbdm-max=300&vprt-min=1&vprt-max=300&vshe-min=1&vshe-max=300&vtkk-min=1&vtkk-max=99&vnit-min=30&vnit-max=86400&vtkc-min=1&vtkc-max=99&vvsd-min=0&vvsd-max=500&vgmc-min=0&vgmc-max=500&includeExpansions=1048576)**

**[Second Assault Players](http://battlelog.battlefield.com/bf4/servers/pc/?filtered=1&expand=1&settings=&useLocation=1&useAdvanced=1&q=&maps=XP0_Caspian&maps=XP0_Oman&maps=XP0_Firestorm&maps=XP0_Metro&mapRotation=-1&modeRotation=-1&password=-1&osls=-1&vvsa=-1&vffi=-1&vaba=-1&vkca=-1&v3ca=-1&v3sp=-1&vmsp=-1&vrhe=-1&vhud=-1&vmin=-1&vnta=-1&vbdm-min=1&vbdm-max=300&vprt-min=1&vprt-max=300&vshe-min=1&vshe-max=300&vtkk-min=1&vtkk-max=99&vnit-min=30&vnit-max=86400&vtkc-min=1&vtkc-max=99&vvsd-min=0&vvsd-max=500&vgmc-min=0&vgmc-max=500&includeExpansions=524288)**

**[Naval Strike Players](http://battlelog.battlefield.com/bf4/servers/pc/?filtered=1&expand=1&settings=&useLocation=1&useAdvanced=1&q=&maps=XP2_001&maps=XP2_002&maps=XP2_004&maps=XP2_003&mapRotation=-1&modeRotation=-1&password=-1&osls=-1&vvsa=-1&vffi=-1&vaba=-1&vkca=-1&v3ca=-1&v3sp=-1&vmsp=-1&vrhe=-1&vhud=-1&vmin=-1&vnta=-1&vbdm-min=1&vbdm-max=300&vprt-min=1&vprt-max=300&vshe-min=1&vshe-max=300&vtkk-min=1&vtkk-max=99&vnit-min=30&vnit-max=86400&vtkc-min=1&vtkc-max=99&vvsd-min=0&vvsd-max=500&vgmc-min=0&vgmc-max=500&includeExpansions=2097152)**


**[Dragons Teeth Players](http://battlelog.battlefield.com/bf4/servers/pc/?filtered=1&expand=1&settings=&useLocation=1&useAdvanced=1&q=&maps=XP3_UrbanGdn&maps=XP3_MarketPl&maps=XP3_Prpganda&maps=XP3_WtrFront&mapRotation=-1&modeRotation=-1&password=-1&osls=-1&vvsa=-1&vffi=-1&vaba=-1&vkca=-1&v3ca=-1&v3sp=-1&vmsp=-1&vrhe=-1&vhud=-1&vmin=-1&vnta=-1&vbdm-min=1&vbdm-max=300&vprt-min=1&vprt-max=300&vshe-min=1&vshe-max=300&vtkk-min=1&vtkk-max=99&vnit-min=30&vnit-max=86400&vtkc-min=1&vtkc-max=99&vvsd-min=0&vvsd-max=500&vgmc-min=0&vgmc-max=500&includeExpansions=4194304)**


**[Final Stand Players](http://battlelog.battlefield.com/bf4/servers/pc/?filtered=1&expand=1&settings=&useLocation=1&useAdvanced=1&q=&maps=XP4_WlkrFtry&maps=XP4_SubBase&maps=XP4_Titan&maps=XP4_Arctic&mapRotation=-1&modeRotation=-1&password=-1&osls=-1&vvsa=-1&vffi=-1&vaba=-1&vkca=-1&v3ca=-1&v3sp=-1&vmsp=-1&vrhe=-1&vhud=-1&vmin=-1&vnta=-1&vbdm-min=1&vbdm-max=300&vprt-min=1&vprt-max=300&vshe-min=1&vshe-max=300&vtkk-min=1&vtkk-max=99&vnit-min=30&vnit-max=86400&vtkc-min=1&vtkc-max=99&vvsd-min=0&vvsd-max=500&vgmc-min=0&vgmc-max=500&includeExpansions=8388608)**
 &nbsp;

 &nbsp;

#**What DLC should I get?**

This far into Battlefield 4™ it is kinda all or nothing. Many servers run base maps, or all DLC Maps. 

Also remember this is free DLC. However this is not as big as the DLCs listed below.

**If you like...**

* **Infantry**

 Then I would suggest Dragons Teeth. It has many close quarters maps and is quite a fun DLC.

* **Vehicles**
 
 Then I would suggest China Rising. The maps on China Rising are very large and 3/4 of the maps have Jets, LAV's, Tanks, Helicopters and more. Along with **DIRTBIKES** :D

* **Older Battlefields**

 Then I would suggest Second Assault. It features 4 maps from Battlefield 3™ that are very fun. They feature a lot of vehicular mayhem along with some close quarters infantry gameplay

* **Naval Combat**

 Definitely Naval Assault. The map features quite a bit of land but also a BUNCH of Naval Combat. Nothing like sitting in an Attack Boat and shooting down another boat before  using a TOW Missile to take out the jet above you! Unfortunately some regions do not have Naval Assault commonly, such as Australia.

* **Mix of both**

 Then I would suggest Final Stand. Final Stand is a futuristic DLC with flying unmanned weapons and launch pods!

&nbsp;

* **REMEMBER**

 Buying all the DLCs individually is more expensive then simply getting premium. Not to mention you also do not get the added benefits of Premium.


&nbsp;

#**Should I get premium?**

There a few reasons for why you should, AND, why you shouldn't

&nbsp;

**Reasons for YES:**

*  If you are a frequent player of Battlefield™, then I would highly recommend getting premium. It will give you all of the DLCs + a bunch of premium only customization and quite a few battle-packs.

* A lot of servers only run all DLC or nothing. Meaning if you want to play a Final Stand map and you do own the DLC, you still might not be able to join the server because of the other maps in the rotation

&nbsp;

**Reasons for NO:**

* If you are happy with the base maps then premium might not be for you. Buy the DLC you want to get (Making sure the price does not exceed premium), and hope you can find servers running only that DLC.

&nbsp;

**Premium Exclusives**

* Battlefield 4 Premium comes with a whole range of exclusives excluding just DLC. Here is a full list (comment if something need to be added)

 * 5 Expansion Packs (Combines price of expansions packs is higher then Premium)



 * Personalization Options
  
           * Exclusive Dog-tags
           * Exclusives Camos for |Weapons
           * Exclusive Paints for Vehicles
           * Upon puchase of Premium, you will receive 12 Premium Battlepacks (Containing Premium Items)

   * Priority Position in Queues (This one is amazing. If you are lucky to can jump right into servers with a 10 man queue  

&nbsp;

**Where can I get Battlefield 4 Premium cheap-ish?**

* [This place lists the price of BF4 Premium amongt all thirdparty online retailers](http://www.allkeyshop.com/blog/buy-battlefield-4-premium-cd-key-compare-prices/)(i.e. G2A)

* [Battlefield 4 Premium on Origin](http://www.battlefield.com/au/battlefield-4/premium-membership/)(Can be cheap during sales)

* [Battlefield 4 Edition on Origin](http://www.battlefield.com/au/battlefield-4/premium-edition)(Can be cheap during sales)


&nbsp;

&nbsp;

#**I just bought the game and I have 3 hours played and I'm getting wrecked! My K/D sucks and I don't understand:**

* The game rewards finding individual play-style. There are many ways to contribute to the team, and K/D is less important in Battlefield than it is in other modern shooters. Learn to think tactically about your moves, use cover, choose spawn points wisely; anticipate flanking movements and flank back. Don't be afraid to be a medic or support. (Written by /u/mycrystalcity)

&nbsp;

&nbsp;

#**Additional Content**

At release of the game, there was 5 DLCs planned, but that has since changed.

&nbsp;

* **Night Operations** (Released September 1, 2015)

 Battlefield 4: Night Operations, also called Night Ops, is a free expansion and content update for Battlefield 4 that was released on September 1, 2015[1]. The expansion includes a new nighttime map: Zavod: Graveyard Shift, a night version of Zavod 311 which has an emphasis on stealth and tactical gameplay. More info here ([BF Wiki)](http://battlefield.wikia.com/wiki/Battlefield_4:_Night_Operations)

&nbsp;

* **Community Operations** (Released October 27, 2015)

 Battlefield 4: Community Operations is a free expansion and content update for Battlefield 4 released October 27, 2015 along with the Fall 2015 update. The expansion includes a new map, Operation Outbreak, previously known as the Community Map Project, which was created in heavy collaboration with the Battlefield community. More info here([BF Wiki)](http://battlefield.wikia.com/wiki/Battlefield_4:_Community_Operations)

&nbsp;

* **Legacy Operations** (Released December 15, 2015)

 Battlefield 4: Legacy Operations is a free expansion and content update for Battlefield 4 set to be released on December 15, 2015. The expansion will include an updated version of the Battlefield 2 map, Dragon Valley.

 The expansion will only be available on the PC, Xbox One, and Playstation 4 platforms, and is the first to not be released for the Xbox 360 and Playstation 3. More info here ([BF Wiki)](http://battlefield.wikia.com/wiki/Battlefield_4:_Legacy_Operations)

&nbsp;

#**Weapon Comparisons**

* RPG vs SMAW

 * The RPG and SMAW is a very popular weapon in Battlefield 4 mostly used for anti air combat and taking on ground vehichles. Unlike the Stinger, Igla and Javelin, the RPG and SMAW  is a true fire and forget without the need to lockon.

 * RPG Advantages:
 
           * The RPG reloads faster then the SMAW
           * The RPG takes up less space on your screen allowing you to see more targets.
           * The RPG does roughly 8-12 percent higher damage than the SMAW depending on the vehicle. It can often make the difference between getting the killing blow, or dying.  (thanks /u/Xuvial)

  * SMAW Advantages

           * The SMAW launches faster then the RPG
 
           * The SMAWs max speed is fast then the RPG

           * The SMAW is less effected by gravity then the RPG

* Conclusion

 * Statistically, the SMAW and RPG are similar except for the damage given off by the RPG, however it is still a matter of personal opinion. I prefer the RPG for the look. But many prefer the SMAW for its accuracy. Practice using both and see what is best for you.

&nbsp;

&nbsp;

Thankyou for reading my post! I have put a lot of effort into this and keeping it active and updated. I reply to every comment if it has a question, let me know what you want added to the post and I will try my best to research it all and add it to the post.

&nbsp;

A very special thanks /u/Death3d for sticking this post to the top of /r/battlefield_4. I will keep this updated for as long as I can!''' % (usdate, audate, x360, ps3, xone, ps4, pc))
	sleep(86400)
