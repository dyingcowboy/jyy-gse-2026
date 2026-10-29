# Quibi: An Open Letter (2020)

> 来源: https://quibi-hq.medium.com/an-open-letter-from-quibi-8af6b415377f
> 抓取方式: Playwright 渲染后取正文 (curl 被 Cloudflare/Medium 拦截)

Get app
Write

Sign up

Sign in

Quibi
Quibi
Follow
3 min read
·
Oct 22, 2020

789

An open letter to the employees, investors, and partners who believed in Quibi and made this business possible —

We started with the idea to create the next generation of storytelling and because of you, we were able to create and deliver the best version of what we imagined Quibi to be. So it is with an incredibly heavy heart that today we are announcing that we are winding down the business and looking to sell its content and technology assets.

Quibi was a big idea and there was no one who wanted to make a success of it more than we did. Our failure was not for lack of trying; we’ve considered and exhausted every option available to us.

While the result was not what any of us wanted, we did accomplish a number of things and we are very proud of what the talented Quibi team has built with the blood, sweat, and tears that they poured into this business over these past two years.

We opened the door to the most creative and imaginative minds in Hollywood to innovate from script to screen and the result was content that exceeded our expectations. We challenged engineers to build a mobile platform that enabled a new form of storytelling — and they delivered a groundbreaking and delightful service. And we were joined by ten of the most important advertisers in the world who enthusiastically embraced new ways for their brands to tell their stories.

With the dedication and commitment of our employees and the support we received from our investors and partners, we created a new form of mobile-first premium storytelling.

Get Quibi’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

And yet, Quibi is not succeeding. Likely for one of two reasons: because the idea itself wasn’t strong enough to justify a standalone streaming service or because of our timing.

Unfortunately, we will never know but we suspect it’s been a combination of the two. The circumstances of launching during a pandemic is something we could have never imagined but other businesses have faced these unprecedented challenges and have found their way through it. We were not able to do so.

Which brings us to this moment. As entrepreneurs our instinct is to always pivot, to leave no stone unturned — especially when there is some cash runway left — but we feel that we’ve exhausted all our options. As a result we have reluctantly come to the difficult decision to wind down the business, return cash to our shareholders, and say goodbye to our colleagues with grace. We want you to know we did not give up on this idea without a fight.

Our goal when we launched Quibi was to create a new category of short-form entertainment for mobile devices. Although the circumstances were not right for Quibi to succeed as a standalone company, our team achieved much of what we set out to accomplish, and we are tremendously proud of the award-winning and innovative work that we have produced, both in terms of original content and the underlying technology platform. Over the coming months we will be working hard to find buyers for these valuable assets who can leverage them to their full potential.

We want you to know that we got up every day and genuinely loved coming to work with the most remarkable and passionate team that we have ever assembled. We will be forever proud of the extraordinary partnership we were able to forge between the best of Hollywood and Silicon Valley.

All that is left now is to offer a profound apology for disappointing you and, ultimately, for letting you down. We cannot thank you enough for being there with us, and for us, every step of the way.

Jeffrey Katzenberg and Meg Whitman

Quibi

789

Written by Quibi
27 followers
·
1 following

Got a few minutes? That’s all you need to be entertained, informed & inspired. Quibi presents fresh content from today’s biggest stars, one quick bite at a time

Follow

Help

Status

About

Careers

Press

Blog

Store

Privacy

Rules

Terms

Text to speech"
### Ran Playwright code
```js
await page.evaluate('() => document.querySelector(\'main\')?.innerText ?? document.body.innerText');
```
### Page
- Page URL: https://quibi-hq.medium.com/an-open-letter-from-quibi-8af6b415377f
- Page Title: An open letter from Quibi. to the employees, investors, and… | by Quibi | Medium
- Console: 12 errors, 1 warnings
### Events
- New console entries: .playwright-mcp\console-2026-10-29T02-32-41-663Z.log#L114-L115
