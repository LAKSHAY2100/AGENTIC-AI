# Daily AI News Summary

<think>
Okay, let me tackle this. The user wants me to summarize the provided news articles into markdown format following specific guidelines. First, I need to parse each article's content, extract the date in IST, create a concise summary, and link to the source. 

Starting with the dates: each article has a date in GMT. I need to convert those to IST. Since IST is UTC+5:30 and the dates given are in GMT (UTC), adding 5 hours and 30 minutes should give me the correct IST date. For example, an article dated "Tue, 15 Jul 2025 06:48:10 GMT" would convert to "2025-07-15" since 6:48 AM GMT plus 5h30m is 12:18 PM IST. If the time is after 6:30 PM GMT, it would roll over to the next day. Let me check each date carefully.

Next, the summaries need to be concise. I should read each article's content and extract the key points without extra fluff. For example, the Tesla article mentions their first showroom in India after nine years, the context of market challenges, etc. 

Sorting the articles by date, latest first. The latest dates are from July 15, 2025. I'll need to group those first. The dates provided range from July 14 to July 15. Let me list all the dates converted to IST and sort them in descending order.

For the markdown format, each entry starts with ### [Date]. Then a bullet point with the summary and the URL as a link. Need to ensure the URLs are correctly formatted and linked. Also, check for duplicate entries. For instance, some titles repeat like "Tesla finally enters India..." but the URL is correct, so just use the provided URL.

Wait, looking at the first article, the title repeats twice. The content says "Tesla finally enters India — nine years after Elon Musk first teased its debut | TechCrunch" twice. Maybe a copy-paste error, but the URL is correct. I'll use the URL provided.

Now, check each article's date in IST. For example, the article dated "Tue, 15 Jul 2025 04:36:47 GMT" converts to 10:06:47 IST, so the date remains 2025-07-15. Similarly, "Mon, 14 Jul 2025 20:30:01 GMT" is 14 July 2025, 20:30 GMT. Adding 5h30m gives 01:30 AM IST on 15th, so date is 2025-07-15. Wait, no—if the original date is 14 July 2025 20:30 GMT, adding 5h30m would make it 01:30 AM IST on 15th July. So the date in IST is 2025-07-15. So even articles with dates on 14th July GMT that cross into 15th IST should be listed under 2025-07-15.

I need to process each date. Let me list each article's date (GMT), convert to IST, and then sort by that date.

Let's go through each one:

1. Content about Tesla: Date is Tue, 15 Jul 2025 06:48:10 GMT. Convert to IST: 12:18 PM. So date is 2025-07-15.

2. Nvidia article: Tue, 15 Jul 2025 04:36:47 GMT. Convert to IST: 10:06 AM. Date remains 2025-07-15.

3. Auriga Space: Date is Tue, 15 Jul 2025 13:00:00 GMT. Convert to IST: 18:30. So date remains 2025-07-15.

4. Meta announces crackdown on unoriginal content: Date is Mon, 14 Jul 2025 20:30:01 GMT. Adding 5h30m is 1:30 AM IST 15th. So date is 2025-07-15.

5. Google buys hydropower: Date Tue, 15 Jul 2025 13:05:02 GMT → 18:35 IST → 2025-07-15.

6. Amogy raises $80M: Tue, 15 Jul 2025 11:00:00 GMT → 16:30 IST → 2025-07-15.

7. Geely bringing Zeekr private: Tue, 15 Jul 2025 13:32:10 GMT → 19:02 IST → 2025-07-15.

8. Nextdoor app redesign: Tue, 15 Jul 2025 09:00:00 GMT → 14:30 IST → 2025-07-15.

9. Meta using tents for data centers: Date is Tue, 15 Jul 2025 05:25:13 GMT → 10:55 AM IST → 2025-07-15.

10. ParadeDB article: Date is Tue, 15 Jul 2025 13:24:51 GMT → 18:54 IST → 2025-07-15.

11. Joby Aviation doubles facility: Tue, 15 Jul 2025 13:00:00 GMT → 18:30 IST → 2025-07-15.

