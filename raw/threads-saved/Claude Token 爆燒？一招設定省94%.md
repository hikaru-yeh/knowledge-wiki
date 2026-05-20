---
base: "[[收藏清單_DB.base]]"
url: "https://www.threads.com/@_prem.io/post/DXGDLiTAp8i"
author: "_prem.io"
clip_type: "Claude Code"
date_added: 2026-04-21T13:46:00
---

[https://www.threads.com/@_prem.io/post/DXGDLiTAp8i](https://www.threads.com/@_prem.io/post/DXGDLiTAp8i)

## 主文

AI Threads
04/14/26
I was burning 198,000 tokens per conversation on Claude. Now Saving ~94% of that.
Not from long prompts. Not from big files. Not from cavemen.
From settings I never touched.
Here's what was happening and how I cut it by 94% in 10 minutes.
🧵

## 作者留言

·
Author
Every message you send on Claude loads your full memory profile first.
Not once per chat. Every single message.
Mine was 3,000 tokens. 20 messages in a chat = 60,000 tokens just from my profile sitting in memory.
I hadn't typed a single word yet.

·
Author
Add tool schemas from every connected MCP server.
I had 15+ connected: Make, Notion, Airtable, Slack, ClickUp, n8n, Figma and more.
Each one loads its full schema definition into every message.
That's another 2,000-5,000 tokens per message before your actual question.
Web search being ON by default adds more on top.

·
Author
Per 20-message conversation:
Memory profile: 60,000 tokens
Tool schemas: 40,000 tokens
Web search schema: 10,000 tokens
History + messages: 80,000 tokens
My verbose responses: 8,000 tokens
Total: ~198,000 tokens
Every. Single. Chat.

·
Author
Turn memory OFF completely, if your chats doesn't need your context
Settings → Memory → toggle off.
Your profile stops loading on every message. Zero tokens. Permanently.
This single step cuts 60,000 tokens per 20-message chat.

·
Author
Switch style to Concise.
When you tap the + icon before sending a message you'll see "Use style" option.
Switch from Normal to Concise. Default mini cavemen style.
Claude's responses get shorter by default. No prompt engineering needed. Output tokens drop by ~50%.

·
Author
Turn web search OFF when you don't need live data.
Same + icon menu. One tap.
For automation builds, writing tasks, product thinking - you don't need live search. Turning it off removes that schema overhead immediately.

·
Author
Tool access should already say "On demand" in that same menu.
If it says "Always loaded" - change it.
This stops all your MCP tool schemas from loading upfront and only loads the relevant one when actually needed.

·
Author
For context you actually need - use Notion.
Create 3 lean pages:
Your identity + brand rules
Platform-specific technical rules
Active project details
When you need context, one line at the start of a chat: "Load my profile from Notion."
I fetch it once. It stays for the whole conversation. Not repeated every message.

·
Author
Before: ~198,000 tokens per 20-message chat
After: ~10,000 tokens
94% reduction.
Same output. Same quality. Nothing lost.
The fix wasn't better prompts. It was understanding what loads before you type anything.
Most people optimising their Claude usage are solving the wrong layer.

·
Author
If you're on Claude Pro and hitting limits faster than expected - it's probably not your prompts.
Check your memory size. Check your connected tools. Check your style setting.
The overhead was always there. Most people just never looked.
Drop a comment if this saved you tokens. Curious how many people had no idea this was happening.

·
Author
Quick note before the fixes.
The memory number (3,000 tokens) is accurate - I counted it directly.
Tool schema and web search overhead are estimates. Anthropic doesn't publish exact token costs for these internally. Real numbers depend on how many tools you have connected and which models you use.
The 94% reduction is real for my specific setup. Yours will vary. But the direction is the same - these settings are burning tokens most people never think about.

AI Threads
04/14/26
·

·
Author
Fair point on caching — within an active session repeat-load does drop to ~10% cost. But two things: default TTL is 5 minutes not 1 hour (per Anthropic docs), idle past that and it resets. And every new chat starts cold with no cache. Turning memory off removes the overhead entirely vs just making it cheaper. Instead using context only when needed like I get it from notion.

·

·
Author
Just do not feed that compiled profile context on every chat session. Use that in starting of the chat. Basically I have very less profile memory context now, turned down from 3000 to ~200. Use only tools that you need on that session. I have 15 connectors which I use across different chats but not all needed in every chat. Web search and extended only when needed. This compiles on every message that you send. I calculated based on 20 message per chat. But logic is same.

·
Author
Interesting. Can you share more about that!?

·
Author
Not 100% sure but trying that as well. Will post if I get something worth sharing.

·
Author
Yeah... Few things to check and update before you start a new chat and you're done.