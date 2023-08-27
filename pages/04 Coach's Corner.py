import streamlit as st
from utils import *

def coaching():
    st.markdown("# Coach's Corner")
    with st.sidebar: get_sideBar("Coach's Corner")

    st.markdown("This will ultimately serve as our wiki for coaching philsophy and decisions.")
    st.markdown("")
    st.markdown("Caveat: If you have strong thoughts and opinions let them be heard and we will figure it out. This is just a starting point, but I think it's important to be transparent. I will try to keep this updated as we go.")

    with st.expander("Click to reveal Batting Order Philosphy"):
        st.markdown('''First 5 batters generally get one extra at bat, so as a result, these spots will always be top 5 batters at a given time. 

### Leadoff 
While originally believed to be a speedy runner, watching TecoWestinghouse, and also how our next few hitters hit, we can see this position does not necessarily need to be our fastest person. They will almost certainly be hit in by spots 2-3. What we need from this position is someone who is:
1. Always on base (high batting %, high on base %). Out's are absolutely devastating from a leadoff.
2. Smart enough to take pitches, elongate game, and be situational since at end of games we may need this from someone who gets an extra at bat. 
3. Needs to be able to handle a little added pressure.

### 2 and 3
I put these together because they are in many ways the same justifications with only slight modifications. These must be your two best hitters. What is *Best* can be hard to determine, but in practice, they:
1. get on most often (BA), 
2. they get the most big hits (Doubles/Triples/HRs),
3. they are situational (understand late game situations), 
4. they understand how to move runners across (RBIs),
5. and they score (Runs). 

Many schools of thought vary but I typically follow the 2 hole is your best hitter, and 3 hole is runner up. These two need to generate between 4-5 runs per game between scoring and RBIs. 

## 4 and 5
Again these are put together because they are interchangeable in many ways. 

While it would be great to have Power Hitters in the classical sense of 4 and 5, in softball it's a little different. We need runs, and for us to sustain innings we need runners. 4 and 5 hole get an extra at bat typically so we need our next most reliable hitters. 

These batters often need to function as leadoffs/2/3 holes too. The chances are decent that 2 or 3 has already cleared the bases. So if 4 comes up with no one on, a HR does little to help us, but an out kills us. We need hitters who are getting on base as priority 1, and then getting extra base hits as priority 2. 

----

A note past 5. We now get into situational orders dependent upon who remains relative to each other. As a general philosophy you want to extend innings placing high contact earlier, followed by power and then end it with your lowest BA/OBP guys. Since we have typically 11-12 guys a game, I'm going to make a lineup to 12, but the groupings would get extended to 15. So 6 and 7 might become 6-9. 8-9 might become 10-13, etc. 

----
### 6 and 7
We need to keep innings going, piling on runs after a hopefully strong start from our top 5. Spray hitters with high BA and OBP are key. Depends on composition of who is present, but almost always a more reliable hitter who can sustain innings.

### 8 and 9 
At this point we are ready to start filtering in high risk, high reward folks. Might have lower BA but they also have a chance of jumping on a pitch and going deep, or really pushing the basepaths. 

### 10, 11, 12
To round out, we add in those who are not getting on base frequently. As an order of priority, higher BA, more hits, will likely bat before those with the opposite. 
''')
                    

    with st.expander("Click to reveal Batting Order Justification"):
        st.markdown('''

These justifications take into account both seasons, however a bit more weight is added to recency. Maybe 70/30 ish. This can change, and I'll try to keep it updated as the season goes on. I like to give folks some confidence by letting them hit in a position for a game or two before making big switches. This can change and is just representative of he 20-30 at bats most people have gotten. 
### Leadoff 
Based on what we need out of a leadoff its Beep. Most singles last season, situational awareness demonstrated in the game we needed extended, BA in top 3. Not bottom speed when he wants. He gives us a chance to score immediately. 
Next up: Grace, Cody, Spangler
### 2 and 3
Tyler and Josh. Tops in almost every category. Highest two in. slugging % by a ways. Hits per at bat, xb hits per at bat. I give Tyler the edge in the two hole because he has more Hits/At bat. 

Next up: Grace, Cody, Spangler

## 4 and 5
Grace and Ben. Can function as leadoffs, always on base, HR power, effort on basepaths to keep innings alive. This one was close, Cody had a slightly better season 2 than Ben, but Ben had such a dominate season 1. Slight edge Ben.

Next Up: Cody, Spangler

----

A note past 5. We now get into situational orders dependent upon who remains relative to each other. Groupings do not relate to exact order but where in the extended order they are likely to bat.

----
### 6 and 7
Cody, Spangler, Chris, Forrest

I like having lefties mixed in here to keep teams moving so will sometimes stagger them. These are next four up in BA so satisfies contact need, with some power as well from Forrest and Cody. 

Next Up: Dan, Niko
### 8 and 9 
Dan, Niko

Home run power so its a good time to plug in that high risk/reward before end of lineup. Below 500 batting average. 

Next Up: Renzo
### 10, 11, 12

Renzo, Frank, Sean, Shack

Below 300 BA last season, could put Renzo at the end to add a functional *second* leadoff given his speed.
 ''')
                    

    with st.expander("Click to reveal Fielding Philsophy"):
        st.markdown(''' 
Overall philosophy is this: Put people in positions to succeed! Not everyone is a good player at each position. Some positions have a lot tougher job than others. Want to accentuate players strengths and mitigate weaknesses. 

# Infield
### Pitcher
One of the most important positions on the field. Can be extremely mentally taxing. You must be a goldfish. The single most important need is: Strikes. Rather give up hits than walks and hits. 

### Catcher
This is one of the most engaging positions in the field. You are constantly involved, and while it does not require much lateral movement, there are times where high importance plays at the plate are critical and require focus and hand eye coordination. Need someone who can mantain, 

### 1st base
Important position because if we can't make plays at first going to be tough to get out of innings. Needs to be conscious of baking up plays at home. Scooping balls and hustling down overthrows also key. 

### 2nd base
Typically the position that gets more approachable grounders and low intensity throws to first. Good lateral range is useful, and high IQ. Needs to be really conscious:
1. plays at second with runners on first
2. Cutoffs from right field
3. Throws to second from left
4. maintaining position at 2nd during run down situations

### SS 
Most important position in the infield, and perhaps on the field. The most difficult. Needs all the high IQ mentioned above for situational awareness as well as strong arm, quick reactions, and a short memory. 

### 3rd base
Second toughest after short. Needs basically all of the same attributes except some lessened lateral agility acceptable. Needs to be very conscious of throws home and backing up there.


------
# Outfield

As a philosophy on the outfield, positioning may be dependent upon who we have and what combination of outfielders we have. We play an over exaggerated shift with certain personell and then straight up positioning with others. In general, its good to stagger players with high range to Left Field and Right Center. Allowing for players with less range to play in positions that get more direct hits.
### Left Field
Preferably a mobile and high range player with an ok arm since most throws will go directly to short stop cut off. The balls hit to left may be line drives which are hard to play so an outfielder with some experience is preferable. 

### Left Center
Balls hit to left center are often times bombs to the fence. Therefore asking a player to play this with deep positioning puts them in the best location for success. They have both left field and right center to help with shallow balls and cutoffs for very deep throws.

### Right Center
In the exaggerated shift position this is the position that is expected to do the most. By playing a center or shallow center position they are expected to cover the most ground, and at times be the cutoff for both Right and Left Center. High Baseball IQ, speed, and arm strength are pivotal for success.

### Right
While the classical, stick your worst outfielder here position, in softball good teams actually pick on this position a lot. So to mitigate this we play Right fielders a lot like left fielders, deep positioning with the expectation of catching direct popups and quickly stopping the grounders hit and getting it to cutoff (most typically Right Center fielder). Teams that are good will punish this position so it needs to be prepared.
''')

if __name__ == "__main__":
    coaching()
