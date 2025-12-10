# CSC226 Final Project

## Instructions

**Author(s)**: Lindsay Manabat and Julius Fritz

️**Google Doc Link**: https://docs.google.com/document/d/1ZJxvK9T8e1s6n0YdTw4ysDT0Wz4_HKCg75EftcwxkJg/edit?usp=sharing

---

## Milestone 1: Setup, Planning, Design

️**Title**: `Blackjack`

**Purpose**: `The orginal idea of blackjack but with a twist of having a special card.`

**Source Assignment(s)**: ` Homework on "The Game of Nim. Teamwork on 'Intro to Classes, The Legend of Tuna"`

️**CRC Card(s)**:
![Don't leave me in your README!](image/crc.png "Image of CRC card as an example. Upload your CRC card(s) in place of this one. ")
![Player CRC card!](image/Player%20CRC.png "Player CRC Card")
![Dealer CRC card!](image/Dealer%20CRC.png "Dealer CRC Card")
![Screen CRC card!](image/Screen.png "Screen CRC Card")
![Character CRC card!](image/Character%20CRC.png "Character CRC Card")
![Button CRC Card!](image/Button%20CRC%20Card.png "Button CRC Card")

**Branches**: This project will **require** effective use of git.
```
    Branch 1 starting name: manabatl3
    Branch 2 starting name: fritzj2
```

### References

- https://www.247blackjack.com/
- https://www.piskelapp.com/ (We used this to create the images)
- https://www.pygame.org/docs/
- https://docs.python.org/3/library/unittest.html
- https://www.youtube.com/watch?v=G8MYGDf_9ho (For learning how to add buttons to the screen)
- https://www.pygame.org/wiki/Spritesheet
- https://stackoverflow.com/questions/20109487/how-do-i-use-sprite-sheets-in-pygame (For the real help with the spritesheet introduction)
- 

---

## Milestone 2: Code Setup and Issue Queue
```
    We think the pace we're working seems good. We're worried that it'll eventually catch up on us and working on the screen with pygame. 
    We've been cordinating pretty well and hope to continue. We're getting the hang of using/writing issue queue. Get better on using the feedback 
    we got from David and implement it onto the next work session. Use the LAB TA hours for better understanding on how to approach what we want to do.
```

---

## Milestone 3: Virtual Check-In

**Completion Percentage**: `65-70%`

```
    We're confident about completing this project in time because we know how much we still need to do and setting aside time to work on them.
    We worked on the framework of the upcoming steps which allows us to break it down easier and faster. We've chipped away from the really hard and complicated steps
    so we feel more confident in whats left. Instead of working on it individually so much we're working on it together at the same time, making it easier to add our own opinions, ideas, features, and debugging.
    
```

---

## Milestone 4: Final Code, Presentation, Demo

### User Instructions

```
    How to play Blackjack, 1st you start with betting. Then your goal is to get as close as possible to 21 while beating the dealer. You use the hit 
    button to draw a new card and the stand button to pass the turn to the dealer. There are 4 types of special cards which change the amount of money you bet and the
    amount of money you have. Afterwards you compare the values of each hand to see which are the closest to 21. Then press space to play again.
```

### Errors and Constraints

```
    The held button bug with the spacebar and holding stand which smashes through different rounds really quickly. 
    This could be fixed by removing the ability to hold two buttons at the same time.
    
```

### Reflection

- Why did you select the project that you did?
- How closely did your final project reflect your initial design?
- What did you learn from this process?
- What was the hardest part of the final project?
- What would you do differently next time, knowing what you know now?
- How well did you work with your partner? What made it go well? What made it challenging?

```
    Lindsay Manabat: We both orginially had two different ideas on what we wanted to do. Mine had something to do with creating a maze,
    while his was to make a duplicate of Blackjack but adding different features. We both thought out the pros and cons for the games 
    and chose BlackJack as it was the easiest one to plan off with. I'd say our final project reflected towards our initial design because 
    we were able to implement the special cards we wanted and at the same time have a regular blackjack card game. 
    
    This project has taught me more on how to use different functions, methods, and even learning how to use Spritesheets. The hardest was to fully understand how we wanted the code to plan out exactly what 
    we wanted. The spritesheets specifically was the hardest to understand because we had to pharse the code specifcially not really writing the code and it's function. 
    You had to choose it's specific suit and read the image then also display the image. We also had a hard time making sure the game turns were being changed so we used a alising method which
    I'm not too sure was the best idea at the moment but it helped us create the game eventually. 
    
    I guess planning everything out specifically to know which direction we should immieditatly go to. Because we knew what we wanted to do, it was just making sure which of which need to be done first. I believe my partner and I worked really well 
    with everything. We were able to communicate and function well together. I liked the idea of us physically working together to really help debug and work on certain 
    features together and also change things within how we felt about it. We were able to really give each of our own opinions on certain decisions together which made 
    the game design better. This also then made it so neither of us was lost or confused about how we're designing the game. Though, this did set us back a bit because we 
    weren't really working on it on our own other than that one time when we couldn't meet due to one of us being busy. But overall I didn't think we had much of a struggle 
    working together. 
```

```
    Julius Fritz: We selcted the project that we did because it was a game that I knew and it is something I thought would be simple and fun to play
        It turned out similar to the inital design but the screen layout was WAY off from what I was intially expecting. It still plays in a similar manner but the special cards-
        changed pretty drastically along the way I learned a lot about how to use spritesheets and working with images, they are tedious and hard to use when just given numbers
        so make them as simple as possible. I learned how to use objects in a very interesting way to somewhat run a bunch of objects inside of another, kind of like an aquiarium-
        full of fish. The spritesheet was by far the most difficult thing here, it reads in a very far removed way from traditional english.
        This in turn mkaes it very hard to read and write since it wasn't something I could just say outloud to make it functional. It is such-
        a complex system (in my opinion) and made it very hard to get correct. 
        
        The turn alias was a solution that I made originally that could realistically be solved by just tossing the-
        object into another object. The example of this is with the Button class and the Turn_of_Play method from the game class. They both pass around the turn variable, which could have just-
        been changed by passing the game()'s attribute turn into the Button. 
       
        I believe that we worked together pretty well and quite extensivley. We chose to work next to each other-
        similar to partner programming for a lot of the work, this allowed us to almost always be on the same page as one another. This especically helped during the rougher starting stages-
        of the project where there were still fuzzy parts to work out through the code. Some of the hard parts that we had would have to include the time where I missed class during the introduction-
        of the assignment, causing us to start like a week later than we needed too. Physically working together really was the only drawback we had. Although it always kept us on the same page,-
        we really didn't accomplish much outside of those meetings meaning we had gaps where we weren't working on it. The only time that we really worked separatley was the week before it was due,-
        where we made significant progress without the other person. However, this did mean we were always on the same page, and none of us ever got left behind.
        One more issue working togther was Thanksgiving break, where neither one of us really worked on it. It's a small issue and we were both on break, but it is still a chunk of time where nothing really got done.
```

---