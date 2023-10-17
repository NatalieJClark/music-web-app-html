# Music Web App HTML

## Introduction

- This is my Music Web App HTML project for Makers Module 4 - Web Applications
- It is the second project for phase 3 of the module

## Aims

I used this project to:
- [x] Consolidate HTML structure knowledge
- [x] Consolidate knnoledge of testing for HTML content
- [x] Learn how to use templates to return dynamic HTML
- [x] Learn how to use links to send GET requests
- [x] Learn how to test links

## Feedback

> Morning Natalie! I've just gone through your final challenge submission from the Web module!
> 
> Honestly at this point my feedback must seem repetitive because your process continues to be immaculate, so these are just a few edited highlight:
>
> - When encountering errors (especially unexpected ones), reviewing them for yourself in a web browser to see what was happening
> - You knew what errors you were expecting to see, and you immediately noticed when a different error was occurring (e.g. methhods typo)
> - When you were getting the "resolves to 4 list elements" failure in your Playwright code - you genuinely solved that faster than I would have!
> - Finishing the video by sanity-checking the site again in a browser
>
> I hope you found the Playwright stuff fun - we spend weeks looking at it on the Quality Engineering course, because it gets a lot more complicated than that, especially as the webpage complexity increases.
> Semantically I might have done the final test differently, although I appreciate that you were following the albums page example that Kay had done. Your (and Kay's) final test is technically what we call a "scenario test" or a "journey test": you're performing a series of actions to walk through a website in the same way that a user would.
> What this means is, technically clicking the Taylor Swift link, waiting for the Taylor Swift page to load, and checking the text on the page is actually unnecessary: you already know that the /artists/<id> page renders correctly, because that's what your previous test did. This isn't a problem, but in a test suite for a large application - let's imagine you were doing this 1000 times - these extra page loads can add up to a lot of extra time running the tests.
> In case you're curious, here's how I might have done the same test in the Quality Engineering course (though to reiterate, you did exactly what we expected of you!):
``` python
# NB I've skipped the db seed / goto steps
link_text = page.locator("text='Taylor Swift'")
a_tag = link_text.locator("xpath=..") # This means "get the parent element", i.e. it finds the <a> tag
expect(a_tag).to_have_attribute("href", "/artists/3")
```
> You're right, that code is uglier than what you've got! But it will probably run half a second faster, because you don't need to click the link, wait for the server to request the artist data from the database, and render the template. And you can safely do this because your test_get_artist_with_id test is already giving you the confidence that the link will work when clicked.
>
> Anyway I definitely got carried away with feedback there, because I saw the opportunity to make a developer into a better tester, which is a chance I'll always take!