12. Meta's AI strategy shift: Mon, 14 Jul 2025 22:44:24 GMT → 04:14 AM IST 15th → 2025-07-15.

13. DOGE staffer leaks API key: Tue, 15 Jul 2025 13:40:00 GMT → 19:10 IST → 2025-07-15.

14. Matt Miller's new fund: Mon, 14 Jul 2025 21:56:19 GMT → 03:26 AM IST 15th → 2025-07-15.

15. Brian Singerman's new fund: Mon, 14 Jul 2025 23:33:28 GMT → 05:03 AM IST 15th → 2025-07-15.

So all articles except one (if any) have dates of 2025-07-15. Wait, let me check again. Wait, the first article's date was Tue, 15 Jul 2025 06:48:10 GMT, which is 12:18 PM IST, so date is 2025-07-15. The article with date Mon, 14 Jul 2025 20:30:01 GMT (Meta cracks down) is 01:30 AM IST on 15th, so date is 2025-07-15. So all articles are on 2025-07-15 IST. Wait, but the user provided some dates as Mon, 14 Jul... but converted to IST they are on 15th. So all articles are under 2025-07-15. Wait, is there any article that has a date in IST as 14th? Let's check.

For example, an article with GMT date Thu, 11 Jul 2025 00:00:00 GMT would be 05:30 AM IST on 11th July. So unless the article's GMT date is before 6:30 PM IST (since 6:30 PM IST is 1:00 PM GMT). Wait no. Wait, IST is UTC+5:30. So to find when GMT date is after 18:30 IST, but maybe not. Wait, perhaps I got the conversion wrong. Let me take an example: if an article's GMT date is Mon, 14 Jul 2025 23:59:59 GMT. Then IST would be 23:59:59 +5h30m = next day 5:29:59 AM IST. So the date in IST is 15th. So any article with GMT date on 14th July after 18:30 IST (i.e., 12:00 PM GMT) would actually be 15th IST. Wait, no, let me clarify.

To convert GMT to IST, add 5 hours 30 minutes. So for example:

- GMT date: 2025-07-14 18:30:00 → IST: 2025-07-15 00:00:00. So any GMT date after 18:30 on 14th July would roll over to 15th IST.

Looking at the article with date "Mon, 14 Jul 2025 20:30:01 GMT" → adding 5h30m gives 01:30:01 AM on 15th July IST. So the IST date is 2025-07-15.

Therefore, all articles provided have their IST date as 2025-07-15. Therefore, all should be under the same date. But maybe I missed something. Wait, the user provided some articles with GMT dates on Tue, 15 Jul 2025 and some on Mon, 14 Jul 2025. But when converted to IST, all of them fall under 2025-07-15. So all the articles are from the same date in IST. Therefore, in the markdown, all summaries will be under ### [2025-07-15].

Wait, but the user's instruction says to sort news by date wise (latest first). But since all are on the same date, the order depends on the time. But since the user wants the latest first, we need to sort the entries by their GMT date (since the IST date is the same). However, the user didn't specify sorting by time, just by date. But since all are on the same date, they can be listed in any order. However, perhaps the user expects the most recent GMT entries first. Let's check the GMT dates of each article.

Looking at the GMT dates:

- The latest GMT date is Tue, 15 Jul 2025 13:40:00 GMT (DOGE staffer leaks API key). Then comes Geely (13:32), Google hydropower (13:05), Joby Aviation (13:00), Auriga Space (13:00), etc. So sorting by GMT date descending.

So the order should be:

1. DOGE staffer leaks API key (13:40)
2. Geely brings Zeekr private (13:32)
3. Google hydropower deal (13:05)
4. Joby Aviation doubles facility (13:00)
5. Auriga Space raises $6M (13:00)
6. ParadeDB article (13:24)
7. Nextdoor app redesign (09:00)
8. Meta using tents (05:25)
9. Nvidia resuming China sales (04:36)
10. Tesla in India (06:48)
Wait, no, Tesla's GMT date is 06:48 on 15th. So in GMT order:

