# Write the best poem about agency — agency-poem-01

- Bounty: https://make.fun/bounty/agency-poem-01
- Deadline: 15 Nov 2026, 09:00 UTC = 16:00 WIB
- Prize: $250 total, 1st $40, 2nd $25, 3rd $15, 4th-10th $5, 11th-100th $1.50
- Entry: public GitHub repo, MIT license, `main.py` at root
- Program writes one poem (UTF-8, 1-1000 chars) to `/output/entry.txt`
- Poem chosen: candidate B, "Ledger of Small Decisions"

## Local verification

```bash
python3 main.py
sha256sum /output/entry.txt
python3 main.py
sha256sum /output/entry.txt
wc -m /output/entry.txt
```

Both runs must produce identical bytes. No network calls.

## NOT done yet — submit blockers

- No public GitHub repo created, no commit pushed.
- No make.fun sign-in, no Solana keypair / API key created.
- No transcript bundle / submit.
- Transcript risk: a handed-over (manually exported) session may be ranked but take no paid place. Competing for rewards needs building in a harness whose sessions are recorded and bundle-able.

Submit only after the owner approves sign-in / keypair / GitHub steps.
