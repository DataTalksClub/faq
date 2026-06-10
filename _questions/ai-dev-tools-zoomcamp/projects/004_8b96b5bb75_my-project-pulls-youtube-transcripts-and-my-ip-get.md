---
id: 8b96b5bb75
question: "My project pulls YouTube transcripts and my IP gets blocked. Is there a workaround that isn't paid?"
sort_order: 4
---

YouTube blocks data-center IPs, so free/data-center proxies are unreliable; residential proxies generally work but cost a little (students used webshare, oxylabs, and decodo - which has a short free trial - around $3-4/month). Since you're downloading text, not video, traffic is small and cheap. Watch out for a second source of blocks: `yt-dlp` may also need cookies. Most of the time goes into deploying behind a proxy in the cloud, so plan for it.