The latest GMT is DOGE (13:40), then Geely (13:32), Google (13:05), Joby (13:00), Auriga (13:00), ParadeDB (13:24), Nextdoor (09:00), Meta tents (05:25), Nvidia (04:36), Tesla (06:48). Wait, Tesla is at 06:48, which is earlier than 09:00. So the order would be:

1. DOGE (13:40)
2. Geely (13:32)
3. Google (13:05)
4. Joby (13:00)
5. Auriga (13:00)
6. ParadeDB (13:24)
Wait, ParadeDB is at 13:24 GMT, which is after 13:00. So ParadeDB would be after Joby and Auriga. Then Nextdoor (09:00), Meta tents (05:25), Nvidia (04:36), Tesla (06:48). Wait, Tesla's GMT is 06:48, which is between Meta tents (05:25) and Nextdoor (09:00). So the order would be:

- 04:36: Nvidia
- 05:25: Meta tents
- 06:48: Tesla
- 09:00: Nextdoor
- 13:00: Joby & Auriga
- 13:05: Google
- 13:24: ParadeDB
- 13:32: Geely
- 13:40: DOGE

So the sorted order by GMT (latest first) is:

1. DOGE (13:40)
2. Geely (13:32)
3. Google (13:05)
4. Joby (13:00)
5. Auriga (13:00)
6. ParadeDB (13:24)
Wait, ParadeDB is 13:24, which is after Joby and Auriga. So after 13:00, 13:24 comes next. Then 13:32 and 13:40.

Then the earlier ones:

Nextdoor (09:00), Tesla (06:48), Meta tents (05:25), Nvidia (04:36).

So the order of summaries should be:

