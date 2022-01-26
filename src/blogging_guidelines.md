# Blogging Guidelines

Blogging serves many purposes, to the benefit of both the person blogging as well as the rest of the class. 

**Benefits to the person blogging.** The best way to master new material is to teach to someone else. However, having students teach the class does not scale and so blogging is a substitute. When you elect to write a blog post for this course, it means you will engage with the course material in a detailed, systematic fashion. Blog posts are _not_ transcriptions; as a student, you should view blogging as part of a pedagogical toolkit. Blogging is additionally a way to _practice scientific communication_ and to showcase what you know and are learning in a more public way (although [how public you want to be is up to you](#identity-management)).

**Benefits to the rest of the class.** Each person in this class has their individual background, which will inform their posts. Each individual may see something different in the content presented and interpret it differently. The diversity of student backgrounds can enrich learning. Through blog comments, the rest of the class can engage with the poster's perspective. 

## Logistics

The general procedure for blogging is:

1. [Make your intent to blog known](#intent-to-blog).
2. [Take notes during class](#taking-notes). _Note: you must actually attend lecture in-person in order to write blog posts._
3. [Submit your revised notes on Github](#submitting-notes).

Blogging should happen in two phases: during the first phase you will be taking contemporaneous notes and during the second phase you will write up your notes. 

### Intent to blog 

Not every class is eligible for a blog post and only one unit (i.e., a single person or two people working together) may elect to post for each eligible class. Therefore, a reminder to elect to blog will be posted in the [Announcements channel](https://teams.microsoft.com/l/channel/19%3a651bd0634b2b4860904830cd9efd50d5%40thread.tacv2/Announcements?groupId=e1375d3a-909d-4b56-860a-2d7ddc4912a5&tenantId=1c177758-4d6b-43dc-aaeb-3b9c42562967) on Teams. If you are interested in blogging, please reply to the post with your intent. I will designate the person who will be blogging by 9pm the night before class using the following algorithm:

1. Select the first person who has not yet _been selected_ to blog. 
2. If no such person exists, select randomly from the pool of people who have previously blogged. 

Note that if you have been selected to blog but fail to submit your post, I will not select you to blog in the future. 


### Taking notes

Taking notes is hard! When taking notes, do not expect you will be able to participate at the same level of engagement as you would, were you not taking notes. Do, however, feel empowered to **interrupt whenever you miss something**. 

Beacuse scribing is not transcription, while it is possible to take notes in a way that ends up differing very little from its final form, I expect most students to see a signficant change from their raw notes to the submitted version. 

#### Handwriting vs. Typing

You are free to use whatever medium for note-taking works best for you. If you do not consider yourself to be a good note-taker, consider using blogging to try out different methods of note-taking to see what works best for you.[^1] I will allow two students to submit a blog post together as co-authors, but they must coordinate and merge the work amongst themselves.


#### On the use of recording devices

You may use recording devices to aid in your note-taking. However, this is very likely to end up being more work than taking contemporaneous notes!


### Submitting blog posts

You should write your blog posts in [Markdown](https://www.markdownguide.org/basic-syntax/) and they should follow the [content guidelines](#content-guidelines).
<a id="correct-title"></a>
Be sure to name the blog post according to the following format:


`<month>_<day>_<lecture title>.md`

So the first blog post would be:

`01_21_knowledge_representation.md`

When you are ready to submit, follow these steps:

#### If this is your first blog post
1. [Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) the [course repository](https://github.com/uvm-maple/CS295A-S22).
2. [Clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) the repository you just forked to your local machine:
    * **Command line, over ssh**: `git clone git@github.com:<your_username>/CS295A-S22.git`. 
    * **Command line, over http:** `git clone https://github.com/<your_username>/CS295A-S22.git`
    * **Through the GUI**: No idea.
3. Add the _course repository_ (i.e., the one you forked from) as a [remote](https://docs.github.com/en/get-started/getting-started-with-git/managing-remote-repositories). From inside the directory you just cloned, call:
`git remote add upstream git@github.com:uvm-maple/CS295A-S22.git
` _Note: I have no idea how to do this with non-command line tooling_.
4. Continue to the [general instructions](#general-instructions).

#### General Instructions

5. Pull from upstream to ensure the local version of your repository is up-to-date: `git pull upstream main`.
6. Add your blog post with the [correct filename](#correct-title) to the folder `src/blog`.
7. Push to your forked repository:
    1. `git add src/blog/<month>_<day>_<lecture title>.md`
    2. `git commit -m 'new blog post'`
    3. `git push origin main`
8. Open a [pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork) against the parent (remote) repository.

The first time you submit a blog post, you should be prompted to agree to the [consent form](https://gist.github.com/etosch/ad909c10f5da4e60bea125d15e47edcf), notifying you of your FERPA rights and trasferring responsibility for management of personally identifying information to you.

Note: _Late notes will not be accepted. There is **no grade penalty for not submitting your notes**. If you fail to submit your notes and do not have the usual documentation (i.e., medical or personal reasons), you will not be selected to blog in the future._


## Content Guidelines

Scribe notes will be graded on *completeness*, *correctness*, and *legibility*. I do not expect you to produce transcriptions, but I do expect some narrative structure.

I will be using the following grading rubric; all elements are pass/fail, so students will only receive grades from the set {0, 3, 6, 9}:

* 3pts - Complete coverage of topics covered in lecture in narrative form. There should be heirarchical organization to the post, including summary bullet points that are expanded upon in the body of the post. 
* 3pts - Additional commentary and supplementary links. I expect all students to include enrichment information in posts, either relating to applications of the topic, news articles, recent research, tutorials, etc. I am looking for a deeper engagement with the material in this section. 
* 3pts (graduate only) - A small, worked-out example problem in the space that functions as an explainer for the topic covered. The complexity of this problem should be greater than the in-class quizzes, but less than the theory assignments. 


# Identity management

The blog for this course will be public. However, your status as a student in this course is protected by FERPA and therefore your identity on public blog posts does not need to be public as well. You will need to sign a [consent form](https://gist.github.com/etosch/ad909c10f5da4e60bea125d15e47edcf) in order to contribute blog posts. If you wish to use a non-identifying account, you will need to contact me to let me know who you are so you can receive credit!

[^1]: I, personally, have always struggled with note-taking. I never looked back at my notes and never understood the purpose. It was not until the middle of graduate school until I learned to take notes as a way that worked for me: I would just write what I heard and generally not look at what I was writing. I learned this from [Edward Z. Yang](http://ezyang.com), who used to publish his raw notes online, but I cannot find them now. In any case, this meant that early on I had a lot of typos and portions of my notes that were effectively illegible. Eventually, they started to look like [this](https://docs.google.com/document/d/1f8tcvQCVcS6pJ2qECe_mDsdsO4adbyKoNuE3FlUne9c/edit?usp=sharing). I also found it helpful to share my note document with someone as I was typing to help check my understanding live. You can see an example of this [here](https://docs.google.com/document/d/1At8G0OK6TngKrd7Owbq0rBRzAbSaxV97TvkC1zImjDA/edit?usp=sharing), where my then-advisor responded to my notes in real time.