- DOGE
- Geely
- Google
- Joby
- Auriga
- ParadeDB
- Geely (wait, no, Geely is at 13:32, then ParadeDB is 13:24. Wait, 13:24 is earlier than 13:32. So the order for the 13:00 to 13:40 entries is:

Joby (13:00), Auriga (13:00), Google (13:05), then ParadeDB (13:24), then Geely (13:32), then DOGE (13:40).

So the correct order is:

1. DOGE (13:40)
2. Geely (13:32)
3. ParadeDB (13:24)
4. Google (13:05)
5. Joby (13:00)
6. Auriga (13:00)
7. Nextdoor (09:00)
8. Tesla (06:48)
9. Meta tents (05:25)
10. Nvidia (04:36)
11. Meta AI strategy (22:44 GMT, which is 04:14 IST 15th)
12. Matt Miller's fund (21:56 GMT → 03:26 IST)
13. Brian Singerman's fund (23:33 GMT → 05:03 IST)
14. Meta Facebook crackdown (20:30 GMT → 01:30 IST)

Wait, but the Meta AI strategy article has a GMT date of Mon, 14 Jul 2025 22:44:24 GMT. Converting to IST is 04:14 AM on 15th. So that's earlier than the others. Similarly, Matt Miller's fund is 21:56 GMT → 03:26 AM IST. Brian's fund is 23:33 GMT → 05:03 AM IST. Meta Facebook is 20:30 GMT → 01:30 AM IST.

So all these four articles have GMT dates on Mon, 14 Jul 2025, converting to IST on 15th but earlier in the day. The order from earliest to latest GMT:

Meta Facebook (20:30 GMT), Matt Miller's fund (21:56), Brian's fund (23:33), Meta AI strategy (22:44), and then the others starting from 04:36 onwards.

So overall, the sorted order from latest GMT to earliest:

1. DOGE (13:40)
2. Geely (13:32)
3. Google (13:05)
4. Joby (13:00)
5. Auriga (13:00)
6. ParadeDB (13:24)
Wait, ParadeDB is 13:24 GMT, which is after 13:00 but before 13:32. So between Joby/Auriga and Geely.

So the order should be:

1. DOGE (13:40)
2. Geely (13:32)
3. ParadeDB (13:24)
4. Google (13:05)
5. Joby (13:00)
6. Auriga (13:00)
7. Nextdoor (09:00)
8. Tesla (06:48)
9. Meta tents (05:25)
10. Nvidia (04:36)
11. Meta AI strategy (22:44 GMT)
12. Brian's fund (23:33 GMT)
13. Matt Miller's fund (21:56 GMT)
14. Meta Facebook (20:30 GMT)

Wait, but Meta AI strategy is at 22:44 GMT, which is earlier than DOGE's 13:40. Wait no, DOGE is on 15th July, while Meta AI strategy is on 14th July but converted to 15th. So the order should be all the 15th July GMT entries first, then the 14th July GMT entries converted to 15th. But since the user wants latest first, all the articles are on IST date 2025-07-15, so sorted by GMT in descending order.

So the correct order of the articles is:

1. DOGE (13:40)
2. Geely (13:32)
3. ParadeDB (13:24)
4. Google (13:05)
5. Joby (13:00)
6. Auriga (13:00)
7. Nextdoor (09:00)
8. Tesla (06:48)
9. Meta tents (05:25)
10. Nvidia (04:36)
11. Brian's fund (23:33 GMT, which is 05:03 IST 15th)
12. Meta AI strategy (22:44 GMT → 04:14 IST)
13. Matt Miller's fund (21:56 GMT → 03:26 IST)
14. Meta Facebook (20:30 GMT → 01:30 IST)

Wait, but Brian's fund is GMT date Mon, 14 Jul 2025 23:33:28 → converted to 05:03 IST 15th. Meta AI strategy is Mon, 14 Jul 2025 22:44:24 → 04:14 IST. Matt Miller's fund is Mon, 14 Jul 2025 21:56:19 → 03:26 IST. Meta Facebook is Mon, 14 Jul 2025 20:30:01 → 01:30 IST. So the order of these four is:

Meta Facebook (01:30 IST) → Matt Miller (03:26) → Meta AI (04:14) → Brian's fund (05:03). Then the others from 04:36 onwards.

Therefore, the final order is:

1. DOGE (13:40)
2. Geely (13:32)
3. ParadeDB (13:24)
4. Google (13:05)
5. Joby (13:00)
6. Auriga (13:00)
7. Nextdoor (09:00)
8. Tesla (06:48)
9. Meta tents (05:25)
10. Nvidia (04:36)
11. Brian's fund (05:03)
12. Meta AI (04:14)
13. Matt Miller's fund (03:26)
14. Meta Facebook (01:30)

But wait, the Brian's fund is at 05:03 IST, which is after Nvidia (04:36). So the order after Nvidia would be:

Nvidia (04:36) → Meta AI (04:14) → Matt Miller (03:26) → Meta Facebook (01:30). Wait, no. The GMT order is:

Meta Facebook (20:30 GMT), Matt Miller (21:56), Brian's fund (23:33), Meta AI (22:44). Wait, the GMT dates for these four are:

Meta Facebook: Mon, 14 Jul 2025 20:30:01 GMT

Matt Miller's fund: Mon, 14 Jul 2025 21:56:19 GMT

Meta AI: Mon, 14 Jul 2025 22:44:24 GMT

Brian's fund: Mon, 14 Jul 2025 23:33:28 GMT

So their GMT order is:

Meta Facebook (20:30), Matt Miller (21:56), Meta AI (22:44), Brian's fund (23:33). So in descending GMT order, it's Brian's fund, then Meta AI, then Matt Miller, then Meta Facebook. But converted to IST, their order is:

Brian's fund: 05:03 IST

Meta AI: 04:14 IST

Matt Miller: 03:26 IST

Meta Facebook: 01:30 IST

So the descending order based on GMT (latest first) would be Brian's fund (23:33 GMT), Meta AI (22:44), Matt Miller (21:56), Meta Facebook (20:30). Therefore, in the final list, these four should be ordered as Brian's fund, Meta AI, Matt Miller, Meta Facebook, each with their respective GMT dates, but all converted to the same IST date.

Therefore, the final order of all articles from latest GMT to earliest is:

1. DOGE (13:40)
2. Geely (13:32)
3. ParadeDB (13:24)
4. Google (13:05)
5. Joby (13:00)
6. Auriga (13:00)
7. Nextdoor (09:00)
8. Tesla (06:48)
9. Meta tents (05:25)
10. Nvidia (04:36)
11. Brian's fund (23:33 GMT → 05:03 IST)
12. Meta AI (22:44 GMT → 04:14 IST)
13. Matt Miller's fund (21:56 GMT → 03:26 IST)
14. Meta Facebook (20:30 GMT → 01:30 IST)

So the summaries should be ordered accordingly. Now, creating the markdown with this order. Each entry under ### [2025-07-15], sorted by GMT in descending order.

Now, writing each summary concisely. For example:

For Tesla: "Tesla has opened its first showroom in India, nine years after Elon Musk first teased the move in 2016, facing challenges in major markets and competition from local players like BYD."

For Nvidia: "Nvidia is resuming sales of H20 AI chips to China after regulatory changes, following a period of restrictions and reversals under the Trump administration."

Each summary should be a single sentence or two, capturing the main point without extra details.

Also, check for any duplicate entries. The first article mentions Tesla being in India, and there's another entry for Tesla, but the content is the same. The URL is the same. So only include it once.

Wait, looking back, the user provided two entries for Tesla with the same content and URL. So need to ensure each article is unique. The user's input has all unique articles, so each should be summarized once.

Now, compiling all the entries in order.
</think>

### [2025-07-15]
- [A DOGE staffer with access to Americans' personal data leaked a private xAI API key](https://techcrunch.com/2025/07/15/doge-staffer-with-access-to-americans-personal-data-leaked-private-xai-api-key/)
- [China’s Geely is officially bringing its luxury EV startup Zeekr private](https://techcrunch.com/2025/07/15/chinas-geely-is-officially-bringing-its-luxury-ev-startup-zeekr-private/)
- [ParadeDB takes on Elasticsearch as interest in Postgres explodes amid AI boom](https://techcrunch.com/2025/07/15/paradedb-takes-on-elasticsearch-as-interest-in-postgres-explodes-amid-ai-boom/)
- [Google inks $3B deal to buy hydropower from Brookfield](https://techcrunch.com/2025/07/15/google-inks-3b-deal-to-buy-hydropower-from-brookfield/)
- [Joby Aviation doubles pilot eVTOL facility capacity as it races toward air taxi launch](https://techcrunch.com/2025/07/15/joby-aviation-doubles-pilot-evtol-facility-capacity-as-it-races-toward-air-taxi-launch/)
- [Auriga Space raises $6M to shoot rockets off an electromagnetic launch track](https://techcrunch.com/2025/07/15/auriga-space-raises-6m-to-shoot-rockets-off-an-electromagnetic-launch-track/)
- [Nextdoor redesigns app with AI recommendations, local news, and real-time emergency alerts](https://techcrunch.com/2025/07/15/nextdoor-redesigns-app-with-ai-recommendations-local-news-and-real-time-emergency-alerts/)
- [Tesla finally enters India — nine years after Elon Musk first teased its debut](https://techcrunch.com/2025/07/14/tesla-finally-enters-india-nine-years-after-elon-musk-first-teased-its-debut/)
- [Meta is reportedly using actual tents to build data centers](https://techcrunch.com/2025/07/14/meta-is-reportedly-using-actual-tents-to-build-data-centers/)
- [Nvidia is set to resume China chip sales after months of regulatory whiplash](https://techcrunch.com/2025/07/14/nvidia-is-set-to-resume-china-chip-sales-after-months-of-regulatory-whiplash/)
- [Brian Singerman's new fund has a twist — and Peter Thiel as a big backer](https://techcrunch.com/2025/07/14/brian-singermans-new-fund-has-a-twist-and-peter-thiel-as-a-big-backer/)
- [Meta built its AI reputation on openness — that may be changing](https://techcrunch.com/2025/07/14/meta-built-its-ai-reputation-on-openness-that-may-be-changing/)
- [Former Sequoia partner Matt Miller raises $355M for new fund — with Sequoia's backing](https://techcrunch.com/2025/07/14/former-sequoia-partner-matt-miller-raises-355m-for-new-fund-with-sequoias-backing/)
- [Following YouTube, Meta announces crackdown on 'unoriginal' Facebook content](https://techcrunch.com/2025/07/14/following-youtube-meta-announces-crackdown-on-unoriginal-facebook-content/)